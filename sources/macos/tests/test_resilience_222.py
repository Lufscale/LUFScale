import errno
import io
import math
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image
from mutagen.id3 import ID3, APIC, TIT2
from PySide6.QtWidgets import QApplication, QWidget, QHeaderView
from lufscale.audio.resilience import (repaired_mp3_source, validate_measurements,
    InvalidAudioError, ArtworkError, publish_completed, require_destination_volume)
from lufscale.audio.core import ConversionJob,LoudnessSettings
from lufscale.processing.conversion import ConversionWorker
from lufscale.ui.dialogs import IssueListDialog

APP = QApplication.instance() or QApplication([])
GOOD = dict(input_i='-14', input_tp='-2', input_lra='4', input_thresh='-24',target_offset='0')

class ResilienceTests(unittest.TestCase):
    def test_columns_remain_independently_resizable(self):
        parent=QWidget(); dialog=IssueListDialog(parent,'Errors',[],'errors')
        header=dialog.issue_table.header()
        dialog.show();APP.processEvents()
        for index in range(3):
            self.assertEqual(header.sectionResizeMode(index),QHeaderView.ResizeMode.Interactive)
            header.resizeSection(index,411+index*23)
        APP.processEvents()
        self.assertEqual([header.sectionSize(i) for i in range(3)],[411,434,457])
        dialog.close();parent.close()

    def test_positive_nan_and_infinite_measurements_rejected_but_silence_allowed(self):
        validate_measurements(GOOD)
        for value in ('26.27','24.21','26.94','nan','inf','-100'):
            with self.assertRaises(InvalidAudioError):validate_measurements(dict(GOOD,input_i=value))
        validate_measurements(dict(GOOD,input_i='-inf',input_tp='-inf'))

    def test_webp_mislabeled_jpeg_repaired_without_changing_source_or_audio(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/'source.mp3';source.write_bytes(b'original audio bytes')
            image=io.BytesIO();Image.new('RGB',(20,20),'red').save(image,'WEBP')
            tags=ID3();tags.add(TIT2(encoding=3,text=['Keep title']))
            tags.add(APIC(encoding=3,mime='image/jpg',type=3,desc='Front',data=image.getvalue()));tags.save(source)
            original=source.read_bytes(); folder=root/'work';folder.mkdir()
            fixed,count=repaired_mp3_source(source,folder)
            self.assertEqual(count,1);self.assertEqual(source.read_bytes(),original)
            self.assertTrue(fixed.read_bytes().endswith(b'original audio bytes'))
            tags=ID3(fixed);self.assertEqual(str(tags['TIT2']),'Keep title')
            pic=tags.getall('APIC')[0];self.assertEqual(pic.mime,'image/png')
            with Image.open(io.BytesIO(pic.data)) as im:self.assertEqual(im.size,(20,20))
            self.assertEqual(repaired_mp3_source(fixed,folder),(fixed,0))
            pic.data=b'broken';tags.save(fixed)
            with self.assertRaises(ArtworkError):repaired_mp3_source(fixed,folder)

    def test_delivery_failure_keeps_completed_file_and_existing_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);src=root/'ready.mp3';dst=root/'dest.mp3'
            src.write_bytes(b'new audio');dst.write_bytes(b'old audio')
            with patch('lufscale.audio.resilience.os.replace',side_effect=OSError(errno.EIO,'disk disconnected')):
                with self.assertRaises(OSError):publish_completed(src,dst,lambda:None)
            self.assertEqual(src.read_bytes(),b'new audio');self.assertEqual(dst.read_bytes(),b'old audio')
            self.assertEqual(list(root.glob('*.delivery')),[])
            publish_completed(src,dst,lambda:None)
            self.assertEqual(dst.read_bytes(),b'new audio')

    def test_missing_mac_volume_is_not_recreated(self):
        with patch.object(Path,'is_mount',return_value=False):
            with self.assertRaises(OSError):require_destination_volume(Path('/Volumes/LUFScale-missing/album/track.mp3'))

    def test_worker_retains_output_and_stops_on_delivery_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'source.wav';source.write_bytes(b'completed audio fixture')
            destination=root/'out'/'source.wav'
            worker=ConversionWorker('ffmpeg',[source],root/'out',LoudnessSettings(-14,11,-1),True,'convert',1,False,False,False,'en')
            with patch('lufscale.processing.conversion.QStandardPaths.writableLocation',return_value=str(root/'local')), patch.object(worker,'_analyze_path_full',return_value=GOOD), patch('lufscale.processing.conversion.publish_completed',side_effect=OSError(errno.EIO,'disk disconnected')):
                result=worker._process_job(ConversionJob(source,destination),GOOD,0,{})
            self.assertEqual(result['_status_code'],'error');self.assertTrue(worker._cancel_event.is_set())
            retained=Path(result['_recovery_path']);self.assertEqual(retained.read_bytes(),source.read_bytes())
            self.assertTrue((retained.parent/'destination.json').is_file());self.assertFalse(destination.exists())
            self.assertIn('Processing stopped',result['détail'])
