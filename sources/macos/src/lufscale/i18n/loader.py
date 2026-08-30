"""Main catalogue and unified access to LUFScale translations."""

from __future__ import annotations

from typing import Any

from .translations import (
    EXTRA_TEXTS,
    TRANSLATION_UPDATES_12406,
    TRANSLATION_UPDATES_12407,
    TRANSLATION_UPDATES_12408,
)
from .translations_12410 import (
    NEW_LANGUAGE_TEXTS_12410,
    TRANSLATION_UPDATES_12410,
)
from .translations_12412 import TRANSLATION_UPDATES_12412
from .translations_12413 import TRANSLATION_UPDATES_12413
from .translations_12414 import TRANSLATION_UPDATES_12414
from .translations_12415 import TRANSLATION_UPDATES_12415
from .translations_12416 import TRANSLATION_UPDATES_12416
from .translations_12417 import TRANSLATION_UPDATES_12417
from .translations_12418 import TRANSLATION_UPDATES_12418
from .translations_12419 import TRANSLATION_UPDATES_12419
from .translations_12420 import TRANSLATION_UPDATES_12420
from .translations_12421 import TRANSLATION_UPDATES_12421
from .translations_12422 import TRANSLATION_UPDATES_12422
from .translations_12423 import TRANSLATION_UPDATES_12423
from .translations_12424 import TRANSLATION_UPDATES_12424
from .translations_12425 import TRANSLATION_UPDATES_12425
from .translations_12426 import TRANSLATION_UPDATES_12426
from .translations_12427 import TRANSLATION_UPDATES_12427
from .translations_12428 import TRANSLATION_UPDATES_12428
from .translations_12429 import TRANSLATION_UPDATES_12429
from .translations_12430 import TRANSLATION_UPDATES_12430
from .translations_12431 import TRANSLATION_UPDATES_12431
from .translations_12432 import TRANSLATION_UPDATES_12432
from .translations_12433 import TRANSLATION_UPDATES_12433
from .translations_12434 import TRANSLATION_UPDATES_12434
from .translations_12435 import TRANSLATION_UPDATES_12435
from .translations_12500 import TRANSLATION_UPDATES_12500
from .translations_20000 import TRANSLATION_UPDATES_20000
from .translations_20100 import TRANSLATION_UPDATES_20100
from .translations_20200 import TRANSLATION_UPDATES_20200
from .translations_20300 import TRANSLATION_UPDATES_20300
from .translations_20400 import TRANSLATION_UPDATES_20400
from .translations_20500 import TRANSLATION_UPDATES_20500
from .translations_20600 import TRANSLATION_UPDATES_20600
from .translations_20700 import TRANSLATION_UPDATES_20700
from .translations_20800 import TRANSLATION_UPDATES_20800
from .translations_20900 import TRANSLATION_UPDATES_20900
from .translations_201000 import TRANSLATION_UPDATES_201000
from .translations_201100 import TRANSLATION_UPDATES_201100
from .translations_201200 import TRANSLATION_UPDATES_201200
from .translations_201300 import TRANSLATION_UPDATES_201300
from .translations_201400 import TRANSLATION_UPDATES_201400
from .translations_201500 import TRANSLATION_UPDATES_201500
from .translations_201600 import TRANSLATION_UPDATES_201600
from .translations_201700 import TRANSLATION_UPDATES_201700
from .translations_211000 import TRANSLATION_UPDATES_211000
from .translations_211100 import TRANSLATION_UPDATES_211100


LANGUAGES = (
    # Every selectable catalogue is backed by its dedicated PDF guide.
    ("fr", "Français"),
    ("en", "English"),
    ("es", "Español"),
    ("it", "Italiano"),
    ("pt", "Português"),
    ("ru", "Русский"),
    ("ja", "日本語"),
    ("hi", "हिन्दी"),
    ("zh", "简体中文"),
    ("ko", "한국어"),
    ("id", "Bahasa Indonesia"),
    ("tr", "Türkçe"),
)
SUPPORTED_LANGUAGES = {code for code, _label in LANGUAGES}


