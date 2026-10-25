"""Unified access to the standalone Windows translation catalogue."""

from __future__ import annotations

from typing import Any

from .catalog_windows import EXTRA_TEXTS, LANGUAGES, TEXTS


SUPPORTED_LANGUAGES = {code for code, _label in LANGUAGES}


TEXTS.update({
    "invalid_audio_measurement": ("Mesures audio invalides : fichier endommagé ou décodage incorrect. Fichier ignoré, sans modification. {error}", "Invalid audio measurements: damaged file or incorrect decoding. File skipped without modification. {error}"),
    "artwork_invalid": ("Pochette illisible : fichier ignoré pour préserver son contenu. {error}", "Unreadable artwork: file skipped to preserve its contents. {error}"),
    "artwork_repaired": ("Pochette(s) corrigée(s) : {count}", "Artwork repaired: {count}"),
    "destination_failed": ("Écriture vers la destination impossible. Traitement arrêté ; vérifier le disque et les droits d’accès, puis relancer. {error}", "Cannot write to the destination. Processing stopped; check the drive and access permissions, then run again. {error}"),
    "output_recovered": ("Résultat conservé pour récupération : {path}", "Output retained for recovery: {path}"),
})

# Recovery and artwork messages for all supported languages.
EXTRA_TEXTS['es'].update({'invalid_audio_measurement': 'Mediciones de audio inválidas: archivo dañado o decodificación incorrecta. Archivo omitido sin modificar. {error}', 'artwork_invalid': 'Carátula ilegible: archivo omitido para conservar su contenido. {error}', 'artwork_repaired': 'Carátulas corregidas: {count}', 'destination_failed': 'No se puede escribir en el destino. Proceso detenido; compruebe el disco y los permisos antes de reiniciar. {error}', 'output_recovered': 'Resultado conservado para recuperación: {path}'})
EXTRA_TEXTS['it'].update({'invalid_audio_measurement': 'Misure audio non valide: file danneggiato o decodifica errata. File ignorato senza modifiche. {error}', 'artwork_invalid': 'Copertina illeggibile: file ignorato per conservarne il contenuto. {error}', 'artwork_repaired': 'Copertine corrette: {count}', 'destination_failed': 'Impossibile scrivere nella destinazione. Elaborazione interrotta; controllare disco e permessi prima di riprovare. {error}', 'output_recovered': 'Risultato conservato per il recupero: {path}'})
EXTRA_TEXTS['pt'].update({'invalid_audio_measurement': 'Medições de áudio inválidas: ficheiro danificado ou descodificação incorreta. Ficheiro ignorado sem alterações. {error}', 'artwork_invalid': 'Capa ilegível: ficheiro ignorado para preservar o conteúdo. {error}', 'artwork_repaired': 'Capas corrigidas: {count}', 'destination_failed': 'Não é possível escrever no destino. Processamento interrompido; verifique o disco e as permissões antes de tentar novamente. {error}', 'output_recovered': 'Resultado guardado para recuperação: {path}'})
EXTRA_TEXTS['ru'].update({'invalid_audio_measurement': 'Недопустимые измерения звука: файл повреждён или декодирован неверно. Файл пропущен без изменений. {error}', 'artwork_invalid': 'Обложка не читается: файл пропущен для сохранения содержимого. {error}', 'artwork_repaired': 'Исправлено обложек: {count}', 'destination_failed': 'Запись в папку назначения невозможна. Обработка остановлена; проверьте диск и права доступа перед повторным запуском. {error}', 'output_recovered': 'Результат сохранён для восстановления: {path}'})
EXTRA_TEXTS['ja'].update({'invalid_audio_measurement': '音声測定値が無効です。ファイルの破損またはデコードの問題があります。変更せずスキップしました。{error}', 'artwork_invalid': '画像を読み込めません。内容を保持するためファイルをスキップしました。{error}', 'artwork_repaired': '修正した画像数: {count}', 'destination_failed': '保存先に書き込めません。処理を停止しました。ディスクとアクセス権を確認して再実行してください。{error}', 'output_recovered': '復元用に保持した出力: {path}'})
EXTRA_TEXTS['hi'].update({'invalid_audio_measurement': 'ऑडियो माप अमान्य हैं: फ़ाइल क्षतिग्रस्त है या डिकोडिंग गलत है। फ़ाइल बिना बदलाव के छोड़ दी गई। {error}', 'artwork_invalid': 'कवर पढ़ा नहीं जा सकता: सामग्री सुरक्षित रखने के लिए फ़ाइल छोड़ दी गई। {error}', 'artwork_repaired': 'सुधारे गए कवर: {count}', 'destination_failed': 'गंतव्य पर लिखा नहीं जा सकता। प्रक्रिया रोक दी गई; दोबारा चलाने से पहले डिस्क और अनुमतियाँ जाँचें। {error}', 'output_recovered': 'पुनर्प्राप्ति के लिए सुरक्षित परिणाम: {path}'})
EXTRA_TEXTS['zh'].update({'invalid_audio_measurement': '音频测量值无效：文件损坏或解码错误。已跳过文件，未作修改。{error}', 'artwork_invalid': '封面无法读取：为保留内容，已跳过文件。{error}', 'artwork_repaired': '已修复封面：{count}', 'destination_failed': '无法写入目标位置。处理已停止；请检查磁盘和访问权限后重新运行。{error}', 'output_recovered': '已保留结果以供恢复：{path}'})
EXTRA_TEXTS['ko'].update({'invalid_audio_measurement': '오디오 측정값이 잘못되었습니다. 파일 손상 또는 디코딩 오류입니다. 수정 없이 파일을 건너뛰었습니다. {error}', 'artwork_invalid': '표지를 읽을 수 없습니다. 내용을 보존하기 위해 파일을 건너뛰었습니다. {error}', 'artwork_repaired': '수정한 표지: {count}', 'destination_failed': '대상에 쓸 수 없습니다. 처리를 중지했습니다. 디스크와 접근 권한을 확인한 후 다시 실행하세요. {error}', 'output_recovered': '복구를 위해 보관한 결과: {path}'})
EXTRA_TEXTS['id'].update({'invalid_audio_measurement': 'Pengukuran audio tidak valid: berkas rusak atau dekode salah. Berkas dilewati tanpa perubahan. {error}', 'artwork_invalid': 'Sampul tidak terbaca: berkas dilewati untuk mempertahankan isinya. {error}', 'artwork_repaired': 'Sampul diperbaiki: {count}', 'destination_failed': 'Tidak dapat menulis ke tujuan. Pemrosesan dihentikan; periksa disk dan izin akses sebelum menjalankan ulang. {error}', 'output_recovered': 'Hasil disimpan untuk pemulihan: {path}'})
EXTRA_TEXTS['tr'].update({'invalid_audio_measurement': 'Geçersiz ses ölçümleri: dosya bozuk veya çözümleme hatalı. Dosya değiştirilmeden atlandı. {error}', 'artwork_invalid': 'Kapak okunamıyor: içeriği korumak için dosya atlandı. {error}', 'artwork_repaired': 'Düzeltilen kapaklar: {count}', 'destination_failed': 'Hedefe yazılamıyor. İşlem durduruldu; yeniden çalıştırmadan önce diski ve erişim izinlerini kontrol edin. {error}', 'output_recovered': 'Kurtarma için saklanan sonuç: {path}'})

def translate(language: str, key: str, **values: Any) -> str:
    if language in EXTRA_TEXTS:
        template = EXTRA_TEXTS[language].get(key, TEXTS[key][1])
    else:
        selected = 1 if language == "en" else 0
        template = TEXTS[key][selected]
    return template.format(**values)


__all__ = [
    "EXTRA_TEXTS",
    "LANGUAGES",
    "SUPPORTED_LANGUAGES",
    "TEXTS",
    "translate",
]