TEXTS = {
    "activity_cancelled": (
        "Activité : traitement annulé",
        "Activity: processing cancelled",
    ),
    "activity_cancelling": ("Activité : annulation en cours…", "Activity: cancelling…"),
    "activity_completed": (
        "Activité : traitement terminé",
        "Activity: processing completed",
    ),
    "activity_compliant": ("Conformes : {count}", "Compliant: {count}"),
    "activity_detected": (
        "Activité : {total} fichier(s) détecté(s)",
        "Activity: {total} file(s) detected",
    ),
    "activity_errors": ("Erreurs : {count}", "Errors: {count}"),
    "activity_files": ("Fichiers : {count}", "Files: {count}"),
    "activity_idle": ("Activité : en attente", "Activity: waiting"),
    "activity_preparing": (
        "Activité : préparation des fichiers…",
        "Activity: preparing files…",
    ),
    "activity_progress": (
        "{total} fichiers • réussis {success} • alertes {warnings} • erreurs "
        "{failed} • repris/ignorés {skipped} • conformes {compliant}",
        "{total} files • successful {success} • warnings {warnings} • errors "
        "{failed} • resumed/skipped {skipped} • compliant {compliant}",
    ),
    "activity_skipped": ("Repris/ignorés : {count}", "Resumed/skipped: {count}"),
    "activity_successes": ("Réussis : {count}", "Successful: {count}"),
    "activity_warnings": ("Alertes : {count}", "Warnings: {count}"),
    "adaptive_disabled_log": (
        "Analyse adaptative — sondes rapides arrêtées après {sample} mesures "
        "({successes} succès, gain estimé {percent:+.1f} %).",
        "Adaptive analysis — fast probes stopped after {sample} measurements "
        "({successes} successes, estimated saving {percent:+.1f}%).",
    ),
    "add_folders": ("Ajouter des dossiers…", "Add folders…"),
    "add_mp3": ("Ajouter des fichiers audio…", "Add audio files…"),
    "add_replaygain": ("Ajouter ReplayGain", "Add ReplayGain"),
    "add_source_files": ("Ajouter des fichiers audio", "Add audio files"),
    "add_source_folder": ("Ajouter un dossier source", "Add a source folder"),
    "album_gain_detail": (
        "Gain album commun {gain:+.2f} dB.",
        "Shared album gain {gain:+.2f} dB.",
    ),
    "album_gain_log": (
        "Album « {album} » — gain commun {gain:+.2f} dB.",
        "Album “{album}” — shared gain {gain:+.2f} dB.",
    ),
    "album_measurement_error": (
        "Mesure de l’album impossible : {error}",
        "Album measurement failed: {error}",
    ),
    "album_mode_log": (
        "Mode Album — chaque dossier contenant des fichiers audio forme un album.",
        "Album mode — each folder containing audio files is treated as an album.",
    ),
    "albums_measurement": (
        "Mesure de {count} album(s)…",
        "Measuring {count} album(s)…",
    ),
    "already_completed": (
        "Déjà terminé lors d’une exécution précédente.",
        "Already completed during a previous run.",
    ),
    "already_compliant_badge": ("CONFORME", "COMPLIANT"),
    "already_compliant_copy": (
        "Déjà conforme : copie audio à l’identique, sans réencodage.",
        "Already compliant: copied unchanged without audio re-encoding.",
    ),
    "already_compliant_log": (
        "déjà conforme, sans réencodage",
        "already compliant, no re-encoding",
    ),
    "analysis_cache_summary": (
        "Cache d’analyse — {hits} mesure(s) réutilisée(s).",
        "Analysis cache — {hits} measurement(s) reused.",
    ),
    "analysis_impossible": ("Analyse impossible : {error}", "Analysis failed: {error}"),
    "analysis_method": ("Méthode d’analyse", "Analysis method"),
    "analysis_method_adaptive": (
        "Adaptatif — arrêt si non rentable",
        "Adaptive — stops when unprofitable",
    ),
    "analysis_method_fast": ("Rapide — expérimental", "Fast — experimental"),
    "analysis_method_historical": ("Historique — référence", "Historical — reference"),
    "analysis_method_log": (
        "Méthode d’analyse — {method}.",
        "Analysis method — {method}.",
    ),
    "analysis_method_tooltip": (
        "La version stable utilise automatiquement la mesure historique "
        "complète, seule méthode validée sur le corpus de référence. Les "
        "variantes Rapide et Adaptatif ne sont plus proposées.",
        "The stable version automatically uses the full historical "
        "measurement, the only method validated on the reference corpus. "
        "Fast and Adaptive are no longer offered.",
    ),
    "analysis_progress": (
        "Analyse {current}/{total} : {file}",
        "Analysis {current}/{total}: {file}",
    ),
    "analyze": ("Analyser", "Analyze"),
    "analyze_operation": ("analyse/simulation", "analysis/simulation"),
    "analyzed_progress": ("Analysé : {file}", "Analyzed: {file}"),
    "app_name": ("LUFScale", "LUFScale"),
    "audio_copy_replaygain": (
        "Flux audio copié sans réencodage ; balises ReplayGain ajoutées.",
        "Audio stream copied without re-encoding; ReplayGain tags added.",
    ),
    "audio_tab": ("Audio", "Audio"),
    "auto_start": (
        "Démarrer automatiquement après un dépôt ou un collage",
        "Start automatically after a drop or paste",
    ),
    "auto_start_tooltip": (
        "Lance automatiquement le traitement après l’ajout de sources par "
        "glisser-déposer ou collage, si une destination est déjà choisie.",
        "Automatically starts processing after sources are added by drag-and-drop "
        "or paste, when a destination has already been selected.",
    ),
    "cancel": ("Annuler", "Cancel"),
    "cancelled_summary": (
        "Annulé — {success} réussi(s), {failed} erreur(s), {skipped} "
        "repris/ignoré(s), {warnings} alerte(s), {compliant} conforme(s) — "
        "{duration}.",
        "Cancelled — {success} successful, {failed} error(s), {skipped} "
        "resumed/skipped, {warnings} warning(s), {compliant} compliant — "
        "{duration}.",
    ),
    "cancelling": ("Annulation en cours…", "Cancelling…"),
    "choose": ("Choisir…", "Choose…"),
    "choose_output": (
        "Choisir le dossier de destination",
        "Choose the destination folder",
    ),
    "clipboard": ("Presse-papiers", "Clipboard"),
    "clipboard_empty": (
        "Le presse-papiers ne contient aucun chemin de dossier ou fichier audio "
        "compatible.",
        "The clipboard does not contain a valid folder or supported audio-file path.",
    ),
    "close_question": (
        "Annuler le traitement et fermer l’application ?",
        "Cancel processing and close the application?",
    ),
    "completed_dialog_summary": (
        "État : terminé\n"
        "Fichiers : {files}\n"
        "Réussis : {success}\n"
        "Erreurs : {failed}\n"
        "Repris ou ignorés : {skipped}\n"
        "Alertes : {warnings}\n"
        "Conformes : {compliant}\n"
        "Temps total : {duration}",
        "Status: completed\n"
        "Files: {files}\n"
        "Successful: {success}\n"
        "Errors: {failed}\n"
        "Resumed or skipped: {skipped}\n"
        "Warnings: {warnings}\n"
        "Compliant: {compliant}\n"
        "Total time: {duration}",
    ),
    "completed_summary": (
        "Terminé — {success} réussi(s), {failed} erreur(s), {skipped} "
        "repris/ignoré(s), {warnings} alerte(s), {compliant} conforme(s) — "
        "{duration}.",
        "Completed — {success} successful, {failed} error(s), {skipped} "
        "resumed/skipped, {warnings} warning(s), {compliant} compliant — "
        "{duration}.",
    ),
    "completed_with_errors": (
        "Traitement terminé avec alertes",
        "Processing completed with warnings",
    ),
    "convert": ("Uniformiser", "Normalize"),
    "convert_operation": ("uniformisation audio", "audio normalization"),
    "cpu_tooltip": (
        "Utilisation totale du processeur du Mac, mise à jour chaque seconde pendant le "
        "traitement.",
        "Total Mac CPU usage, updated every second during processing.",
    ),
    "cpu_unavailable": ("N/D", "N/A"),
    "cpu_usage": ("CPU", "CPU"),
    "create_report": ("Créer un rapport CSV", "Create a CSV report"),
    "custom": ("Personnalisé", "Custom"),
    "decrease_value": ("Diminuer la valeur", "Decrease value"),
    "description": (
        "Uniformise le volume perçu en mode Piste ou Album, sans modifier les originaux.",
        "Balances perceived loudness in Track or Album mode without changing the "
        "originals.",
    ),
    "destination": ("Destination", "Destination"),
    "dialog_ok": ("OK", "OK"),
    "destination_error": (
        "ERREUR — destination inaccessible : {error}",
        "ERROR — destination unavailable: {error}",
    ),
    "destination_path_tooltip": (
        "Cliquez dans le chemin, puis utilisez les flèches, Début/Fin ou la "
        "molette. Le chemin est sélectionnable et copiable, mais non "
        "modifiable.",
        "Click the path, then use the arrow keys, Home/End or the mouse "
        "wheel. The path can be selected and copied, but not edited.",
    ),
    "drop_subtitle": (
        "MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — sous-dossiers acceptés",
        "MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — subfolders supported",
    ),
    "drop_title": (
        "Déposez ici vos dossiers ou fichiers audio",
        "Drop folders or audio files here",
    ),
    "elapsed_time": ("Temps écoulé : {duration}", "Elapsed time: {duration}"),
    "error_progress": ("Erreur : {file}", "Error: {file}"),
    "estimated_result": (
        "Résultat estimé, aucun fichier créé.",
        "Estimated result; no file created.",
    ),
    "estimated_total_calculating": (
        "Temps total estimé : calcul en cours…",
        "Estimated total time: calculating…",
    ),
    "estimated_total_time": (
        "Temps total estimé : {duration}",
        "Estimated total time: {duration}",
    ),
    "estimated_total_time_with_finish": (
        "Temps total estimé : {duration} — {time}",
        "Estimated total time: {duration} — {time}",
    ),
    "estimated_total_time_with_day_finish": (
        "Temps total estimé : {duration} — {days} j. {time}",
        "Estimated total time: {duration} — {days} d. {time}",
    ),
    "estimated_total_unavailable": (
        "Temps total estimé : non disponible",
        "Estimated total time: unavailable",
    ),
    "ffmpeg_download_button": (
        "Ouvrir le site officiel FFmpeg",
        "Open the official FFmpeg website",
    ),
    "ffmpeg_error_no_detail": (
        "Erreur FFmpeg sans détail.",
        "FFmpeg error without details.",
    ),
    "ffmpeg_execution_error": (
        "Impossible d’exécuter FFmpeg : {error}",
        "Unable to run FFmpeg: {error}",
    ),
    "ffmpeg_incompatible": ("FFmpeg incompatible", "Incompatible FFmpeg"),
    "ffmpeg_missing": ("FFmpeg introuvable", "FFmpeg not found"),
    "ffmpeg_missing_encoders": (
        "Cette version de FFmpeg ne contient pas tous les encodeurs audio "
        "requis : {encoders}.",
        "This FFmpeg build does not include all required audio encoders: {encoders}.",
    ),
    "ffmpeg_missing_message": (
        "FFmpeg doit être installé et accessible dans le PATH, ou placé à côté "
        "du programme.",
        "FFmpeg must be installed and available in PATH, or placed next to the "
        "program.",
    ),
    "ffmpeg_no_lame": (
        "Cette version de FFmpeg ne contient pas l’encodeur MP3 libmp3lame.",
        "This FFmpeg build does not include the libmp3lame MP3 encoder.",
    ),
    "ffmpeg_no_loudnorm": (
        "Cette version de FFmpeg ne contient pas le filtre loudnorm.",
        "This FFmpeg build does not include the loudnorm filter.",
    ),
    "ffmpeg_not_responding": (
        "FFmpeg ne répond pas correctement.",
        "FFmpeg is not responding correctly.",
    ),
    "file_exists": ("Le fichier existe déjà.", "The file already exists."),
    "finalization_completed": (
        "Finalisation terminée en {duration}.",
        "Finalization completed in {duration}.",
    ),
    "finalizing": (
        "Finalisation — rapport, cache d’analyse et données de reprise…",
        "Finalizing — report, analysis cache and resume data…",
    ),
    "files_found": (
        "{total} fichier(s) audio trouvé(s) — {operation} — {parallel} traitement(s) "
        "parallèle(s).",
        "{total} audio file(s) found — {operation} — {parallel} parallel process(es).",
    ),
    "folder": ("Dossier", "Folder"),
    "folder_unavailable": ("Dossier inaccessible", "Folder unavailable"),
    "guide_help_tooltip": (
        "Ouvre le guide PDF complet dans la langue sélectionnée.",
        "Opens the complete PDF guide in the selected language.",
    ),
    "guide_missing_message": (
        "Le guide PDF n’a pas été trouvé : {path}",
        "The PDF guide could not be found: {path}",
    ),
    "guide_missing_title": ("Guide indisponible", "Guide unavailable"),
    "guide_open_error": (
        "macOS n’a pas pu ouvrir le guide PDF : {path}",
        "macOS could not open the PDF guide: {path}",
    ),
    "help_button": ("Aide", "Help"),
    "help_overview": (
        "• Normalisation réelle, ReplayGain ou analyse des formats MP3, FLAC, WAV, "
        "AIFF, M4A, OGG et Opus.\n"
        "• Modes Piste et Album avec conservation des écarts entre les titres.\n"
        "• Arborescence, métadonnées et pochettes conservées lorsque FFmpeg peut les "
        "recopier.\n"
        "• Originaux jamais déplacés ni modifiés.\n"
        "• Parallélisme Auto, cache d’analyse et reprise après interruption.\n"
        "• Contrôle qualité, rapport CSV, progression, CPU, vumètre de sonie et durée "
        "totale estimée.\n"
        "• Sélecteur de 12 langues, chacune avec son catalogue d’interface et son "
        "guide PDF dédiés.",
        "• Normalization, ReplayGain or analysis of MP3, FLAC, WAV, AIFF, M4A, OGG and "
        "Opus audio.\n"
        "• Track and Album modes with preserved differences between tracks.\n"
        "• Folder tree, metadata and artwork preserved when FFmpeg can copy them.\n"
        "• Originals are never moved or modified.\n"
        "• Auto parallelism, analysis cache and resume after interruption.\n"
        "• Quality control, CSV report, progress, CPU, loudness meter and estimated "
        "total duration.\n"
        "• 12-language selector, each with its own interface catalogue and PDF guide.",
    ),
    "help_title": ("Principales caractéristiques", "Main features"),
    "increase_value": ("Augmenter la valeur", "Increase value"),
    "interface_ffmpeg_message": (
        "L’interface fonctionne, mais la conversion nécessite FFmpeg. "
        "Installez FFmpeg puis relancez l’application.",
        "The interface is available, but conversion requires FFmpeg. Install "
        "FFmpeg and restart the application.",
    ),
    "internal_error": ("Erreur interne : {error}", "Internal error: {error}"),
    "input_lufs_log": ("entrée {value} LUFS", "input {value} LUFS"),
    "output_lufs_log": ("sortie {value} LUFS", "output {value} LUFS"),
    "output_lufs_unavailable": ("sortie LUFS indisponible", "output LUFS unavailable"),
    "interrupted": ("Traitement interrompu.", "Processing interrupted."),
    "invalid_location": ("Emplacement invalide", "Invalid location"),
    "language": ("Langue", "Language"),
    "language_tooltip": (
        "Change immédiatement la langue de l’interface, des messages et des futurs "
        "rapports CSV. Les douze choix disposent chacun d’un catalogue et d’un guide "
        "dédiés. Le choix est mémorisé.",
        "Immediately changes the interface, messages, and future CSV reports. Each of "
        "the twelve choices has its own catalogue and guide. The choice is "
        "remembered.",
    ),
    "level_mode": ("Mode de niveau", "Loudness mode"),
    "log_help_text": (
        "Chaque ligne concerne un fichier ou une étape générale.\n"
        "\n"
        "• Début : état du traitement (RÉUSSI, ALERTE, ERREUR, repris ou ignoré).\n"
        "• Puis : nom du fichier audio et temps consacré à ce fichier.\n"
        "• LUFS avec contrôle qualité : niveau d’entrée → niveau final remesuré.\n"
        "• « sortie … LUFS » sans contrôle qualité : sonie du fichier livré, remesurée "
        "sans évaluation, alerte ni réessai correctif.\n"
        "• Fin : résultat du contrôle qualité et détail éventuel.\n"
        "\n"
        "Couleurs : vert = réussite ; orange = alerte ; rouge = fichier non terminé ; "
        "violet bleuté = reprise ; gris = information, élément ignoré ou annulation.\n"
        "\n"
        "QC ALERTE — crête signifie que la crête vraie remesurée en sortie dépasse de "
        "plus de 0,25 dB la limite choisie. Le fichier est tout de même créé : ce n’est "
        "pas une erreur de conversion. En revanche, il ne respecte pas strictement le "
        "plafond demandé et offre moins de marge pour un nouvel encodage ou certains "
        "convertisseurs. Plus la valeur dBTP se rapproche de 0, plus le risque de crête "
        "inter-échantillons augmente. Pour corriger une alerte persistante, choisissez "
        "une cible LUFS plus basse ou une crête maximale plus prudente, par exemple "
        "−2,0 dBTP, puis relancez le fichier.\n"
        "\n"
        "Les temps cumulés additionnent le travail de tous les traitements parallèles. "
        "Le temps total correspond à la durée réellement écoulée.",
        "Each line describes a file or a general processing step.\n"
        "\n"
        "• Start: processing status (SUCCESS, WARNING, ERROR, resumed or skipped).\n"
        "• Then: audio filename and time spent on that file.\n"
        "• LUFS with quality control: input level → remeasured final level.\n"
        "• “output … LUFS” without quality control: delivered-file loudness, remeasured "
        "without assessment, warning, or corrective retry.\n"
        "• End: quality-control result and any additional detail.\n"
        "\n"
        "Colors: green = success; orange = warning; red = unfinished file; blue-violet "
        "= resumed file; gray = information, skipped item or cancellation.\n"
        "\n"
        "QC WARNING — peak means that the output’s remeasured true peak is more than "
        "0.25 dB above the selected limit. The file is still created: this is not a "
        "conversion error. However, it does not strictly meet the requested ceiling and "
        "leaves less headroom for another encode or some converters. The closer dBTP is "
        "to 0, the greater the risk of inter-sample peaks. To correct a persistent "
        "warning, choose a quieter LUFS target or a safer maximum peak, such as −2.0 "
        "dBTP, then process the file again.\n"
        "\n"
        "Cumulative times add the work performed by all parallel tasks. Total time is "
        "the actual elapsed duration.",
    ),
    "log_placeholder": (
        "Le compte rendu apparaîtra ici.",
        "The processing log will appear here.",
    ),
    "log_title": ("Journal de traitement", "Processing log"),
    "loudness_meter_estimated": ("Estimé", "Estimated"),
    "loudness_meter_help_text": (
        "Le trait rouge est la cible. La valeur bleue est la dernière sortie "
        "remesurée. Min et Max couvrent en permanence les 8 dernières sorties "
        "remesurées ; à chaque nouvelle mesure, la plus ancienne sort de cette "
        "fenêtre. Le vumètre reste inactif sans contrôle qualité.",
        "The red line is the target. The blue value is the latest remeasured "
        "output. Min and Max continuously cover the latest 8 remeasured "
        "outputs; each new measurement removes the oldest one from the "
        "window. The meter stays inactive without quality control.",
    ),
    "loudness_meter_maximum": ("Max {value}", "Max {value}"),
    "loudness_meter_measured": ("Mesuré", "Measured"),
    "loudness_meter_minimum": ("Min {value}", "Min {value}"),
    "loudness_meter_target": ("Cible {value} LUFS", "Target {value} LUFS"),
    "loudness_meter_title": ("Vumètre de sonie", "Loudness meter"),
    "loudness_meter_tooltip": (
        "Le trait rouge représente la cible. La valeur bleue à gauche suit la "
        "dernière sortie remesurée. À droite, Min et Max sont recalculés sur une "
        "fenêtre glissante des 8 dernières sorties ainsi qu’au début d’un "
        "nouveau lot.",
        "The red line is the target. The blue value on the left follows the "
        "latest remeasured output. On the right, Min and Max are recalculated "
        "over a rolling window of the latest 8 outputs and at the start of a new "
        "batch.",
    ),
    "loudness_meter_waiting": (
        "En attente d’un fichier audio",
        "Waiting for an audio file",
    ),
    "loudness_score_acceptable": ("Acceptable", "Acceptable"),
    "loudness_score_check": ("À vérifier", "Check"),
    "loudness_score_excellent": ("Excellent", "Excellent"),
    "loudness_score_good": ("Bon", "Good"),
    "loudness_score_needs_qc": (
        "Score cible : activez le contrôle qualité",
        "Target score: enable quality control",
    ),
    "loudness_score_not_applicable": (
        "Score cible : non applicable",
        "Target score: not applicable",
    ),
    "loudness_score_tooltip": (
        "Le score utilise la même fenêtre glissante que Min et Max : les 8 "
        "dernières sorties réellement remesurées. À chaque nouvelle mesure, "
        "la plus ancienne sort du calcul. "
        "L’écart RMS (racine carrée de la moyenne des écarts au carré) résume, "
        "en une valeur, la distance globale entre les sonies obtenues et leurs "
        "valeurs attendues. Plus il est proche de 0 LU, plus la série est "
        "fidèle aux cibles : 100 = résultat exact, 50 = écart RMS de 0,5 LU, "
        "soit la tolérance du contrôle qualité, et 0 = 1 LU ou davantage. En "
        "mode Album, la valeur attendue de chaque piste tient compte du gain "
        "commun afin de préserver les écarts voulus.",
        "The score uses the same rolling window as Min and Max: the latest 8 "
        "outputs that were actually remeasured. Each new measurement removes "
        "the oldest one from the calculation. RMS error "
        "(the square root of the mean squared differences) summarizes the "
        "overall distance between achieved loudness values and their targets. "
        "The closer it is to 0 LU, the more accurately the batch matches its "
        "targets: 100 = exact result, 50 = 0.5 LU RMS error, the "
        "quality-control tolerance, and 0 = 1 LU or more. In Album mode, each "
        "track’s expected value includes the shared gain so the intended "
        "differences are preserved.",
    ),
    "loudness_score_value": (
        "Score cible : {score}/100\n{rating}\nÉcart RMS : {deviation}\xa0LU",
        "Target score: {score}/100\n{rating}\nRMS error: {deviation}\xa0LU",
    ),
    "loudness_score_waiting": ("Score cible : en attente", "Target score: waiting"),
    "measurement_unavailable": ("Mesure indisponible.", "Measurement unavailable."),
    "mode_album": (
        "Album — conserve les écarts entre pistes",
        "Album — preserves differences between tracks",
    ),
    "mode_album_label": ("Album", "Album"),
    "mode_tooltip": (
        "Piste règle chaque fichier audio séparément. Album calcule un gain commun pour "
        "chaque dossier afin de conserver les écarts de volume entre ses pistes.",
        "Track adjusts each audio file separately. Album calculates one shared gain per "
        "folder to preserve the loudness differences between its tracks.",
    ),
    "mode_track": (
        "Piste — même niveau pour chaque fichier",
        "Track — same level for every file",
    ),
    "mode_track_label": ("Piste", "Track"),
    "mp3": ("Audio", "Audio"),
    "mp3_filter": (
        "Audio compatible (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)",
        "Supported audio (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)",
    ),
    "destination_required_start": (
        "Choisissez d’abord le dossier de destination avec le bouton « Choisir… ».",
        "First choose the destination folder with the “Choose…” button.",
    ),
    "no_folder": ("Aucun dossier choisi", "No folder selected"),
    "no_mp3": (
        "Aucun fichier audio compatible trouvé.",
        "No supported audio files were found.",
    ),
    "no_new_source": (
        "Aucun nouveau dossier ou fichier audio compatible n’a été ajouté.",
        "No new valid folder or supported audio file was added.",
    ),
    "not_performed": ("Non effectué", "Not performed"),
    "open_output_error": (
        "Impossible d’ouvrir le dossier de destination : {error}",
        "Unable to open the destination folder: {error}",
    ),
    "operation": ("Opération", "Operation"),
    "operation_analyze": (
        "Analyser seulement — simulation sans fichier créé",
        "Analyze only — simulation without creating files",
    ),
    "operation_analyze_label": ("Analyse seulement", "Analysis only"),
    "operation_convert": (
        "Uniformiser — normaliser réellement l’audio",
        "Normalize — process the audio itself",
    ),
    "operation_convert_label": ("Uniformisation audio", "Audio normalization"),
    "operation_replaygain": (
        "ReplayGain — sans réencodage audio",
        "ReplayGain — no audio re-encoding",
    ),
    "operation_replaygain_label": ("ReplayGain", "ReplayGain"),
    "operation_tooltip": (
        "Uniformiser normalise réellement l’audio dans son format d’origine. Les "
        "formats avec pertes (MP3, M4A/AAC, OGG et Opus) doivent être réencodés : "
        "leur taille dépend alors de la qualité choisie et peut augmenter. FLAC est "
        "aussi réencodé sans perte ; sa compression peut varier légèrement car les "
        "échantillons ont changé. WAV et AIFF restent non compressés à fréquence, "
        "canaux et profondeur compatibles avec la source. ReplayGain conserve le "
        "flux audio et ajoute des balises lorsque le conteneur les accepte. "
        "Analyser simule le résultat sans créer de fichier.",
        "Normalize processes the audio in its original format. Lossy formats (MP3, "
        "M4A/AAC, OGG and Opus) must be re-encoded: their size then depends on the "
        "selected quality and may increase. FLAC is also re-encoded losslessly; its "
        "compression may vary slightly because the samples changed. WAV and AIFF "
        "remain uncompressed with source-compatible rate, channels and depth. "
        "ReplayGain preserves the audio stream and adds tags when supported. "
        "Analyze simulates the result without creating a file.",
    ),
    "options_tab": ("Options", "Options"),
    "option_status_auto_start": ("AUT", "AUT"),
    "option_status_overwrite": ("ÉCR", "OVR"),
    "option_status_quality_control": ("CQ", "QC"),
    "option_status_report": ("CSV", "CSV"),
    "option_status_resume": ("REP", "RES"),
    "option_status_skip_compliant": ("NRC", "SKP"),
    "overwrite": ("Écraser les fichiers existants", "Overwrite existing files"),
    "overwrite_tooltip": (
        "Autorise le remplacement d’un fichier audio déjà présent dans la "
        "destination. Les fichiers sources ne sont jamais écrasés.",
        "Allows an audio file already present in the destination to be replaced. "
        "Source files are never overwritten.",
    ),
    "parallel": ("Traitements parallèles", "Parallel processes"),
    "parallel_adjusted": (
        "Parallélisme automatique — {active} traitement(s), CPU {cpu:.0f} %.",
        "Automatic parallelism — {active} process(es), CPU {cpu:.0f}%.",
    ),
    "parallel_auto": ("Auto", "Auto"),
    "parallel_auto_log": (
        "automatique, maximum {maximum}",
        "automatic, maximum {maximum}",
    ),
    "parallel_tooltip": (
        "Détermine combien de fichiers peuvent être traités simultanément.\n"
        "\n"
        "• Auto démarre avec au plus 4 tâches. Lorsque la mesure CPU est disponible, "
        "le programme la contrôle chaque seconde : il ajoute une tâche sous 70 % "
        "d’occupation et en retire une au-dessus de 92 %.\n"
        "• Auto ne dépasse jamais le nombre de processeurs logiques détectés, avec "
        "un plafond absolu de 16 tâches.\n"
        "• Si la mesure CPU n’est pas disponible, Auto utilise directement ce "
        "plafond détecté sans adaptation dynamique.\n"
        "• Une valeur numérique fixe le nombre maximal de tâches simultanées ; ce "
        "n’est pas une cible d’occupation CPU.\n"
        "\n"
        "Davantage de tâches peut accélérer un grand lot, mais augmente la charge, "
        "la température et l’accès au disque. Utilisez − jusqu’à afficher Auto.",
        "Determines how many files can be processed at the same time.\n"
        "\n"
        "• Auto starts with at most 4 jobs. When CPU measurement is available, it "
        "checks once per second: it adds one job below 70% usage and removes one "
        "above 92%.\n"
        "• Auto never exceeds the detected logical CPU count, with an absolute "
        "ceiling of 16 jobs.\n"
        "• If CPU measurement is unavailable, Auto uses that detected ceiling "
        "directly without dynamic adjustment.\n"
        "• A numeric value fixes the maximum number of simultaneous jobs; it is not "
        "a CPU-usage target.\n"
        "\n"
        "More jobs can speed up a large batch, but increase CPU load, heat and disk "
        "activity. Press − until Auto is shown.",
    ),
    "paste": ("Coller", "Paste"),
    "path_left": ("Voir la partie gauche du chemin", "Show the left part of the path"),
    "path_right": (
        "Voir la partie droite du chemin",
        "Show the right part of the path",
    ),
    "pause": ("Pause", "Pause"),
    "peak": ("Crête maximale", "Maximum true peak"),
    "peak_tooltip": (
        "La crête maximale est un plafond, pas un volume à atteindre. Elle limite en "
        "dBTP les pointes les plus hautes de la forme d’onde reconstruite, y compris "
        "entre les échantillons, afin de réduire le risque d’écrêtage après encodage ou "
        "transcodage.\n"
        "\n"
        "• -1,0 dBTP — plafond courant pour la diffusion ; niveau maximal plus élevé.\n"
        "• -1,5 dBTP — réglage par défaut, compromis prudent pour des MP3.\n"
        "• -2,0 dBTP — marge supplémentaire, utile pour les fichiers destinés à être "
        "réencodés ou pour une cible sonore élevée.\n"
        "• 0 dBTP — aucune marge ; déconseillé pour un MP3.\n"
        "\n"
        "Une valeur plus négative protège davantage, mais peut empêcher certains "
        "morceaux très dynamiques d’atteindre exactement la cible LUFS.",
        "Maximum true peak is a ceiling, not a level to reach. It limits the highest "
        "reconstructed waveform peaks in dBTP, including peaks between samples, to "
        "reduce clipping after encoding or transcoding.\n"
        "\n"
        "• -1.0 dBTP — common delivery ceiling with the highest output peak level.\n"
        "• -1.5 dBTP — the default and a cautious compromise for MP3 files.\n"
        "• -2.0 dBTP — extra headroom, useful when files may be encoded again or when "
        "using a high loudness target.\n"
        "• 0 dBTP — no headroom and not recommended for MP3.\n"
        "\n"
        "A more negative value is safer, but may prevent highly dynamic tracks from "
        "reaching the LUFS target exactly.",
    ),
    "phase_summary": (
        "Répartition estimée du temps total — analyse {analysis}, conversion "
        "{conversion}, contrôle qualité {quality}.",
        "Estimated total-time allocation — analysis {analysis}, conversion "
        "{conversion}, quality control {quality}.",
    ),
    "pipeline_enabled": (
        "Pipeline Piste — chaque conversion démarre dès que son analyse est terminée.",
        "Track pipeline — each conversion starts as soon as its analysis is complete.",
    ),
    "pre_measurement": ("Mesure avant traitement…", "Measuring input files…"),
    "preset": ("Préréglage", "Preset"),
    "preset_dynamic": ("Musique dynamique", "Dynamic music"),
    "preset_library": ("Bibliothèque — recommandé", "Music library — recommended"),
    "preset_streaming": ("Streaming plus présent", "Louder streaming"),
    "preset_tooltip": (
        "Applique en une fois une cible sonore, une crête maximale et une qualité "
        "audio cohérentes. Toute modification manuelle sélectionne Personnalisé.",
        "Applies a consistent loudness target, maximum true peak and audio quality at "
        "once. Any manual change selects Custom.",
    ),
    "processing_cancelled": ("Traitement annulé.", "Processing cancelled."),
    "processing_completed": ("Traitement terminé", "Processing completed"),
    "processing_in_progress": ("Traitement en cours", "Processing in progress"),
    "processing_paused": ("Traitement en pause.", "Processing paused."),
    "processing_resumed": ("Traitement repris.", "Processing resumed."),
    "progress_status": ("{status} : {file}", "{status}: {file}"),
    "qc_impossible": (
        "ALERTE — contrôle impossible : {error}",
        "WARNING — quality control failed: {error}",
    ),
    "qc_log": (" — contrôle qualité : {quality}", " — quality control: {quality}"),
    "qc_ok": ("RÉUSSI", "SUCCESS"),
    "qc_warning": ("ALERTE — {detail}", "WARNING — {detail}"),
    "quality": ("Qualité audio", "Audio quality"),
    "quality_control": ("Contrôle qualité automatique", "Automatic quality control"),
    "quality_control_tooltip": (
        "Remesure chaque sortie, quel que soit son format. Seuls les MP3 "
        "traités par le chemin dynamique peuvent ensuite être réencodés "
        "jusqu’à trois fois pour corriger un écart. Désactiver cette option "
        "ne change pas la qualité de l’encodeur, mais supprime la vérification "
        "finale, ces corrections et l’activité du vumètre.",
        "Remeasures every output, regardless of format. Only MP3 files "
        "processed through the dynamic path may then be re-encoded up to "
        "three times to correct a deviation. Disabling this option does not "
        "change encoder quality, but removes final verification, those "
        "corrections, and meter activity.",
    ),
    "quality_tooltip": (
        "Règle le compromis qualité/taille des formats compressés. Plus le chiffre "
        "est bas, plus la qualité et le débit sont élevés. Ce réglage ne change ni la "
        "cible LUFS ni la crête maximale.\n"
        "\n"
        "• 0 — qualité maximale, recommandée pour préserver les détails.\n"
        "• 1 à 2 — très haute qualité.\n"
        "• 3 à 4 — bon compromis qualité/taille.\n"
        "• 5 à 9 — fichiers plus petits, avec davantage de pertes.\n"
        "\n"
        "FLAC reste sans perte quelle que soit la valeur. WAV et AIFF ignorent ce "
        "réglage et conservent la fréquence et la profondeur PCM compatibles avec la "
        "source. Pour MP3, M4A, OGG et Opus, une faible valeur peut demander un débit "
        "supérieur à celui du fichier d’origine : la sortie sera alors plus "
        "volumineuse. Une valeur plus élevée réduit généralement la taille, sans "
        "garantir un nombre d’octets identique, car ces encodeurs utilisent souvent "
        "un débit variable. Réencoder un format avec pertes ne restaure pas les "
        "informations déjà perdues.",
        "Controls the quality/size trade-off for compressed formats. Lower numbers "
        "use higher quality and bitrate. It changes neither the LUFS target nor "
        "maximum true peak.\n"
        "\n"
        "• 0 — maximum quality, recommended to preserve detail.\n"
        "• 1 to 2 — very high quality.\n"
        "• 3 to 4 — a good quality/size compromise.\n"
        "• 5 to 9 — smaller files with progressively more loss.\n"
        "\n"
        "FLAC remains lossless at every value. WAV and AIFF ignore this setting and "
        "preserve source-compatible rate and PCM depth. For MP3, M4A, OGG and Opus, a "
        "low value may request a higher bitrate than the original, making the output "
        "larger. A higher value generally reduces size, without guaranteeing the same "
        "byte count because these encoders often use variable bitrate. Re-encoding a "
        "lossy source cannot restore discarded information.",
    ),
    "ready": ("Prêt", "Ready"),
    "recursive_scan": (
        "Analyse récursive des dossiers…",
        "Scanning folders recursively…",
    ),
    "remove_all": ("Tout retirer", "Remove all"),
    "remove_selection": ("Retirer la sélection", "Remove selection"),
    "replaygain_operation": (
        "ReplayGain sans réencodage",
        "ReplayGain without re-encoding",
    ),
    "replaygain_tags_missing": (
        "Balises ReplayGain non retrouvées.",
        "ReplayGain tags were not found.",
    ),
    "report_album_dbtp": ("dbtp_album_avant", "album_input_dbtp"),
    "report_album_lufs": ("lufs_album_avant", "album_input_lufs"),
    "report_destination": ("destination", "destination"),
    "report_detail": ("détail", "detail"),
    "report_error": (
        "ALERTE — rapport CSV impossible : {error}",
        "WARNING — unable to create CSV report: {error}",
    ),
    "report_filename_prefix": ("Rapport_LUFScale", "LUFScale_Report"),
    "report_gain": ("gain_db", "gain_db"),
    "report_input_dbtp": ("dbtp_avant", "input_dbtp"),
    "report_input_lufs": ("lufs_avant", "input_lufs"),
    "report_log": ("Rapport CSV — {path}", "CSV report — {path}"),
    "report_mode": ("mode", "mode"),
    "report_operation": ("opération", "operation"),
    "report_output_dbtp": ("dbtp_apres", "output_dbtp"),
    "report_output_lufs": ("lufs_apres", "output_lufs"),
    "report_path": ("Rapport : {path}", "Report: {path}"),
    "report_qc": ("controle_qualite", "quality_control"),
    "report_qc_engine": ("moteur_qc", "qc_engine"),
    "report_seconds": ("temps_secondes", "elapsed_seconds"),
    "report_source": ("source", "source"),
    "report_status": ("statut", "status"),
    "report_tooltip": (
        "Crée dans la destination un rapport détaillé avec les mesures, durées et "
        "alertes.",
        "Creates a detailed report in the destination with measurements, durations and "
        "warnings.",
    ),
    "resume": ("Reprendre après une interruption", "Resume after an interruption"),
    "resume_not_saved": (
        " Reprise non enregistrée : {error}",
        " Resume checkpoint not saved: {error}",
    ),
    "resume_processing": ("Reprendre", "Resume"),
    "resume_tooltip": (
        "Les fichiers déjà terminés avec les mêmes réglages sont reconnus et ne sont "
        "pas retraités.",
        "Files already completed with the same settings are recognized and not "
        "processed again.",
    ),
    "resumed_progress": ("Repris : {file}", "Resumed: {file}"),
    "scan_error": ("ERREUR — {error}", "ERROR — {error}"),
    "scanning_folders": ("Analyse des dossiers…", "Scanning folders…"),
    "settings": ("Réglages", "Settings"),
    "show_finder": ("Afficher dans le Finder", "Show in Finder"),
    "show_option_help": ("Afficher l’aide : {option}", "Show help: {option}"),
    "silent_album_copy": (
        "Album silencieux ou non mesurable copié.",
        "Silent or unmeasurable album copied.",
    ),
    "silent_copy": (
        "Audio silencieux ou non mesurable copié.",
        "Silent or unmeasurable audio copied.",
    ),
    "silent_copy_no_replaygain": (
        "Audio silencieux copié sans balise ReplayGain.",
        "Silent audio copied without ReplayGain tags.",
    ),
    "silent_unmeasurable": (
        "Audio silencieux ou non mesurable.",
        "Silent or unmeasurable audio.",
    ),
    "simulation": ("Simulation", "Simulation"),
    "skip_compliant": (
        "Ne pas réencoder les fichiers déjà conformes",
        "Do not re-encode files that already comply",
    ),
    "skip_compliant_tooltip": (
        "Activé par défaut. Après l’analyse, un fichier dont la sonie est à "
        "±0,5 LU de la cible et dont la crête vraie ne dépasse pas le plafond "
        "est copié à l’identique, sans réencodage. En mode Album, la "
        "conformité de la sonie est évaluée sur l’album entier. Cela préserve "
        "exactement sa qualité et sa taille ; le journal l’indique clairement.",
        "Enabled by default. After analysis, a file whose loudness is within "
        "±0.5 LU of the target and whose true peak does not exceed the ceiling "
        "is copied unchanged, without re-encoding. In Album mode, loudness "
        "compliance is evaluated for the whole album. This preserves its exact "
        "quality and size; the log states it clearly.",
    ),
    "skipped_progress": ("Ignoré : {file}", "Skipped: {file}"),
    "source_audio_count": ("Fichiers : {count}", "Files: {count}"),
    "source_list_more": (
        "… {count} autre(s) source(s) conservée(s)",
        "… {count} more source(s) retained",
    ),
    "source_safety": (
        "Les fichiers sources ne sont jamais déplacés ni modifiés.",
        "Source files are never moved or modified.",
    ),
    "source_selection_tooltip": (
        "Sélection multiple : ⌘ clic pour des éléments séparés, Maj clic "
        "pour une plage.",
        "Multiple selection: Command-click for separate items, Shift-click "
        "for a range.",
    ),
    "sources_added": ("{count} source(s) ajoutée(s).", "{count} source(s) added."),
    "start": ("Démarrer", "Start"),
    "status_analyzed": ("ANALYSÉ", "ANALYZED"),
    "status_cancelled": ("ANNULÉ", "CANCELLED"),
    "status_error": ("ERREUR", "ERROR"),
    "status_ok": ("RÉUSSI", "SUCCESS"),
    "status_resumed": ("REPRIS", "RESUMED"),
    "status_skipped": ("IGNORÉ", "SKIPPED"),
    "status_warning": ("ALERTE", "WARNING"),
    "switch_to_dark": ("Mode sombre", "Dark mode"),
    "switch_to_light": ("Mode clair", "Light mode"),
    "tagline": (
        "Uniformise le volume audio perçu",
        "Balances perceived audio loudness",
    ),
    "target": ("Cible sonore", "Loudness target"),
    "target_tooltip": (
        "La cible sonore est la sonie intégrée visée sur l’ensemble du morceau, "
        "exprimée en LUFS. Une valeur moins négative produit un fichier perçu plus "
        "fort : -14 LUFS est plus fort que -16 LUFS. Un écart de 2 LU correspond "
        "approximativement à 2 dB de différence de niveau avant une éventuelle "
        "limitation de crête.\n"
        "\n"
        "Repères : -18 LUFS pour conserver davantage de calme et de dynamique ; -16 "
        "LUFS pour un équilibre général ; -14 LUFS pour une restitution plus forte de "
        "type streaming. Les plateformes peuvent ensuite appliquer leur propre "
        "normalisation.\n"
        "\n"
        "Cette cible n’aplatit pas à elle seule les variations internes du morceau. Si "
        "la crête maximale empêche d’atteindre la cible sans écrêtage, le résultat "
        "peut rester légèrement plus bas.",
        "The loudness target is the intended integrated loudness across the whole "
        "track, expressed in LUFS. A less negative value produces a louder file: -14 "
        "LUFS is louder than -16 LUFS. A 2 LU difference is approximately a 2 dB level "
        "difference before any peak limiting.\n"
        "\n"
        "Guidance: -18 LUFS for a calmer and more dynamic result; -16 LUFS for a "
        "general balance; -14 LUFS for a louder streaming-style result. Platforms may "
        "then apply their own playback normalization.\n"
        "\n"
        "This target does not by itself flatten the dynamics inside the track. If the "
        "maximum true peak prevents the target from being reached without clipping, "
        "the result may remain slightly lower.",
    ),
    "theme_accessible": (
        "Changer l’apparence de l’application. Le choix est mémorisé.",
        "Change the application appearance. The choice is remembered.",
    ),
    "total_time": ("Temps total : {duration}", "Total time: {duration}"),
    "track_mode_log": (
        "Mode Piste — chaque fichier audio est traité séparément.",
        "Track mode — each audio file is processed separately.",
    ),
    "track_two_pass": (
        "Normalisation Piste en deux passes.",
        "Two-pass Track normalization.",
    ),
    "true_peak_meter_exceeded": ("Dépassement {margin} dB", "Exceeded by {margin} dB"),
    "true_peak_meter_margin": ("Marge {margin} dB", "Headroom {margin} dB"),
    "true_peak_meter_title": ("Marge de crête", "True-peak headroom"),
    "true_peak_meter_tooltip": (
        "Compare la crête vraie de la dernière sortie au plafond choisi. Le "
        "repère indique la dernière valeur et le triangle conserve la crête "
        "la plus haute du lot. Vert signifie que le plafond est respecté, "
        "orange un dépassement jusqu’à 0,25 dB et rouge un dépassement "
        "supérieur. La tolérance orange est celle du contrôle qualité de "
        "LUFScale, pas une norme de diffusion. Le graphique est réinitialisé "
        "à chaque série.",
        "Compares the last output’s true peak with the selected ceiling. The "
        "marker shows the latest value and the triangle retains the batch’s "
        "highest peak. Green means the ceiling is met, amber means an "
        "exceedance up to 0.25 dB, and red means a larger exceedance. The "
        "amber tolerance belongs to LUFScale quality control and is not a "
        "delivery standard. The graph resets for every batch.",
    ),
    "true_peak_meter_waiting": (
        "En attente d’une mesure dBTP",
        "Waiting for a dBTP measurement",
    ),
    "version_changes": (
        "• La confirmation de fermeture pendant un traitement est traduite dans les douze langues.\n"
        "• Une marge fixe sépare le journal et le vumètre de la barre inférieure ; seul le journal grandit avec la fenêtre.\n"
        "• Le titre et la barre d’onglets des Réglages utilisent une hauteur commune : le japonais, le chinois et l’hindi ne décalent plus le contenu.\n"
        "• Le moteur audio et les calculs de normalisation sont inchangés.",
        "• The close confirmation shown during processing is translated in all twelve languages.\n"
        "• A fixed gap separates the processing log and loudness meter from the bottom status bar; only the log grows with the window.\n"
        "• The Settings title and tab bar use a shared fixed height, so Japanese, Chinese and Hindi no longer shift the content.\n"
        "• The audio engine and normalization calculations are unchanged.",
    ),
    "version_changes_title": (
        "Nouveautés de la version {version}",
        "What’s new in version {version}",
    ),
    "version_label": ("Version {version}", "Version {version}"),
    "volume": ("Volume", "Volume"),
    "volume_loud": ("Fort : -14 LUFS", "Loud: -14 LUFS"),
    "volume_normal": ("Normal : -16 LUFS", "Normal: -16 LUFS"),
    "volume_soft": ("Doux : -18 LUFS", "Soft: -18 LUFS"),
    "volume_tooltip": (
        "Ce réglage est un raccourci vers la cible sonore ; il ne règle pas le volume "
        "d’écoute du Mac.\n"
        "\n"
        "• Doux : -18 LUFS — niveau plus calme, davantage de dynamique et moins de "
        "risque de solliciter le limiteur.\n"
        "• Normal : -16 LUFS — compromis équilibré, conseillé comme point de départ "
        "pour une bibliothèque personnelle.\n"
        "• Fort : -14 LUFS — restitution plus présente, proche de la cible de lecture "
        "normale de Spotify, mais susceptible de demander davantage de limitation.\n"
        "• Personnalisé — permet de saisir directement une autre cible LUFS.\n"
        "\n"
        "Ces valeurs sont des choix pratiques, pas une norme universelle.",
        "This setting is a shortcut to the loudness target; it does not change the Mac "
        "playback volume.\n"
        "\n"
        "• Soft: -18 LUFS — calmer level, more dynamic headroom and less chance of "
        "engaging the limiter.\n"
        "• Normal: -16 LUFS — balanced compromise and a useful starting point for a "
        "personal library.\n"
        "• Loud: -14 LUFS — more forward playback, close to Spotify’s Normal playback "
        "target, but more likely to require limiting.\n"
        "• Custom — lets you enter another LUFS target directly.\n"
        "\n"
        "These are practical choices, not a universal standard.",
    ),
    "zero_album_gain": (
        "Gain album nul ; audio copié.",
        "Zero album gain; audio copied.",
    ),
}


TEXTS.update(
    {
        "close_button": ("Fermer", "Close"),
        "errors_button": ("Erreurs ({count})", "Errors ({count})"),
        "errors_button_tooltip": (
            "Ouvre la liste des erreurs avec le nom du fichier, son chemin et le détail. Disponible pendant une pause ou après le traitement.",
            "Opens the error list with filename, path, and details. Available while paused or after processing.",
        ),
        "errors_dialog_title": ("Erreurs du traitement", "Processing errors"),
        "issue_detail_column": ("Détail", "Details"),
        "issue_file_column": ("Fichier", "File"),
        "issue_path_column": ("Chemin", "Path"),
        "save_issue_list": ("Enregistrer en CSV…", "Save as CSV…"),
        "save_issue_list_error": (
            "Impossible d’enregistrer la liste : {error}",
            "Unable to save the list: {error}",
        ),
        "save_issue_list_error_title": (
            "Enregistrement impossible",
            "Unable to save",
        ),
        "save_issue_list_title": ("Enregistrer la liste CSV", "Save CSV list"),
        "csv_file_filter": ("Fichiers CSV (*.csv)", "CSV files (*.csv)"),
        "warnings_button": ("Alertes ({count})", "Warnings ({count})"),
        "warnings_button_tooltip": (
            "Ouvre la liste des alertes avec le nom du fichier, son chemin et le détail. Disponible pendant une pause ou après le traitement.",
            "Opens the warning list with filename, path, and details. Available while paused or after processing.",
        ),
        "warnings_dialog_title": ("Alertes du traitement", "Processing warnings"),
    }
)

TEXTS["log_help_text"] = (
    "Chaque ligne concerne un fichier ou une étape générale.\n\n"
    "• Une ligne réussie commence directement par le nom du fichier : RÉUSSI n’est plus répété.\n"
    "• CONFORME, REPRIS, IGNORÉ, ANNULÉ et ERREUR restent affichés lorsqu’ils apportent une information utile.\n"
    "• Les niveaux indiquent l’entrée → la sortie remesurée, puis le résultat éventuel du contrôle qualité.\n"
    "• Les boutons Alertes et Erreurs ouvrent des listes indépendantes avec le nom, le chemin et le détail. Ils sont disponibles pendant une pause ou après le traitement, et chaque liste peut être enregistrée.\n\n"
    "Couleurs : vert = réussite ; orange = alerte ; rouge = fichier non terminé ; violet bleuté = reprise ; gris = information, élément ignoré ou annulation.\n\n"
    "QC ALERTE — crête signifie que la crête vraie remesurée en sortie dépasse de plus de 0,25 dB la limite choisie. Le fichier est tout de même créé : ce n’est pas une erreur de conversion. Pour corriger une alerte persistante, choisissez une cible LUFS plus basse ou une crête maximale plus prudente, par exemple −2,0 dBTP, puis relancez le fichier.\n\n"
    "Les temps cumulés additionnent le travail de tous les traitements parallèles. Le temps total correspond à la durée réellement écoulée.",
    "Each line describes a file or a general processing step.\n\n"
    "• A successful line starts directly with the filename: SUCCESS is no longer repeated.\n"
    "• COMPLIANT, RESUMED, SKIPPED, CANCELLED, and ERROR remain visible when they add useful information.\n"
    "• Levels show input → remeasured output, followed by any quality-control result.\n"
    "• The Warnings and Errors buttons open separate lists with filename, path, and details. They are available while paused or after processing, and each list can be saved.\n\n"
    "Colors: green = success; orange = warning; red = unfinished file; blue-violet = resumed file; gray = information, skipped item, or cancellation.\n\n"
    "QC WARNING — peak means that the output’s remeasured true peak is more than 0.25 dB above the selected limit. The file is still created: this is not a conversion error. To correct a persistent warning, choose a quieter LUFS target or a safer maximum peak, such as −2.0 dBTP, then process the file again.\n\n"
    "Cumulative times add the work performed by all parallel tasks. Total time is the actual elapsed duration.",
)

TEXTS["version_changes"] = (
    "• L’aide du contrôle qualité précise que toutes les sorties sont remesurées ; seuls les MP3 du chemin dynamique peuvent recevoir jusqu’à trois réencodages correctifs.\n"
    "• Les six voyants d’options n’affichent plus de description au survol.\n"
    "• Le résultat du contrôle qualité est entièrement traduit dans le journal, sans sigle anglais dans les autres langues.\n"
    "• Le journal et le vumètre utilisent des en-têtes de même hauteur ; le titre du vumètre reste dans sa zone et le vumètre conserve sa taille fixe.\n"
    "• Le panneau de score utilise une palette plus douce, cohérente avec le thème actif.\n"
    "• Le moteur audio et les calculs de normalisation sont inchangés.",
    "• Quality-control help now states that every output is remeasured; only dynamic-path MP3 files may receive up to three corrective re-encodes.\n"
    "• The six option lights no longer display hover descriptions.\n"
    "• Quality-control results are fully localized in the log, without an English abbreviation in other languages.\n"
    "• The log and loudness meter use equal-height headers; the meter title stays in its area and the meter keeps its fixed size.\n"
    "• The score panel uses a softer palette consistent with the active theme.\n"
    "• The audio engine and normalization calculations are unchanged.",
)

# French and English live in the tuple catalogue rather than EXTRA_TEXTS.
TEXTS["version_changes"] = (
    TRANSLATION_UPDATES_12406["fr"]["version_changes"],
    TRANSLATION_UPDATES_12406["en"]["version_changes"],
)

# These labels were historically confined to core/report code.  Give them a
# tuple-catalogue fallback before merging the three new complete catalogues so
# ``translate`` remains safe even when an integration requests them directly.
TEXTS.setdefault(
    "warning_list_title",
    ("Alertes du traitement", "Processing warnings"),
)
TEXTS.setdefault(
    "error_list_title",
    ("Erreurs du traitement", "Processing errors"),
)
TEXTS.setdefault("status_compliant", ("CONFORME", "COMPLIANT"))

for _key in (
    "loudness_meter_current_file",
    "loudness_meter_no_file",
    "loudness_meter_worst_file",
    "loudness_meter_worst_file_detail",
    "loudness_meter_help_text",
    "loudness_meter_tooltip",
    "loudness_score_tooltip",
):
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12406["fr"][_key],
        TRANSLATION_UPDATES_12406["en"][_key],
    )

for _key in (
    "loudness_meter_help_text",
    "loudness_meter_tooltip",
    "loudness_score_tooltip",
    "quality_control_tooltip",
    "option_status_overwrite",
    "option_status_skip_compliant",
    "option_status_resume",
    "option_status_quality_control",
    "option_status_report",
    "option_status_auto_start",
    "version_changes",
):
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12407["fr"][_key],
        TRANSLATION_UPDATES_12407["en"][_key],
    )

for _key in (
    "help_overview",
    "loudness_meter_help_text",
    "loudness_score_check",
    "loudness_score_tooltip",
    "save_dialog_location",
    "save_dialog_filename",
    "save_dialog_filetype",
    "save_dialog_save",
    "save_dialog_cancel",
    "version_changes",
):
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12408["fr"][_key],
        TRANSLATION_UPDATES_12408["en"][_key],
    )

for _language, _updates in NEW_LANGUAGE_TEXTS_12410.items():
    EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _language, _updates in TRANSLATION_UPDATES_12410.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12410["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12410["fr"][_key],
        TRANSLATION_UPDATES_12410["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12412.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12412["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12412["fr"][_key],
        TRANSLATION_UPDATES_12412["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12413.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12413["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12413["fr"][_key],
        TRANSLATION_UPDATES_12413["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12414.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12414["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12414["fr"][_key],
        TRANSLATION_UPDATES_12414["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12415.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12415["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12415["fr"][_key],
        TRANSLATION_UPDATES_12415["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12416.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12416["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12416["fr"][_key],
        TRANSLATION_UPDATES_12416["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12417.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12417["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12417["fr"][_key],
        TRANSLATION_UPDATES_12417["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12418.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12418["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12418["fr"][_key],
        TRANSLATION_UPDATES_12418["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12419.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12419["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12419["fr"][_key],
        TRANSLATION_UPDATES_12419["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12420.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12420["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12420["fr"][_key],
        TRANSLATION_UPDATES_12420["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12421.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12421["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12421["fr"][_key],
        TRANSLATION_UPDATES_12421["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12422.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12422["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12422["fr"][_key],
        TRANSLATION_UPDATES_12422["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12423.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12423["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12423["fr"][_key],
        TRANSLATION_UPDATES_12423["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12424.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12424["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12424["fr"][_key],
        TRANSLATION_UPDATES_12424["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12425.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12425["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12425["fr"][_key],
        TRANSLATION_UPDATES_12425["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12426.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12426["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12426["fr"][_key],
        TRANSLATION_UPDATES_12426["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12427.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12427["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12427["fr"][_key],
        TRANSLATION_UPDATES_12427["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12428.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12428["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12428["fr"][_key],
        TRANSLATION_UPDATES_12428["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12429.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12429["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12429["fr"][_key],
        TRANSLATION_UPDATES_12429["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12430.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12430["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12430["fr"][_key],
        TRANSLATION_UPDATES_12430["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12431.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12431["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12431["fr"][_key],
        TRANSLATION_UPDATES_12431["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12432.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12432["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12432["fr"][_key],
        TRANSLATION_UPDATES_12432["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12433.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12433["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12433["fr"][_key],
        TRANSLATION_UPDATES_12433["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12434.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12434["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12434["fr"][_key],
        TRANSLATION_UPDATES_12434["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12435.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12435["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12435["fr"][_key],
        TRANSLATION_UPDATES_12435["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_12500.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_12500["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_12500["fr"][_key],
        TRANSLATION_UPDATES_12500["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20000.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20000["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20000["fr"][_key],
        TRANSLATION_UPDATES_20000["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20100.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20100["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20100["fr"][_key],
        TRANSLATION_UPDATES_20100["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20200.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20200["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20200["fr"][_key],
        TRANSLATION_UPDATES_20200["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20300.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20300["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20300["fr"][_key],
        TRANSLATION_UPDATES_20300["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20400.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20400["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20400["fr"][_key],
        TRANSLATION_UPDATES_20400["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20500.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20500["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20500["fr"][_key],
        TRANSLATION_UPDATES_20500["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20600.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20600["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20600["fr"][_key],
        TRANSLATION_UPDATES_20600["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20700.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20700["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20700["fr"][_key],
        TRANSLATION_UPDATES_20700["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20800.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20800["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20800["fr"][_key],
        TRANSLATION_UPDATES_20800["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_20900.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_20900["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_20900["fr"][_key],
        TRANSLATION_UPDATES_20900["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201000.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201000["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201000["fr"][_key],
        TRANSLATION_UPDATES_201000["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201100.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201100["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201100["fr"][_key],
        TRANSLATION_UPDATES_201100["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201200.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201200["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201200["fr"][_key],
        TRANSLATION_UPDATES_201200["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201300.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201300["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201300["fr"][_key],
        TRANSLATION_UPDATES_201300["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201400.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201400["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201400["fr"][_key],
        TRANSLATION_UPDATES_201400["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201500.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201500["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201500["fr"][_key],
        TRANSLATION_UPDATES_201500["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201600.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201600["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201600["fr"][_key],
        TRANSLATION_UPDATES_201600["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_201700.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_201700["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_201700["fr"][_key],
        TRANSLATION_UPDATES_201700["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_211000.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_211000["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_211000["fr"][_key],
        TRANSLATION_UPDATES_211000["en"][_key],
    )

for _language, _updates in TRANSLATION_UPDATES_211100.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS.setdefault(_language, {}).update(_updates)

for _key in TRANSLATION_UPDATES_211100["fr"]:
    TEXTS[_key] = (
        TRANSLATION_UPDATES_211100["fr"][_key],
        TRANSLATION_UPDATES_211100["en"][_key],
    )

# The level-mode selector and its grouped-processing implementation were
# removed in 1.24.33.  Historical update modules remain readable as release
# records, but their retired keys must no longer be reachable at runtime.
_REMOVED_LEVEL_MODE_KEYS = {
    "album_analysis_help_text",
    "album_analysis_live_progress",
    "album_analysis_progress_bar",
    "album_analysis_reason_log",
    "album_gain_detail",
    "album_gain_log",
    "album_measurement_error",
    "album_measurement_progress",
    "album_mode_log",
    "album_qc_ok",
    "album_simulation_levels_log",
    "album_simulation_notice_log",
    "album_simulation_summary_log",
    "album_track_measurement_progress",
    "albums_measurement",
    "guide_album_advanced_body",
    "guide_album_advanced_title",
    "level_mode",
    "loudness_comparison_album_simulation_note",
    "loudness_comparison_album_simulation_waiting",
    "mode_album",
    "mode_album_label",
    "mode_tooltip",
    "mode_track",
    "mode_track_label",
    "operation_analyze_album",
    "report_album_dbtp",
    "report_album_lufs",
    "silent_album_copy",
    "simulate_album",
    "track_mode_log",
    "zero_album_gain",
}
for _key in _REMOVED_LEVEL_MODE_KEYS:
    TEXTS.pop(_key, None)
    for _localized in EXTRA_TEXTS.values():
        _localized.pop(_key, None)


def translate(language: str, key: str, **values: Any) -> str:
    if language in EXTRA_TEXTS:
        template = EXTRA_TEXTS[language].get(key, TEXTS[key][1])
    else:
        selected = 1 if language == "en" else 0
        template = TEXTS[key][selected]
    return template.format(**values)
