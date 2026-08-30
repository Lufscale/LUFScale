"""Final standalone translation catalogue for LUFScale 2.1.12 on Windows."""

from __future__ import annotations

LANGUAGES = (('fr', 'Français'),
 ('en', 'English'),
 ('es', 'Español'),
 ('it', 'Italiano'),
 ('pt', 'Português'),
 ('ru', 'Русский'),
 ('ja', '日本語'),
 ('hi', 'हिन्दी'),
 ('zh', '简体中文'),
 ('ko', '한국어'),
 ('id', 'Bahasa Indonesia'),
 ('tr', 'Türkçe'))

TEXTS = {'activity_cancelled': ('Activité : traitement annulé', 'Activity: processing cancelled'),
 'activity_cancelling': ('Activité : annulation en cours…', 'Activity: cancelling…'),
 'activity_completed': ('Activité : traitement terminé', 'Activity: processing completed'),
 'activity_compliant': ('Conformes : {count}', 'Compliant: {count}'),
 'activity_detected': ('Activité : {total} fichier(s) détecté(s)', 'Activity: {total} file(s) detected'),
 'activity_errors': ('Erreurs : {count}', 'Errors: {count}'),
 'activity_files': ('Fichiers : {count}', 'Files: {count}'),
 'activity_idle': ('Activité : en attente', 'Activity: waiting'),
 'activity_preparing': ('Activité : préparation des fichiers…', 'Activity: preparing files…'),
 'activity_progress': ('{total} fichiers • réussis {success} • alertes {warnings} • erreurs {failed} • repris/ignorés '
                       '{skipped} • conformes {compliant}',
                       '{total} files • successful {success} • warnings {warnings} • errors {failed} • resumed/skipped '
                       '{skipped} • compliant {compliant}'),
 'activity_skipped': ('Repris/ignorés : {count}', 'Resumed/skipped: {count}'),
 'activity_successes': ('Réussis : {count}', 'Successful: {count}'),
 'activity_warnings': ('Alertes : {count}', 'Warnings: {count}'),
 'adaptive_disabled_log': ('Analyse adaptative — sondes rapides arrêtées après {sample} mesures ({successes} succès, '
                           'gain estimé {percent:+.1f} %).',
                           'Adaptive analysis — fast probes stopped after {sample} measurements ({successes} '
                           'successes, estimated saving {percent:+.1f}%).'),
 'add_folders': ('Ajouter des dossiers…', 'Add folders…'),
 'add_mp3': ('Ajouter des fichiers audio…', 'Add audio files…'),
 'add_replaygain': ('Ajouter ReplayGain', 'Add ReplayGain'),
 'add_source_files': ('Ajouter des fichiers audio', 'Add audio files'),
 'add_source_folder': ('Ajouter un dossier source', 'Add a source folder'),
 'already_completed': ('Déjà terminé lors d’une exécution précédente.', 'Already completed during a previous run.'),
 'already_compliant_badge': ('CONFORME', 'COMPLIANT'),
 'already_compliant_copy': ('Déjà conforme : copie audio à l’identique, sans réencodage.',
                            'Already compliant: copied unchanged without audio re-encoding.'),
 'already_compliant_log': ('déjà conforme, sans réencodage', 'already compliant, no re-encoding'),
 'analysis_cache_summary': ('Cache d’analyse — {hits} mesure(s) réutilisée(s).',
                            'Analysis cache — {hits} measurement(s) reused.'),
 'analysis_impossible': ('Analyse impossible : {error}', 'Analysis failed: {error}'),
 'analysis_measurement_progress': ('Analyse {current}/{total} — {file} — {value}',
                                   'Analysis {current}/{total} — {file} — {value}'),
 'analysis_method': ('Méthode d’analyse', 'Analysis method'),
 'analysis_method_adaptive': ('Adaptatif — arrêt si non rentable', 'Adaptive — stops when unprofitable'),
 'analysis_method_fast': ('Rapide — expérimental', 'Fast — experimental'),
 'analysis_method_historical': ('Historique — référence', 'Historical — reference'),
 'analysis_method_log': ('Méthode d’analyse — {method}.', 'Analysis method — {method}.'),
 'analysis_method_tooltip': ('La version stable utilise automatiquement la mesure historique complète, seule méthode '
                             'validée sur le corpus de référence. Les variantes Rapide et Adaptatif ne sont plus '
                             'proposées.',
                             'The stable version automatically uses the full historical measurement, the only method '
                             'validated on the reference corpus. Fast and Adaptive are no longer offered.'),
 'analysis_progress': ('Analyse {current}/{total} : {file}', 'Analysis {current}/{total}: {file}'),
 'analysis_progress_help_text': ('En mode Analyser seulement, le graphique Avant, le journal et la barre de '
                                 'progression avancent fichier par fichier dès qu’une mesure est terminée ; Après '
                                 'reste immobile.',
                                 'In Analyze-only mode, the Before graph, log, and progress bar advance file by file '
                                 'as each measurement finishes; After stays still.'),
 'analyze': ('Analyser', 'Analyze'),
 'analyze_only_fresh_help_text': ('Analyser seulement remesure entièrement chaque source avec FFmpeg à chaque '
                                  'lancement. Le graphique Avant et la progression avancent fichier par fichier. Aucun '
                                  'fichier audio ni contrôle qualité de sortie n’est créé.',
                                  'Analyze-only fully remeasures every source with FFmpeg on each run. The Before '
                                  'graph and progress advance file by file. No audio file or output quality control is '
                                  'created.'),
 'analyze_operation': ('analyse/simulation', 'analysis/simulation'),
 'analyzed_progress': ('Analysé : {file}', 'Analyzed: {file}'),
 'app_name': ('LUFScale', 'LUFScale'),
 'audio_copy_replaygain': ('Flux audio copié sans réencodage ; balises ReplayGain ajoutées.',
                           'Audio stream copied without re-encoding; ReplayGain tags added.'),
 'audio_tab': ('Audio', 'Audio'),
 'auto_start': ('Démarrer automatiquement après un dépôt ou un collage', 'Start automatically after a drop or paste'),
 'auto_start_tooltip': ('Lance automatiquement le traitement après l’ajout de sources par glisser-déposer ou collage, '
                        'si une destination est déjà choisie.',
                        'Automatically starts processing after sources are added by drag-and-drop or paste, when a '
                        'destination has already been selected.'),
 'cancel': ('Annuler', 'Cancel'),
 'cancelled_summary': ('Annulé — {success} réussi(s), {failed} erreur(s), {skipped} repris/ignoré(s), {warnings} '
                       'alerte(s), {compliant} conforme(s) — {duration}.',
                       'Cancelled — {success} successful, {failed} error(s), {skipped} resumed/skipped, {warnings} '
                       'warning(s), {compliant} compliant — {duration}.'),
 'cancelling': ('Annulation en cours…', 'Cancelling…'),
 'choose': ('Choisir…', 'Choose…'),
 'choose_output': ('Choisir le dossier de destination', 'Choose the destination folder'),
 'clipboard': ('Presse-papiers', 'Clipboard'),
 'clipboard_empty': ('Le presse-papiers ne contient aucun chemin de dossier ou fichier audio compatible.',
                     'The clipboard does not contain a valid folder or supported audio-file path.'),
 'close_button': ('Fermer', 'Close'),
 'close_question': ('Annuler le traitement et fermer l’application ?', 'Cancel processing and close the application?'),
 'completed_dialog_summary': ('État : terminé\n'
                              'Fichiers : {files}\n'
                              'Réussis : {success}\n'
                              'Erreurs : {failed}\n'
                              'Repris ou ignorés : {skipped}\n'
                              'Alertes : {warnings}\n'
                              'Conformes : {compliant}\n'
                              'Temps total : {duration}',
                              'Status: completed\n'
                              'Files: {files}\n'
                              'Successful: {success}\n'
                              'Errors: {failed}\n'
                              'Resumed or skipped: {skipped}\n'
                              'Warnings: {warnings}\n'
                              'Compliant: {compliant}\n'
                              'Total time: {duration}'),
 'completed_summary': ('Terminé — {success} réussi(s), {failed} erreur(s), {skipped} repris/ignoré(s), {warnings} '
                       'alerte(s), {compliant} conforme(s) — {duration}.',
                       'Completed — {success} successful, {failed} error(s), {skipped} resumed/skipped, {warnings} '
                       'warning(s), {compliant} compliant — {duration}.'),
 'completed_with_errors': ('Traitement terminé avec alertes', 'Processing completed with warnings'),
 'convert': ('Uniformiser', 'Normalize'),
 'convert_operation': ('uniformisation audio', 'audio normalization'),
 'cpu_tooltip': ('Utilisation totale du processeur du système, mise à jour chaque seconde pendant le traitement.',
                 'Total system CPU usage, updated every second during processing.'),
 'cpu_unavailable': ('N/D', 'N/A'),
 'cpu_usage': ('CPU', 'CPU'),
 'create_report': ('Créer un rapport CSV', 'Create a CSV report'),
 'csv_file_filter': ('Fichiers CSV (*.csv)', 'CSV files (*.csv)'),
 'custom': ('Personnalisé', 'Custom'),
 'decrease_value': ('Diminuer la valeur', 'Decrease value'),
 'description': ('Uniformise le volume perçu fichier par fichier, sans modifier les originaux.',
                 'Balances perceived loudness file by file without changing the originals.'),
 'destination': ('Destination', 'Destination'),
 'destination_error': ('ERREUR — destination inaccessible : {error}', 'ERROR — destination unavailable: {error}'),
 'destination_path_tooltip': ('Cliquez dans le chemin, puis utilisez les flèches, Début/Fin ou la molette. Le chemin '
                              'est sélectionnable et copiable, mais non modifiable.',
                              'Click the path, then use the arrow keys, Home/End or the mouse wheel. The path can be '
                              'selected and copied, but not edited.'),
 'destination_required_start': ('Choisissez d’abord le dossier de destination avec le bouton « Choisir… ».',
                                'First choose the destination folder with the “Choose…” button.'),
 'dialog_ok': ('OK', 'OK'),
 'drop_subtitle': ('MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — sous-dossiers acceptés',
                   'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — subfolders supported'),
 'drop_title': ('Déposez ici vos dossiers ou fichiers audio', 'Drop folders or audio files here'),
 'elapsed_time': ('Temps écoulé : {duration}', 'Elapsed time: {duration}'),
 'error_list_title': ('Erreurs du traitement', 'Processing errors'),
 'error_progress': ('Erreur : {file}', 'Error: {file}'),
 'errors_button': ('Erreurs ({count})', 'Errors ({count})'),
 'errors_button_tooltip': ('Ouvre la liste des erreurs avec le nom du fichier, son chemin et le détail. Disponible '
                           'pendant une pause ou après le traitement.',
                           'Opens the error list with filename, path, and details. Available while paused or after '
                           'processing.'),
 'errors_dialog_title': ('Erreurs du traitement', 'Processing errors'),
 'estimated_result': ('Résultat estimé, aucun fichier créé.', 'Estimated result; no file created.'),
 'estimated_total_calculating': ('Temps total estimé : calcul en cours…', 'Estimated total time: calculating…'),
 'estimated_total_time': ('Temps total estimé : {duration}', 'Estimated total time: {duration}'),
 'estimated_total_time_with_day_finish': ('Temps total estimé : {duration} — {days} j. {time}',
                                          'Estimated total time: {duration} — {days} d. {time}'),
 'estimated_total_time_with_finish': ('Temps total estimé : {duration} — {time}',
                                      'Estimated total time: {duration} — {time}'),
 'estimated_total_unavailable': ('Temps total estimé : non disponible', 'Estimated total time: unavailable'),
 'ffmpeg_download_button': ('Ouvrir le site officiel FFmpeg', 'Open the official FFmpeg website'),
 'ffmpeg_error_no_detail': ('Erreur FFmpeg sans détail.', 'FFmpeg error without details.'),
 'ffmpeg_execution_error': ('Impossible d’exécuter FFmpeg : {error}', 'Unable to run FFmpeg: {error}'),
 'ffmpeg_incompatible': ('FFmpeg incompatible', 'Incompatible FFmpeg'),
 'ffmpeg_missing': ('FFmpeg introuvable', 'FFmpeg not found'),
 'ffmpeg_missing_encoders': ('Cette version de FFmpeg ne contient pas tous les encodeurs audio requis : {encoders}.',
                             'This FFmpeg build does not include all required audio encoders: {encoders}.'),
 'ffmpeg_missing_message': ('FFmpeg doit être installé et accessible dans le PATH, ou placé à côté du programme.',
                            'FFmpeg must be installed and available in PATH, or placed next to the program.'),
 'ffmpeg_no_lame': ('Cette version de FFmpeg ne contient pas l’encodeur MP3 libmp3lame.',
                    'This FFmpeg build does not include the libmp3lame MP3 encoder.'),
 'ffmpeg_no_loudnorm': ('Cette version de FFmpeg ne contient pas le filtre loudnorm.',
                        'This FFmpeg build does not include the loudnorm filter.'),
 'ffmpeg_not_responding': ('FFmpeg ne répond pas correctement.', 'FFmpeg is not responding correctly.'),
 'file_exists': ('Le fichier existe déjà.', 'The file already exists.'),
 'files_found': ('{total} fichier(s) audio trouvé(s) — {operation} — {parallel} traitement(s) parallèle(s).',
                 '{total} audio file(s) found — {operation} — {parallel} parallel process(es).'),
 'finalization_completed': ('Finalisation terminée en {duration}.', 'Finalization completed in {duration}.'),
 'finalizing': ('Finalisation — rapport, cache d’analyse et données de reprise…',
                'Finalizing — report, analysis cache and resume data…'),
 'folder': ('Dossier', 'Folder'),
 'folder_unavailable': ('Dossier inaccessible', 'Folder unavailable'),
 'guide_analysis_method': ('LUFScale utilise automatiquement la mesure historique complète, seule méthode validée sur '
                           'le corpus de référence.',
                           'LUFScale automatically uses the full historical measurement, the only method validated on '
                           'the reference corpus.'),
 'guide_analyze_prediction_body': ('Analyser seulement peut calculer une estimation à partir de la mesure source, mais '
                                   'ne crée ni fichier audio ni contrôle qualité de sortie.',
                                   'Analyze-only may calculate an estimate from the source measurement, but creates no '
                                   'audio file and no output quality control.'),
 'guide_analyze_prediction_title': ('Estimation sans sortie', 'Estimate without output'),
 'guide_build_body': ('Sous Windows 10 1809 ou ultérieur, ou Windows 11 x86-64 :\n'
                      '\n'
                      '1. Téléchargez « LUFScale-2.1.12-Setup-x64.exe » avec son fichier SHA-256.\n'
                      '2. Vérifiez le SHA-256, puis double-cliquez sur l’installateur.\n'
                      '3. Lisez et acceptez la licence GNU GPL, puis suivez l’assistant.\n'
                      '4. Lancez LUFScale depuis le menu Démarrer.\n'
                      '\n'
                      'L’application, Python, PySide6/Qt, FFmpeg, les codecs, les guides et les licences sont déjà '
                      'inclus. L’installation ne télécharge rien et ne demande aucune commande PowerShell. Un '
                      'désinstalleur Windows est créé automatiquement.\n'
                      '\n'
                      'La distribution communautaire n’est pas signée ; après vérification du fichier et de sa '
                      'somme, Windows SmartScreen peut demander une confirmation.',
                      'On x86-64 Windows 10 1809 or later, or Windows 11:\n'
                      '\n'
                      '1. Download “LUFScale-2.1.12-Setup-x64.exe” with its SHA-256 file.\n'
                      '2. Verify SHA-256, then double-click the installer.\n'
                      '3. Read and accept the GNU GPL licence, then follow the wizard.\n'
                      '4. Start LUFScale from the Start menu.\n'
                      '\n'
                      'The application, Python, PySide6/Qt, FFmpeg, codecs, guides and licences are already included. '
                      'Setup downloads nothing and requires no PowerShell command. A Windows uninstaller is created '
                      'automatically.\n'
                      '\n'
                      'The community distribution is unsigned; after checking the file and its checksum, Windows '
                      'SmartScreen may request confirmation.'),
 'guide_build_title': ('Installer LUFScale sous Windows x86-64', 'Install LUFScale on Windows x86-64'),
 'guide_estimated_total_help': ('Temps total estimé : 12 min - fin vers 14:30. « 12 min » est la durée totale estimée '
                                'et « 14:30 » l’heure de fin prévue. Si la fin dépasse minuit, le nombre de jours '
                                's’ajoute automatiquement devant l’heure, par exemple « 2 j. 14:30 ».',
                                'Estimated total time: 12 min - finishing around 14:30. “12 min” is the estimated '
                                'total duration and “14:30” the expected finish time. If completion passes midnight, '
                                'the day count is automatically added before the time, for example “2 d. 14:30”.'),
 'guide_file_processing_body': ('Chaque fichier reçoit sa propre mesure et son propre gain pour se rapprocher de la '
                                'cible LUFS choisie, sous la limite True Peak.',
                                'Every file receives its own measurement and gain to approach the selected LUFS target '
                                'under the True Peak limit.'),
 'guide_file_processing_title': ('Traitement fichier par fichier', 'File-by-file processing'),
 'guide_help_tooltip': ('Ouvre le guide PDF complet dans la langue sélectionnée.',
                        'Opens the complete PDF guide in the selected language.'),
 'guide_level_mode_body': ('Piste - recommandé : rapproche chaque fichier de la cible. Album - avancé et spécialisé : '
                           'applique un gain commun et conserve les contrastes. Utilisez Album pour une œuvre écoutée '
                           'dans son ordre ; Piste pour la lecture aléatoire ou un niveau régulier fichier par '
                           'fichier.',
                           'Track - recommended: brings each file toward target. Album - advanced and specialized: '
                           'applies one shared gain and preserves contrasts. Use Album for a work heard in order; '
                           'Track for shuffle playback or a consistent file-to-file level.'),
 'guide_license_body': ('LUFScale est un logiciel libre distribué sous GNU GPL-3.0-or-later. Cette licence autorise '
                        'son utilisation, son étude, sa modification et sa redistribution selon ses conditions. Les '
                        'sources, avis et licences tierces accompagnent la distribution. Le logiciel est fourni sans '
                        'garantie.',
                        'LUFScale is free software distributed under GNU GPL-3.0-or-later. This licence permits use, '
                        'study, modification and redistribution under its terms. Source code, notices and third-party '
                        'licences accompany the distribution. The software is provided without warranty.'),
 'guide_license_feature': ('• Logiciel libre GNU GPL-3.0-or-later : utilisation, étude, modification et redistribution '
                           'autorisées selon la licence.\n'
                           '• Installateur Windows x86-64 hors ligne avec Python, Qt et FFmpeg intégrés. Windows 11 est '
                           'recommandé ; Windows 10 1809 ou ultérieur reste une cible de compatibilité, mais son '
                           'support standard Microsoft est terminé.',
                           '• GNU GPL-3.0-or-later free software: use, study, modification and redistribution are '
                           'permitted under the licence.\n'
                           '• Offline Windows x86-64 installer with Python, Qt and FFmpeg included. Windows 11 is '
                           'recommended; Windows 10 1809 or later remains a compatibility target, but Microsoft '
                           'standard support has ended.'),
 'guide_license_title': ('Logiciel libre et redistribution', 'Free software and redistribution'),
 'guide_log_legend_cancelled': ('Traitement interrompu volontairement ; ce n’est pas une erreur.',
                                'Processing was intentionally stopped; this is not an error.'),
 'guide_log_legend_compliant': ('Copie audio inchangée : la source respectait déjà la cible et la limite de crête.',
                                'Unchanged audio copy: the source already met the target and peak limit.'),
 'guide_log_legend_error': ('Le fichier concerné n’a pas pu être terminé.',
                            'The affected file could not be completed.'),
 'guide_log_legend_success': ('Traitement terminé sans anomalie détectée.',
                              'Processing completed with no detected anomaly.'),
 'guide_log_legend_warning': ('La sortie existe, mais une mesure dépasse la tolérance prévue.',
                              'The output exists, but one measurement is outside the expected tolerance.'),
 'guide_missing_message': ('Le guide PDF n’a pas été trouvé : {path}', 'The PDF guide could not be found: {path}'),
 'guide_missing_title': ('Guide indisponible', 'Guide unavailable'),
 'guide_open_error': ('Impossible d’ouvrir le guide PDF : {path}', 'The PDF guide could not be opened: {path}'),
 'guide_quality_priority_body': ('LUFScale mesure la sonie de vos fichiers et, avec Uniformiser, ajuste réellement '
                                 'leur volume perçu vers une cible LUFS tout en contrôlant la crête vraie. Chaque '
                                 'source est analysée sur toute sa durée, puis la sortie est remesurée et vérifiée. Le '
                                 'résultat ne dépend pas de balises ni d’un lecteur compatible : le niveau devient '
                                 'plus cohérent entre les fichiers, les écarts sont signalés et les originaux restent '
                                 'intacts.',
                                 'LUFScale measures file loudness and, with Normalize, physically adjusts perceived '
                                 'volume toward a LUFS target while controlling true peak. Each source is analysed '
                                 'over its full duration, then the output is remeasured and verified. The result does '
                                 'not depend on tags or a compatible player: levels become more consistent across '
                                 'files, deviations are flagged, and originals remain untouched.'),
 'guide_quality_priority_title': ('À quoi sert LUFScale ?', 'What does LUFScale do?'),
 'help_button': ('Aide', 'Help'),
 'help_overview': ('• Normalisation réelle, ReplayGain ou analyse des formats MP3, FLAC, WAV, AIFF, M4A, OGG et Opus.\n'
                   '• Chaque fichier est mesuré et traité séparément vers la cible choisie.\n'
                   '• Arborescence, métadonnées et pochettes sont conservées lorsque FFmpeg peut les recopier.\n'
                   '• Les originaux ne sont jamais déplacés ni modifiés.\n'
                   '• Parallélisme Auto, cache d’analyse et reprise après interruption.\n'
                   '• Contrôle qualité, rapport CSV, progression, CPU et historiques LUFS Avant/Après.\n'
                   '• Interface et guides PDF en 12 langues.',
                   '• True normalization, ReplayGain or analysis for MP3, FLAC, WAV, AIFF, M4A, OGG and Opus.\n'
                   '• Every file is measured and processed separately toward the selected target.\n'
                   '• Folder structure, metadata and artwork are preserved when FFmpeg can copy them.\n'
                   '• Originals are never moved or modified.\n'
                   '• Auto parallelism, analysis cache and resume after interruption.\n'
                   '• Quality control, CSV report, progress, CPU and Before/After LUFS histories.\n'
                   '• Interface and PDF guides in 12 languages.'),
 'help_title': ('Principales caractéristiques', 'Main features'),
 'increase_value': ('Augmenter la valeur', 'Increase value'),
 'input_lufs_log': ('entrée {value} LUFS', 'input {value} LUFS'),
 'interface_ffmpeg_message': ('Le moteur audio FFmpeg intégré est absent ou inutilisable. Réinstallez LUFScale depuis '
                              'l’archive complète de distribution.',
                              'The bundled FFmpeg audio engine is missing or unusable. Reinstall LUFScale from the '
                              'complete distribution archive.'),
 'internal_error': ('Erreur interne : {error}', 'Internal error: {error}'),
 'interrupted': ('Traitement interrompu.', 'Processing interrupted.'),
 'invalid_location': ('Emplacement invalide', 'Invalid location'),
 'issue_detail_column': ('Détail', 'Details'),
 'issue_file_column': ('Fichier', 'File'),
 'issue_path_column': ('Chemin', 'Path'),
 'language': ('Langue', 'Language'),
 'language_tooltip': ('Change immédiatement la langue de l’interface, des messages et des futurs rapports CSV. Les '
                      'douze choix disposent chacun d’un catalogue et d’un guide dédiés. Le choix est mémorisé.',
                      'Immediately changes the interface, messages, and future CSV reports. Each of the twelve choices '
                      'has its own catalogue and guide. The choice is remembered.'),
 'log_help_text': ('Chaque ligne concerne un fichier ou une étape générale.\n'
                   '\n'
                   '• Une ligne réussie commence directement par le nom du fichier : RÉUSSI n’est plus répété.\n'
                   '• CONFORME, REPRIS, IGNORÉ, ANNULÉ et ERREUR restent affichés lorsqu’ils apportent une information '
                   'utile.\n'
                   '• Les niveaux indiquent l’entrée → la sortie remesurée, puis le résultat éventuel du contrôle '
                   'qualité.\n'
                   '• Les boutons Alertes et Erreurs ouvrent des listes indépendantes avec le nom, le chemin et le '
                   'détail. Ils sont disponibles pendant une pause ou après le traitement, et chaque liste peut être '
                   'enregistrée.\n'
                   '\n'
                   'Couleurs : vert = réussite ; orange = alerte ; rouge = fichier non terminé ; violet bleuté = '
                   'reprise ; gris = information, élément ignoré ou annulation.\n'
                   '\n'
                   'QC ALERTE — sonie signifie que la sortie remesurée diffère de la valeur attendue de plus de ±0,60 '
                   'LU. Une valeur plus négative est plus basse ; une valeur moins négative est plus forte. L’écart '
                   'est la valeur absolue de la différence : -14,69 au lieu de -14,00 donne 0,69 LU. Le fichier est '
                   'tout de même créé : ce n’est pas une erreur de conversion. Aucune action n’est obligatoire si le '
                   'résultat convient à l’écoute ; si la cible doit être stricte, consultez le détail et le CSV, puis '
                   'vérifiez la cible et le plafond True Peak avant de réessayer. Le message seul ne permet pas '
                   'd’attribuer avec certitude l’écart au plafond, à l’encodeur ou à une limite de correction.\n'
                   '\n'
                   'QC ALERTE — crête signifie que la crête vraie remesurée dépasse de plus de 0,25 dB la limite '
                   'choisie. Le fichier est tout de même créé. Pour une alerte persistante, choisissez une cible LUFS '
                   'plus basse ou une crête maximale plus prudente, par exemple -2,0 dBTP, puis relancez le fichier.\n'
                   '\n'
                   'Les temps cumulés additionnent le travail de tous les traitements parallèles. Le temps total '
                   'correspond à la durée réellement écoulée.',
                   'Each line concerns a file or a general processing step.\n'
                   '\n'
                   '• A successful line starts directly with the filename: SUCCESS is no longer repeated.\n'
                   '• COMPLIANT, RESUMED, SKIPPED, CANCELLED and ERROR remain when they add useful information.\n'
                   '• Levels show input → remeasured output, followed by any quality-control result.\n'
                   '• Warnings and Errors open separate lists containing filename, path and details. They are '
                   'available while paused or after processing, and each list can be saved.\n'
                   '\n'
                   'Colours: green = success; orange = warning; red = unfinished file; blue-purple = resumed; grey = '
                   'information, skipped item or cancellation.\n'
                   '\n'
                   'QC WARNING — loudness means the remeasured output differs from its expected value by more than '
                   '±0.60 LU. A more negative value is quieter; a less negative value is louder. The deviation is the '
                   'absolute difference: -14.69 instead of -14.00 is 0.69 LU. The file is still created; this is not a '
                   'conversion failure. No action is required if it sounds acceptable. For a strict target, inspect '
                   'the details and CSV, then check the target and True Peak ceiling before retrying. The message '
                   'alone cannot prove whether the ceiling, encoder or a correction limit caused the deviation.\n'
                   '\n'
                   'QC WARNING — peak means the remeasured true peak exceeds the selected limit by more than 0.25 dB. '
                   'The file is still created. For a persistent warning, choose a lower LUFS target or a safer peak '
                   'ceiling, for example -2.0 dBTP, then process the file again.\n'
                   '\n'
                   'Cumulative times add the work of all parallel jobs. Total time is the actual elapsed duration.'),
 'log_placeholder': ('Le compte rendu apparaîtra ici.', 'The processing log will appear here.'),
 'log_title': ('Journal de traitement', 'Processing log'),
 'loudness_comparison_after': ('Après', 'After'),
 'loudness_comparison_analysis_only': ('Aucune sortie en mode Analyser seulement', 'No output in Analyze-only mode'),
 'loudness_comparison_before': ('Avant', 'Before'),
 'loudness_comparison_help_text': ('Chaque fichier ajoute un point à droite et décale l’historique vers la gauche. '
                                   'Avant affiche toujours la source mesurée. Avec Uniformiser, Après affiche la '
                                   'sortie réellement remesurée. Avec ReplayGain, le second graphique en pointillés '
                                   'affiche une estimation de lecture : sonie source + gain inscrit dans la balise '
                                   'Track. Le signe ≈ et la mention Lecteur compatible rappellent qu’il ne s’agit pas '
                                   'd’une mesure physique du fichier livré. Un lecteur incompatible conserve le niveau '
                                   'd’origine ; un lecteur compatible peut aussi modifier le résultat selon son '
                                   'préamplificateur ou sa protection contre l’écrêtage. Les deux graphiques gardent '
                                   'la même échelle fixe de ±6 LU autour de la cible. Analyser seulement n’a pas de '
                                   'sortie Après.',
                                   'Each file adds a point on the right and moves history left. Before always shows '
                                   'the measured source. With Normalize, After shows the actually remeasured output. '
                                   'With ReplayGain, the dashed second graph shows a playback estimate: source '
                                   'loudness plus the gain stored in the Track tag. The ≈ sign and Compatible player '
                                   'note make clear that this is not a physical measurement of the delivered file. An '
                                   'incompatible player keeps the original level; a compatible player may also alter '
                                   'the result through preamp or clipping prevention. Both graphs keep the same fixed '
                                   '±6 LU scale around target. Analyze-only has no After output.'),
 'loudness_comparison_increased': ('Écart augmenté de {value} LU', 'Difference increased by {value} LU'),
 'loudness_comparison_needs_qc': ('Activez le contrôle qualité pour comparer', 'Enable quality control to compare'),
 'loudness_comparison_no_after': ('Pas de courbe Après pour cette opération', 'No After curve for this operation'),
 'loudness_comparison_not_applicable': ('Comparaison indisponible pour cette opération',
                                        'Comparison unavailable for this operation'),
 'loudness_comparison_reached': ('Cible atteinte · écart {value} LU', 'Target reached · difference {value} LU'),
 'loudness_comparison_reduced': ('Écart réduit de {value} LU', 'Difference reduced by {value} LU'),
 'loudness_comparison_replaygain_after': ('Lecture RG estimée', 'Estimated RG playback'),
 'loudness_comparison_replaygain_note': ('Lecteur compatible · audio inchangé', 'Compatible player · audio unchanged'),
 'loudness_comparison_scale': ('Vue ±{scale} LU · tol. QC ±{tolerance} LU',
                               'View ±{scale} LU · QC tol. ±{tolerance} LU'),
 'loudness_comparison_target': ('Cible {value} LUFS', 'Target {value} LUFS'),
 'loudness_comparison_title': ('Évolution de la sonie', 'Loudness change'),
 'loudness_comparison_tooltip': ('Avant montre la sonie physique. En ReplayGain, le second graphique estime la lecture '
                                 'compatible à partir du gain inscrit ; le fichier audio reste inchangé.',
                                 'Before shows physical loudness. In ReplayGain, the second graph estimates '
                                 'compatible-player playback from the stored gain; audio remains unchanged.'),
 'loudness_comparison_unchanged': ('Écart inchangé', 'Difference unchanged'),
 'loudness_comparison_waiting': ('En attente d’un fichier traité', 'Waiting for a processed file'),
 'loudness_meter_current_file': ('Dernier : {file}', 'Latest: {file}'),
 'loudness_meter_estimated': ('Estimé', 'Estimated'),
 'loudness_meter_help_text': ('Le trait rouge est la cible et la valeur bleue est la sonie réellement remesurée de la '
                              'dernière sortie. Elle monte ou descend à chaque fichier. Le score résume les 8 '
                              'dernières sorties remesurées. Si le panneau rouge indique « Voir les alertes », mettez '
                              'le traitement en pause ou attendez sa fin, puis ouvrez Alertes pour identifier les '
                              'fichiers concernés. Le vumètre reste inactif sans contrôle qualité.',
                              'The red line is the target and the blue value is the latest output’s genuinely '
                              'remeasured loudness. It moves up or down for every file. The score summarizes the '
                              'latest 8 remeasured outputs. If the red panel says “View warnings”, pause processing or '
                              'wait for it to finish, then open Warnings to identify the affected files. The meter '
                              'stays inactive without quality control.'),
 'loudness_meter_maximum': ('Max {value}', 'Max {value}'),
 'loudness_meter_measured': ('Mesuré', 'Measured'),
 'loudness_meter_minimum': ('Min {value}', 'Min {value}'),
 'loudness_meter_no_file': ('En attente d’une analyse', 'Waiting for an analysis'),
 'loudness_meter_target': ('Cible {value} LUFS', 'Target {value} LUFS'),
 'loudness_meter_title': ('Vumètre de sonie', 'Loudness meter'),
 'loudness_meter_tooltip': ('Cible en rouge ; sonie réellement remesurée de la dernière sortie en bleu.',
                            'Red target; latest output’s genuinely remeasured loudness in blue.'),
 'loudness_meter_waiting': ('En attente d’un fichier audio', 'Waiting for an audio file'),
 'loudness_meter_worst_file': ('Plus grand écart : {file}', 'Largest error: {file}'),
 'loudness_meter_worst_file_detail': ('Plus grand écart des 8 dernières analyses : {file} — {measured} LUFS pour '
                                      '{expected} LUFS, écart {deviation} LU.',
                                      'Largest error in the latest 8 analyses: {file} — {measured} LUFS for {expected} '
                                      'LUFS, {deviation} LU error.'),
 'loudness_score_acceptable': ('Acceptable', 'Acceptable'),
 'loudness_score_check': ('Voir les alertes', 'View warnings'),
 'loudness_score_excellent': ('Excellent', 'Excellent'),
 'loudness_score_good': ('Bon', 'Good'),
 'loudness_score_needs_qc': ('Score cible : activez le contrôle qualité', 'Target score: enable quality control'),
 'loudness_score_not_applicable': ('Score cible : non applicable', 'Target score: not applicable'),
 'loudness_score_tooltip': ('Le score utilise les 8 dernières sorties réellement remesurées. 100 = résultat exact, 50 '
                            '= écart RMS de 0,60 LU et 0 = 1,20 LU ou plus. Le panneau rouge implique qu’au moins une '
                            'alerte de sonie peut être consultée avec le bouton Alertes.',
                            'The score uses the latest 8 genuinely remeasured outputs. 100 is exact, 50 is 0.60 LU RMS '
                            'error, and 0 is 1.20 LU or more. A red panel means at least one loudness warning can be '
                            'reviewed with the Warnings button.'),
 'loudness_score_value': ('Score cible : {score}/100\n{rating}\nÉcart RMS : {deviation}\xa0LU',
                          'Target score: {score}/100\n{rating}\nRMS error: {deviation}\xa0LU'),
 'loudness_score_waiting': ('Score cible : en attente', 'Target score: waiting'),
 'measurement_unavailable': ('Mesure indisponible.', 'Measurement unavailable.'),
 'mp3': ('Audio', 'Audio'),
 'mp3_filter': ('Audio compatible (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
                'Supported audio (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)'),
 'no_folder': ('Aucun dossier choisi', 'No folder selected'),
 'no_mp3': ('Aucun fichier audio compatible trouvé.', 'No supported audio files were found.'),
 'no_new_source': ('Aucun nouveau dossier ou fichier audio compatible n’a été ajouté.',
                   'No new valid folder or supported audio file was added.'),
 'not_performed': ('Non effectué', 'Not performed'),
 'open_output_error': ('Impossible d’ouvrir le dossier de destination : {error}',
                       'The destination folder could not be opened: {error}'),
 'operation': ('Opération', 'Operation'),
 'operation_analyze': ('Analyser seulement — aucun fichier créé', 'Analyze only — no file created'),
 'operation_analyze_label': ('Analyse seulement', 'Analysis only'),
 'operation_convert': ('Uniformiser — normaliser réellement l’audio', 'Normalize — process the audio itself'),
 'operation_convert_label': ('Uniformisation audio', 'Audio normalization'),
 'operation_help_text': ('Uniformiser traite chaque fichier séparément, vise la cible LUFS sous la limite True Peak, '
                         'puis remesure la sortie. ReplayGain ne modifie pas les échantillons. Analyser seulement '
                         'produit des mesures et, si demandé, un rapport CSV, mais aucun fichier audio.',
                         'Normalize processes every file separately, targets LUFS under the True Peak limit, and '
                         'remeasures the output. ReplayGain does not change samples. Analyze-only produces '
                         'measurements and an optional CSV report, but no audio file.'),
 'operation_replaygain': ('ReplayGain — sans réencodage audio', 'ReplayGain — no audio re-encoding'),
 'operation_replaygain_label': ('ReplayGain', 'ReplayGain'),
 'operation_tooltip': ('Uniformiser modifie réellement l’audio pour viser la cible. ReplayGain copie le flux audio et '
                       'ajoute des balises. Analyser seulement mesure chaque source sans créer de fichier audio.',
                       'Normalize physically changes audio toward target. ReplayGain copies the stream and adds tags. '
                       'Analyze-only measures each source without creating audio files.'),
 'option_status_auto_start': ('AUTO', 'AUTO'),
 'option_status_overwrite': ('ÉCRAS', 'OVER'),
 'option_status_quality_control': ('QUAL', 'QUAL'),
 'option_status_report': ('CSV', 'CSV'),
 'option_status_resume': ('REPR', 'RES'),
 'option_status_skip_compliant': ('SAUT', 'SKIP'),
 'options_tab': ('Options', 'Options'),
 'output_lufs_log': ('sortie {value} LUFS', 'output {value} LUFS'),
 'output_lufs_unavailable': ('sortie LUFS indisponible', 'output LUFS unavailable'),
 'overwrite': ('Écraser les fichiers existants', 'Overwrite existing files'),
 'overwrite_tooltip': ('Autorise le remplacement d’un fichier audio déjà présent dans la destination. Les fichiers '
                       'sources ne sont jamais écrasés.',
                       'Allows an audio file already present in the destination to be replaced. Source files are never '
                       'overwritten.'),
 'parallel': ('Traitements parallèles', 'Parallel processes'),
 'parallel_adjusted': ('Parallélisme automatique — {active} traitement(s), CPU {cpu:.0f} %.',
                       'Automatic parallelism — {active} process(es), CPU {cpu:.0f}%.'),
 'parallel_auto': ('Auto', 'Auto'),
 'parallel_auto_log': ('automatique, maximum {maximum}', 'automatic, maximum {maximum}'),
 'parallel_tooltip': ('Détermine combien de fichiers peuvent être traités simultanément.\n'
                      '\n'
                      '• Auto démarre avec au plus 4 tâches. Lorsque la mesure CPU est disponible, le programme la '
                      'contrôle chaque seconde : il ajoute une tâche sous 70 % d’occupation et en retire une au-dessus '
                      'de 92 %.\n'
                      '• Auto ne dépasse jamais le nombre de processeurs logiques détectés, avec un plafond absolu de '
                      '16 tâches.\n'
                      '• Si la mesure CPU n’est pas disponible, Auto utilise directement ce plafond détecté sans '
                      'adaptation dynamique.\n'
                      '• Une valeur numérique fixe le nombre maximal de tâches simultanées ; ce n’est pas une cible '
                      'd’occupation CPU.\n'
                      '\n'
                      'Davantage de tâches peut accélérer un grand lot, mais augmente la charge, la température et '
                      'l’accès au disque. Utilisez − jusqu’à afficher Auto.',
                      'Determines how many files can be processed at the same time.\n'
                      '\n'
                      '• Auto starts with at most 4 jobs. When CPU measurement is available, it checks once per '
                      'second: it adds one job below 70% usage and removes one above 92%.\n'
                      '• Auto never exceeds the detected logical CPU count, with an absolute ceiling of 16 jobs.\n'
                      '• If CPU measurement is unavailable, Auto uses that detected ceiling directly without dynamic '
                      'adjustment.\n'
                      '• A numeric value fixes the maximum number of simultaneous jobs; it is not a CPU-usage target.\n'
                      '\n'
                      'More jobs can speed up a large batch, but increase CPU load, heat and disk activity. Press − '
                      'until Auto is shown.'),
 'paste': ('Coller', 'Paste'),
 'path_left': ('Voir la partie gauche du chemin', 'Show the left part of the path'),
 'path_right': ('Voir la partie droite du chemin', 'Show the right part of the path'),
 'pause': ('Pause', 'Pause'),
 'peak': ('Crête maximale', 'Maximum true peak'),
 'peak_tooltip': ('La crête maximale est un plafond, pas un volume à atteindre. Elle limite en dBTP les pointes les '
                  'plus hautes de la forme d’onde reconstruite, y compris entre les échantillons, afin de réduire le '
                  'risque d’écrêtage après encodage ou transcodage.\n'
                  '\n'
                  '• -1,0 dBTP — plafond courant pour la diffusion ; niveau maximal plus élevé.\n'
                  '• -1,5 dBTP — réglage par défaut, compromis prudent pour des MP3.\n'
                  '• -2,0 dBTP — marge supplémentaire, utile pour les fichiers destinés à être réencodés ou pour une '
                  'cible sonore élevée.\n'
                  '• 0 dBTP — aucune marge ; déconseillé pour un MP3.\n'
                  '\n'
                  'Une valeur plus négative protège davantage, mais peut empêcher certains morceaux très dynamiques '
                  'd’atteindre exactement la cible LUFS.',
                  'Maximum true peak is a ceiling, not a level to reach. It limits the highest reconstructed waveform '
                  'peaks in dBTP, including peaks between samples, to reduce clipping after encoding or transcoding.\n'
                  '\n'
                  '• -1.0 dBTP — common delivery ceiling with the highest output peak level.\n'
                  '• -1.5 dBTP — the default and a cautious compromise for MP3 files.\n'
                  '• -2.0 dBTP — extra headroom, useful when files may be encoded again or when using a high loudness '
                  'target.\n'
                  '• 0 dBTP — no headroom and not recommended for MP3.\n'
                  '\n'
                  'A more negative value is safer, but may prevent highly dynamic tracks from reaching the LUFS target '
                  'exactly.'),
 'phase_summary': ('Répartition estimée du temps total — analyse {analysis}, conversion {conversion}, contrôle qualité '
                   '{quality}.',
                   'Estimated total-time allocation — analysis {analysis}, conversion {conversion}, quality control '
                   '{quality}.'),
 'pipeline_enabled': ('Pipeline Piste — chaque conversion démarre dès que son analyse est terminée.',
                      'Track pipeline — each conversion starts as soon as its analysis is complete.'),
 'pre_measurement': ('Mesure avant traitement…', 'Measuring input files…'),
 'preset': ('Préréglage', 'Preset'),
 'preset_dynamic': ('Musique dynamique', 'Dynamic music'),
 'preset_library': ('Bibliothèque — recommandé', 'Music library — recommended'),
 'preset_streaming': ('Streaming plus présent', 'Louder streaming'),
 'preset_tooltip': ('Applique en une fois une cible sonore, une crête maximale et une qualité audio cohérentes. Toute '
                    'modification manuelle sélectionne Personnalisé.',
                    'Applies a consistent loudness target, maximum true peak and audio quality at once. Any manual '
                    'change selects Custom.'),
 'processing_cancelled': ('Traitement annulé.', 'Processing cancelled.'),
 'processing_completed': ('Traitement terminé', 'Processing completed'),
 'processing_in_progress': ('Traitement en cours', 'Processing in progress'),
 'processing_paused': ('Traitement en pause.', 'Processing paused.'),
 'processing_resumed': ('Traitement repris.', 'Processing resumed.'),
 'progress_status': ('{status} : {file}', '{status}: {file}'),
 'qc_impossible': ('ALERTE — contrôle impossible : {error}', 'WARNING — quality control failed: {error}'),
 'qc_log': (' — contrôle qualité : {quality}', ' — quality control: {quality}'),
 'qc_ok': ('RÉUSSI', 'SUCCESS'),
 'qc_warning': ('ALERTE — {detail}', 'WARNING — {detail}'),
 'quality': ('Qualité audio', 'Audio quality'),
 'quality_control': ('Contrôle qualité automatique', 'Automatic quality control'),
 'quality_control_tooltip': ('Remesure chaque sortie. Les corrections continuent de viser ±0,50 LU ; une alerte de '
                             'sonie n’apparaît qu’au-delà de ±0,60 LU. Les MP3 dynamiques gardent jusqu’à trois essais '
                             'correctifs ; WAV, AIFF et FLAC peuvent recevoir jusqu’à deux reprises depuis la source '
                             'si la marge True Peak le permet. Désactiver cette option supprime la vérification, les '
                             'reprises et l’activité du vumètre.',
                             'Remeasures every output. Corrections still target ±0.50 LU; a loudness warning appears '
                             'only beyond ±0.60 LU. Dynamic MP3 keeps up to three corrective attempts; WAV, AIFF, and '
                             'FLAC may receive up to two fresh-source retries when True Peak headroom allows. '
                             'Disabling this option removes verification, retries, and meter activity.'),
 'quality_tooltip': ('Règle le compromis qualité/taille des formats compressés. Plus le chiffre est bas, plus la '
                     'qualité et le débit sont élevés. Ce réglage ne change ni la cible LUFS ni la crête maximale.\n'
                     '\n'
                     '• 0 — qualité maximale, recommandée pour préserver les détails.\n'
                     '• 1 à 2 — très haute qualité.\n'
                     '• 3 à 4 — bon compromis qualité/taille.\n'
                     '• 5 à 9 — fichiers plus petits, avec davantage de pertes.\n'
                     '\n'
                     'FLAC reste sans perte quelle que soit la valeur. WAV et AIFF ignorent ce réglage et conservent '
                     'la fréquence et la profondeur PCM compatibles avec la source. Pour MP3, M4A, OGG et Opus, une '
                     'faible valeur peut demander un débit supérieur à celui du fichier d’origine : la sortie sera '
                     'alors plus volumineuse. Une valeur plus élevée réduit généralement la taille, sans garantir un '
                     'nombre d’octets identique, car ces encodeurs utilisent souvent un débit variable. Réencoder un '
                     'format avec pertes ne restaure pas les informations déjà perdues.',
                     'Controls the quality/size trade-off for compressed formats. Lower numbers use higher quality and '
                     'bitrate. It changes neither the LUFS target nor maximum true peak.\n'
                     '\n'
                     '• 0 — maximum quality, recommended to preserve detail.\n'
                     '• 1 to 2 — very high quality.\n'
                     '• 3 to 4 — a good quality/size compromise.\n'
                     '• 5 to 9 — smaller files with progressively more loss.\n'
                     '\n'
                     'FLAC remains lossless at every value. WAV and AIFF ignore this setting and preserve '
                     'source-compatible rate and PCM depth. For MP3, M4A, OGG and Opus, a low value may request a '
                     'higher bitrate than the original, making the output larger. A higher value generally reduces '
                     'size, without guaranteeing the same byte count because these encoders often use variable '
                     'bitrate. Re-encoding a lossy source cannot restore discarded information.'),
 'ready': ('Prêt', 'Ready'),
 'recursive_scan': ('Analyse récursive des dossiers…', 'Scanning folders recursively…'),
 'remove_all': ('Tout retirer', 'Remove all'),
 'remove_selection': ('Retirer la sélection', 'Remove selection'),
 'replaygain_help_text': ('ReplayGain calcule un gain conseillé et écrit les balises REPLAYGAIN_TRACK_GAIN/PEAK. Le '
                          'flux audio est copié sans réencodage (-c:a copy) : les échantillons ne changent pas. Seul '
                          'un lecteur compatible applique ces balises. Le fichier ne reçoit donc pas physiquement la '
                          'cible LUFS et son True Peak réel n’est pas limité.',
                          'ReplayGain calculates a suggested gain and writes REPLAYGAIN_TRACK_GAIN/PEAK tags. The '
                          'audio stream is copied without re-encoding (-c:a copy), so samples do not change. Only a '
                          'compatible player applies the tags. The file therefore does not physically reach target '
                          'LUFS and its actual True Peak is not limited.'),
 'replaygain_levels_log': ('audio inchangé : {before} LUFS · gain ReplayGain {gain} dB en métadonnées · cible réglée '
                           '{target} LUFS (lecteur compatible requis)',
                           'audio unchanged: {before} LUFS · ReplayGain {gain} dB in metadata · configured target '
                           '{target} LUFS (compatible player required)'),
 'replaygain_log_help_text': ('En ReplayGain, le journal indique la sonie physique inchangée, le gain inscrit dans les '
                              'métadonnées et la cible réglée. Si le contrôle qualité est activé, « audio inchangé et '
                              'balises vérifiées » signifie que la sonie et la crête ont été comparées à la source et '
                              'que les balises ont été relues ; cela ne signifie pas que le fichier mesure '
                              'physiquement la cible.',
                              'In ReplayGain, the log shows unchanged physical loudness, the gain written to metadata '
                              'and the configured target. With quality control enabled, ‘audio unchanged and tags '
                              'verified’ means loudness and peak were compared with the source and tags were read '
                              'back; it does not mean that the file physically measures at the target.'),
 'replaygain_operation': ('ReplayGain sans réencodage', 'ReplayGain without re-encoding'),
 'replaygain_qc_help_text': ('Avec le contrôle qualité activé, ReplayGain remesure le fichier livré pour confirmer que '
                             'sa sonie physique et sa crête sont restées inchangées, puis vérifie les balises Track. '
                             'Un succès confirme l’audio préservé et les balises présentes, pas l’atteinte physique de '
                             'la cible.',
                             'With quality control enabled, ReplayGain remeasures the delivered file to confirm '
                             'unchanged physical loudness and peak, then checks the Track tags. Success confirms '
                             'preserved audio and present tags, not physical target loudness.'),
 'replaygain_qc_ok': ('RÉUSSI — audio inchangé et balises vérifiées', 'SUCCESS — audio unchanged and tags verified'),
 'replaygain_tags_missing': ('Balises ReplayGain non retrouvées.', 'ReplayGain tags were not found.'),
 'replaygain_usefulness_text': ('Intérêt de ReplayGain : harmoniser le volume à la lecture, sans perte de réencodage '
                                'et de façon réversible, pour une bibliothèque utilisée avec un lecteur compatible. '
                                'Pour livrer un fichier qui mesure physiquement la cible dans tous les lecteurs, '
                                'utilisez Uniformiser.',
                                'ReplayGain is useful for reversible, no-re-encode playback leveling in a library used '
                                'with a compatible player. To deliver a file that physically measures at the target in '
                                'every player, use Normalize.'),
 'report_destination': ('destination', 'destination'),
 'report_detail': ('détail', 'detail'),
 'report_error': ('ALERTE — rapport CSV impossible : {error}', 'WARNING — unable to create CSV report: {error}'),
 'report_filename_prefix': ('Rapport_LUFScale', 'LUFScale_Report'),
 'report_gain': ('gain_db', 'gain_db'),
 'report_input_dbtp': ('dbtp_avant', 'input_dbtp'),
 'report_input_lufs': ('lufs_avant', 'input_lufs'),
 'report_log': ('Rapport CSV — {path}', 'CSV report — {path}'),
 'report_mode': ('mode', 'mode'),
 'report_operation': ('opération', 'operation'),
 'report_output_dbtp': ('dbtp_apres', 'output_dbtp'),
 'report_output_lufs': ('lufs_apres', 'output_lufs'),
 'report_path': ('Rapport : {path}', 'Report: {path}'),
 'report_qc': ('controle_qualite', 'quality_control'),
 'report_qc_engine': ('moteur_qc', 'qc_engine'),
 'report_seconds': ('temps_secondes', 'elapsed_seconds'),
 'report_source': ('source', 'source'),
 'report_status': ('statut', 'status'),
 'report_tooltip': ('Crée dans la destination un rapport CSV détaillé avec les mesures, durées et alertes. Aucun '
                    'fichier JSON diagnostic n’est ajouté.',
                    'Creates a detailed CSV report in the destination with measurements, durations and warnings. No '
                    'diagnostic JSON file is added.'),
 'resume': ('Reprendre après une interruption', 'Resume after an interruption'),
 'resume_not_saved': (' Reprise non enregistrée : {error}', ' Resume checkpoint not saved: {error}'),
 'resume_processing': ('Reprendre', 'Resume'),
 'resume_tooltip': ('Les fichiers déjà terminés avec les mêmes réglages sont reconnus et ne sont pas retraités.',
                    'Files already completed with the same settings are recognized and not processed again.'),
 'resumed_progress': ('Repris : {file}', 'Resumed: {file}'),
 'save_dialog_cancel': ('Annuler', 'Cancel'),
 'save_dialog_filename': ('Nom du fichier', 'File name'),
 'save_dialog_filetype': ('Format', 'Format'),
 'save_dialog_location': ('Dossier', 'Location'),
 'save_dialog_overwrite': ('Remplacer', 'Replace'),
 'save_dialog_overwrite_message': ('Le fichier « {file} » existe déjà.', 'The file “{file}” already exists.'),
 'save_dialog_overwrite_title': ('Remplacer le fichier ?', 'Replace file?'),
 'save_dialog_parent': ('Dossier parent', 'Parent folder'),
 'save_dialog_save': ('Enregistrer', 'Save'),
 'save_issue_list': ('Enregistrer en CSV…', 'Save as CSV…'),
 'save_issue_list_error': ('Impossible d’enregistrer la liste : {error}', 'Unable to save the list: {error}'),
 'save_issue_list_error_title': ('Enregistrement impossible', 'Unable to save'),
 'save_issue_list_title': ('Enregistrer la liste CSV', 'Save CSV list'),
 'scan_error': ('ERREUR — {error}', 'ERROR — {error}'),
 'scanning_folders': ('Analyse des dossiers…', 'Scanning folders…'),
 'settings': ('Réglages', 'Settings'),
 'open_folder': ('Ouvrir le dossier', 'Open folder'),
 'show_option_help': ('Afficher l’aide : {option}', 'Show help: {option}'),
 'silent_copy': ('Audio silencieux ou non mesurable copié.', 'Silent or unmeasurable audio copied.'),
 'silent_copy_no_replaygain': ('Audio silencieux copié sans balise ReplayGain.',
                               'Silent audio copied without ReplayGain tags.'),
 'silent_unmeasurable': ('Audio silencieux ou non mesurable.', 'Silent or unmeasurable audio.'),
 'simulation': ('Simulation', 'Simulation'),
 'skip_compliant': ('Ne pas réencoder les fichiers déjà conformes', 'Do not re-encode files that already comply'),
 'skip_compliant_tooltip': ('Activé par défaut. Après l’analyse, un fichier situé à ±0,10 LU de la cible et sous la '
                            'limite True Peak est copié à l’identique, sans réencodage.',
                            'Enabled by default. After analysis, a file within ±0.10 LU of target and below the True '
                            'Peak limit is copied unchanged without re-encoding.'),
 'skipped_progress': ('Ignoré : {file}', 'Skipped: {file}'),
 'source_audio_count': ('Fichiers : {count}', 'Files: {count}'),
 'source_list_more': ('… {count} autre(s) source(s) conservée(s)', '… {count} more source(s) retained'),
 'source_safety': ('Les fichiers sources ne sont jamais déplacés ni modifiés.',
                   'Source files are never moved or modified.'),
 'source_selection_tooltip': ('Sélection multiple : Ctrl+clic pour des éléments séparés, Maj+clic pour une plage.',
                              'Multiple selection: Ctrl+click for separate items, Shift+click for a range.'),
 'sources_added': ('{count} source(s) ajoutée(s).', '{count} source(s) added.'),
 'start': ('Démarrer', 'Start'),
 'status_analyzed': ('ANALYSÉ', 'ANALYZED'),
 'status_cancelled': ('ANNULÉ', 'CANCELLED'),
 'status_compliant': ('CONFORME', 'COMPLIANT'),
 'status_error': ('ERREUR', 'ERROR'),
 'status_ok': ('RÉUSSI', 'SUCCESS'),
 'status_resumed': ('REPRIS', 'RESUMED'),
 'status_skipped': ('IGNORÉ', 'SKIPPED'),
 'status_warning': ('ALERTE', 'WARNING'),
 'switch_to_dark': ('Mode sombre', 'Dark mode'),
 'switch_to_light': ('Mode clair', 'Light mode'),
 'tagline': ('Uniformise le volume audio perçu', 'Balances perceived audio loudness'),
 'target': ('Cible sonore', 'Loudness target'),
 'target_tooltip': ('La cible sonore est la sonie intégrée visée sur l’ensemble du morceau, exprimée en LUFS. Une '
                    'valeur moins négative produit un fichier perçu plus fort : -14 LUFS est plus fort que -16 LUFS. '
                    'Un écart de 2 LU correspond approximativement à 2 dB de différence de niveau avant une éventuelle '
                    'limitation de crête.\n'
                    '\n'
                    'Repères : -18 LUFS pour conserver davantage de calme et de dynamique ; -16 LUFS pour un équilibre '
                    'général ; -14 LUFS pour une restitution plus forte de type streaming. Les plateformes peuvent '
                    'ensuite appliquer leur propre normalisation.\n'
                    '\n'
                    'Cette cible n’aplatit pas à elle seule les variations internes du morceau. Si la crête maximale '
                    'empêche d’atteindre la cible sans écrêtage, le résultat peut rester légèrement plus bas.',
                    'The loudness target is the intended integrated loudness across the whole track, expressed in '
                    'LUFS. A less negative value produces a louder file: -14 LUFS is louder than -16 LUFS. A 2 LU '
                    'difference is approximately a 2 dB level difference before any peak limiting.\n'
                    '\n'
                    'Guidance: -18 LUFS for a calmer and more dynamic result; -16 LUFS for a general balance; -14 LUFS '
                    'for a louder streaming-style result. Platforms may then apply their own playback normalization.\n'
                    '\n'
                    'This target does not by itself flatten the dynamics inside the track. If the maximum true peak '
                    'prevents the target from being reached without clipping, the result may remain slightly lower.'),
 'theme_accessible': ('Changer l’apparence de l’application. Le choix est mémorisé.',
                      'Change the application appearance. The choice is remembered.'),
 'total_time': ('Temps total : {duration}', 'Total time: {duration}'),
 'track_two_pass': ('Normalisation Piste en deux passes.', 'Two-pass Track normalization.'),
 'true_peak_meter_exceeded': ('Dépassement {margin} dB', 'Exceeded by {margin} dB'),
 'true_peak_meter_margin': ('Marge {margin} dB', 'Headroom {margin} dB'),
 'true_peak_meter_title': ('Marge de crête', 'True-peak headroom'),
 'true_peak_meter_tooltip': ('Compare la crête vraie de la dernière sortie au plafond choisi. Le repère indique la '
                             'dernière valeur et le triangle conserve la crête la plus haute du lot. Vert signifie que '
                             'le plafond est respecté, orange un dépassement jusqu’à 0,25 dB et rouge un dépassement '
                             'supérieur. La tolérance orange est celle du contrôle qualité de LUFScale, pas une norme '
                             'de diffusion. Le graphique est réinitialisé à chaque série.',
                             'Compares the last output’s true peak with the selected ceiling. The marker shows the '
                             'latest value and the triangle retains the batch’s highest peak. Green means the ceiling '
                             'is met, amber means an exceedance up to 0.25 dB, and red means a larger exceedance. The '
                             'amber tolerance belongs to LUFScale quality control and is not a delivery standard. The '
                             'graph resets for every batch.'),
 'true_peak_meter_waiting': ('En attente d’une mesure dBTP', 'Waiting for a dBTP measurement'),
 'version_changes': ('• Installateur hors ligne unique pour Windows 10/11 x86-64.\n'
                     '• Python, PySide6/Qt, FFmpeg, les codecs, les guides et les licences sont intégrés ; aucune '
                     'commande PowerShell ni aucun téléchargement pendant l’installation.\n'
                     '• La construction vérifie loudnorm et les encodeurs avant de créer le programme d’installation '
                     'et son SHA-256.',
                     '• Single offline installer for Windows 10/11 x86-64.\n'
                     '• Python, PySide6/Qt, FFmpeg, codecs, guides and licences are included; installation requires no '
                     'PowerShell command or download.\n'
                     '• The build validates loudnorm and the encoders before creating the setup and its SHA-256.'),
 'version_changes_title': ('Nouveautés de la version {version}', 'What’s new in version {version}'),
 'version_label': ('Version {version}', 'Version {version}'),
 'volume': ('Volume', 'Volume'),
 'volume_loud': ('Fort : -14 LUFS', 'Loud: -14 LUFS'),
 'volume_normal': ('Normal : -16 LUFS', 'Normal: -16 LUFS'),
 'volume_soft': ('Doux : -18 LUFS', 'Soft: -18 LUFS'),
 'volume_tooltip': ('Ce réglage est un raccourci vers la cible sonore ; il ne règle pas le volume d’écoute du '
                    'système.\n'
                    '\n'
                    '• Doux : -18 LUFS — niveau plus calme, davantage de dynamique et moins de risque de solliciter le '
                    'limiteur.\n'
                    '• Normal : -16 LUFS — compromis équilibré, conseillé comme point de départ pour une bibliothèque '
                    'personnelle.\n'
                    '• Fort : -14 LUFS — restitution plus présente, proche de la cible de lecture normale de Spotify, '
                    'mais susceptible de demander davantage de limitation.\n'
                    '• Personnalisé — permet de saisir directement une autre cible LUFS.\n'
                    '\n'
                    'Ces valeurs sont des choix pratiques, pas une norme universelle.',
                    'This setting is a shortcut to the loudness target; it does not change the system playback '
                    'volume.\n'
                    '\n'
                    '• Soft: -18 LUFS — calmer level, more dynamic headroom and less chance of engaging the limiter.\n'
                    '• Normal: -16 LUFS — balanced compromise and a useful starting point for a personal library.\n'
                    '• Loud: -14 LUFS — more forward playback, close to Spotify’s Normal playback target, but more '
                    'likely to require limiting.\n'
                    '• Custom — lets you enter another LUFS target directly.\n'
                    '\n'
                    'These are practical choices, not a universal standard.'),
 'warning_list_title': ('Alertes du traitement', 'Processing warnings'),
 'warnings_button': ('Alertes ({count})', 'Warnings ({count})'),
 'warnings_button_tooltip': ('Ouvre la liste des alertes avec le nom du fichier, son chemin et le détail. Disponible '
                             'pendant une pause ou après le traitement.',
                             'Opens the warning list with filename, path, and details. Available while paused or after '
                             'processing.'),
 'warnings_dialog_title': ('Alertes du traitement', 'Processing warnings')}

EXTRA_TEXTS = {'es': {'activity_cancelled': 'Actividad: proceso cancelado',
        'activity_cancelling': 'Actividad: cancelando…',
        'activity_completed': 'Actividad: proceso finalizado',
        'activity_compliant': 'Conformes: {count}',
        'activity_detected': 'Actividad: {total} archivo(s) detectado(s)',
        'activity_errors': 'Errores: {count}',
        'activity_files': 'Archivos: {count}',
        'activity_idle': 'Actividad: en espera',
        'activity_preparing': 'Actividad: preparando archivos…',
        'activity_progress': '{total} archivos • correctos {success} • alertas {warnings} • errores {failed} • '
                             'reanudados/omitidos {skipped} • conformes {compliant}',
        'activity_skipped': 'Reanudados/omitidos: {count}',
        'activity_successes': 'Correctos: {count}',
        'activity_warnings': 'Alertas: {count}',
        'adaptive_disabled_log': 'Análisis adaptativo — sondas rápidas detenidas tras {sample} mediciones ({successes} '
                                 'éxitos, ahorro estimado {percent:+.1f} %).',
        'add_folders': 'Añadir carpetas…',
        'add_mp3': 'Añadir archivos de audio…',
        'add_replaygain': 'Añadir ReplayGain',
        'add_source_files': 'Añadir archivos de audio',
        'add_source_folder': 'Añadir una carpeta de origen',
        'already_completed': 'Ya finalizado durante una ejecución anterior.',
        'already_compliant_badge': 'CONFORME',
        'already_compliant_copy': 'Ya conforme: copia idéntica sin recodificar el audio.',
        'already_compliant_log': 'ya conforme, sin recodificación',
        'analysis_cache_summary': 'Caché de análisis — {hits} medición(es) reutilizada(s).',
        'analysis_impossible': 'No se pudo analizar: {error}',
        'analysis_measurement_progress': 'Análisis {current}/{total} — {file} — {value}',
        'analysis_method': 'Método de análisis',
        'analysis_method_adaptive': 'Adaptativo — se detiene si no compensa',
        'analysis_method_fast': 'Rápido — experimental',
        'analysis_method_historical': 'Histórico — referencia',
        'analysis_method_log': 'Método de análisis — {method}.',
        'analysis_method_tooltip': 'La versión estable usa automáticamente la medición histórica completa, única '
                                   'validada en el corpus de referencia. Rápido y Adaptativo ya no se ofrecen.',
        'analysis_progress': 'Análisis {current}/{total}: {file}',
        'analysis_progress_help_text': 'En Solo analizar, el gráfico Antes, el registro y la barra avanzan archivo por '
                                       'archivo al terminar cada medición; Después permanece inmóvil.',
        'analyze': 'Analizar',
        'analyze_only_fresh_help_text': 'Solo analizar vuelve a medir cada fuente completa con FFmpeg en cada '
                                        'ejecución. El gráfico Antes y el progreso avanzan archivo por archivo, sin '
                                        'salida ni control de calidad de salida.',
        'analyze_operation': 'análisis/simulación',
        'analyzed_progress': 'Analizado: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Flujo de audio copiado sin recodificar; etiquetas ReplayGain añadidas.',
        'audio_tab': 'Audio',
        'auto_start': 'Iniciar automáticamente después de soltar o pegar',
        'auto_start_tooltip': 'Inicia automáticamente el proceso después de añadir fuentes mediante arrastrar y soltar '
                              'o pegar, si ya se ha elegido un destino.',
        'cancel': 'Cancelar',
        'cancelled_summary': 'Cancelado — {success} correcto(s), {failed} error(es), {skipped} '
                             'reanudado(s)/omitido(s), {warnings} aviso(s), {compliant} conforme(s) — {duration}.',
        'cancelling': 'Cancelando…',
        'choose': 'Elegir…',
        'choose_output': 'Elegir la carpeta de destino',
        'clipboard': 'Portapapeles',
        'clipboard_empty': 'El portapapeles no contiene una ruta válida de carpeta o archivo de audio compatible.',
        'close_button': 'Cerrar',
        'close_question': '¿Cancelar el proceso y cerrar la aplicación?',
        'completed_dialog_summary': 'Estado: finalizado\n'
                                    'Archivos: {files}\n'
                                    'Correctos: {success}\n'
                                    'Errores: {failed}\n'
                                    'Reanudados u omitidos: {skipped}\n'
                                    'Avisos: {warnings}\n'
                                    'Conformes: {compliant}\n'
                                    'Tiempo total: {duration}',
        'completed_summary': 'Finalizado — {success} correcto(s), {failed} error(es), {skipped} '
                             'reanudado(s)/omitido(s), {warnings} aviso(s), {compliant} conforme(s) — {duration}.',
        'completed_with_errors': 'Proceso finalizado con avisos',
        'convert': 'Normalizar',
        'convert_operation': 'uniformización de audio',
        'cpu_tooltip': 'Uso total del procesador del sistema, actualizado cada segundo durante el proceso.',
        'cpu_unavailable': 'N/D',
        'cpu_usage': 'CPU',
        'create_report': 'Crear un informe CSV',
        'csv_file_filter': 'Archivos CSV (*.csv)',
        'custom': 'Personalizado',
        'decrease_value': 'Disminuir el valor',
        'description': 'Uniforma el volumen percibido archivo por archivo sin modificar los originales.',
        'destination': 'Destino',
        'destination_error': 'ERROR — destino no disponible: {error}',
        'destination_path_tooltip': 'Haz clic en la ruta y usa las flechas, Inicio/Fin o la rueda. Se puede '
                                    'seleccionar y copiar, pero no modificar.',
        'destination_required_start': 'Primero elija la carpeta de destino con el botón «Elegir…».',
        'dialog_ok': 'Aceptar',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — se admiten subcarpetas',
        'drop_title': 'Suelta aquí tus carpetas o archivos de audio',
        'elapsed_time': 'Tiempo transcurrido: {duration}',
        'error_list_title': 'Errores de procesamiento',
        'error_progress': 'Error: {file}',
        'errors_button': 'Errores ({count})',
        'errors_button_tooltip': 'Abre la lista de errores con nombre de archivo, ruta y detalle. Disponible durante '
                                 'una pausa o después del proceso.',
        'errors_dialog_title': 'Errores del proceso',
        'estimated_result': 'Resultado estimado; no se creó ningún archivo.',
        'estimated_total_calculating': 'Tiempo total estimado: calculando…',
        'estimated_total_time': 'Tiempo total estimado: {duration}',
        'estimated_total_time_with_day_finish': 'Tiempo total estimado: {duration} — {days} d. {time}',
        'estimated_total_time_with_finish': 'Tiempo total estimado: {duration} — {time}',
        'estimated_total_unavailable': 'Tiempo total estimado: no disponible',
        'ffmpeg_download_button': 'Abrir el sitio oficial de FFmpeg',
        'ffmpeg_error_no_detail': 'Error de FFmpeg sin detalles.',
        'ffmpeg_execution_error': 'No se puede ejecutar FFmpeg: {error}',
        'ffmpeg_incompatible': 'FFmpeg incompatible',
        'ffmpeg_missing': 'No se encuentra FFmpeg',
        'ffmpeg_missing_encoders': 'Esta versión de FFmpeg no incluye todos los codificadores de audio necesarios: '
                                   '{encoders}.',
        'ffmpeg_missing_message': 'FFmpeg debe estar instalado y disponible en PATH, o situado junto al programa.',
        'ffmpeg_no_lame': 'Esta compilación de FFmpeg no incluye el codificador MP3 libmp3lame.',
        'ffmpeg_no_loudnorm': 'Esta compilación de FFmpeg no incluye el filtro loudnorm.',
        'ffmpeg_not_responding': 'FFmpeg no responde correctamente.',
        'file_exists': 'El archivo ya existe.',
        'files_found': '{total} archivo(s) de audio encontrado(s) — {operation} — {parallel} proceso(s) paralelo(s).',
        'finalization_completed': 'Finalización terminada en {duration}.',
        'finalizing': 'Finalización — informe, caché de análisis y datos de reanudación…',
        'folder': 'Carpeta',
        'folder_unavailable': 'Carpeta no disponible',
        'guide_analysis_method': 'LUFScale utiliza automáticamente la medición histórica completa, el único método '
                                 'validado en el corpus de referencia.',
        'guide_analyze_prediction_body': 'Solo analizar puede estimar el resultado, pero no crea audio ni control de '
                                         'calidad de salida.',
        'guide_analyze_prediction_title': 'Estimación sin salida',
        'guide_build_body': 'En Windows 10 1809 o posterior, o Windows 11 x86-64:\n'
                            '\n'
                            '1. Descargue «LUFScale-2.1.12-Setup-x64.exe» y su archivo SHA-256.\n'
                            '2. Verifique el SHA-256 y haga doble clic en el instalador.\n'
                            '3. Lea y acepte la licencia GNU GPL y siga el asistente.\n'
                            '4. Inicie LUFScale desde el menú Inicio.\n'
                            '\n'
                            'La aplicación, Python, PySide6/Qt, FFmpeg, códecs, guías y licencias ya están incluidos. '
                            'La instalación no descarga nada ni requiere comandos de PowerShell. Se crea '
                            'automáticamente un desinstalador de Windows.\n'
                            '\n'
                            'La distribución no está firmada; tras verificar el archivo y su suma, SmartScreen puede '
                            'pedir confirmación.',
        'guide_build_title': 'Instalar LUFScale en Windows x86-64',
        'guide_estimated_total_help': 'Tiempo total estimado: 12 min - fin hacia las 14:30. «12 min» es la duración '
                                      'total estimada y «14:30» la hora prevista de fin. Si se supera la medianoche, '
                                      'se añade automáticamente el número de días antes de la hora, por ejemplo «2 d. '
                                      '14:30».',
        'guide_file_processing_body': 'Cada archivo recibe su propia medición y ganancia para acercarse al objetivo '
                                      'LUFS bajo el límite True Peak.',
        'guide_file_processing_title': 'Procesamiento por archivo',
        'guide_help_tooltip': 'Abre la guía PDF completa en el idioma seleccionado.',
        'guide_level_mode_body': 'Pista - recomendado: acerca cada archivo al objetivo. Álbum - avanzado y '
                                 'especializado: aplica una ganancia común y conserva los contrastes. Use Álbum para '
                                 'una obra escuchada en orden; Pista para reproducción aleatoria o un nivel regular '
                                 'entre archivos.',
        'guide_license_body': 'LUFScale es software libre distribuido bajo GNU GPL-3.0-or-later. Esta licencia permite '
                              'usarlo, estudiarlo, modificarlo y redistribuirlo conforme a sus condiciones. La '
                              'distribución incluye el código fuente, los avisos y las licencias de terceros. El '
                              'software se proporciona sin garantía.',
        'guide_license_feature': '• Software libre GNU GPL-3.0-or-later: la licencia permite usarlo, estudiarlo, '
                                 'modificarlo y redistribuirlo.\n'
                                 '• Instalador sin conexión Windows x86-64 con Python, Qt y FFmpeg incluidos. Se '
                                 'recomienda Windows 11; Windows 10 1809 o posterior sigue siendo un objetivo de '
                                 'compatibilidad, aunque finalizó su soporte estándar de Microsoft.',
        'guide_license_title': 'Software libre y redistribución',
        'guide_log_legend_cancelled': 'El procesamiento se detuvo voluntariamente; no es un error.',
        'guide_log_legend_compliant': 'Copia de audio sin cambios: la fuente ya respetaba el objetivo y el límite de '
                                      'pico.',
        'guide_log_legend_error': 'No se pudo completar el archivo afectado.',
        'guide_log_legend_success': 'Procesamiento finalizado sin anomalías detectadas.',
        'guide_log_legend_warning': 'La salida existe, pero una medición supera la tolerancia prevista.',
        'guide_missing_message': 'No se ha encontrado la guía PDF: {path}',
        'guide_missing_title': 'Guía no disponible',
        'guide_open_error': 'No se pudo abrir la guía PDF: {path}',
        'guide_quality_priority_body': 'LUFScale mide la sonoridad de los archivos y, con Normalizar, ajusta '
                                       'físicamente el volumen percibido hacia un objetivo LUFS mientras controla el '
                                       'pico real. Cada fuente se analiza en toda su duración y después se vuelve a '
                                       'medir y verificar la salida. El resultado no depende de etiquetas ni de un '
                                       'reproductor compatible: los niveles son más coherentes entre archivos, se '
                                       'señalan las desviaciones y los originales permanecen intactos.',
        'guide_quality_priority_title': '¿Para qué sirve LUFScale?',
        'help_button': 'Ayuda',
        'help_overview': '• Normalización real, ReplayGain o análisis de MP3, FLAC, WAV, AIFF, M4A, OGG y Opus.\n'
                         '• Cada archivo se mide y procesa por separado hacia el objetivo elegido.\n'
                         '• Se conservan estructura, metadatos y carátulas compatibles. Los originales nunca cambian.\n'
                         '• Paralelismo Auto, caché, reanudación, control de calidad, CSV, progreso, CPU e historiales '
                         'LUFS.\n'
                         '• Interfaz y guías PDF en 12 idiomas.',
        'help_title': 'Características principales',
        'increase_value': 'Aumentar el valor',
        'input_lufs_log': 'entrada {value} LUFS',
        'interface_ffmpeg_message': 'El motor de audio FFmpeg integrado falta o no se puede usar. Reinstale LUFScale '
                                    'desde el archivo de distribución completo.',
        'internal_error': 'Error interno: {error}',
        'interrupted': 'Proceso interrumpido.',
        'invalid_location': 'Ubicación no válida',
        'issue_detail_column': 'Detalle',
        'issue_file_column': 'Archivo',
        'issue_path_column': 'Ruta',
        'language': 'Idioma',
        'language_tooltip': 'Cambia inmediatamente el idioma de la interfaz, los mensajes y los futuros informes CSV. '
                            'La elección se guarda.',
        'log_help_text': 'Cada línea corresponde a un archivo o a una etapa general.\n'
                         '\n'
                         '• Una línea correcta empieza directamente por el nombre del archivo; ya no se repite '
                         'CORRECTO.\n'
                         '• CONFORME, REANUDADO, OMITIDO, CANCELADO y ERROR permanecen cuando aportan información '
                         'útil.\n'
                         '• Los niveles muestran entrada → salida medida de nuevo y, después, el posible resultado del '
                         'control de calidad.\n'
                         '• Alertas y Errores abren listas separadas con nombre, ruta y detalle. Están disponibles '
                         'durante una pausa o al terminar y cada lista puede guardarse.\n'
                         '\n'
                         'Colores: verde = correcto; naranja = alerta; rojo = archivo no terminado; violeta azulado = '
                         'reanudado; gris = información, omisión o cancelación.\n'
                         '\n'
                         'ALERTA QC — sonoridad significa que la salida medida difiere del valor esperado más de ±0,60 '
                         'LU. Un valor más negativo suena más bajo y uno menos negativo, más alto. La desviación es la '
                         'diferencia absoluta: -14,69 en vez de -14,00 equivale a 0,69 LU. El archivo se crea '
                         'igualmente; no es un fallo de conversión. Si el resultado suena bien no es obligatorio '
                         'actuar. Para un objetivo estricto, revise el detalle y el CSV, y compruebe el objetivo y el '
                         'límite True Peak antes de repetir. El mensaje por sí solo no determina si la causa es el '
                         'límite, el codificador o un límite de corrección.\n'
                         '\n'
                         'ALERTA QC — pico significa que el pico real medido supera el límite elegido más de 0,25 dB. '
                         'El archivo se crea igualmente. Si persiste, elija un objetivo LUFS más bajo o un límite más '
                         'prudente, por ejemplo -2,0 dBTP, y repita.\n'
                         '\n'
                         'Los tiempos acumulados suman el trabajo de todas las tareas paralelas. El tiempo total es la '
                         'duración real transcurrida.',
        'log_placeholder': 'El informe del proceso aparecerá aquí.',
        'log_title': 'Registro de procesamiento',
        'loudness_comparison_after': 'Después',
        'loudness_comparison_analysis_only': 'Sin salida en el modo Solo analizar',
        'loudness_comparison_before': 'Antes',
        'loudness_comparison_help_text': 'Cada archivo añade un punto a la derecha. Antes siempre muestra la fuente '
                                         'medida. Con Normalizar, Después muestra la salida realmente medida de nuevo. '
                                         'Con ReplayGain, el segundo gráfico discontinuo estima la reproducción: '
                                         'sonoridad de la fuente más la ganancia Track guardada. El signo ≈ y la nota '
                                         'Reproductor compatible indican que no es una medición física del archivo '
                                         'entregado. Un reproductor incompatible conserva el nivel original; uno '
                                         'compatible puede variar el resultado por el preamplificador o la protección '
                                         'contra recorte. Ambos gráficos mantienen la misma escala fija de ±6 LU. Solo '
                                         'analizar no tiene salida Después.',
        'loudness_comparison_increased': 'Diferencia aumentada en {value} LU',
        'loudness_comparison_needs_qc': 'Active el control de calidad para comparar',
        'loudness_comparison_no_after': 'Sin curva Después para esta operación',
        'loudness_comparison_not_applicable': 'Comparación no disponible para esta operación',
        'loudness_comparison_reached': 'Objetivo alcanzado · diferencia {value} LU',
        'loudness_comparison_reduced': 'Diferencia reducida en {value} LU',
        'loudness_comparison_replaygain_after': 'Reproducción RG estimada',
        'loudness_comparison_replaygain_note': 'Reproductor compatible · audio intacto',
        'loudness_comparison_scale': 'Vista ±{scale} LU · tol. QC ±{tolerance} LU',
        'loudness_comparison_target': 'Objetivo {value} LUFS',
        'loudness_comparison_title': 'Evolución de sonoridad',
        'loudness_comparison_tooltip': 'Antes muestra la sonoridad física. En ReplayGain, el segundo gráfico estima la '
                                       'reproducción compatible a partir de la ganancia guardada.',
        'loudness_comparison_unchanged': 'Diferencia sin cambios',
        'loudness_comparison_waiting': 'Esperando un archivo procesado',
        'loudness_meter_current_file': 'Último: {file}',
        'loudness_meter_estimated': 'Estimado',
        'loudness_meter_help_text': 'La línea roja es el objetivo y el valor azul es la sonoridad realmente medida de '
                                    'la última salida. Sube o baja con cada archivo. La puntuación resume las últimas '
                                    '8 salidas medidas. Si el panel rojo indica «Ver alertas», pause el proceso o '
                                    'espere a que termine y abra Alertas para identificar los archivos afectados.',
        'loudness_meter_maximum': 'Máx {value}',
        'loudness_meter_measured': 'Medido',
        'loudness_meter_minimum': 'Mín {value}',
        'loudness_meter_no_file': 'Esperando un análisis',
        'loudness_meter_target': 'Objetivo {value} LUFS',
        'loudness_meter_title': 'Medidor de sonoridad',
        'loudness_meter_tooltip': 'Objetivo rojo; última salida realmente medida en azul.',
        'loudness_meter_waiting': 'Esperando un archivo de audio',
        'loudness_meter_worst_file': 'Mayor desviación: {file}',
        'loudness_meter_worst_file_detail': 'Mayor desviación de los últimos 8 análisis: {file} — {measured} LUFS para '
                                            '{expected} LUFS, desviación {deviation} LU.',
        'loudness_score_acceptable': 'Aceptable',
        'loudness_score_check': 'Ver alertas',
        'loudness_score_excellent': 'Excelente',
        'loudness_score_good': 'Buena',
        'loudness_score_needs_qc': 'Puntuación objetivo: active el control de calidad',
        'loudness_score_not_applicable': 'Puntuación objetivo: no aplicable',
        'loudness_score_tooltip': 'La puntuación usa las últimas 8 salidas medidas. 100 es exacto, 50 equivale a un '
                                  'error RMS de 0,60 LU y 0 a 1,20 LU o más. Un panel rojo implica que se puede '
                                  'consultar al menos una alerta de sonoridad con el botón Alertas.',
        'loudness_score_value': 'Puntuación objetivo: {score}/100\n{rating}\nError RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Puntuación objetivo: en espera',
        'measurement_unavailable': 'Medición no disponible.',
        'mp3': 'MP3',
        'mp3_filter': 'Audio compatible (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Ninguna carpeta seleccionada',
        'no_mp3': 'No se encontraron archivos de audio compatibles.',
        'no_new_source': 'No se añadió ninguna carpeta ni archivo de audio compatible.',
        'not_performed': 'No realizado',
        'open_output_error': 'No se pudo abrir la carpeta de destino: {error}',
        'operation': 'Operación',
        'operation_analyze': 'Solo analizar — sin archivo creado',
        'operation_analyze_label': 'Solo análisis',
        'operation_convert': 'Uniformizar — normalizar realmente el audio',
        'operation_convert_label': 'Uniformización de audio',
        'operation_help_text': 'Normalizar procesa cada archivo por separado y vuelve a medir la salida. ReplayGain no '
                               'cambia las muestras. Solo analizar produce medidas y, opcionalmente, un CSV, pero '
                               'ningún archivo de audio.',
        'operation_replaygain': 'ReplayGain — sin recodificar el audio',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Normalizar modifica el audio hacia el objetivo. ReplayGain copia el flujo y añade '
                             'etiquetas. Solo analizar mide sin crear audio.',
        'option_status_auto_start': 'AUTO',
        'option_status_overwrite': 'SOB',
        'option_status_quality_control': 'CAL',
        'option_status_report': 'CSV',
        'option_status_resume': 'REA',
        'option_status_skip_compliant': 'OMIT',
        'options_tab': 'Opciones',
        'output_lufs_log': 'salida {value} LUFS',
        'output_lufs_unavailable': 'LUFS de salida no disponible',
        'overwrite': 'Sobrescribir archivos existentes',
        'overwrite_tooltip': 'Permite reemplazar un MP3 que ya existe en el destino. Los archivos de origen nunca se '
                             'sobrescriben.',
        'parallel': 'Procesos en paralelo',
        'parallel_adjusted': 'Paralelismo automático — {active} proceso(s), CPU {cpu:.0f} %.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automático, máximo {maximum}',
        'parallel_tooltip': 'Determina cuántos archivos pueden procesarse simultáneamente.\n'
                            '\n'
                            '• Auto comienza con un máximo de 4 tareas. Cuando se puede medir la CPU, la comprueba '
                            'cada segundo: añade una tarea por debajo del 70 % de uso y retira una por encima del 92 '
                            '%.\n'
                            '• Auto nunca supera el número de procesadores lógicos detectados y tiene un límite '
                            'absoluto de 16 tareas.\n'
                            '• Si no se puede medir la CPU, Auto utiliza directamente ese límite detectado sin '
                            'adaptación dinámica.\n'
                            '• Un valor numérico fija el número máximo de tareas simultáneas; no es un objetivo de uso '
                            'de CPU.\n'
                            '\n'
                            'Más tareas pueden acelerar un lote grande, pero aumentan la carga, la temperatura y la '
                            'actividad del disco. Pulsa − hasta que aparezca Auto.',
        'paste': 'Pegar',
        'path_left': 'Ver la parte izquierda de la ruta',
        'path_right': 'Ver la parte derecha de la ruta',
        'pause': 'Pausa',
        'peak': 'Pico real máximo',
        'peak_tooltip': 'El pico real máximo es un límite, no un nivel que se deba alcanzar. Limita en dBTP los picos '
                        'más altos de la onda reconstruida, incluidos los que aparecen entre muestras, para reducir la '
                        'saturación después de codificar o transcodificar.\n'
                        '\n'
                        '• -1,0 dBTP — límite habitual de entrega, con el pico de salida más alto.\n'
                        '• -1,5 dBTP — valor predeterminado y compromiso prudente para MP3.\n'
                        '• -2,0 dBTP — margen adicional, útil si el archivo puede volver a codificarse o si se usa un '
                        'objetivo de sonoridad alto.\n'
                        '• 0 dBTP — sin margen; no recomendado para MP3.\n'
                        '\n'
                        'Un valor más negativo es más seguro, pero puede impedir que pistas muy dinámicas alcancen '
                        'exactamente el objetivo LUFS.',
        'phase_summary': 'Distribución estimada del tiempo total — análisis {analysis}, conversión {conversion}, '
                         'control de calidad {quality}.',
        'pipeline_enabled': 'Canalización de pistas — cada conversión comienza en cuanto termina su análisis.',
        'pre_measurement': 'Midiendo los archivos de entrada…',
        'preset': 'Preajuste',
        'preset_dynamic': 'Música dinámica',
        'preset_library': 'Biblioteca musical — recomendado',
        'preset_streaming': 'Streaming más intenso',
        'preset_tooltip': 'Aplica de una vez un objetivo de sonoridad, un pico real máximo y una calidad MP3 '
                          'coherentes. Cualquier cambio manual selecciona Personalizado.',
        'processing_cancelled': 'Proceso cancelado.',
        'processing_completed': 'Proceso finalizado',
        'processing_in_progress': 'Proceso en curso',
        'processing_paused': 'Proceso en pausa.',
        'processing_resumed': 'Proceso reanudado.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'AVISO — no se pudo realizar el control de calidad: {error}',
        'qc_log': ' — control de calidad: {quality}',
        'qc_ok': 'CORRECTO',
        'qc_warning': 'AVISO — {detail}',
        'quality': 'Calidad de audio',
        'quality_control': 'Control de calidad automático',
        'quality_control_tooltip': 'Vuelve a medir cada salida. Las correcciones siguen buscando ±0,50 LU; la alerta '
                                   'de sonoridad solo aparece fuera de ±0,60 LU. Los MP3 dinámicos conservan hasta '
                                   'tres intentos; WAV, AIFF y FLAC pueden repetirse desde la fuente hasta dos veces '
                                   'si hay margen True Peak. Desactivar elimina verificación, repeticiones y actividad '
                                   'del medidor.',
        'quality_tooltip': 'Regula el compromiso entre calidad y tamaño de los formatos comprimidos. Cuanto menor sea '
                           'el número, mayores serán la calidad y el caudal. Este ajuste no cambia el objetivo LUFS ni '
                           'el pico real máximo.\n'
                           '\n'
                           '• 0 — calidad máxima, recomendada para conservar los detalles.\n'
                           '• 1 a 2 — calidad muy alta.\n'
                           '• 3 a 4 — buen equilibrio entre calidad y tamaño.\n'
                           '• 5 a 9 — archivos más pequeños, con más pérdidas.\n'
                           '\n'
                           'FLAC sigue siendo sin pérdidas sea cual sea el valor. WAV y AIFF ignoran este ajuste y '
                           'conservan la frecuencia y profundidad PCM compatibles con la fuente. Para MP3, M4A, OGG y '
                           'Opus, un valor bajo puede exigir un caudal superior al original y producir un archivo '
                           'mayor. Un valor más alto suele reducir el tamaño, sin garantizar el mismo número de bytes '
                           'porque estos codificadores suelen usar VBR. Recodificar un formato con pérdidas no '
                           'recupera la información ya perdida.',
        'ready': 'Listo',
        'recursive_scan': 'Analizando carpetas de forma recursiva…',
        'remove_all': 'Quitar todo',
        'remove_selection': 'Quitar selección',
        'replaygain_help_text': 'ReplayGain calcula una ganancia y escribe REPLAYGAIN_TRACK_GAIN/PEAK. El flujo se '
                                'copia sin recodificar (-c:a copy); solo un reproductor compatible aplica las '
                                'etiquetas. El LUFS y el True Peak físicos no cambian.',
        'replaygain_levels_log': 'audio sin cambios: {before} LUFS · ReplayGain {gain} dB en metadatos · objetivo '
                                 'configurado {target} LUFS (requiere reproductor compatible)',
        'replaygain_log_help_text': 'En ReplayGain, el registro muestra la sonoridad física sin cambios, la ganancia '
                                    'escrita en los metadatos y el objetivo configurado. Con el control de calidad '
                                    'activado, «audio intacto y etiquetas verificadas» significa que sonoridad y pico '
                                    'se compararon con la fuente y que las etiquetas se volvieron a leer; no significa '
                                    'que el archivo mida físicamente el objetivo.',
        'replaygain_operation': 'ReplayGain sin recodificación',
        'replaygain_qc_help_text': 'Con el control de calidad activado, ReplayGain vuelve a medir el archivo entregado '
                                   'para confirmar que su sonoridad física y su pico no han cambiado, y después '
                                   'verifica las etiquetas Track. Un resultado correcto confirma que el audio se '
                                   'conserva y que las etiquetas están presentes, no que el objetivo se haya alcanzado '
                                   'físicamente.',
        'replaygain_qc_ok': 'CORRECTO — audio intacto y etiquetas verificadas',
        'replaygain_tags_missing': 'No se encontraron las etiquetas ReplayGain.',
        'replaygain_usefulness_text': 'ReplayGain sirve para igualar el volumen de reproducción de forma reversible y '
                                      'sin recodificación en una biblioteca usada con un reproductor compatible. Para '
                                      'entregar un archivo que mida físicamente el objetivo en todos los '
                                      'reproductores, use Normalizar.',
        'report_destination': 'destino',
        'report_detail': 'detalle',
        'report_error': 'AVISO — no se pudo crear el informe CSV: {error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'ganancia_db',
        'report_input_dbtp': 'dbtp_entrada',
        'report_input_lufs': 'lufs_entrada',
        'report_log': 'Informe CSV — {path}',
        'report_mode': 'modo',
        'report_operation': 'operación',
        'report_output_dbtp': 'dbtp_salida',
        'report_output_lufs': 'lufs_salida',
        'report_path': 'Informe: {path}',
        'report_qc': 'control_calidad',
        'report_qc_engine': 'motor_control_calidad',
        'report_seconds': 'tiempo_segundos',
        'report_source': 'origen',
        'report_status': 'estado',
        'report_tooltip': 'Crea únicamente un informe CSV con medidas, tiempos y alertas; no añade un JSON de '
                          'diagnóstico.',
        'resume': 'Reanudar después de una interrupción',
        'resume_not_saved': ' No se guardó el punto de reanudación: {error}',
        'resume_processing': 'Reanudar',
        'resume_tooltip': 'Los archivos ya terminados con los mismos ajustes se reconocen y no se vuelven a procesar.',
        'resumed_progress': 'Reanudado: {file}',
        'save_dialog_cancel': 'Cancelar',
        'save_dialog_filename': 'Nombre del archivo',
        'save_dialog_filetype': 'Formato',
        'save_dialog_location': 'Ubicación',
        'save_dialog_overwrite': 'Reemplazar',
        'save_dialog_overwrite_message': 'El archivo «{file}» ya existe.',
        'save_dialog_overwrite_title': '¿Reemplazar el archivo?',
        'save_dialog_parent': 'Carpeta superior',
        'save_dialog_save': 'Guardar',
        'save_issue_list': 'Guardar como CSV…',
        'save_issue_list_error': 'No se pudo guardar la lista: {error}',
        'save_issue_list_error_title': 'No se pudo guardar',
        'save_issue_list_title': 'Guardar la lista CSV',
        'scan_error': 'ERROR — {error}',
        'scanning_folders': 'Analizando carpetas…',
        'settings': 'Ajustes',
        'open_folder': 'Abrir carpeta',
        'show_option_help': 'Mostrar ayuda: {option}',
        'silent_copy': 'Audio silencioso o no medible copiado.',
        'silent_copy_no_replaygain': 'Audio silencioso copiado sin etiquetas ReplayGain.',
        'silent_unmeasurable': 'Audio silencioso o no medible.',
        'simulation': 'Simulación',
        'skip_compliant': 'No recodificar los archivos ya conformes',
        'skip_compliant_tooltip': 'Tras el análisis, un archivo a ±0,10 LU del objetivo y bajo el límite True Peak se '
                                  'copia sin recodificar.',
        'skipped_progress': 'Omitido: {file}',
        'source_audio_count': 'Archivos: {count}',
        'source_list_more': '… se conservan {count} fuentes más',
        'source_safety': 'Los archivos de origen nunca se mueven ni se modifican.',
        'source_selection_tooltip': 'Selección múltiple: Ctrl+clic para elementos separados y Mayús+clic para un '
                                    'intervalo.',
        'sources_added': '{count} fuente(s) añadida(s).',
        'start': 'Iniciar',
        'status_analyzed': 'ANALIZADO',
        'status_cancelled': 'CANCELADO',
        'status_compliant': 'CONFORME',
        'status_error': 'ERROR',
        'status_ok': 'CORRECTO',
        'status_resumed': 'REANUDADO',
        'status_skipped': 'OMITIDO',
        'status_warning': 'AVISO',
        'switch_to_dark': 'Modo oscuro',
        'switch_to_light': 'Modo claro',
        'tagline': 'Uniformiza el volumen de audio percibido',
        'target': 'Objetivo de sonoridad',
        'target_tooltip': 'El objetivo de sonoridad es la sonoridad integrada deseada para toda la pista, expresada en '
                          'LUFS. Un valor menos negativo produce un archivo más fuerte: -14 LUFS es más fuerte que -16 '
                          'LUFS. Una diferencia de 2 LU equivale aproximadamente a 2 dB de nivel antes de una eventual '
                          'limitación de pico.\n'
                          '\n'
                          'Referencias: -18 LUFS para un resultado más tranquilo y dinámico; -16 LUFS para un '
                          'equilibrio general; -14 LUFS para un resultado más fuerte de tipo streaming. Las '
                          'plataformas pueden aplicar después su propia normalización de reproducción.\n'
                          '\n'
                          'Este objetivo no aplana por sí solo la dinámica interna de la pista. Si el pico real máximo '
                          'impide alcanzar el objetivo sin saturación, el resultado puede quedar ligeramente más bajo.',
        'theme_accessible': 'Cambiar la apariencia de la aplicación. La elección se guarda.',
        'total_time': 'Tiempo total: {duration}',
        'track_two_pass': 'Normalización de pista en dos pasadas.',
        'true_peak_meter_exceeded': 'Exceso {margin} dB',
        'true_peak_meter_margin': 'Margen {margin} dB',
        'true_peak_meter_title': 'Margen de pico',
        'true_peak_meter_tooltip': 'Compara el pico real de la última salida con el límite elegido. El marcador '
                                   'muestra el último valor y el triángulo conserva el pico más alto del lote. Verde: '
                                   'límite respetado; naranja: exceso de hasta 0,25 dB; rojo: exceso mayor. La '
                                   'tolerancia naranja pertenece al control de calidad de LUFScale y no es una norma '
                                   'de entrega. Se reinicia con cada lote.',
        'true_peak_meter_waiting': 'Esperando una medición dBTP',
        'version_changes': '• Instalador único sin conexión para Windows 10/11 x86-64.\n'
                           '• Incluye Python, PySide6/Qt, FFmpeg, códecs, guías y licencias; no descarga ni requiere '
                           'PowerShell durante la instalación.\n'
                           '• La compilación valida loudnorm y los codificadores antes de crear el instalador y su SHA-256.',
        'version_changes_title': 'Novedades de la versión {version}',
        'version_label': 'Versión {version}',
        'volume': 'Volumen',
        'volume_loud': 'Fuerte: -14 LUFS',
        'volume_normal': 'Normal: -16 LUFS',
        'volume_soft': 'Suave: -18 LUFS',
        'volume_tooltip': 'Este ajuste es un acceso directo al objetivo de sonoridad; no cambia el volumen de escucha '
                          'del sistema.\n'
                          '\n'
                          '• Suave: -18 LUFS — nivel más tranquilo, más margen dinámico y menos riesgo de activar el '
                          'limitador.\n'
                          '• Normal: -16 LUFS — compromiso equilibrado y buen punto de partida para una biblioteca '
                          'personal.\n'
                          '• Fuerte: -14 LUFS — reproducción más presente, cercana al objetivo Normal de Spotify, pero '
                          'con más probabilidad de necesitar limitación.\n'
                          '• Personalizado — permite introducir directamente otro objetivo LUFS.\n'
                          '\n'
                          'Son opciones prácticas, no una norma universal.',
        'warning_list_title': 'Advertencias de procesamiento',
        'warnings_button': 'Alertas ({count})',
        'warnings_button_tooltip': 'Abre la lista de alertas con nombre de archivo, ruta y detalle. Disponible durante '
                                   'una pausa o después del proceso.',
        'warnings_dialog_title': 'Alertas del proceso'},
 'hi': {'activity_cancelled': 'गतिविधि: प्रसंस्करण रद्द',
        'activity_cancelling': 'गतिविधि: रद्द किया जा रहा है…',
        'activity_completed': 'गतिविधि: प्रसंस्करण पूरा',
        'activity_compliant': 'अनुरूप: {count}',
        'activity_detected': 'गतिविधि: {total} फ़ाइल मिलीं',
        'activity_errors': 'त्रुटि: {count}',
        'activity_files': 'फ़ाइलें: {count}',
        'activity_idle': 'गतिविधि: प्रतीक्षा में',
        'activity_preparing': 'गतिविधि: फ़ाइलें तैयार हो रही हैं…',
        'activity_progress': '{total} फ़ाइलें • सफल {success} • चेतावनी {warnings} • त्रुटि {failed} • जारी/छोड़े '
                             '{skipped} • अनुरूप {compliant}',
        'activity_skipped': 'जारी/छोड़े: {count}',
        'activity_successes': 'सफल: {count}',
        'activity_warnings': 'चेतावनी: {count}',
        'adaptive_disabled_log': 'अनुकूली विश्लेषण — {sample} माप के बाद तेज़ जाँच बंद ({successes} सफल, अनुमानित बचत '
                                 '{percent:+.1f}%)।',
        'add_folders': 'फ़ोल्डर जोड़ें…',
        'add_mp3': 'ऑडियो फ़ाइलें जोड़ें…',
        'add_replaygain': 'ReplayGain जोड़ें',
        'add_source_files': 'ऑडियो फ़ाइलें जोड़ें',
        'add_source_folder': 'स्रोत फ़ोल्डर जोड़ें',
        'already_completed': 'पिछले रन में पहले ही पूरा।',
        'already_compliant_badge': 'अनुरूप',
        'already_compliant_copy': 'पहले से अनुरूप: ऑडियो पुनः एनकोड किए बिना समान कॉपी।',
        'already_compliant_log': 'पहले से अनुरूप, पुनः एनकोड नहीं',
        'analysis_cache_summary': 'विश्लेषण कैश — {hits} मापन पुनः उपयोग हुए।',
        'analysis_impossible': 'विश्लेषण विफल: {error}',
        'analysis_measurement_progress': 'विश्लेषण {current}/{total} — {file} — {value}',
        'analysis_method': 'विश्लेषण विधि',
        'analysis_method_adaptive': 'अनुकूली — लाभ न हो तो बंद',
        'analysis_method_fast': 'तेज़ — प्रायोगिक',
        'analysis_method_historical': 'पूर्ण मापन — संदर्भ पद्धति',
        'analysis_method_log': 'विश्लेषण विधि — {method}।',
        'analysis_method_tooltip': 'स्थिर संस्करण अपने-आप पूर्ण ऐतिहासिक संदर्भ माप का उपयोग करता है; संदर्भ संग्रह पर '
                                   'सत्यापित यही एक विधि है। तेज़ और अनुकूली विकल्प अब उपलब्ध नहीं हैं।',
        'analysis_progress': 'विश्लेषण {current}/{total}: {file}',
        'analysis_progress_help_text': 'केवल विश्लेषण मोड में प्रत्येक मापन पूरा होने पर ऊपर का ग्राफ, प्रसंस्करण लॉग '
                                       'और प्रगति पट्टी फ़ाइल-दर-फ़ाइल आगे बढ़ते हैं; नीचे का ग्राफ स्थिर रहता है।',
        'analyze': 'विश्लेषण करें',
        'analyze_only_fresh_help_text': 'केवल विश्लेषण हर बार FFmpeg से प्रत्येक स्रोत को पूरा मापता है। ऊपर का ग्राफ '
                                        'और प्रगति फ़ाइल-दर-फ़ाइल बढ़ते हैं; कोई आउटपुट या आउटपुट गुणवत्ता-जाँच नहीं '
                                        'होती।',
        'analyze_operation': 'विश्लेषण/अनुकरण',
        'analyzed_progress': 'विश्लेषित: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'ऑडियो स्ट्रीम बिना पुनः एन्कोडिंग कॉपी हुई; ReplayGain टैग जोड़े गए।',
        'audio_tab': 'ऑडियो',
        'auto_start': 'ड्रॉप या पेस्ट के बाद स्वतः शुरू करें',
        'auto_start_tooltip': 'गंतव्य चुना होने पर ड्रैग-एंड-ड्रॉप या पेस्ट से स्रोत जुड़ते ही प्रसंस्करण शुरू करता '
                              'है।',
        'cancel': 'रद्द करें',
        'cancelled_summary': 'रद्द — {success} सफल, {failed} त्रुटि, {skipped} जारी/छोड़े, {warnings} चेतावनी, '
                             '{compliant} अनुरूप — {duration}।',
        'cancelling': 'रद्द किया जा रहा है…',
        'choose': 'चुनें…',
        'choose_output': 'गंतव्य फ़ोल्डर चुनें',
        'clipboard': 'क्लिपबोर्ड',
        'clipboard_empty': 'क्लिपबोर्ड में किसी फ़ोल्डर या समर्थित ऑडियो फ़ाइल का मान्य पथ नहीं है।',
        'close_button': 'बंद करें',
        'close_question': 'प्रसंस्करण रद्द कर अनुप्रयोग बंद करें?',
        'completed_dialog_summary': 'स्थिति: पूर्ण\n'
                                    'फ़ाइलें: {files}\n'
                                    'सफल: {success}\n'
                                    'त्रुटियाँ: {failed}\n'
                                    'जारी या छोड़े गए: {skipped}\n'
                                    'चेतावनियाँ: {warnings}\n'
                                    'अनुरूप: {compliant}\n'
                                    'कुल समय: {duration}',
        'completed_summary': 'पूरा — {success} सफल, {failed} त्रुटि, {skipped} जारी/छोड़े, {warnings} चेतावनी, '
                             '{compliant} अनुरूप — {duration}।',
        'completed_with_errors': 'प्रसंस्करण चेतावनियों के साथ पूरा',
        'convert': 'समान करें',
        'convert_operation': 'ऑडियो सामान्यीकरण',
        'cpu_tooltip': 'प्रसंस्करण के दौरान हर सेकंड अपडेट होने वाला सिस्टम का कुल CPU उपयोग।',
        'cpu_unavailable': 'उपलब्ध नहीं',
        'cpu_usage': 'CPU',
        'create_report': 'CSV रिपोर्ट बनाएँ',
        'csv_file_filter': 'CSV फ़ाइलें (*.csv)',
        'custom': 'कस्टम',
        'decrease_value': 'मान घटाएँ',
        'description': 'मूल फ़ाइल बदले बिना हर फ़ाइल का perceived volume अलग से समान करता है।',
        'destination': 'गंतव्य',
        'destination_error': 'त्रुटि — गंतव्य उपलब्ध नहीं: {error}',
        'destination_path_tooltip': 'पथ पर क्लिक करें, फिर तीर कुंजियों, Home/End या माउस व्हील का उपयोग करें। पथ चुना '
                                    'और कॉपी किया जा सकता है, लेकिन बदला नहीं जा सकता।',
        'destination_required_start': 'पहले “चुनें…” बटन से गंतव्य फ़ोल्डर चुनें।',
        'dialog_ok': 'ठीक है',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — उप-फ़ोल्डर सहित',
        'drop_title': 'फ़ोल्डर या ऑडियो फ़ाइलें यहाँ छोड़ें',
        'elapsed_time': 'बीता समय: {duration}',
        'error_list_title': 'प्रसंस्करण त्रुटियाँ',
        'error_progress': 'त्रुटि: {file}',
        'errors_button': 'त्रुटियाँ ({count})',
        'errors_button_tooltip': 'फ़ाइल नाम, पथ और विवरण सहित त्रुटि सूची खोलता है। विराम के दौरान या प्रसंस्करण के '
                                 'बाद उपलब्ध।',
        'errors_dialog_title': 'प्रसंस्करण त्रुटियाँ',
        'estimated_result': 'अनुमानित परिणाम; कोई फ़ाइल नहीं बनी।',
        'estimated_total_calculating': 'अनुमानित कुल समय: गणना जारी…',
        'estimated_total_time': 'अनुमानित कुल समय: {duration}',
        'estimated_total_time_with_day_finish': 'अनुमानित कुल समय: {duration} — {days} दिन। {time}',
        'estimated_total_time_with_finish': 'अनुमानित कुल समय: {duration} — {time}',
        'estimated_total_unavailable': 'अनुमानित कुल समय: उपलब्ध नहीं',
        'ffmpeg_download_button': 'FFmpeg की आधिकारिक वेबसाइट खोलें',
        'ffmpeg_error_no_detail': 'बिना विवरण की FFmpeg त्रुटि।',
        'ffmpeg_execution_error': 'FFmpeg नहीं चल सका: {error}',
        'ffmpeg_incompatible': 'असंगत FFmpeg',
        'ffmpeg_missing': 'FFmpeg नहीं मिला',
        'ffmpeg_missing_encoders': 'इस FFmpeg में सभी आवश्यक ऑडियो एनकोडर नहीं हैं: {encoders}।',
        'ffmpeg_missing_message': 'FFmpeg स्थापित और PATH में उपलब्ध होना चाहिए, या प्रोग्राम के पास रखा होना चाहिए।',
        'ffmpeg_no_lame': 'इस FFmpeg बिल्ड में libmp3lame MP3 एन्कोडर नहीं है।',
        'ffmpeg_no_loudnorm': 'इस FFmpeg बिल्ड में loudnorm फ़िल्टर नहीं है।',
        'ffmpeg_not_responding': 'FFmpeg सही उत्तर नहीं दे रहा है।',
        'file_exists': 'फ़ाइल पहले से मौजूद है।',
        'files_found': '{total} ऑडियो फ़ाइलें मिलीं — {operation} — {parallel} समानांतर प्रक्रियाएँ।',
        'finalization_completed': 'अंतिम चरण {duration} में पूरा हुआ।',
        'finalizing': 'अंतिम चरण — रिपोर्ट, विश्लेषण कैश और पुनःआरंभ डेटा…',
        'folder': 'फ़ोल्डर',
        'folder_unavailable': 'फ़ोल्डर उपलब्ध नहीं',
        'guide_analysis_method': 'LUFScale संदर्भ-संग्रह पर सत्यापित पूर्ण ऐतिहासिक मापन पद्धति का स्वचालित उपयोग करता '
                                 'है।',
        'guide_analyze_prediction_body': 'केवल विश्लेषण अनुमान दे सकता है, लेकिन कोई ऑडियो फ़ाइल या आउटपुट '
                                         'गुणवत्ता-जाँच नहीं बनाता।',
        'guide_analyze_prediction_title': 'बिना आउटपुट का अनुमान',
        'guide_build_body': 'Windows 10 1809 या बाद के अथवा Windows 11 x86-64 पर:\n'
                            '\n'
                            '1. “LUFScale-2.1.12-Setup-x64.exe” और उसकी SHA-256 फ़ाइल डाउनलोड करें।\n'
                            '2. SHA-256 जाँचें और इंस्टॉलर पर डबल-क्लिक करें।\n'
                            '3. GNU GPL लाइसेंस पढ़कर स्वीकार करें और विज़ार्ड का पालन करें।\n'
                            '4. Start मेनू से LUFScale खोलें।\n'
                            '\n'
                            'एप्लिकेशन, Python, PySide6/Qt, FFmpeg, codecs, guides और licences पहले से शामिल हैं। '
                            'इंस्टॉलेशन कुछ डाउनलोड नहीं करता और PowerShell command नहीं माँगता। Windows '
                            'uninstaller अपने-आप बनता है।\n'
                            '\n'
                            'वितरण signed नहीं है; फ़ाइल और checksum जाँचने के बाद SmartScreen पुष्टि माँग सकता है।',
        'guide_build_title': 'Windows x86-64 पर LUFScale इंस्टॉल करें',
        'guide_estimated_total_help': 'अनुमानित कुल समय: 12 मिनट — लगभग 14:30 पर समाप्ति। ‘12 मिनट’ अनुमानित कुल अवधि '
                                      'और ‘14:30’ अपेक्षित समाप्ति समय है। आधी रात पार होने पर समय से पहले दिनों की '
                                      'संख्या अपने-आप जुड़ती है, जैसे ‘2 दिन — 14:30’।',
        'guide_file_processing_body': 'प्रत्येक फ़ाइल के अपने मापन और गेन से ट्रू पीक सीमा के भीतर लक्ष्य LUFS प्राप्त '
                                      'किया जाता है।',
        'guide_file_processing_title': 'फ़ाइल-दर-फ़ाइल प्रसंस्करण',
        'guide_help_tooltip': 'चुनी हुई भाषा में पूरा PDF मार्गदर्शक खोलता है।',
        'guide_level_mode_body': 'Track - recommended: हर file को target के पास लाता है। Album - advanced specialized: '
                                 'common gain लगाकर contrasts बचाता है। क्रम में सुने जाने वाले work के लिए Album; '
                                 'shuffle या समान file level के लिए Track चुनें।',
        'guide_license_body': 'LUFScale GNU GPL-3.0-or-later के अंतर्गत वितरित मुक्त सॉफ्टवेयर है। लाइसेंस की शर्तों '
                              'के अनुसार इसका उपयोग, अध्ययन, संशोधन और पुनर्वितरण किया जा सकता है। स्रोत कोड, सूचनाएँ '
                              'और तृतीय-पक्ष लाइसेंस वितरण में शामिल हैं। सॉफ्टवेयर बिना किसी वारंटी के दिया जाता है।',
        'guide_license_feature': '• GNU GPL-3.0-or-later मुक्त सॉफ़्टवेयर: लाइसेंस के अनुसार उपयोग, अध्ययन, बदलाव और '
                                 'पुनर्वितरण की अनुमति है।\n'
                                 '• Python, Qt और FFmpeg सहित offline Windows x86-64 installer। Windows 11 अनुशंसित है; '
                                 'Windows 10 1809 या बाद का संस्करण compatibility target है, लेकिन Microsoft standard '
                                 'support समाप्त हो चुका है।',
        'guide_license_title': 'मुक्त सॉफ्टवेयर और पुनर्वितरण',
        'guide_log_legend_cancelled': 'प्रोसेसिंग जानबूझकर रोकी गई; यह त्रुटि नहीं है।',
        'guide_log_legend_compliant': 'ऑडियो बिना बदले कॉपी हुआ: स्रोत पहले से लक्ष्य और पीक सीमा में था।',
        'guide_log_legend_error': 'संबंधित फ़ाइल की प्रोसेसिंग पूरी नहीं हो सकी।',
        'guide_log_legend_success': 'प्रोसेसिंग बिना किसी गड़बड़ी के पूरी हुई।',
        'guide_log_legend_warning': 'आउटपुट बना है, लेकिन एक माप तय सहनशीलता से बाहर है।',
        'guide_missing_message': 'PDF मार्गदर्शक नहीं मिला: {path}',
        'guide_missing_title': 'मार्गदर्शक उपलब्ध नहीं',
        'guide_open_error': 'PDF गाइड नहीं खुल सकी: {path}',
        'guide_quality_priority_body': 'LUFScale फ़ाइलों की ध्वनि-तीव्रता मापता है और सामान्यीकरण के साथ ट्रू पीक '
                                       'नियंत्रित करते हुए अनुभूत ध्वनि को LUFS लक्ष्य तक वास्तव में समायोजित करता है। '
                                       'प्रत्येक स्रोत की पूरी अवधि का विश्लेषण होता है, फिर आउटपुट को दोबारा मापकर '
                                       'जाँचा जाता है। परिणाम टैग या संगत प्लेयर पर निर्भर नहीं रहता: फ़ाइलों के स्तर '
                                       'अधिक समान होते हैं, विचलन बताए जाते हैं और मूल फ़ाइलें नहीं बदलतीं।',
        'guide_quality_priority_title': 'LUFScale क्या करता है?',
        'help_button': 'सहायता',
        'help_overview': '• MP3, FLAC, WAV, AIFF, M4A, OGG और Opus का सामान्यीकरण, ReplayGain या विश्लेषण।\n'
                         '• प्रत्येक फ़ाइल अलग मापी जाती है और चुने हुए लक्ष्य तक संसाधित होती है।\n'
                         '• फ़ोल्डर संरचना, मेटाडेटा और कलाकृति सुरक्षित रहती है; मूल फ़ाइलें नहीं बदलतीं।\n'
                         '• समानांतर प्रसंस्करण, कैश, पुनः आरंभ, गुणवत्ता-जाँच, CSV, प्रगति, CPU और LUFS इतिहास।\n'
                         '• 12 भाषाओं में अंतरफलक और PDF मार्गदर्शिका।',
        'help_title': 'मुख्य विशेषताएँ',
        'increase_value': 'मान बढ़ाएँ',
        'input_lufs_log': 'इनपुट {value} LUFS',
        'interface_ffmpeg_message': 'अंतर्निहित FFmpeg ऑडियो इंजन गायब है या उपयोग योग्य नहीं है। पूर्ण वितरण संग्रह '
                                    'से LUFScale दोबारा इंस्टॉल करें।',
        'internal_error': 'आंतरिक त्रुटि: {error}',
        'interrupted': 'प्रसंस्करण बाधित।',
        'invalid_location': 'अमान्य स्थान',
        'issue_detail_column': 'विवरण',
        'issue_file_column': 'फ़ाइल',
        'issue_path_column': 'पथ',
        'language': 'भाषा',
        'language_tooltip': 'इंटरफ़ेस, संदेशों और भविष्य की CSV रिपोर्ट की भाषा तुरंत बदलता है। चयन सहेजा जाता है।',
        'log_help_text': 'प्रत्येक पंक्ति किसी फ़ाइल या सामान्य प्रसंस्करण चरण से संबंधित है।\n'
                         '\n'
                         '• सफल पंक्ति सीधे फ़ाइल नाम से शुरू होती है; सफलता शब्द दोहराया नहीं जाता।\n'
                         '• अनुरूप, पुनः आरंभ, छोड़ी गई, रद्द और त्रुटि अवस्थाएँ तभी दिखाई जाती हैं जब वे उपयोगी सूचना '
                         'दें।\n'
                         '• स्तर इनपुट से दोबारा मापे गए आउटपुट तक और फिर संभावित गुणवत्ता-जाँच परिणाम दिखाते हैं।\n'
                         '• चेतावनी और त्रुटि अलग सूचियाँ खोलते हैं जिनमें नाम, पथ और विवरण होते हैं। वे विराम के समय '
                         'या प्रसंस्करण के बाद उपलब्ध हैं और प्रत्येक सूची सहेजी जा सकती है।\n'
                         '\n'
                         'रंग: हरा = सफलता; नारंगी = चेतावनी; लाल = अधूरी फ़ाइल; नीला-बैंगनी = पुनः आरंभ; धूसर = '
                         'सूचना, छोड़ी गई या रद्द अवस्था।\n'
                         '\n'
                         'QC चेतावनी — ध्वनि-तीव्रता का अर्थ है कि दोबारा मापा आउटपुट अपेक्षित मान से ±0.60 LU से अधिक '
                         'अलग है। अधिक ऋणात्मक मान धीमा और कम ऋणात्मक मान तेज़ है। अंतर निरपेक्ष है: -14.00 के बजाय '
                         '-14.69 का अंतर 0.69 LU है। फ़ाइल फिर भी बनती है; यह रूपांतरण विफलता नहीं है। सुनने में ठीक '
                         'हो तो कार्रवाई आवश्यक नहीं। कठोर लक्ष्य के लिए विवरण और CSV देखें, फिर लक्ष्य और ट्रू पीक '
                         'सीमा जाँचकर दोबारा चलाएँ। केवल संदेश से यह तय नहीं होता कि कारण सीमा, एन्कोडर या सुधार-सीमा '
                         'है।\n'
                         '\n'
                         'QC चेतावनी — पीक का अर्थ है कि दोबारा मापा ट्रू पीक चुनी सीमा से 0.25 dB से अधिक ऊपर है। '
                         'फ़ाइल फिर भी बनती है। चेतावनी बनी रहे तो कम LUFS लक्ष्य या अधिक सुरक्षित पीक सीमा, जैसे -2.0 '
                         'dBTP, चुनकर फिर प्रसंस्करण करें।\n'
                         '\n'
                         'संचित समय सभी समानांतर कार्यों का काम जोड़ता है। कुल समय वास्तविक बीती अवधि है।',
        'log_placeholder': 'प्रसंस्करण लॉग यहाँ दिखाई देगा।',
        'log_title': 'प्रसंस्करण लॉग',
        'loudness_comparison_after': 'बाद में',
        'loudness_comparison_analysis_only': 'केवल विश्लेषण में कोई आउटपुट नहीं',
        'loudness_comparison_before': 'पहले',
        'loudness_comparison_help_text': 'प्रत्येक फ़ाइल दाईं ओर एक बिंदु जोड़ती है। ऊपर वाला ग्राफ हमेशा मापा गया '
                                         'स्रोत दिखाता है। सामान्यीकरण में नीचे वाला ग्राफ वास्तव में दोबारा मापा '
                                         'आउटपुट दिखाता है। ReplayGain में दूसरा बिंदीदार ग्राफ स्रोत की ध्वनि-तीव्रता '
                                         'और संग्रहीत Track Gain से प्लेबैक का अनुमान दिखाता है। ≈ चिह्न और संगत '
                                         'प्लेयर का संकेत बताते हैं कि यह दी गई फ़ाइल का भौतिक मापन नहीं है। असंगत '
                                         'प्लेयर मूल स्तर रखता है; संगत प्लेयर प्रीएम्प या क्लिपिंग-रोकथाम के कारण '
                                         'परिणाम बदल सकता है। दोनों ग्राफ समान स्थिर ±6 LU पैमाना रखते हैं। केवल '
                                         'विश्लेषण में नीचे कोई आउटपुट नहीं होता।',
        'loudness_comparison_increased': 'अंतर {value} LU बढ़ा',
        'loudness_comparison_needs_qc': 'तुलना के लिए गुणवत्ता नियंत्रण चालू करें',
        'loudness_comparison_no_after': 'इस क्रिया के लिए बाद का graph नहीं',
        'loudness_comparison_not_applicable': 'इस क्रिया के लिए तुलना उपलब्ध नहीं',
        'loudness_comparison_reached': 'लक्ष्य प्राप्त · अंतर {value} LU',
        'loudness_comparison_reduced': 'अंतर {value} LU कम हुआ',
        'loudness_comparison_replaygain_after': 'अनुमानित RG playback',
        'loudness_comparison_replaygain_note': 'संगत प्लेयर · ऑडियो अपरिवर्तित',
        'loudness_comparison_scale': 'दृश्य ±{scale} LU · QC सीमा ±{tolerance} LU',
        'loudness_comparison_target': 'लक्ष्य {value} LUFS',
        'loudness_comparison_title': 'ध्वनि-तीव्रता में बदलाव',
        'loudness_comparison_tooltip': 'ऊपर भौतिक ध्वनि-तीव्रता दिखती है। ReplayGain में नीचे वाला ग्राफ संग्रहीत गेन '
                                       'से संगत प्लेबैक का अनुमान दिखाता है।',
        'loudness_comparison_unchanged': 'अंतर नहीं बदला',
        'loudness_comparison_waiting': 'प्रोसेस की गई फ़ाइल की प्रतीक्षा',
        'loudness_meter_current_file': 'नवीनतम: {file}',
        'loudness_meter_estimated': 'अनुमानित',
        'loudness_meter_help_text': 'लाल रेखा लक्ष्य है और नीला मान अंतिम output की वास्तव में दोबारा मापी गई loudness '
                                    'है। यह हर file पर ऊपर या नीचे जाता है। Score अंतिम 8 दोबारा मापे गए outputs का '
                                    'सार देता है। लाल panel में «चेतावनियाँ देखें» आए तो processing रोकें या पूरी होने '
                                    'दें, फिर प्रभावित files पहचानने के लिए चेतावनियाँ खोलें।',
        'loudness_meter_maximum': 'अधिक {value}',
        'loudness_meter_measured': 'मापा गया',
        'loudness_meter_minimum': 'न्यून {value}',
        'loudness_meter_no_file': 'विश्लेषण की प्रतीक्षा',
        'loudness_meter_target': 'लक्ष्य {value} LUFS',
        'loudness_meter_title': 'ध्वनि-तीव्रता मीटर',
        'loudness_meter_tooltip': 'लाल लक्ष्य; अंतिम output का वास्तविक दोबारा मापा मान नीले रंग में।',
        'loudness_meter_waiting': 'ऑडियो फ़ाइल की प्रतीक्षा',
        'loudness_meter_worst_file': 'सबसे बड़ा अंतर: {file}',
        'loudness_meter_worst_file_detail': 'पिछले 8 विश्लेषणों में सबसे बड़ा अंतर: {file} — {expected} LUFS लक्ष्य के '
                                            'लिए {measured} LUFS, अंतर {deviation} LU।',
        'loudness_score_acceptable': 'स्वीकार्य',
        'loudness_score_check': 'चेतावनियाँ देखें',
        'loudness_score_excellent': 'उत्कृष्ट',
        'loudness_score_good': 'अच्छा',
        'loudness_score_needs_qc': 'लक्ष्य स्कोर: गुणवत्ता नियंत्रण चालू करें',
        'loudness_score_not_applicable': 'लक्ष्य स्कोर: लागू नहीं',
        'loudness_score_tooltip': 'Score अंतिम 8 दोबारा मापे गए outputs का उपयोग करता है। 100 सटीक, 50 का अर्थ 0.60 LU '
                                  'RMS अंतर और 0 का अर्थ 1.20 LU या अधिक है। लाल panel का अर्थ है कि चेतावनियाँ button '
                                  'में कम से कम एक loudness warning उपलब्ध है।',
        'loudness_score_value': 'लक्ष्य स्कोर: {score}/100\n{rating}\nRMS त्रुटि: {deviation}\xa0LU',
        'loudness_score_waiting': 'लक्ष्य स्कोर: प्रतीक्षा',
        'measurement_unavailable': 'मापन उपलब्ध नहीं।',
        'mp3': 'MP3',
        'mp3_filter': 'समर्थित ऑडियो (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'कोई फ़ोल्डर नहीं चुना गया',
        'no_mp3': 'कोई समर्थित ऑडियो फ़ाइल नहीं मिली।',
        'no_new_source': 'कोई नया मान्य फ़ोल्डर या समर्थित ऑडियो फ़ाइल नहीं जोड़ी गई।',
        'not_performed': 'नहीं किया गया',
        'open_output_error': 'गंतव्य फ़ोल्डर नहीं खुल सका: {error}',
        'operation': 'क्रिया',
        'operation_analyze': 'केवल विश्लेषण — कोई नई फ़ाइल नहीं बनेगी',
        'operation_analyze_label': 'केवल विश्लेषण',
        'operation_convert': 'सामान्यीकृत करें — ऑडियो को वास्तव में संसाधित करें',
        'operation_convert_label': 'ऑडियो सामान्यीकरण',
        'operation_help_text': 'सामान्यीकरण प्रत्येक फ़ाइल को अलग संसाधित कर आउटपुट फिर मापता है। ReplayGain नमूने '
                               'नहीं बदलता। केवल विश्लेषण मापन और वैकल्पिक CSV बनाता है, ऑडियो नहीं।',
        'operation_replaygain': 'ReplayGain — ऑडियो का पुनः एन्कोडिंग नहीं',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'सामान्यीकरण ऑडियो बदलता है। ReplayGain धारा को कॉपी कर टैग जोड़ता है। केवल विश्लेषण '
                             'ऑडियो बनाए बिना मापता है।',
        'option_status_auto_start': 'स्वतः',
        'option_status_overwrite': 'अधि',
        'option_status_quality_control': 'गुण',
        'option_status_report': 'CSV',
        'option_status_resume': 'जारी',
        'option_status_skip_compliant': 'छोड़',
        'options_tab': 'विकल्प',
        'output_lufs_log': 'आउटपुट {value} LUFS',
        'output_lufs_unavailable': 'आउटपुट LUFS उपलब्ध नहीं',
        'overwrite': 'मौजूदा फ़ाइलें अधिलेखित करें',
        'overwrite_tooltip': 'गंतव्य में पहले से मौजूद MP3 को बदलने देता है। स्रोत फ़ाइलें कभी अधिलेखित नहीं होतीं।',
        'parallel': 'समानांतर प्रक्रियाएँ',
        'parallel_adjusted': 'स्वचालित समानांतरता — {active} प्रक्रियाएँ, CPU {cpu:.0f}%।',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'स्वचालित, अधिकतम {maximum}',
        'parallel_tooltip': 'एक समय में संसाधित होने वाली फ़ाइलों की संख्या तय करता है।\n'
                            '\n'
                            '• स्वचालित मोड अधिकतम 4 कार्यों से शुरू होता है। CPU मापन उपलब्ध हो तो 70% से कम उपयोग पर '
                            'एक कार्य जोड़ता और 92% से अधिक पर एक हटाता है।\n'
                            '• यह मिले तार्किक CPU की संख्या और 16 की पूर्ण सीमा से अधिक नहीं जाता।\n'
                            '• CPU मापन न हो तो उपलब्ध सीमा सीधे उपयोग होती है।\n'
                            '• संख्या एक साथ चलने वाले कार्यों की अधिकतम सीमा है; यह CPU उपयोग का लक्ष्य नहीं है।\n'
                            '\n'
                            'स्वचालित दिखने तक − दबाएँ।',
        'paste': 'चिपकाएँ',
        'path_left': 'पथ का बायाँ भाग दिखाएँ',
        'path_right': 'पथ का दायाँ भाग दिखाएँ',
        'pause': 'रोकें',
        'peak': 'अधिकतम ट्रू पीक',
        'peak_tooltip': 'अधिकतम ट्रू पीक एक सीमा है, प्राप्त करने का लक्ष्य नहीं। यह नमूनों के बीच की चोटियों सहित '
                        'पुनर्निर्मित तरंग की सबसे ऊँची चोटियों को dBTP में सीमित करता है।\n'
                        '\n'
                        '• -1.0 dBTP — सामान्य वितरण सीमा।\n'
                        '• -1.5 dBTP — MP3 के लिए सावधान डिफ़ॉल्ट।\n'
                        '• -2.0 dBTP — पुनः एन्कोडिंग या ऊँचे लक्ष्य के लिए अतिरिक्त हेडरूम।\n'
                        '• 0 dBTP — कोई हेडरूम नहीं; MP3 के लिए अनुशंसित नहीं।\n'
                        '\n'
                        'अधिक ऋणात्मक मान सुरक्षित है, पर बहुत डायनेमिक ट्रैक को लक्ष्य तक पहुँचने से रोक सकता है।',
        'phase_summary': 'अनुमानित कुल-समय विभाजन — विश्लेषण {analysis}, परिवर्तन {conversion}, गुणवत्ता नियंत्रण '
                         '{quality}।',
        'pipeline_enabled': 'ट्रैक पाइपलाइन — विश्लेषण पूरा होते ही प्रत्येक परिवर्तन शुरू होता है।',
        'pre_measurement': 'इनपुट फ़ाइलें मापी जा रही हैं…',
        'preset': 'प्रीसेट',
        'preset_dynamic': 'डायनेमिक संगीत',
        'preset_library': 'संगीत लाइब्रेरी — अनुशंसित',
        'preset_streaming': 'अधिक तेज़ स्ट्रीमिंग',
        'preset_tooltip': 'ध्वनि-तीव्रता लक्ष्य, अधिकतम ट्रू पीक और MP3 गुणवत्ता का सुसंगत समूह एक साथ लागू करता है। '
                          'कोई मैन्युअल बदलाव कस्टम चुनता है।',
        'processing_cancelled': 'प्रसंस्करण रद्द।',
        'processing_completed': 'प्रसंस्करण पूरा',
        'processing_in_progress': 'प्रसंस्करण जारी',
        'processing_paused': 'प्रसंस्करण रुका हुआ है।',
        'processing_resumed': 'प्रसंस्करण फिर शुरू हुआ।',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'चेतावनी — गुणवत्ता नियंत्रण विफल: {error}',
        'qc_log': ' — गुणवत्ता नियंत्रण: {quality}',
        'qc_ok': 'सफल',
        'qc_warning': 'चेतावनी — {detail}',
        'quality': 'ऑडियो गुणवत्ता',
        'quality_control': 'स्वचालित गुणवत्ता नियंत्रण',
        'quality_control_tooltip': 'प्रत्येक आउटपुट फिर मापा जाता है। सुधार ±0.50 LU को लक्ष्य बनाते हैं; '
                                   'ध्वनि-तीव्रता चेतावनी केवल ±0.60 LU से बाहर आती है। गतिशील MP3 के अधिकतम तीन '
                                   'प्रयास होते हैं; ट्रू पीक की गुंजाइश मिलने पर WAV, AIFF और FLAC स्रोत से दो बार तक '
                                   'दोहराए जा सकते हैं। इसे बंद करने पर सत्यापन, पुनः प्रयास और मीटर गतिविधि हट जाती '
                                   'है।',
        'quality_tooltip': 'संपीड़ित प्रारूपों के लिए गुणवत्ता और आकार का संतुलन तय करता है। संख्या जितनी कम होगी, '
                           'गुणवत्ता और बिटरेट उतने अधिक होंगे। यह सेटिंग LUFS लक्ष्य या अधिकतम True Peak नहीं बदलती।\n'
                           '\n'
                           '• 0 — अधिकतम गुणवत्ता, विवरण बचाने के लिए अनुशंसित।\n'
                           '• 1 से 2 — बहुत उच्च गुणवत्ता।\n'
                           '• 3 से 4 — गुणवत्ता/आकार का अच्छा संतुलन।\n'
                           '• 5 से 9 — अधिक हानि के साथ छोटी फ़ाइलें।\n'
                           '\n'
                           'FLAC हर मान पर lossless रहता है। WAV और AIFF इस सेटिंग को अनदेखा कर source-compatible PCM '
                           'sample rate और bit depth रखते हैं। MP3, M4A, OGG और Opus में कम मान source से अधिक bitrate '
                           'माँग सकता है, इसलिए output बड़ा हो सकता है। बड़ा मान आम तौर पर आकार घटाता है, लेकिन VBR के '
                           'कारण समान bytes की गारंटी नहीं देता। Lossy format को फिर encode करने से पहले खोई जानकारी '
                           'वापस नहीं आती।',
        'ready': 'तैयार',
        'recursive_scan': 'फ़ोल्डर पुनरावर्ती रूप से स्कैन हो रहे हैं…',
        'remove_all': 'सभी हटाएँ',
        'remove_selection': 'चयन हटाएँ',
        'replaygain_help_text': 'ReplayGain गेन की गणना करके REPLAYGAIN_TRACK_GAIN/PEAK टैग लिखता है। ऑडियो बिना पुनः '
                                'एन्कोडिंग (-c:a copy) कॉपी होता है; केवल संगत प्लेयर टैग लागू करता है। भौतिक LUFS और '
                                'ट्रू पीक नहीं बदलते।',
        'replaygain_levels_log': 'audio unchanged: {before} LUFS · metadata में ReplayGain {gain} dB · configured '
                                 'target {target} LUFS (compatible player आवश्यक)',
        'replaygain_log_help_text': 'ReplayGain में लॉग अपरिवर्तित भौतिक ध्वनि-तीव्रता, मेटाडेटा में लिखा गेन और '
                                    'निर्धारित लक्ष्य दिखाता है। गुणवत्ता-जाँच चालू होने पर ‘ऑडियो अपरिवर्तित और टैग '
                                    'सत्यापित’ का अर्थ है कि ध्वनि-तीव्रता और पीक की स्रोत से तुलना हुई और टैग फिर '
                                    'पढ़े गए; इसका अर्थ यह नहीं कि फ़ाइल लक्ष्य पर भौतिक रूप से मापी गई।',
        'replaygain_operation': 'बिना पुनः एन्कोडिंग ReplayGain',
        'replaygain_qc_help_text': 'गुणवत्ता-जाँच चालू होने पर ReplayGain दी गई फ़ाइल को फिर मापकर पुष्टि करता है कि '
                                   'भौतिक ध्वनि-तीव्रता और पीक नहीं बदले, फिर Track टैग जाँचता है। सफलता ऑडियो '
                                   'सुरक्षित रहने और टैग मौजूद होने की पुष्टि करती है, लक्ष्य के भौतिक रूप से मिलने की '
                                   'नहीं।',
        'replaygain_qc_ok': 'सफल — audio unchanged और tags verified',
        'replaygain_tags_missing': 'ReplayGain टैग नहीं मिले।',
        'replaygain_usefulness_text': 'ReplayGain संगत प्लेयर वाली लाइब्रेरी में बिना पुनः एन्कोडिंग, वापस बदले जा '
                                      'सकने वाले प्लेबैक-समानीकरण के लिए उपयोगी है। हर प्लेयर में फ़ाइल को लक्ष्य पर '
                                      'भौतिक रूप से मापने के लिए सामान्यीकरण उपयोग करें।',
        'report_destination': 'गंतव्य',
        'report_detail': 'विवरण',
        'report_error': 'चेतावनी — CSV रिपोर्ट नहीं बन सकी: {error}',
        'report_filename_prefix': 'LUFScale_रिपोर्ट',
        'report_gain': 'गेन_db',
        'report_input_dbtp': 'इनपुट_dbtp',
        'report_input_lufs': 'इनपुट_lufs',
        'report_log': 'CSV रिपोर्ट — {path}',
        'report_mode': 'मोड',
        'report_operation': 'क्रिया',
        'report_output_dbtp': 'आउटपुट_dbtp',
        'report_output_lufs': 'आउटपुट_lufs',
        'report_path': 'रिपोर्ट: {path}',
        'report_qc': 'गुणवत्ता_नियंत्रण',
        'report_qc_engine': 'गुणवत्ता_जाँच_इंजन',
        'report_seconds': 'बीता_समय_सेकंड',
        'report_source': 'स्रोत',
        'report_status': 'स्थिति',
        'report_tooltip': 'केवल CSV बनता है, जिसमें मापन, समय और चेतावनियाँ होती हैं; निदान JSON नहीं बनता।',
        'resume': 'रुकावट के बाद जारी रखें',
        'resume_not_saved': ' पुनः आरंभ बिंदु सहेजा नहीं गया: {error}',
        'resume_processing': 'जारी रखें',
        'resume_tooltip': 'उसी सेटिंग से पूरी हुई फ़ाइलें पहचान ली जाती हैं और फिर संसाधित नहीं होतीं।',
        'resumed_progress': 'जारी: {file}',
        'save_dialog_cancel': 'रद्द करें',
        'save_dialog_filename': 'फ़ाइल नाम',
        'save_dialog_filetype': 'प्रारूप',
        'save_dialog_location': 'स्थान',
        'save_dialog_overwrite': 'बदलें',
        'save_dialog_overwrite_message': 'फ़ाइल “{file}” पहले से मौजूद है।',
        'save_dialog_overwrite_title': 'फ़ाइल बदलें?',
        'save_dialog_parent': 'ऊपरी फ़ोल्डर',
        'save_dialog_save': 'सहेजें',
        'save_issue_list': 'CSV के रूप में सहेजें…',
        'save_issue_list_error': 'सूची सहेजी नहीं जा सकी: {error}',
        'save_issue_list_error_title': 'सहेजना संभव नहीं',
        'save_issue_list_title': 'CSV सूची सहेजें',
        'scan_error': 'त्रुटि — {error}',
        'scanning_folders': 'फ़ोल्डर स्कैन हो रहे हैं…',
        'settings': 'सेटिंग्स',
        'open_folder': 'फ़ोल्डर खोलें',
        'show_option_help': 'सहायता दिखाएँ: {option}',
        'silent_copy': 'मौन या माप न सकने योग्य ऑडियो कॉपी हुआ।',
        'silent_copy_no_replaygain': 'मौन ऑडियो ReplayGain टैग के बिना कॉपी हुआ।',
        'silent_unmeasurable': 'मौन या माप न सकने योग्य ऑडियो।',
        'simulation': 'अनुकरण',
        'skip_compliant': 'पहले से अनुरूप फ़ाइलों को दोबारा एनकोड न करें',
        'skip_compliant_tooltip': 'लक्ष्य के ±0.10 LU और ट्रू पीक सीमा में फ़ाइल बिना पुनः एन्कोडिंग कॉपी होती है।',
        'skipped_progress': 'छोड़ा: {file}',
        'source_audio_count': 'फ़ाइलें: {count}',
        'source_list_more': '… {count} और स्रोत सुरक्षित हैं',
        'source_safety': 'स्रोत फ़ाइलें कभी स्थानांतरित या संशोधित नहीं होतीं।',
        'source_selection_tooltip': 'एकाधिक चयन: अलग वस्तुओं के लिए Ctrl-क्लिक और श्रेणी के लिए Shift-क्लिक।',
        'sources_added': '{count} स्रोत जोड़े गए।',
        'start': 'शुरू करें',
        'status_analyzed': 'विश्लेषित',
        'status_cancelled': 'रद्द',
        'status_compliant': 'अनुरूप',
        'status_error': 'त्रुटि',
        'status_ok': 'सफल',
        'status_resumed': 'जारी',
        'status_skipped': 'छोड़ा',
        'status_warning': 'चेतावनी',
        'switch_to_dark': 'गहरा मोड',
        'switch_to_light': 'हल्का मोड',
        'tagline': 'सुनाई देने वाली ऑडियो ध्वनि-तीव्रता को समान करता है',
        'target': 'ध्वनि-तीव्रता लक्ष्य',
        'target_tooltip': 'ध्वनि-तीव्रता लक्ष्य पूरे ट्रैक की अपेक्षित समेकित ध्वनि-तीव्रता है, जिसे LUFS में व्यक्त '
                          'किया जाता है। कम ऋणात्मक मान अधिक तेज़ फ़ाइल बनाता है: -14 LUFS, -16 LUFS से तेज़ है। 2 LU '
                          'का अंतर पीक सीमितकरण से पहले लगभग 2 dB के स्तर-अंतर के बराबर है।\n'
                          '\n'
                          'मार्गदर्शन: अधिक शांत और डायनेमिक परिणाम के लिए -18 LUFS; सामान्य संतुलन के लिए -16 LUFS; '
                          'अधिक तेज़ स्ट्रीमिंग-जैसे परिणाम के लिए -14 LUFS।\n'
                          '\n'
                          'यह लक्ष्य ट्रैक की आंतरिक डायनेमिक्स को स्वयं सपाट नहीं करता। अधिकतम ट्रू पीक लक्ष्य तक '
                          'बिना क्लिपिंग पहुँचना रोक सकता है।',
        'theme_accessible': 'ऐप का रूप बदलें। यह चुनाव याद रखा जाएगा।',
        'total_time': 'कुल समय: {duration}',
        'track_two_pass': 'दो-पास ट्रैक सामान्यीकरण।',
        'true_peak_meter_exceeded': 'अधिक {margin} dB',
        'true_peak_meter_margin': 'हेडरूम {margin} dB',
        'true_peak_meter_title': 'पीक हेडरूम',
        'true_peak_meter_tooltip': 'अंतिम आउटपुट के true peak की चुनी सीमा से तुलना करता है। चिह्न अंतिम मान और '
                                   'त्रिकोण बैच का सबसे ऊँचा पीक रखता है। हरा: सीमा पूरी; नारंगी: 0.25 dB तक अधिक; '
                                   'लाल: इससे अधिक। नारंगी सहनशीलता LUFScale गुणवत्ता जाँच की है, वितरण मानक नहीं। हर '
                                   'बैच पर रीसेट होता है।',
        'true_peak_meter_waiting': 'dBTP माप की प्रतीक्षा',
        'version_changes': '• Windows 10/11 x86-64 के लिए एक offline installer।\n'
                           '• Python, PySide6/Qt, FFmpeg, codecs, guides और licences शामिल हैं; install करते समय कोई '
                           'download या PowerShell command नहीं।\n'
                           '• Setup और SHA-256 बनाने से पहले loudnorm और सभी encoders जाँचे जाते हैं।',
        'version_changes_title': 'संस्करण {version} में नया',
        'version_label': 'संस्करण {version}',
        'volume': 'वॉल्यूम',
        'volume_loud': 'तेज़: -14 LUFS',
        'volume_normal': 'सामान्य: -16 LUFS',
        'volume_soft': 'हल्का: -18 LUFS',
        'volume_tooltip': 'यह ध्वनि-तीव्रता लक्ष्य का शॉर्टकट है; यह सिस्टम का प्लेबैक वॉल्यूम नहीं बदलता।\n'
                          '\n'
                          '• हल्का: -18 LUFS — शांत स्तर, अधिक डायनेमिक हेडरूम और लिमिटर सक्रिय होने की कम संभावना।\n'
                          '• सामान्य: -16 LUFS — निजी लाइब्रेरी के लिए संतुलित शुरुआती विकल्प।\n'
                          '• तेज़: -14 LUFS — अधिक प्रमुख ध्वनि, लेकिन सीमितकरण की अधिक संभावना।\n'
                          '• कस्टम — कोई दूसरा LUFS लक्ष्य सीधे दर्ज करें।\n'
                          '\n'
                          'ये व्यावहारिक विकल्प हैं, सार्वभौमिक मानक नहीं।',
        'warning_list_title': 'प्रसंस्करण चेतावनियाँ',
        'warnings_button': 'चेतावनियाँ ({count})',
        'warnings_button_tooltip': 'फ़ाइल नाम, पथ और विवरण सहित चेतावनी सूची खोलता है। विराम के दौरान या प्रसंस्करण के '
                                   'बाद उपलब्ध।',
        'warnings_dialog_title': 'प्रसंस्करण चेतावनियाँ'},
 'id': {'activity_cancelled': 'Aktivitas: dibatalkan',
        'activity_cancelling': 'Aktivitas: membatalkan…',
        'activity_completed': 'Aktivitas: selesai',
        'activity_compliant': 'Sesuai: {count}',
        'activity_detected': 'Aktivitas: {total} berkas terdeteksi',
        'activity_errors': 'Kesalahan: {count}',
        'activity_files': 'Berkas: {count}',
        'activity_idle': 'Aktivitas: menunggu',
        'activity_preparing': 'Aktivitas: menyiapkan berkas…',
        'activity_skipped': 'Dilanjutkan/dilewati: {count}',
        'activity_successes': 'Berhasil: {count}',
        'activity_warnings': 'Peringatan: {count}',
        'adaptive_disabled_log': 'Analisis adaptif — pemeriksaan cepat dihentikan setelah {sample} pengukuran '
                                 '({successes} berhasil, perkiraan penghematan {percent:+.1f}%).',
        'add_folders': 'Tambah folder…',
        'add_mp3': 'Tambah berkas audio…',
        'add_replaygain': 'Tambah ReplayGain',
        'add_source_files': 'Tambahkan berkas audio',
        'add_source_folder': 'Tambahkan folder sumber',
        'already_completed': 'Sudah selesai pada proses sebelumnya.',
        'already_compliant_badge': 'SESUAI',
        'already_compliant_copy': 'Sudah sesuai: disalin tanpa perubahan dan tanpa enkode ulang audio.',
        'already_compliant_log': 'sudah sesuai, tanpa enkode ulang',
        'analysis_cache_summary': 'Cache analisis — {hits} pengukuran digunakan kembali.',
        'analysis_impossible': 'Analisis gagal: {error}',
        'analysis_measurement_progress': 'Analisis {current}/{total} — {file} — {value}',
        'analysis_method': 'Metode analisis',
        'analysis_method_adaptive': 'Adaptif — berhenti bila tidak bermanfaat',
        'analysis_method_fast': 'Cepat — eksperimental',
        'analysis_method_historical': 'Pengukuran lengkap — metode acuan',
        'analysis_method_tooltip': 'Versi stabil otomatis memakai pengukuran penuh historis, yaitu satu-satunya metode '
                                   'yang telah divalidasi pada korpus acuan. Metode Cepat dan Adaptif tidak '
                                   'ditawarkan.',
        'analysis_progress_help_text': 'Dalam Hanya analisis, grafik Sebelum, log, dan bilah progres bergerak per '
                                       'berkas setelah setiap pengukuran; Sesudah tetap diam.',
        'analyze': 'Analisis',
        'analyze_only_fresh_help_text': 'Analisis saja mengukur ulang tiap sumber secara penuh dengan FFmpeg pada '
                                        'setiap proses. Grafik Sebelum dan kemajuan bergerak per berkas; tidak ada '
                                        'keluaran atau QC keluaran.',
        'analyze_operation': 'analisis/simulasi',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Aliran audio disalin tanpa enkode ulang; tag ReplayGain ditambahkan.',
        'audio_tab': 'Audio',
        'auto_start': 'Mulai otomatis setelah letakkan atau tempel',
        'auto_start_tooltip': 'Memulai saat sumber ditambahkan jika tujuan siap.',
        'cancel': 'Batal',
        'cancelled_summary': 'Dibatalkan — {success} berhasil, {failed} kesalahan, {skipped} dilanjutkan/dilewati, '
                             '{warnings} peringatan, {compliant} sesuai — {duration}.',
        'cancelling': 'Membatalkan…',
        'choose': 'Pilih…',
        'choose_output': 'Pilih folder tujuan',
        'clipboard': 'Papan klip',
        'clipboard_empty': 'Papan klip tidak berisi jalur folder atau audio yang didukung.',
        'close_button': 'Tutup',
        'close_question': 'Batalkan pemrosesan dan tutup aplikasi?',
        'completed_dialog_summary': 'Status: selesai\n'
                                    'Berkas: {files}\n'
                                    'Berhasil: {success}\n'
                                    'Kesalahan: {failed}\n'
                                    'Dilanjutkan atau dilewati: {skipped}\n'
                                    'Peringatan: {warnings}\n'
                                    'Sesuai: {compliant}\n'
                                    'Waktu total: {duration}',
        'completed_summary': 'Selesai — {success} berhasil, {failed} kesalahan, {skipped} dilanjutkan/dilewati, '
                             '{warnings} peringatan, {compliant} sesuai — {duration}.',
        'completed_with_errors': 'Pemrosesan selesai dengan peringatan',
        'convert': 'Normalisasi',
        'convert_operation': 'normalisasi audio',
        'cpu_tooltip': 'Penggunaan CPU total sistem selama pemrosesan.',
        'cpu_usage': 'CPU',
        'create_report': 'Buat laporan CSV',
        'csv_file_filter': 'Berkas CSV (*.csv)',
        'custom': 'Kustom',
        'decrease_value': 'Kurangi nilai',
        'description': 'Menyeragamkan volume tiap berkas tanpa mengubah sumber asli.',
        'destination': 'Tujuan',
        'destination_error': 'GALAT — tujuan tidak tersedia: {error}',
        'destination_path_tooltip': 'Jalur dapat dipilih dan disalin, tetapi tidak dapat diubah.',
        'destination_required_start': 'Pilih folder tujuan sebelum memulai.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus · subfolder didukung',
        'drop_title': 'Letakkan folder atau berkas audio di sini',
        'elapsed_time': 'Waktu berlalu: {duration}',
        'error_list_title': 'Kesalahan pemrosesan',
        'errors_button': 'Kesalahan ({count})',
        'errors_button_tooltip': 'Membuka daftar kesalahan berisi nama berkas, jalur, dan rincian. Tersedia saat '
                                 'dijeda atau setelah pemrosesan.',
        'errors_dialog_title': 'Kesalahan pemrosesan',
        'estimated_result': 'Hasil perkiraan; tidak ada berkas dibuat.',
        'estimated_total_calculating': 'Perkiraan waktu total: menghitung…',
        'estimated_total_time': 'Perkiraan waktu total: {duration}',
        'estimated_total_time_with_day_finish': 'Perkiraan waktu total: {duration} — {days} hari {time}',
        'estimated_total_time_with_finish': 'Perkiraan waktu total: {duration} — selesai sekitar {time}',
        'estimated_total_unavailable': 'Perkiraan waktu total: tidak tersedia',
        'ffmpeg_download_button': 'Buka situs web resmi FFmpeg',
        'ffmpeg_error_no_detail': 'Galat FFmpeg tanpa rincian.',
        'ffmpeg_execution_error': 'Tidak dapat menjalankan FFmpeg: {error}',
        'ffmpeg_incompatible': 'FFmpeg tidak kompatibel',
        'ffmpeg_missing': 'FFmpeg tidak ditemukan',
        'ffmpeg_missing_encoders': 'Versi FFmpeg ini tidak menyertakan semua enkoder audio yang diperlukan: '
                                   '{encoders}.',
        'ffmpeg_missing_message': 'FFmpeg harus terpasang dan tersedia melalui PATH atau ditempatkan di samping '
                                  'program.',
        'ffmpeg_no_lame': 'Build FFmpeg ini tidak menyertakan enkoder MP3 libmp3lame.',
        'ffmpeg_no_loudnorm': 'Versi FFmpeg ini tidak menyertakan filter loudnorm.',
        'ffmpeg_not_responding': 'FFmpeg tidak merespons dengan benar.',
        'file_exists': 'Berkas sudah ada.',
        'files_found': '{total} berkas audio ditemukan — {operation} — {parallel} proses paralel.',
        'finalization_completed': 'Finalisasi selesai dalam {duration}.',
        'finalizing': 'Finalisasi — laporan, cache analisis, dan data pelanjutan…',
        'folder': 'Folder',
        'folder_unavailable': 'Folder tidak tersedia',
        'guide_analysis_method': 'LUFScale secara otomatis memakai pengukuran historis penuh, satu-satunya metode yang '
                                 'telah divalidasi pada korpus acuan.',
        'guide_analyze_prediction_body': 'Analisis saja dapat memperkirakan hasil, tetapi tidak membuat audio atau QC '
                                         'keluaran.',
        'guide_analyze_prediction_title': 'Perkiraan tanpa keluaran',
        'guide_build_body': 'Pada Windows 10 1809 atau lebih baru, atau Windows 11 x86-64:\n'
                            '\n'
                            '1. Unduh “LUFScale-2.1.12-Setup-x64.exe” beserta berkas SHA-256.\n'
                            '2. Periksa SHA-256, lalu klik dua kali pemasang.\n'
                            '3. Baca dan setujui lisensi GNU GPL, lalu ikuti wisaya.\n'
                            '4. Jalankan LUFScale dari menu Start.\n'
                            '\n'
                            'Aplikasi, Python, PySide6/Qt, FFmpeg, codec, panduan, dan lisensi sudah disertakan. '
                            'Pemasangan tidak mengunduh apa pun dan tidak memerlukan perintah PowerShell. Penghapus '
                            'instalasi Windows dibuat otomatis.\n'
                            '\n'
                            'Distribusi tidak ditandatangani; setelah memeriksa berkas dan checksum, SmartScreen dapat '
                            'meminta konfirmasi.',
        'guide_build_title': 'Pasang LUFScale di Windows x86-64',
        'guide_estimated_total_help': 'Perkiraan waktu total: 12 mnt - selesai sekitar 14:30. ‘12 mnt’ adalah '
                                      'perkiraan durasi total dan ‘14:30’ waktu selesai. Jika melewati tengah malam, '
                                      'jumlah hari otomatis ditambahkan sebelum waktu, misalnya ‘2 h. 14:30’.',
        'guide_file_processing_body': 'Setiap berkas memakai pengukuran dan gain sendiri untuk mendekati target LUFS '
                                      'di bawah batas True Peak.',
        'guide_file_processing_title': 'Pemrosesan per berkas',
        'guide_help_tooltip': 'Membuka panduan PDF lengkap dalam bahasa yang dipilih.',
        'guide_level_mode_body': 'Trek - disarankan: mendekatkan tiap berkas ke target. Album - lanjutan dan khusus: '
                                 'memakai gain bersama dan mempertahankan kontras. Gunakan Album untuk karya yang '
                                 'didengar berurutan; Trek untuk acak atau tingkat antarberkas yang konsisten.',
        'guide_license_body': 'LUFScale adalah perangkat lunak bebas yang didistribusikan menurut GNU '
                              'GPL-3.0-or-later. Lisensi ini mengizinkan penggunaan, pembelajaran, perubahan, dan '
                              'distribusi ulang sesuai ketentuannya. Kode sumber, pemberitahuan, dan lisensi pihak '
                              'ketiga disertakan. Perangkat lunak diberikan tanpa jaminan.',
        'guide_license_feature': '• Perangkat lunak bebas GNU GPL-3.0-or-later: lisensi mengizinkan penggunaan, studi, '
                                 'perubahan, dan distribusi ulang.\n'
                                 '• Pemasang luring Windows x86-64 dengan Python, Qt, dan FFmpeg. Windows 11 '
                                 'disarankan; Windows 10 1809 atau lebih baru tetap menjadi sasaran kompatibilitas, '
                                 'tetapi dukungan standar Microsoft telah berakhir.',
        'guide_license_title': 'Perangkat lunak bebas dan distribusi ulang',
        'guide_log_legend_cancelled': 'Pemrosesan sengaja dihentikan; ini bukan kesalahan.',
        'guide_log_legend_compliant': 'Audio disalin tanpa perubahan: sumber sudah memenuhi target dan batas puncak.',
        'guide_log_legend_error': 'Berkas terkait tidak dapat diselesaikan.',
        'guide_log_legend_success': 'Pemrosesan selesai tanpa anomali yang terdeteksi.',
        'guide_log_legend_warning': 'Keluaran tersedia, tetapi satu pengukuran berada di luar toleransi.',
        'guide_missing_message': 'Panduan PDF tidak ditemukan: {path}',
        'guide_missing_title': 'Panduan tidak tersedia',
        'guide_open_error': 'Panduan PDF tidak dapat dibuka: {path}',
        'guide_quality_priority_body': 'LUFScale mengukur loudness berkas dan, dengan Normalisasi, benar-benar '
                                       'menyesuaikan volume yang terdengar menuju target LUFS sambil mengendalikan '
                                       'true peak. Setiap sumber dianalisis sepanjang durasinya, lalu keluaran diukur '
                                       'ulang dan diverifikasi. Hasilnya tidak bergantung pada tag atau pemutar yang '
                                       'kompatibel: tingkat antarberkas menjadi lebih konsisten, penyimpangan '
                                       'ditandai, dan berkas asli tetap utuh.',
        'guide_quality_priority_title': 'Apa fungsi LUFScale?',
        'help_button': 'Bantuan',
        'help_overview': '• Normalisasi, ReplayGain, atau analisis MP3, FLAC, WAV, AIFF, M4A, OGG, dan Opus.\n'
                         '• Setiap berkas diukur dan diproses terpisah menuju target.\n'
                         '• Struktur, metadata, dan sampul yang kompatibel dipertahankan; sumber tidak berubah.\n'
                         '• Pemrosesan paralel, cache, lanjut, QC, CSV, kemajuan, CPU, dan riwayat LUFS.\n'
                         '• Antarmuka dan panduan PDF dalam 12 bahasa.',
        'help_title': 'Fitur utama',
        'increase_value': 'Tambah nilai',
        'input_lufs_log': 'Masukan {value} LUFS',
        'interface_ffmpeg_message': 'Mesin audio FFmpeg bawaan hilang atau tidak dapat digunakan. Instal ulang '
                                    'LUFScale dari arsip distribusi lengkap.',
        'internal_error': 'Galat internal: {error}',
        'interrupted': 'Pemrosesan terhenti.',
        'invalid_location': 'Lokasi tidak valid',
        'issue_detail_column': 'Rincian',
        'issue_file_column': 'Berkas',
        'issue_path_column': 'Jalur',
        'language': 'Bahasa',
        'language_tooltip': 'Langsung mengubah bahasa antarmuka, pesan, dan laporan CSV berikutnya.',
        'log_help_text': 'Setiap baris menjelaskan berkas atau tahap pemrosesan umum.\n'
                         '\n'
                         '• Baris berhasil langsung dimulai dengan nama berkas; status BERHASIL tidak diulang.\n'
                         '• SESUAI, DILANJUTKAN, DILEWATI, DIBATALKAN, dan GALAT tetap tampil bila memberi informasi '
                         'berguna.\n'
                         '• Level menunjukkan masukan → keluaran yang diukur ulang, lalu hasil kontrol kualitas bila '
                         'ada.\n'
                         '• Peringatan dan Kesalahan membuka daftar terpisah berisi nama, path, dan detail. Daftar '
                         'tersedia saat jeda atau setelah pemrosesan dan masing-masing dapat disimpan.\n'
                         '\n'
                         'Warna: hijau=berhasil; oranye=peringatan; merah=berkas belum selesai; biru-ungu=dilanjutkan; '
                         'abu-abu=informasi, dilewati, atau dibatalkan.\n'
                         '\n'
                         'PERINGATAN QC—loudness berarti keluaran yang diukur ulang berbeda lebih dari ±0,60 LU dari '
                         'nilai yang diharapkan. Nilai yang lebih negatif lebih pelan; yang kurang negatif lebih '
                         'keras. Deviasi adalah selisih absolut: -14,69 alih-alih -14,00 berarti 0,69 LU. Berkas tetap '
                         'dibuat; ini bukan kegagalan konversi. Tidak wajib bertindak jika hasilnya enak didengar. '
                         'Untuk target ketat, periksa detail dan CSV, lalu cek target dan batas True Peak sebelum '
                         'mencoba lagi. Pesan ini saja tidak membuktikan apakah penyebabnya batas, encoder, atau batas '
                         'koreksi.\n'
                         '\n'
                         'PERINGATAN QC—peak berarti True Peak hasil ukur ulang melampaui batas yang dipilih lebih '
                         'dari 0,25 dB. Berkas tetap dibuat. Jika berulang, pilih target LUFS lebih rendah atau batas '
                         'peak lebih aman, misalnya -2,0 dBTP, lalu proses ulang.\n'
                         '\n'
                         'Waktu kumulatif menjumlahkan pekerjaan semua tugas paralel. Waktu total adalah durasi nyata '
                         'yang berlalu.',
        'log_placeholder': 'Log pemrosesan akan tampil di sini.',
        'log_title': 'Log pemrosesan',
        'loudness_comparison_after': 'Sesudah',
        'loudness_comparison_analysis_only': 'Tidak ada keluaran dalam Hanya analisis',
        'loudness_comparison_before': 'Sebelum',
        'loudness_comparison_help_text': 'Setiap berkas menambah titik di kanan. Sebelum selalu menampilkan sumber '
                                         'terukur. Pada Normalisasi, Sesudah menampilkan hasil yang benar-benar diukur '
                                         'ulang. Pada ReplayGain, grafik kedua bergaris putus-putus memperkirakan '
                                         'pemutaran: loudness sumber ditambah Track Gain tersimpan. Tanda ≈ dan '
                                         'catatan Pemutar kompatibel menegaskan bahwa ini bukan pengukuran fisik '
                                         'berkas hasil. Pemutar yang tidak kompatibel mempertahankan level asli; '
                                         'pemutar kompatibel dapat mengubah hasil melalui preamp atau pencegahan '
                                         'clipping. Kedua grafik memakai skala tetap ±6 LU yang sama. Analisis saja '
                                         'tidak memiliki keluaran Sesudah.',
        'loudness_comparison_increased': 'Selisih bertambah {value} LU',
        'loudness_comparison_needs_qc': 'Aktifkan kontrol mutu untuk membandingkan',
        'loudness_comparison_no_after': 'Tidak ada kurva Sesudah untuk operasi ini',
        'loudness_comparison_not_applicable': 'Perbandingan tidak tersedia untuk operasi ini',
        'loudness_comparison_reached': 'Target tercapai · selisih {value} LU',
        'loudness_comparison_reduced': 'Selisih berkurang {value} LU',
        'loudness_comparison_replaygain_after': 'Estimasi pemutaran RG',
        'loudness_comparison_replaygain_note': 'Pemutar kompatibel · audio tetap',
        'loudness_comparison_scale': 'Tampilan ±{scale} LU · tol. QC ±{tolerance} LU',
        'loudness_comparison_target': 'Target {value} LUFS',
        'loudness_comparison_title': 'Perubahan kenyaringan',
        'loudness_comparison_tooltip': 'Sebelum menunjukkan loudness fisik. Pada ReplayGain, grafik kedua '
                                       'memperkirakan pemutaran kompatibel dari gain tersimpan.',
        'loudness_comparison_unchanged': 'Selisih tidak berubah',
        'loudness_comparison_waiting': 'Menunggu berkas yang diproses',
        'loudness_meter_estimated': 'Perkiraan',
        'loudness_meter_help_text': 'Meter membandingkan keluaran terakhir yang benar-benar diukur ulang dengan '
                                    'target. Nilai dan kurva diperbarui per berkas; ini adalah loudness terintegrasi '
                                    'seluruh berkas, bukan level pemutaran sesaat. Meter memang tidak aktif bila '
                                    'kontrol kualitas otomatis dimatikan atau pada Analisis saja yang tidak memiliki '
                                    'keluaran.',
        'loudness_meter_measured': 'Terukur',
        'loudness_meter_no_file': 'Menunggu analisis',
        'loudness_meter_title': 'Meter kenyaringan',
        'loudness_meter_tooltip': 'Merah menunjukkan target; biru menunjukkan kenyaringan keluaran terbaru yang '
                                  'benar-benar diukur ulang.',
        'loudness_meter_waiting': 'Menunggu berkas audio',
        'loudness_score_acceptable': 'Dapat diterima',
        'loudness_score_check': 'Lihat peringatan',
        'loudness_score_excellent': 'Sangat baik',
        'loudness_score_needs_qc': 'Skor target: aktifkan kontrol kualitas',
        'loudness_score_not_applicable': 'Skor target: tidak berlaku',
        'loudness_score_tooltip': 'Skor memakai 8 keluaran terbaru yang benar-benar diukur ulang. Nilai 100 berarti '
                                  'tepat, 50 berarti galat RMS 0,60 LU, dan 0 berarti 1,20 LU atau lebih. Panel merah '
                                  'berarti setidaknya ada satu peringatan kenyaringan yang dapat diperiksa melalui '
                                  'tombol Peringatan.',
        'loudness_score_waiting': 'Skor target: menunggu',
        'measurement_unavailable': 'Pengukuran tidak tersedia',
        'mp3_filter': 'Audio yang didukung (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Belum ada folder',
        'no_mp3': 'Tidak ditemukan berkas audio yang didukung.',
        'no_new_source': 'Tidak ada sumber audio baru.',
        'not_performed': 'Tidak dilakukan',
        'open_output_error': 'Folder tujuan tidak dapat dibuka: {error}',
        'operation': 'Operasi',
        'operation_analyze': 'Analisis saja — tanpa berkas baru',
        'operation_analyze_label': 'Analisis saja — simulasi tanpa berkas',
        'operation_convert': 'Seragamkan — normalkan audio secara nyata',
        'operation_convert_label': 'Normalisasi — benar-benar sesuaikan audio',
        'operation_help_text': 'Normalisasi memproses setiap berkas secara terpisah, membidik target LUFS di bawah '
                               'batas True Peak, lalu mengukur ulang keluaran. ReplayGain tidak mengubah sampel audio. '
                               'Analisis saja menghasilkan pengukuran dan, bila diminta, laporan CSV, tetapi tidak '
                               'membuat berkas audio.',
        'operation_replaygain': 'ReplayGain — tanpa enkode ulang audio',
        'operation_replaygain_label': 'ReplayGain — tanpa enkode ulang audio',
        'operation_tooltip': 'Normalisasi mengubah audio. ReplayGain menyalin aliran dan menambah tag. Analisis saja '
                             'mengukur tanpa membuat audio.',
        'option_status_auto_start': 'AUTO',
        'option_status_overwrite': 'TIMP',
        'option_status_quality_control': 'MUTU',
        'option_status_report': 'CSV',
        'option_status_resume': 'LNJT',
        'option_status_skip_compliant': 'LEWA',
        'options_tab': 'Opsi',
        'output_lufs_unavailable': 'LUFS keluaran tidak tersedia',
        'overwrite': 'Timpa berkas yang ada',
        'overwrite_tooltip': 'Hanya mengganti berkas tujuan, tidak pernah sumber.',
        'parallel': 'Proses paralel',
        'parallel_adjusted': 'Paralelisme otomatis — {active} proses, CPU {cpu:.0f}%.',
        'parallel_auto': 'Otomatis',
        'parallel_auto_log': 'otomatis, maksimum {maximum}',
        'parallel_tooltip': 'Menentukan jumlah berkas yang dapat diproses bersamaan.\n'
                            '\n'
                            '• Otomatis mulai dengan paling banyak 4 tugas. Jika pengukuran CPU tersedia, program '
                            'memeriksanya setiap detik: menambah satu tugas di bawah penggunaan 70% dan mengurangi '
                            'satu di atas 92%.\n'
                            '• Otomatis tidak pernah melampaui jumlah prosesor logis yang terdeteksi, dengan batas '
                            'mutlak 16 tugas.\n'
                            '• Jika CPU tidak dapat diukur, Otomatis langsung memakai batas yang terdeteksi tanpa '
                            'penyesuaian dinamis.\n'
                            '• Angka menetapkan jumlah maksimum tugas serentak; bukan target penggunaan CPU.\n'
                            '\n'
                            'Lebih banyak tugas dapat mempercepat batch besar, tetapi meningkatkan beban, suhu, dan '
                            'akses disk. Tekan − sampai Otomatis tampil.',
        'paste': 'Tempel',
        'path_left': 'Tampilkan bagian kiri jalur',
        'path_right': 'Tampilkan bagian kanan jalur',
        'pause': 'Jeda',
        'peak': 'True peak maksimum',
        'peak_tooltip': 'True peak maksimum adalah batas atas, bukan level yang harus dicapai. Batas ini menahan '
                        'puncak tertinggi gelombang hasil rekonstruksi dalam dBTP, termasuk di antara sampel, untuk '
                        'mengurangi risiko clipping setelah enkode atau transkode.\n'
                        '\n'
                        '• -1,0 dBTP — batas umum distribusi dengan level puncak keluaran tertinggi.\n'
                        '• -1,5 dBTP — nilai baku dan kompromi hati-hati untuk MP3.\n'
                        '• -2,0 dBTP — ruang tambahan, berguna untuk berkas yang akan dienkode ulang atau target '
                        'kenyaringan tinggi.\n'
                        '• 0 dBTP — tanpa ruang; tidak disarankan untuk MP3.\n'
                        '\n'
                        'Nilai yang lebih negatif memberi perlindungan lebih besar, tetapi dapat mencegah trek sangat '
                        'dinamis mencapai target LUFS secara tepat.',
        'phase_summary': 'Pembagian perkiraan waktu total — analisis {analysis}, konversi {conversion}, kendali mutu '
                         '{quality}.',
        'pipeline_enabled': 'Alur trek — setiap konversi dimulai segera setelah analisisnya selesai.',
        'pre_measurement': 'Mengukur berkas masukan…',
        'preset': 'Prasetel',
        'preset_dynamic': 'Musik dinamis',
        'preset_library': 'Perpustakaan musik — disarankan',
        'preset_streaming': 'Streaming lebih kuat',
        'preset_tooltip': 'Menerapkan sekaligus kombinasi target kenyaringan, true peak maksimum, dan mutu audio yang '
                          'konsisten. Perubahan manual apa pun memilih Kustom.',
        'processing_cancelled': 'Pemrosesan dibatalkan.',
        'processing_completed': 'Pemrosesan selesai',
        'processing_in_progress': 'Memproses…',
        'processing_paused': 'Pemrosesan dijeda.',
        'processing_resumed': 'Pemrosesan dilanjutkan.',
        'qc_impossible': 'Kontrol mutu tidak dapat dilakukan: {error}',
        'qc_log': ' — kendali mutu: {quality}',
        'qc_ok': 'Kontrol mutu: sesuai',
        'qc_warning': 'PERINGATAN kontrol mutu — {detail}',
        'quality': 'Mutu audio',
        'quality_control': 'Kontrol mutu otomatis',
        'quality_control_tooltip': 'Mengukur ulang setiap keluaran. Koreksi tetap menargetkan ±0,50 LU; peringatan '
                                   'kenyaringan hanya muncul di luar ±0,60 LU. MP3 dinamis mempertahankan hingga 3 '
                                   'percobaan koreksi; WAV, AIFF, dan FLAC dapat dicoba ulang dari sumber hingga 2 '
                                   'kali jika ruang True Peak memungkinkan. Menonaktifkan opsi ini menghapus '
                                   'verifikasi, percobaan ulang, dan aktivitas meter.',
        'quality_tooltip': 'Mengatur kompromi mutu/ukuran untuk format terkompresi. Semakin kecil angkanya, semakin '
                           'tinggi mutu dan bitrate. Pengaturan ini tidak mengubah target LUFS atau true peak '
                           'maksimum.\n'
                           '\n'
                           '• 0 — mutu maksimum, disarankan untuk mempertahankan detail.\n'
                           '• 1 sampai 2 — mutu sangat tinggi.\n'
                           '• 3 sampai 4 — keseimbangan mutu/ukuran yang baik.\n'
                           '• 5 sampai 9 — berkas lebih kecil dengan kehilangan lebih banyak.\n'
                           '\n'
                           'FLAC tetap lossless untuk nilai apa pun. WAV dan AIFF mengabaikan pengaturan ini serta '
                           'mempertahankan sample rate dan bit depth PCM yang kompatibel dengan sumber. Untuk MP3, '
                           'M4A, OGG, dan Opus, nilai rendah dapat meminta bitrate di atas sumber sehingga keluaran '
                           'lebih besar. Nilai tinggi umumnya mengurangi ukuran tanpa menjamin jumlah byte yang sama '
                           'karena enkoder ini sering memakai VBR. Mengenkode ulang format lossy tidak memulihkan '
                           'informasi yang telah hilang.',
        'ready': 'Siap',
        'recursive_scan': 'Memindai folder secara rekursif…',
        'remove_all': 'Hapus semua',
        'remove_selection': 'Hapus pilihan',
        'replaygain_help_text': 'ReplayGain menghitung gain dan menulis REPLAYGAIN_TRACK_GAIN/PEAK. Audio disalin '
                                'tanpa enkode ulang (-c:a copy); hanya pemutar kompatibel menerapkan tag. LUFS dan '
                                'True Peak fisik tidak berubah.',
        'replaygain_levels_log': 'audio tidak berubah: {before} LUFS · ReplayGain {gain} dB dalam metadata · target '
                                 'pengaturan {target} LUFS (perlu pemutar kompatibel)',
        'replaygain_log_help_text': 'Pada ReplayGain, log menampilkan kenyaringan fisik yang tidak berubah, gain yang '
                                    'ditulis ke metadata, dan target yang diatur. Jika kontrol kualitas aktif, ‘audio '
                                    'tetap dan tag terverifikasi’ berarti kenyaringan dan puncak dibandingkan dengan '
                                    'sumber dan tag dibaca ulang; bukan berarti berkas terukur secara fisik pada '
                                    'target.',
        'replaygain_operation': 'ReplayGain tanpa enkode ulang',
        'replaygain_qc_help_text': 'Jika kontrol kualitas aktif, ReplayGain mengukur ulang berkas hasil untuk '
                                   'memastikan kenyaringan fisik dan puncaknya tetap sama, lalu memeriksa tag Track. '
                                   'Keberhasilan memastikan audio terjaga dan tag tersedia, bukan bahwa target '
                                   'tercapai secara fisik.',
        'replaygain_qc_ok': 'BERHASIL — audio tetap dan tag terverifikasi',
        'replaygain_tags_missing': 'Tag ReplayGain tidak ditemukan.',
        'replaygain_usefulness_text': 'ReplayGain berguna untuk meratakan volume pemutaran secara reversibel tanpa '
                                      'enkode ulang pada pustaka yang memakai pemutar kompatibel. Untuk menghasilkan '
                                      'berkas yang secara fisik terukur pada target di semua pemutar, gunakan '
                                      'Normalisasi.',
        'report_destination': 'tujuan',
        'report_detail': 'rincian',
        'report_error': 'PERINGATAN — tidak dapat membuat laporan CSV: {error}',
        'report_filename_prefix': 'Laporan_LUFScale',
        'report_gain': 'gain_dB',
        'report_input_dbtp': 'masukan_dBTP',
        'report_input_lufs': 'masukan_LUFS',
        'report_log': 'Laporan CSV — {path}',
        'report_operation': 'operasi',
        'report_output_dbtp': 'keluaran_dBTP',
        'report_output_lufs': 'keluaran_LUFS',
        'report_path': 'Laporan: {path}',
        'report_qc': 'kontrol_kualitas',
        'report_qc_engine': 'mesin_kontrol_kualitas',
        'report_seconds': 'detik_berlalu',
        'report_source': 'sumber',
        'report_status': 'status',
        'report_tooltip': 'Hanya membuat laporan CSV berisi pengukuran, waktu, dan peringatan; tidak menambah JSON '
                          'diagnostik.',
        'resume': 'Lanjutkan setelah terputus',
        'resume_not_saved': ' Titik pelanjutan tidak tersimpan: {error}',
        'resume_processing': 'Lanjutkan',
        'resume_tooltip': 'Mengenali berkas yang selesai dengan pengaturan sama.',
        'save_dialog_cancel': 'Batal',
        'save_dialog_filename': 'Nama berkas',
        'save_dialog_filetype': 'Format',
        'save_dialog_location': 'Folder',
        'save_dialog_overwrite': 'Ganti',
        'save_dialog_overwrite_message': 'Berkas “{file}” sudah ada.',
        'save_dialog_overwrite_title': 'Ganti berkas?',
        'save_dialog_parent': 'Folder induk',
        'save_dialog_save': 'Simpan',
        'save_issue_list': 'Simpan sebagai CSV…',
        'save_issue_list_error': 'Daftar tidak dapat disimpan: {error}',
        'save_issue_list_error_title': 'Tidak dapat menyimpan',
        'save_issue_list_title': 'Simpan daftar CSV',
        'scan_error': 'GALAT — {error}',
        'scanning_folders': 'Memindai folder…',
        'settings': 'Pengaturan',
        'open_folder': 'Buka folder',
        'show_option_help': 'Tampilkan bantuan: {option}',
        'silent_copy': 'Audio hening atau tidak terukur disalin.',
        'silent_copy_no_replaygain': 'Audio hening disalin tanpa tag ReplayGain.',
        'silent_unmeasurable': 'Audio hening atau tidak terukur.',
        'simulation': 'Simulasi',
        'skip_compliant': 'Lewati berkas yang sudah sesuai',
        'skip_compliant_tooltip': 'Berkas dalam ±0,10 LU dari target dan di bawah batas True Peak disalin tanpa enkode '
                                  'ulang.',
        'source_audio_count': 'Berkas: {count}',
        'source_list_more': '… {count} sumber lain dipertahankan',
        'source_safety': 'Berkas sumber tidak pernah dipindah atau diubah.',
        'source_selection_tooltip': 'Gunakan Ctrl-klik untuk item terpisah atau Shift-klik untuk suatu rentang.',
        'sources_added': '{count} sumber ditambahkan.',
        'start': 'Mulai',
        'status_analyzed': 'DIANALISIS',
        'status_cancelled': 'DIBATALKAN',
        'status_compliant': 'SESUAI',
        'status_error': 'KESALAHAN',
        'status_ok': 'BERHASIL',
        'status_resumed': 'DILANJUTKAN',
        'status_skipped': 'DILEWATI',
        'status_warning': 'PERINGATAN',
        'switch_to_dark': 'Mode gelap',
        'switch_to_light': 'Mode terang',
        'tagline': 'Menyeragamkan kenyaringan yang terdengar tanpa mengubah sumber.',
        'target': 'Target kenyaringan',
        'target_tooltip': 'Target kenyaringan adalah kenyaringan terintegrasi yang diinginkan untuk seluruh trek, '
                          'dinyatakan dalam LUFS. Nilai yang kurang negatif menghasilkan berkas lebih keras: -14 LUFS '
                          'lebih keras daripada -16 LUFS. Selisih 2 LU kira-kira setara dengan perbedaan level 2 dB '
                          'sebelum pembatasan puncak.\n'
                          '\n'
                          'Panduan: -18 LUFS untuk hasil lebih tenang dan dinamis; -16 LUFS untuk keseimbangan umum; '
                          '-14 LUFS untuk hasil lebih keras bergaya streaming. Platform dapat menerapkan normalisasi '
                          'pemutaran sendiri.\n'
                          '\n'
                          'Target ini tidak dengan sendirinya meratakan dinamika internal trek. Jika true peak '
                          'maksimum mencegah pencapaian target tanpa clipping, hasil dapat tetap sedikit lebih rendah.',
        'theme_accessible': 'Beralih antara mode terang dan gelap',
        'total_time': 'Waktu total: {duration}',
        'track_two_pass': 'Normalisasi trek dua tahap.',
        'true_peak_meter_title': 'Ruang true peak',
        'true_peak_meter_tooltip': 'Membandingkan true peak keluaran terakhir dengan batas yang dipilih. Penanda '
                                   'menunjukkan nilai terbaru dan segitiga menyimpan puncak tertinggi dalam kumpulan. '
                                   'Hijau berarti batas dipenuhi, jingga berarti kelebihan hingga 0,25 dB, dan merah '
                                   'berarti kelebihan yang lebih besar. Toleransi jingga milik kontrol kualitas '
                                   'LUFScale dan bukan standar distribusi. Grafik direset untuk setiap kumpulan.',
        'true_peak_meter_waiting': 'Menunggu pengukuran dBTP',
        'version_changes': '• Satu pemasang luring untuk Windows 10/11 x86-64.\n'
                           '• Python, PySide6/Qt, FFmpeg, codec, panduan, dan lisensi disertakan; pemasangan tanpa '
                           'unduhan atau perintah PowerShell.\n'
                           '• Build memverifikasi loudnorm dan enkoder sebelum membuat pemasang dan SHA-256.',
        'version_changes_title': 'Yang baru di versi {version}',
        'version_label': 'Versi {version}',
        'volume': 'Volume',
        'volume_loud': 'Kuat: -14 LUFS',
        'volume_normal': 'Normal: -16 LUFS',
        'volume_soft': 'Lembut: -18 LUFS',
        'volume_tooltip': 'Pengaturan ini adalah pintasan ke target kenyaringan; tidak mengubah volume pemutaran '
                          'sistem.\n'
                          '\n'
                          '• Lembut: -18 LUFS — level lebih tenang, ruang dinamis lebih besar, dan risiko limiter '
                          'bekerja lebih kecil.\n'
                          '• Normal: -16 LUFS — kompromi seimbang dan titik awal yang baik untuk pustaka pribadi.\n'
                          '• Keras: -14 LUFS — pemutaran lebih menonjol, dekat target pemutaran Normal Spotify, tetapi '
                          'lebih mungkin memerlukan pembatasan.\n'
                          '• Kustom — memasukkan target LUFS lain secara langsung.\n'
                          '\n'
                          'Nilai ini adalah pilihan praktis, bukan standar universal.',
        'warning_list_title': 'Peringatan pemrosesan',
        'warnings_button': 'Peringatan ({count})',
        'warnings_button_tooltip': 'Membuka daftar peringatan berisi nama berkas, jalur, dan rincian. Tersedia saat '
                                   'dijeda atau setelah pemrosesan.',
        'warnings_dialog_title': 'Peringatan pemrosesan'},
 'it': {'activity_cancelled': 'Attività: elaborazione annullata',
        'activity_cancelling': 'Attività: annullamento in corso…',
        'activity_completed': 'Attività: elaborazione completata',
        'activity_compliant': 'Conformi: {count}',
        'activity_detected': 'Attività: {total} file rilevato/i',
        'activity_errors': 'Errori: {count}',
        'activity_files': 'File: {count}',
        'activity_idle': 'Attività: in attesa',
        'activity_preparing': 'Attività: preparazione dei file…',
        'activity_progress': '{total} file • riusciti {success} • avvisi {warnings} • errori {failed} • '
                             'ripresi/ignorati {skipped} • conformi {compliant}',
        'activity_skipped': 'Ripresi/ignorati: {count}',
        'activity_successes': 'Riusciti: {count}',
        'activity_warnings': 'Avvisi: {count}',
        'adaptive_disabled_log': 'Analisi adattiva — sonde rapide arrestate dopo {sample} misurazioni ({successes} '
                                 'successi, risparmio stimato {percent:+.1f}%).',
        'add_folders': 'Aggiungi cartelle…',
        'add_mp3': 'Aggiungi file audio…',
        'add_replaygain': 'Aggiungi ReplayGain',
        'add_source_files': 'Aggiungi file audio',
        'add_source_folder': 'Aggiungi una cartella sorgente',
        'already_completed': 'Già completato durante un’esecuzione precedente.',
        'already_compliant_badge': 'CONFORME',
        'already_compliant_copy': 'Già conforme: copia identica senza ricodifica audio.',
        'already_compliant_log': 'già conforme, senza ricodifica',
        'analysis_cache_summary': 'Cache di analisi — {hits} misurazione/i riutilizzata/i.',
        'analysis_impossible': 'Analisi non riuscita: {error}',
        'analysis_measurement_progress': 'Analisi {current}/{total} — {file} — {value}',
        'analysis_method': 'Metodo di analisi',
        'analysis_method_adaptive': 'Adattivo — si arresta se non conviene',
        'analysis_method_fast': 'Rapido — sperimentale',
        'analysis_method_historical': 'Storico — riferimento',
        'analysis_method_log': 'Metodo di analisi — {method}.',
        'analysis_method_tooltip': 'La versione stabile usa automaticamente la misura storica completa, l’unico metodo '
                                   'convalidato sul corpus di riferimento. Rapido e Adattivo non sono più proposti.',
        'analysis_progress': 'Analisi {current}/{total}: {file}',
        'analysis_progress_help_text': 'In Solo analisi, il grafico Prima, il registro e la barra avanzano file per '
                                       'file al termine di ogni misura; Dopo resta fermo.',
        'analyze': 'Analizza',
        'analyze_only_fresh_help_text': 'Solo analisi rimisura interamente ogni sorgente con FFmpeg a ogni esecuzione. '
                                        'Prima e l’avanzamento procedono file per file, senza uscita né QC di uscita.',
        'analyze_operation': 'analisi/simulazione',
        'analyzed_progress': 'Analizzato: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Flusso audio copiato senza ricodifica; tag ReplayGain aggiunti.',
        'audio_tab': 'Audio',
        'auto_start': 'Avvia automaticamente dopo il trascinamento o l’incolla',
        'auto_start_tooltip': 'Avvia automaticamente l’elaborazione dopo l’aggiunta di sorgenti tramite trascinamento '
                              'o incolla, se è già stata scelta una destinazione.',
        'cancel': 'Annulla',
        'cancelled_summary': 'Annullato — {success} riuscito/i, {failed} errore/i, {skipped} ripreso/i/ignorato/i, '
                             '{warnings} avviso/i, {compliant} conforme/i — {duration}.',
        'cancelling': 'Annullamento in corso…',
        'choose': 'Scegli…',
        'choose_output': 'Scegli la cartella di destinazione',
        'clipboard': 'Appunti',
        'clipboard_empty': 'Gli appunti non contengono un percorso valido di cartella o file audio supportato.',
        'close_button': 'Chiudi',
        'close_question': 'Annullare l’elaborazione e chiudere l’applicazione?',
        'completed_dialog_summary': 'Stato: completato\n'
                                    'File: {files}\n'
                                    'Riusciti: {success}\n'
                                    'Errori: {failed}\n'
                                    'Ripresi o ignorati: {skipped}\n'
                                    'Avvisi: {warnings}\n'
                                    'Conformi: {compliant}\n'
                                    'Tempo totale: {duration}',
        'completed_summary': 'Completato — {success} riuscito/i, {failed} errore/i, {skipped} ripreso/i/ignorato/i, '
                             '{warnings} avviso/i, {compliant} conforme/i — {duration}.',
        'completed_with_errors': 'Elaborazione completata con avvisi',
        'convert': 'Normalizza',
        'convert_operation': 'uniformazione audio',
        'cpu_tooltip': 'Utilizzo totale della CPU del sistema, aggiornato ogni secondo durante l’elaborazione.',
        'cpu_unavailable': 'N/D',
        'cpu_usage': 'CPU',
        'create_report': 'Crea un rapporto CSV',
        'csv_file_filter': 'File CSV (*.csv)',
        'custom': 'Personalizzato',
        'decrease_value': 'Diminuire il valore',
        'description': 'Uniforma il volume percepito file per file senza modificare gli originali.',
        'destination': 'Destinazione',
        'destination_error': 'ERRORE — destinazione non disponibile: {error}',
        'destination_path_tooltip': 'Fai clic sul percorso, quindi usa le frecce, Inizio/Fine o la rotellina. Il '
                                    'percorso può essere selezionato e copiato, ma non modificato.',
        'destination_required_start': 'Scegli prima la cartella di destinazione con il pulsante «Scegli…».',
        'dialog_ok': 'OK',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — sottocartelle incluse',
        'drop_title': 'Trascina qui cartelle o file audio',
        'elapsed_time': 'Tempo trascorso: {duration}',
        'error_list_title': 'Errori di elaborazione',
        'error_progress': 'Errore: {file}',
        'errors_button': 'Errori ({count})',
        'errors_button_tooltip': 'Apre l’elenco degli errori con nome file, percorso e dettagli. Disponibile durante '
                                 'una pausa o dopo l’elaborazione.',
        'errors_dialog_title': 'Errori di elaborazione',
        'estimated_result': 'Risultato stimato; nessun file creato.',
        'estimated_total_calculating': 'Tempo totale stimato: calcolo in corso…',
        'estimated_total_time': 'Tempo totale stimato: {duration}',
        'estimated_total_time_with_day_finish': 'Tempo totale stimato: {duration} — {days} g. {time}',
        'estimated_total_time_with_finish': 'Tempo totale stimato: {duration} — {time}',
        'estimated_total_unavailable': 'Tempo totale stimato: non disponibile',
        'ffmpeg_download_button': 'Apri il sito ufficiale di FFmpeg',
        'ffmpeg_error_no_detail': 'Errore FFmpeg senza dettagli.',
        'ffmpeg_execution_error': 'Impossibile eseguire FFmpeg: {error}',
        'ffmpeg_incompatible': 'FFmpeg incompatibile',
        'ffmpeg_missing': 'FFmpeg non trovato',
        'ffmpeg_missing_encoders': 'Questa versione di FFmpeg non include tutti gli encoder audio richiesti: '
                                   '{encoders}.',
        'ffmpeg_missing_message': 'FFmpeg deve essere installato e disponibile nel PATH, oppure collocato accanto al '
                                  'programma.',
        'ffmpeg_no_lame': 'Questa versione di FFmpeg non include il codificatore MP3 libmp3lame.',
        'ffmpeg_no_loudnorm': 'Questa versione di FFmpeg non include il filtro loudnorm.',
        'ffmpeg_not_responding': 'FFmpeg non risponde correttamente.',
        'file_exists': 'Il file esiste già.',
        'files_found': 'Trovati {total} file audio — {operation} — {parallel} processi paralleli.',
        'finalization_completed': 'Finalizzazione completata in {duration}.',
        'finalizing': 'Finalizzazione — rapporto, cache di analisi e dati di ripresa…',
        'folder': 'Cartella',
        'folder_unavailable': 'Cartella non disponibile',
        'guide_analysis_method': 'LUFScale usa automaticamente la misura storica completa, l’unico metodo convalidato '
                                 'sul corpus di riferimento.',
        'guide_analyze_prediction_body': 'Solo analisi può stimare il risultato, ma non crea audio né controllo '
                                         'qualità di uscita.',
        'guide_analyze_prediction_title': 'Stima senza uscita',
        'guide_build_body': 'In Windows 10 1809 o successivo, oppure Windows 11 x86-64:\n'
                            '\n'
                            '1. Scaricare «LUFScale-2.1.12-Setup-x64.exe» e il relativo file SHA-256.\n'
                            '2. Verificare SHA-256, quindi fare doppio clic sul programma di installazione.\n'
                            '3. Leggere e accettare la licenza GNU GPL e seguire la procedura guidata.\n'
                            '4. Avviare LUFScale dal menu Start.\n'
                            '\n'
                            'Applicazione, Python, PySide6/Qt, FFmpeg, codec, guide e licenze sono già inclusi. '
                            'L’installazione non scarica nulla e non richiede comandi PowerShell. Viene creato '
                            'automaticamente un programma di disinstallazione Windows.\n'
                            '\n'
                            'La distribuzione non è firmata; dopo aver verificato il file e il checksum, SmartScreen '
                            'può chiedere conferma.',
        'guide_build_title': 'Installare LUFScale in Windows x86-64',
        'guide_estimated_total_help': 'Tempo totale stimato: 12 min - fine verso le 14:30. «12 min» è la durata totale '
                                      'stimata e «14:30» l’ora prevista di fine. Se si supera la mezzanotte, il numero '
                                      'di giorni viene aggiunto automaticamente prima dell’ora, per esempio «2 g. '
                                      '14:30».',
        'guide_file_processing_body': 'Ogni file riceve misura e guadagno propri per avvicinarsi all’obiettivo LUFS '
                                      'sotto il limite True Peak.',
        'guide_file_processing_title': 'Elaborazione per file',
        'guide_help_tooltip': 'Apre la guida PDF completa nella lingua selezionata.',
        'guide_level_mode_body': 'Traccia - consigliato: avvicina ogni file all’obiettivo. Album - avanzato e '
                                 'specializzato: applica un guadagno comune e conserva i contrasti. Usare Album per '
                                 'un’opera ascoltata in ordine; Traccia per riproduzione casuale o livello regolare '
                                 'fra file.',
        'guide_license_body': 'LUFScale è software libero distribuito con licenza GNU GPL-3.0-or-later. La licenza ne '
                              'consente uso, studio, modifica e ridistribuzione alle proprie condizioni. La '
                              'distribuzione include sorgenti, avvisi e licenze di terze parti. Il software è fornito '
                              'senza garanzia.',
        'guide_license_feature': '• Software libero GNU GPL-3.0-or-later: la licenza consente uso, studio, modifica e '
                                 'ridistribuzione.\n'
                                 '• Programma di installazione offline Windows x86-64 con Python, Qt e FFmpeg. Windows 11 '
                                 'è consigliato; Windows 10 1809 o successivo resta una destinazione di compatibilità, '
                                 'ma il supporto standard Microsoft è terminato.',
        'guide_license_title': 'Software libero e ridistribuzione',
        'guide_log_legend_cancelled': 'Elaborazione interrotta volontariamente; non è un errore.',
        'guide_log_legend_compliant': 'Copia audio invariata: la sorgente rispettava già obiettivo e limite di picco.',
        'guide_log_legend_error': 'Non è stato possibile completare il file interessato.',
        'guide_log_legend_success': 'Elaborazione completata senza anomalie rilevate.',
        'guide_log_legend_warning': 'L’uscita esiste, ma una misura supera la tolleranza prevista.',
        'guide_missing_message': 'La guida PDF non è stata trovata: {path}',
        'guide_missing_title': 'Guida non disponibile',
        'guide_open_error': 'Impossibile aprire la guida PDF: {path}',
        'guide_quality_priority_body': 'LUFScale misura la sonorità dei file e, con Normalizza, regola fisicamente il '
                                       'volume percepito verso un obiettivo LUFS controllando il picco reale. Ogni '
                                       'sorgente viene analizzata per intero; l’uscita viene poi misurata di nuovo e '
                                       'verificata. Il risultato non dipende da tag o da un lettore compatibile: i '
                                       'livelli sono più coerenti tra i file, gli scostamenti vengono segnalati e gli '
                                       'originali restano intatti.',
        'guide_quality_priority_title': 'A cosa serve LUFScale?',
        'help_button': 'Aiuto',
        'help_overview': '• Normalizzazione reale, ReplayGain o analisi di MP3, FLAC, WAV, AIFF, M4A, OGG e Opus.\n'
                         '• Ogni file viene misurato e trattato separatamente verso l’obiettivo scelto.\n'
                         '• Struttura, metadati e copertine compatibili sono conservati; gli originali non cambiano.\n'
                         '• Parallelismo Auto, cache, ripresa, controllo qualità, CSV, avanzamento, CPU e cronologie '
                         'LUFS.\n'
                         '• Interfaccia e guide PDF in 12 lingue.',
        'help_title': 'Caratteristiche principali',
        'increase_value': 'Aumentare il valore',
        'input_lufs_log': 'ingresso {value} LUFS',
        'interface_ffmpeg_message': 'Il motore audio FFmpeg integrato manca o non è utilizzabile. Reinstalla LUFScale '
                                    'dall’archivio di distribuzione completo.',
        'internal_error': 'Errore interno: {error}',
        'interrupted': 'Elaborazione interrotta.',
        'invalid_location': 'Posizione non valida',
        'issue_detail_column': 'Dettagli',
        'issue_file_column': 'File',
        'issue_path_column': 'Percorso',
        'language': 'Lingua',
        'language_tooltip': 'Cambia immediatamente la lingua dell’interfaccia, dei messaggi e dei futuri rapporti CSV. '
                            'La scelta viene memorizzata.',
        'log_help_text': 'Ogni riga riguarda un file o una fase generale.\n'
                         '\n'
                         '• Una riga riuscita inizia direttamente con il nome del file; RIUSCITO non viene più '
                         'ripetuto.\n'
                         '• CONFORME, RIPRESO, IGNORATO, ANNULLATO ed ERRORE restano quando aggiungono informazioni '
                         'utili.\n'
                         '• I livelli mostrano ingresso → uscita rimisurata, poi l’eventuale risultato del controllo '
                         'qualità.\n'
                         '• Avvisi ed Errori aprono elenchi separati con nome, percorso e dettaglio. Sono disponibili '
                         'in pausa o a fine elaborazione e ogni elenco può essere salvato.\n'
                         '\n'
                         'Colori: verde = riuscito; arancione = avviso; rosso = file non completato; viola-blu = '
                         'ripreso; grigio = informazione, elemento ignorato o annullamento.\n'
                         '\n'
                         'AVVISO QC — sonorità indica che l’uscita rimisurata differisce dal valore atteso di oltre '
                         '±0,60 LU. Un valore più negativo è più basso; uno meno negativo è più forte. Lo scarto è la '
                         'differenza assoluta: -14,69 invece di -14,00 equivale a 0,69 LU. Il file viene comunque '
                         'creato: non è un errore di conversione. Se l’ascolto va bene non è obbligatorio intervenire. '
                         'Per un obiettivo rigoroso, consultare dettaglio e CSV e verificare obiettivo e limite True '
                         'Peak prima di riprovare. Il solo messaggio non identifica con certezza limite, codificatore '
                         'o limite di correzione come causa.\n'
                         '\n'
                         'AVVISO QC — picco indica che il picco reale rimisurato supera il limite scelto di oltre 0,25 '
                         'dB. Il file viene comunque creato. Se l’avviso persiste, scegliere un obiettivo LUFS più '
                         'basso o un limite più prudente, per esempio -2,0 dBTP, e riprovare.\n'
                         '\n'
                         'I tempi cumulativi sommano il lavoro di tutte le attività parallele. Il tempo totale è la '
                         'durata realmente trascorsa.',
        'log_placeholder': 'Il resoconto dell’elaborazione verrà visualizzato qui.',
        'log_title': 'Registro di elaborazione',
        'loudness_comparison_after': 'Dopo',
        'loudness_comparison_analysis_only': 'Nessuna uscita in modalità Solo analisi',
        'loudness_comparison_before': 'Prima',
        'loudness_comparison_help_text': 'Ogni file aggiunge un punto a destra. Prima mostra sempre la sorgente '
                                         'misurata. Con Normalizza, Dopo mostra l’uscita realmente rimisurata. Con '
                                         'ReplayGain, il secondo grafico tratteggiato stima la riproduzione: sonorità '
                                         'sorgente più guadagno Track memorizzato. Il segno ≈ e la nota Lettore '
                                         'compatibile indicano che non è una misura fisica del file consegnato. Un '
                                         'lettore incompatibile mantiene il livello originale; uno compatibile può '
                                         'variare il risultato tramite preamplificazione o protezione dal clipping. I '
                                         'grafici mantengono la stessa scala fissa ±6 LU. Solo analisi non ha '
                                         'un’uscita Dopo.',
        'loudness_comparison_increased': 'Scarto aumentato di {value} LU',
        'loudness_comparison_needs_qc': 'Attivare il controllo qualità per confrontare',
        'loudness_comparison_no_after': 'Nessuna curva Dopo per questa operazione',
        'loudness_comparison_not_applicable': 'Confronto non disponibile per questa operazione',
        'loudness_comparison_reached': 'Obiettivo raggiunto · scarto {value} LU',
        'loudness_comparison_reduced': 'Scarto ridotto di {value} LU',
        'loudness_comparison_replaygain_after': 'Riproduzione RG stimata',
        'loudness_comparison_replaygain_note': 'Lettore compatibile · audio invariato',
        'loudness_comparison_scale': 'Vista ±{scale} LU · toll. QC ±{tolerance} LU',
        'loudness_comparison_target': 'Obiettivo {value} LUFS',
        'loudness_comparison_title': 'Evoluzione della sonorità',
        'loudness_comparison_tooltip': 'Prima mostra la sonorità fisica. In ReplayGain, il secondo grafico stima la '
                                       'riproduzione compatibile dal guadagno memorizzato.',
        'loudness_comparison_unchanged': 'Scarto invariato',
        'loudness_comparison_waiting': 'In attesa di un file elaborato',
        'loudness_meter_current_file': 'Ultimo: {file}',
        'loudness_meter_estimated': 'Stimato',
        'loudness_meter_help_text': 'La linea rossa è l’obiettivo e il valore blu è la sonorità realmente rimisurata '
                                    'dell’ultima uscita. Sale o scende per ogni file. Il punteggio riassume le ultime '
                                    '8 uscite rimisurate. Se il pannello rosso indica «Vedi avvisi», metti in pausa '
                                    'l’elaborazione o attendi la fine, quindi apri Avvisi per identificare i file '
                                    'interessati.',
        'loudness_meter_maximum': 'Max {value}',
        'loudness_meter_measured': 'Misurato',
        'loudness_meter_minimum': 'Min {value}',
        'loudness_meter_no_file': 'In attesa di un’analisi',
        'loudness_meter_target': 'Obiettivo {value} LUFS',
        'loudness_meter_title': 'Misuratore di sonorità',
        'loudness_meter_tooltip': 'Obiettivo rosso; ultima uscita realmente rimisurata in blu.',
        'loudness_meter_waiting': 'In attesa di un file audio',
        'loudness_meter_worst_file': 'Scarto maggiore: {file}',
        'loudness_meter_worst_file_detail': 'Scarto maggiore nelle ultime 8 analisi: {file} — {measured} LUFS rispetto '
                                            'a {expected} LUFS, scarto {deviation} LU.',
        'loudness_score_acceptable': 'Accettabile',
        'loudness_score_check': 'Vedi avvisi',
        'loudness_score_excellent': 'Eccellente',
        'loudness_score_good': 'Buono',
        'loudness_score_needs_qc': 'Punteggio obiettivo: attivare il controllo qualità',
        'loudness_score_not_applicable': 'Punteggio obiettivo: non applicabile',
        'loudness_score_tooltip': 'Il punteggio usa le ultime 8 uscite rimisurate. 100 è esatto, 50 equivale a un '
                                  'errore RMS di 0,60 LU e 0 a 1,20 LU o più. Un pannello rosso indica che almeno un '
                                  'avviso di sonorità è consultabile con il pulsante Avvisi.',
        'loudness_score_value': 'Punteggio obiettivo: {score}/100\n{rating}\nErrore RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Punteggio obiettivo: in attesa',
        'measurement_unavailable': 'Misurazione non disponibile.',
        'mp3': 'MP3',
        'mp3_filter': 'Audio supportato (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Nessuna cartella selezionata',
        'no_mp3': 'Nessun file audio supportato trovato.',
        'no_new_source': 'Non è stata aggiunta alcuna cartella o file audio supportato.',
        'not_performed': 'Non eseguito',
        'open_output_error': 'Impossibile aprire la cartella di destinazione: {error}',
        'operation': 'Operazione',
        'operation_analyze': 'Solo analisi — nessun file creato',
        'operation_analyze_label': 'Solo analisi',
        'operation_convert': 'Uniforma — normalizza realmente l’audio',
        'operation_convert_label': 'Uniformazione audio',
        'operation_help_text': 'Normalizza tratta ogni file separatamente e rimisura l’uscita. ReplayGain non cambia i '
                               'campioni. Solo analisi produce misure e un CSV facoltativo, ma nessun file audio.',
        'operation_replaygain': 'ReplayGain — senza ricodifica audio',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Normalizza modifica l’audio verso l’obiettivo. ReplayGain copia il flusso e aggiunge '
                             'tag. Solo analisi misura senza creare audio.',
        'option_status_auto_start': 'AUTO',
        'option_status_overwrite': 'SOV',
        'option_status_quality_control': 'QUAL',
        'option_status_report': 'CSV',
        'option_status_resume': 'RIP',
        'option_status_skip_compliant': 'SALT',
        'options_tab': 'Opzioni',
        'output_lufs_log': 'uscita {value} LUFS',
        'output_lufs_unavailable': 'LUFS di uscita non disponibile',
        'overwrite': 'Sovrascrivi i file esistenti',
        'overwrite_tooltip': 'Consente di sostituire un MP3 già presente nella destinazione. I file sorgente non '
                             'vengono mai sovrascritti.',
        'parallel': 'Processi paralleli',
        'parallel_adjusted': 'Parallelismo automatico — {active} processo/i, CPU {cpu:.0f} %.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automatico, massimo {maximum}',
        'parallel_tooltip': 'Determina quanti file possono essere elaborati contemporaneamente.\n'
                            '\n'
                            '• Auto parte con al massimo 4 attività. Quando la misurazione CPU è disponibile, la '
                            'controlla ogni secondo: aggiunge un’attività sotto il 70% di utilizzo e ne rimuove una '
                            'sopra il 92%.\n'
                            '• Auto non supera mai il numero di processori logici rilevati, con un limite assoluto di '
                            '16 attività.\n'
                            '• Se la misurazione CPU non è disponibile, Auto usa direttamente quel limite rilevato '
                            'senza adattamento dinamico.\n'
                            '• Un valore numerico fissa il numero massimo di attività simultanee; non è un obiettivo '
                            'di utilizzo CPU.\n'
                            '\n'
                            'Più attività possono accelerare un lotto grande, ma aumentano carico, temperatura e '
                            'attività del disco. Premi − finché non compare Auto.',
        'paste': 'Incolla',
        'path_left': 'Mostra la parte sinistra del percorso',
        'path_right': 'Mostra la parte destra del percorso',
        'pause': 'Pausa',
        'peak': 'Picco reale massimo',
        'peak_tooltip': 'Il picco reale massimo è un limite, non un livello da raggiungere. Limita in dBTP i picchi '
                        'più alti della forma d’onda ricostruita, compresi quelli tra i campioni, per ridurre il '
                        'clipping dopo la codifica o la transcodifica.\n'
                        '\n'
                        '• -1,0 dBTP — limite di consegna comune, con il picco di uscita più alto.\n'
                        '• -1,5 dBTP — valore predefinito e compromesso prudente per gli MP3.\n'
                        '• -2,0 dBTP — margine aggiuntivo, utile se il file verrà ricodificato o con un obiettivo di '
                        'sonorità elevato.\n'
                        '• 0 dBTP — nessun margine; sconsigliato per MP3.\n'
                        '\n'
                        'Un valore più negativo è più sicuro, ma può impedire alle tracce molto dinamiche di '
                        'raggiungere esattamente l’obiettivo LUFS.',
        'phase_summary': 'Ripartizione stimata del tempo totale — analisi {analysis}, conversione {conversion}, '
                         'controllo qualità {quality}.',
        'pipeline_enabled': 'Pipeline Traccia — ogni conversione inizia appena termina la sua analisi.',
        'pre_measurement': 'Misurazione dei file di ingresso…',
        'preset': 'Preimpostazione',
        'preset_dynamic': 'Musica dinamica',
        'preset_library': 'Libreria musicale — consigliata',
        'preset_streaming': 'Streaming più presente',
        'preset_tooltip': 'Applica insieme un obiettivo di sonorità, un picco reale massimo e una qualità MP3 '
                          'coerenti. Ogni modifica manuale seleziona Personalizzato.',
        'processing_cancelled': 'Elaborazione annullata.',
        'processing_completed': 'Elaborazione completata',
        'processing_in_progress': 'Elaborazione in corso',
        'processing_paused': 'Elaborazione in pausa.',
        'processing_resumed': 'Elaborazione ripresa.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'AVVISO — controllo qualità impossibile: {error}',
        'qc_log': ' — controllo qualità: {quality}',
        'qc_ok': 'RIUSCITO',
        'qc_warning': 'AVVISO — {detail}',
        'quality': 'Qualità audio',
        'quality_control': 'Controllo qualità automatico',
        'quality_control_tooltip': 'Rimisura ogni uscita. Le correzioni continuano a mirare a ±0,50 LU; l’avviso di '
                                   'sonorità appare solo oltre ±0,60 LU. Gli MP3 dinamici mantengono fino a tre '
                                   'tentativi; WAV, AIFF e FLAC possono essere rifatti dalla sorgente fino a due volte '
                                   'se resta margine True Peak. Disattivare elimina verifica, tentativi e attività del '
                                   'misuratore.',
        'quality_tooltip': 'Regola il compromesso tra qualità e dimensione dei formati compressi. Più il numero è '
                           'basso, maggiori sono qualità e bitrate. Questa impostazione non modifica l’obiettivo LUFS '
                           'né il picco reale massimo.\n'
                           '\n'
                           '• 0 — qualità massima, consigliata per conservare i dettagli.\n'
                           '• 1-2 — qualità molto alta.\n'
                           '• 3-4 — buon compromesso qualità/dimensione.\n'
                           '• 5-9 — file più piccoli, con maggiori perdite.\n'
                           '\n'
                           'FLAC resta senza perdita a qualsiasi valore. WAV e AIFF ignorano l’impostazione e '
                           'conservano frequenza e profondità PCM compatibili con la sorgente. Per MP3, M4A, OGG e '
                           'Opus, un valore basso può richiedere un bitrate superiore all’originale e produrre un file '
                           'più grande. Un valore più alto di solito riduce la dimensione, senza garantire lo stesso '
                           'numero di byte perché questi codificatori usano spesso il VBR. Ricodificare un formato con '
                           'perdita non ripristina le informazioni già perse.',
        'ready': 'Pronto',
        'recursive_scan': 'Analisi ricorsiva delle cartelle…',
        'remove_all': 'Rimuovi tutto',
        'remove_selection': 'Rimuovi selezione',
        'replaygain_help_text': 'ReplayGain calcola un guadagno e scrive REPLAYGAIN_TRACK_GAIN/PEAK. Il flusso è '
                                'copiato senza ricodifica (-c:a copy); solo un lettore compatibile applica i tag. LUFS '
                                'e True Peak fisici non cambiano.',
        'replaygain_levels_log': 'audio invariato: {before} LUFS · ReplayGain {gain} dB nei metadati · obiettivo '
                                 'impostato {target} LUFS (serve un lettore compatibile)',
        'replaygain_log_help_text': 'In ReplayGain, il registro mostra la sonorità fisica invariata, il guadagno '
                                    'scritto nei metadati e l’obiettivo impostato. Con il controllo qualità attivo, '
                                    '«audio invariato e tag verificati» significa che sonorità e picco sono stati '
                                    'confrontati con la sorgente e che i tag sono stati riletti; non significa che il '
                                    'file misuri fisicamente l’obiettivo.',
        'replaygain_operation': 'ReplayGain senza ricodifica',
        'replaygain_qc_help_text': 'Con il controllo qualità attivo, ReplayGain rimisura il file consegnato per '
                                   'confermare che sonorità fisica e picco siano rimasti invariati, quindi verifica i '
                                   'tag Track. Un esito positivo conferma audio preservato e tag presenti, non il '
                                   'raggiungimento fisico dell’obiettivo.',
        'replaygain_qc_ok': 'RIUSCITO — audio invariato e tag verificati',
        'replaygain_tags_missing': 'Tag ReplayGain non trovati.',
        'replaygain_usefulness_text': 'ReplayGain è utile per uniformare la riproduzione in modo reversibile e senza '
                                      'ricodifica in una libreria usata con un lettore compatibile. Per consegnare un '
                                      'file che misuri fisicamente l’obiettivo in ogni lettore, usare Normalizza.',
        'report_destination': 'destinazione',
        'report_detail': 'dettaglio',
        'report_error': 'AVVISO — impossibile creare il rapporto CSV: {error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'guadagno_db',
        'report_input_dbtp': 'dbtp_ingresso',
        'report_input_lufs': 'lufs_ingresso',
        'report_log': 'Rapporto CSV — {path}',
        'report_mode': 'modalità',
        'report_operation': 'operazione',
        'report_output_dbtp': 'dbtp_uscita',
        'report_output_lufs': 'lufs_uscita',
        'report_path': 'Rapporto: {path}',
        'report_qc': 'controllo_qualità',
        'report_qc_engine': 'motore_controllo_qualità',
        'report_seconds': 'tempo_secondi',
        'report_source': 'sorgente',
        'report_status': 'stato',
        'report_tooltip': 'Crea solo un rapporto CSV con misure, tempi e avvisi; non aggiunge JSON diagnostici.',
        'resume': 'Riprendi dopo un’interruzione',
        'resume_not_saved': ' Punto di ripresa non salvato: {error}',
        'resume_processing': 'Riprendi',
        'resume_tooltip': 'I file già completati con le stesse impostazioni vengono riconosciuti e non vengono '
                          'elaborati di nuovo.',
        'resumed_progress': 'Ripreso: {file}',
        'save_dialog_cancel': 'Annulla',
        'save_dialog_filename': 'Nome file',
        'save_dialog_filetype': 'Formato',
        'save_dialog_location': 'Posizione',
        'save_dialog_overwrite': 'Sostituisci',
        'save_dialog_overwrite_message': 'Il file «{file}» esiste già.',
        'save_dialog_overwrite_title': 'Sostituire il file?',
        'save_dialog_parent': 'Cartella superiore',
        'save_dialog_save': 'Salva',
        'save_issue_list': 'Salva come CSV…',
        'save_issue_list_error': 'Impossibile salvare l’elenco: {error}',
        'save_issue_list_error_title': 'Salvataggio impossibile',
        'save_issue_list_title': 'Salva elenco CSV',
        'scan_error': 'ERRORE — {error}',
        'scanning_folders': 'Analisi delle cartelle…',
        'settings': 'Impostazioni',
        'open_folder': 'Apri cartella',
        'show_option_help': 'Mostra aiuto: {option}',
        'silent_copy': 'Audio silenzioso o non misurabile copiato.',
        'silent_copy_no_replaygain': 'Audio silenzioso copiato senza tag ReplayGain.',
        'silent_unmeasurable': 'Audio silenzioso o non misurabile.',
        'simulation': 'Simulazione',
        'skip_compliant': 'Non ricodificare i file già conformi',
        'skip_compliant_tooltip': 'Dopo l’analisi, un file entro ±0,10 LU dall’obiettivo e sotto il limite True Peak '
                                  'viene copiato senza ricodifica.',
        'skipped_progress': 'Ignorato: {file}',
        'source_audio_count': 'File: {count}',
        'source_list_more': '… altre {count} sorgenti conservate',
        'source_safety': 'I file sorgente non vengono mai spostati né modificati.',
        'source_selection_tooltip': 'Selezione multipla: Ctrl+clic per elementi separati e Maiusc+clic per un intervallo.',
        'sources_added': '{count} sorgente/i aggiunta/e.',
        'start': 'Avvia',
        'status_analyzed': 'ANALIZZATO',
        'status_cancelled': 'ANNULLATO',
        'status_compliant': 'CONFORME',
        'status_error': 'ERRORE',
        'status_ok': 'RIUSCITO',
        'status_resumed': 'RIPRESO',
        'status_skipped': 'IGNORATO',
        'status_warning': 'AVVISO',
        'switch_to_dark': 'Modalità scura',
        'switch_to_light': 'Modalità chiara',
        'tagline': 'Uniforma il volume audio percepito',
        'target': 'Obiettivo di sonorità',
        'target_tooltip': 'L’obiettivo di sonorità è la sonorità integrata desiderata sull’intera traccia, espressa in '
                          'LUFS. Un valore meno negativo produce un file più forte: -14 LUFS è più forte di -16 LUFS. '
                          'Una differenza di 2 LU corrisponde approssimativamente a 2 dB di livello prima di '
                          'un’eventuale limitazione dei picchi.\n'
                          '\n'
                          'Riferimenti: -18 LUFS per un risultato più tranquillo e dinamico; -16 LUFS per un '
                          'equilibrio generale; -14 LUFS per un risultato più forte in stile streaming. Le piattaforme '
                          'possono poi applicare la propria normalizzazione in riproduzione.\n'
                          '\n'
                          'Questo obiettivo non appiattisce da solo la dinamica interna della traccia. Se il picco '
                          'reale massimo impedisce di raggiungerlo senza clipping, il risultato può rimanere '
                          'leggermente più basso.',
        'theme_accessible': 'Cambia l’aspetto dell’applicazione. La scelta viene memorizzata.',
        'total_time': 'Tempo totale: {duration}',
        'track_two_pass': 'Normalizzazione della traccia in due passaggi.',
        'true_peak_meter_exceeded': 'Superamento {margin} dB',
        'true_peak_meter_margin': 'Margine {margin} dB',
        'true_peak_meter_title': 'Margine di picco',
        'true_peak_meter_tooltip': 'Confronta il true peak dell’ultima uscita con il limite scelto. Il marcatore '
                                   'mostra l’ultimo valore e il triangolo conserva il picco più alto del lotto. Verde: '
                                   'limite rispettato; arancione: superamento fino a 0,25 dB; rosso: superiore. La '
                                   'tolleranza arancione è del controllo qualità LUFScale, non una norma di consegna. '
                                   'Si azzera a ogni lotto.',
        'true_peak_meter_waiting': 'In attesa di una misura dBTP',
        'version_changes': '• Un unico programma di installazione offline per Windows 10/11 x86-64.\n'
                           '• Python, PySide6/Qt, FFmpeg, codec, guide e licenze sono inclusi; durante l’installazione '
                           'non servono download o comandi PowerShell.\n'
                           '• La build convalida loudnorm e gli encoder prima di creare il setup e il suo SHA-256.',
        'version_changes_title': 'Novità della versione {version}',
        'version_label': 'Versione {version}',
        'volume': 'Volume',
        'volume_loud': 'Forte: -14 LUFS',
        'volume_normal': 'Normale: -16 LUFS',
        'volume_soft': 'Basso: -18 LUFS',
        'volume_tooltip': 'Questa impostazione è una scorciatoia per l’obiettivo di sonorità; non modifica il volume '
                          'di ascolto del sistema.\n'
                          '\n'
                          '• Basso: -18 LUFS — livello più tranquillo, maggiore margine dinamico e minore probabilità '
                          'di attivare il limiter.\n'
                          '• Normale: -16 LUFS — compromesso equilibrato e buon punto di partenza per una raccolta '
                          'personale.\n'
                          '• Alto: -14 LUFS — riproduzione più presente, vicina all’obiettivo Normale di Spotify, ma '
                          'con maggiore probabilità di richiedere limitazione.\n'
                          '• Personalizzato — consente di inserire direttamente un altro obiettivo LUFS.\n'
                          '\n'
                          'Sono scelte pratiche, non uno standard universale.',
        'warning_list_title': 'Avvisi di elaborazione',
        'warnings_button': 'Avvisi ({count})',
        'warnings_button_tooltip': 'Apre l’elenco degli avvisi con nome file, percorso e dettagli. Disponibile durante '
                                   'una pausa o dopo l’elaborazione.',
        'warnings_dialog_title': 'Avvisi di elaborazione'},
 'ja': {'activity_cancelled': '動作状況：処理をキャンセル',
        'activity_cancelling': '動作状況：キャンセル中…',
        'activity_completed': '動作状況：処理完了',
        'activity_compliant': '適合：{count}',
        'activity_detected': '動作状況：{total}件のファイルを検出',
        'activity_errors': 'エラー：{count}',
        'activity_files': 'ファイル：{count}',
        'activity_idle': '動作状況：待機中',
        'activity_preparing': '動作状況：ファイルを準備中…',
        'activity_progress': '{total} ファイル • 成功 {success} • 警告 {warnings} • エラー {failed} • 再開/スキップ {skipped} • 適合 '
                             '{compliant}',
        'activity_skipped': '再開/スキップ：{count}',
        'activity_successes': '成功：{count}',
        'activity_warnings': '警告：{count}',
        'adaptive_disabled_log': '適応解析 — {sample}回の測定後に高速プローブを停止しました（成功{successes}回、推定短縮率{percent:+.1f}%）。',
        'add_folders': 'フォルダを追加…',
        'add_mp3': '音声ファイルを追加…',
        'add_replaygain': 'ReplayGainを追加',
        'add_source_files': '音声ファイルを追加',
        'add_source_folder': 'ソースフォルダーを追加',
        'already_completed': '前回の実行ですでに完了しています。',
        'already_compliant_badge': '適合済み',
        'already_compliant_copy': '適合済み：音声を再エンコードせず同一コピー。',
        'already_compliant_log': '適合済み、再エンコードなし',
        'analysis_cache_summary': '解析キャッシュ — {hits}件の測定値を再利用しました。',
        'analysis_impossible': '解析に失敗しました：{error}',
        'analysis_measurement_progress': '解析 {current}/{total} — {file} — {value}',
        'analysis_method': '解析方法',
        'analysis_method_adaptive': '適応方式 — 効果がなければ停止',
        'analysis_method_fast': '高速方式 — 実験用',
        'analysis_method_historical': '従来方式 — 基準',
        'analysis_method_log': '解析方法 — {method}。',
        'analysis_method_tooltip': '安定版では、基準コーパスで検証済みの完全な履歴方式を自動的に使用します。高速方式と適応方式は選択肢から削除されました。',
        'analysis_progress': '解析 {current}/{total}：{file}',
        'analysis_progress_help_text': '解析のみでは、各測定の完了時に処理前グラフ、ログ、進行バーがファイル単位で進みます。処理後は動きません。',
        'analyze': '解析',
        'analyze_only_fresh_help_text': '解析のみは実行ごとにFFmpegで各ソース全体を再測定します。処理前グラフと進捗はファイル単位で進み、出力と出力QCはありません。',
        'analyze_operation': '解析／シミュレーション',
        'analyzed_progress': '解析済み：{file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': '再エンコードせず音声をコピーし、ReplayGainタグを追加しました。',
        'audio_tab': 'オーディオ',
        'auto_start': 'ドロップまたは貼り付け後に自動開始',
        'auto_start_tooltip': '保存先が選択済みの場合、ドラッグ＆ドロップまたは貼り付け後に自動で処理を開始します。',
        'cancel': 'キャンセル',
        'cancelled_summary': 'キャンセル — 成功 {success}、エラー {failed}、再開/スキップ {skipped}、警告 {warnings}、適合 {compliant} — '
                             '{duration}。',
        'cancelling': 'キャンセル中…',
        'choose': '選択…',
        'choose_output': '保存先フォルダーを選択',
        'clipboard': 'クリップボード',
        'clipboard_empty': 'クリップボードに有効なフォルダーまたは対応音声ファイルのパスがありません。',
        'close_button': '閉じる',
        'close_question': '処理をキャンセルしてアプリケーションを終了しますか？',
        'completed_dialog_summary': '状態：完了\n'
                                    'ファイル数：{files}\n'
                                    '成功：{success}\n'
                                    'エラー：{failed}\n'
                                    '再開またはスキップ：{skipped}\n'
                                    '警告：{warnings}\n'
                                    '適合：{compliant}\n'
                                    '合計時間：{duration}',
        'completed_summary': '完了 — 成功 {success}、エラー {failed}、再開/スキップ {skipped}、警告 {warnings}、適合 {compliant} — '
                             '{duration}。',
        'completed_with_errors': '警告付きで処理完了',
        'convert': 'ノーマライズ',
        'convert_operation': '音声ノーマライズ',
        'cpu_tooltip': '処理中のシステム全体のCPU使用率を1秒ごとに更新します。',
        'cpu_usage': 'CPU',
        'create_report': 'CSVレポートを作成',
        'csv_file_filter': 'CSVファイル (*.csv)',
        'custom': 'カスタム',
        'decrease_value': '値を減らす',
        'description': '原本を変更せず、ファイルごとに知覚音量をそろえます。',
        'destination': '保存先',
        'destination_error': 'エラー — 保存先を使用できません：{error}',
        'destination_path_tooltip': 'パスをクリックし、矢印キー、Home/End、またはマウスホイールで移動します。選択とコピーはできますが、変更はできません。',
        'destination_required_start': '先に「選択…」ボタンで保存先フォルダーを選んでください。',
        'dialog_ok': '確認',
        'drop_subtitle': 'MP3、FLAC、WAV、AIFF、M4A、OGG、Opus — サブフォルダー対応',
        'drop_title': 'フォルダーまたは音声ファイルをここにドロップ',
        'elapsed_time': '経過時間：{duration}',
        'error_list_title': '処理エラー',
        'error_progress': 'エラー：{file}',
        'errors_button': 'エラー ({count})',
        'errors_button_tooltip': 'ファイル名、パス、詳細を含むエラー一覧を開きます。一時停止中または処理後に利用できます。',
        'errors_dialog_title': '処理エラー',
        'estimated_result': '推定結果です。ファイルは作成されません。',
        'estimated_total_calculating': '推定合計時間：計算中…',
        'estimated_total_time': '推定合計時間：{duration}',
        'estimated_total_time_with_day_finish': '推定合計時間：{duration} — {days}日。{time}',
        'estimated_total_time_with_finish': '推定合計時間：{duration} — {time}',
        'estimated_total_unavailable': '推定合計時間：利用不可',
        'ffmpeg_download_button': 'FFmpeg公式サイトを開く',
        'ffmpeg_error_no_detail': '詳細のないFFmpegエラーです。',
        'ffmpeg_execution_error': 'FFmpegを実行できません: {error}',
        'ffmpeg_incompatible': 'FFmpegに互換性がありません',
        'ffmpeg_missing': 'FFmpegが見つかりません',
        'ffmpeg_missing_encoders': 'この FFmpeg には必要な音声エンコーダーがすべて含まれていません: {encoders}。',
        'ffmpeg_missing_message': 'FFmpegをインストールしてPATHから利用可能にするか、プログラムの隣に配置してください。',
        'ffmpeg_no_lame': 'このFFmpegビルドにはlibmp3lame MP3エンコーダーが含まれていません。',
        'ffmpeg_no_loudnorm': 'このFFmpegビルドにはloudnormフィルターがありません。',
        'ffmpeg_not_responding': 'FFmpegが正しく応答していません。',
        'file_exists': 'ファイルはすでに存在します。',
        'files_found': '{total} 個の音声ファイル — {operation} — {parallel} 並列処理。',
        'finalization_completed': '最終処理は {duration} で完了しました。',
        'finalizing': '最終処理 — レポート、解析キャッシュ、再開データ…',
        'folder': 'フォルダー',
        'folder_unavailable': 'フォルダーを利用できません',
        'guide_analysis_method': 'LUFScaleは、基準コーパスで検証された唯一の方式である完全な履歴測定を自動的に使用します。',
        'guide_analyze_prediction_body': '解析のみは結果を推定できますが、音声ファイルと出力QCは作りません。',
        'guide_analyze_prediction_title': '出力なしの推定',
        'guide_build_body': 'Windows 10 1809以降またはWindows 11 x86-64で行います。\n'
                            '\n'
                            '1. 「LUFScale-2.1.12-Setup-x64.exe」とSHA-256ファイルをダウンロードします。\n'
                            '2. SHA-256を確認してインストーラーをダブルクリックします。\n'
                            '3. GNU GPLライセンスを読み、同意してウィザードに従います。\n'
                            '4. スタートメニューからLUFScaleを起動します。\n'
                            '\n'
                            'アプリ、Python、PySide6/Qt、FFmpeg、コーデック、ガイド、ライセンスは同梱済みです。インストール時のダウンロードやPowerShellコマンドは不要で、Windowsアンインストーラーも自動作成されます。\n'
                            '\n'
                            '配布物は未署名です。ファイルとチェックサムを確認した後、SmartScreenが確認を求める場合があります。',
        'guide_build_title': 'Windows x86-64にLUFScaleをインストール',
        'guide_estimated_total_help': '推定合計時間：12分 - '
                                      '14:30頃に完了。「12分」は推定総時間、「14:30」は予定終了時刻です。日付をまたぐ場合は、時刻の前に日数が自動表示されます（例：『2日。14:30』）。',
        'guide_file_processing_body': '各ファイルの測定値から個別ゲインを計算し、True Peak上限内で目標LUFSに近づけます。',
        'guide_file_processing_title': 'ファイル単位の処理',
        'guide_help_tooltip': '選択した言語の完全なPDFガイドを開きます。',
        'guide_level_mode_body': 'トラック（推奨）は各ファイルを目標へ近づけます。アルバムは上級の特殊モードで、共通ゲインにより曲間のコントラストを保ちます。順番どおり聴く作品にはアルバム、シャッフルやファイルごとの均一化にはトラックを使います。',
        'guide_license_body': 'LUFScaleはGNU '
                              'GPL-3.0-or-laterで配布される自由ソフトウェアです。ライセンス条件に従って使用、調査、変更、再配布できます。ソース、通知、第三者ライセンスを同梱します。本ソフトウェアは無保証で提供されます。',
        'guide_license_feature': '• GNU GPL-3.0-or-later自由ソフトウェアです。ライセンスに従って利用、調査、変更、再配布できます。\n'
                                 '• Python、Qt、FFmpegを同梱したWindows x86-64オフラインインストーラーです。Windows 11を推奨します。Windows 10 '
                                 '1809以降も互換対象ですが、Microsoftの標準サポートは終了しています。',
        'guide_license_title': '自由ソフトウェアと再配布',
        'guide_log_legend_cancelled': '処理は意図的に停止されました。エラーではありません。',
        'guide_log_legend_compliant': '音声を変更せずコピーしました。元ファイルは目標値とピーク上限を満たしていました。',
        'guide_log_legend_error': '対象ファイルの処理を完了できませんでした。',
        'guide_log_legend_success': '異常を検出せずに処理が完了しました。',
        'guide_log_legend_warning': '出力は作成されましたが、測定値の一つが許容範囲外です。',
        'guide_missing_message': 'PDFガイドが見つかりません：{path}',
        'guide_missing_title': 'ガイドを利用できません',
        'guide_open_error': 'PDFガイドを開けませんでした: {path}',
        'guide_quality_priority_body': 'LUFScaleはファイルのラウドネスを測定し、「ノーマライズ」ではトゥルーピークを管理しながら、知覚音量をLUFS目標値へ実際に調整します。各音源を全時間解析し、出力を再測定して検証します。結果はタグや対応プレーヤーに依存せず、ファイル間の音量がより揃い、ずれは通知され、元ファイルは変更されません。',
        'guide_quality_priority_title': 'LUFScaleでできること',
        'help_button': 'ヘルプ',
        'help_overview': '• MP3、FLAC、WAV、AIFF、M4A、OGG、Opusのノーマライズ、ReplayGain、解析。\n'
                         '• 各ファイルを個別に測定し、選択した目標へ処理します。\n'
                         '• フォルダー構造、対応メタデータ、アートワークを保持し、原本は変更しません。\n'
                         '• 並列処理、キャッシュ、再開、品質管理、CSV、進行状況、CPU、LUFS履歴。\n'
                         '• 12言語の画面とPDFガイド。',
        'help_title': '主な機能',
        'increase_value': '値を増やす',
        'input_lufs_log': '入力 {value} LUFS',
        'interface_ffmpeg_message': '内蔵FFmpeg音声エンジンが見つからないか使用できません。完全な配布アーカイブからLUFScaleを再インストールしてください。',
        'internal_error': '内部エラー：{error}',
        'interrupted': '処理が中断されました。',
        'invalid_location': '保存先が無効です',
        'issue_detail_column': '詳細',
        'issue_file_column': 'ファイル',
        'issue_path_column': 'パス',
        'language': '言語',
        'language_tooltip': 'インターフェースの言語をすぐに変更して保存します。未翻訳の技術メッセージは英語で表示されます。',
        'log_help_text': '各行はファイルまたは処理全体の段階を示します。\n'
                         '\n'
                         '• 成功行はファイル名から始まり、「成功」を繰り返しません。\n'
                         '• 適合、再開、スキップ、キャンセル、エラーは、役立つ追加情報がある場合に表示します。\n'
                         '• レベルは入力 → 再測定した出力、その後に品質チェック結果を示します。\n'
                         '• 「警告」と「エラー」は、ファイル名、パス、詳細を含む別々の一覧を開きます。一時停止中または処理後に利用でき、各一覧を保存できます。\n'
                         '\n'
                         '色：緑＝成功、オレンジ＝警告、赤＝未完了、青紫＝再開、灰＝情報・スキップ・キャンセル。\n'
                         '\n'
                         'QC警告―ラウドネスは、再測定出力が期待値から±0.60 '
                         'LUを超えて外れたことを示します。より負の値は小さく、負が少ない値は大きく聞こえます。差は絶対値で、-14.00に対する-14.69は0.69 '
                         'LUです。ファイルは作成されており、変換失敗ではありません。聴感上問題なければ操作は必須ではありません。厳密な目標が必要なら詳細とCSVを確認し、目標とTrue '
                         'Peak上限を確認して再実行してください。この表示だけでは、上限、エンコーダー、補正限界のどれが原因か断定できません。\n'
                         '\n'
                         'QC警告―ピークは、再測定True Peakが選択した上限を0.25 dB超えたことを示します。ファイルは作成されます。繰り返す場合は、LUFS目標を下げるか、例えば-2.0 '
                         'dBTPのように安全な上限を選び、再処理してください。\n'
                         '\n'
                         '累積時間は並列タスクの作業時間を合計します。合計時間は実際の経過時間です。',
        'log_placeholder': '処理結果がここに表示されます。',
        'log_title': '処理ログ',
        'loudness_comparison_after': '処理後',
        'loudness_comparison_analysis_only': '解析のみでは出力を作成しません',
        'loudness_comparison_before': '処理前',
        'loudness_comparison_help_text': '各ファイルは右側に点を追加します。「前」は常に測定した入力です。ノーマライズの「後」は実際に再測定した出力です。ReplayGainの第2グラフは破線で、入力ラウドネス＋保存されたTrack '
                                         'Gainによる再生を推定します。≈記号と対応プレーヤーの注記は、出力ファイルの物理測定ではないことを示します。非対応プレーヤーでは元の音量のままです。対応プレーヤーでもプリアンプやクリッピング防止により結果が変わる場合があります。両グラフは共通の固定±6 '
                                         'LUスケールです。解析のみには「後」の出力がありません。',
        'loudness_comparison_increased': '偏差が {value} LU 増加',
        'loudness_comparison_needs_qc': '比較するには品質管理を有効にしてください',
        'loudness_comparison_no_after': 'この操作では処理後グラフを表示しません',
        'loudness_comparison_not_applicable': 'この操作では比較できません',
        'loudness_comparison_reached': '目標範囲内 · 偏差 {value} LU',
        'loudness_comparison_reduced': '偏差を {value} LU 縮小',
        'loudness_comparison_replaygain_after': 'RG再生の推定',
        'loudness_comparison_replaygain_note': '対応プレーヤー · 音声は不変',
        'loudness_comparison_scale': '表示 ±{scale} LU・QC許容 ±{tolerance} LU',
        'loudness_comparison_target': '目標 {value} LUFS',
        'loudness_comparison_title': 'ラウドネスの変化',
        'loudness_comparison_tooltip': '「前」は物理ラウドネスです。ReplayGainの第2グラフは保存ゲインから対応プレーヤーでの再生を推定します。',
        'loudness_comparison_unchanged': '偏差は変わりません',
        'loudness_comparison_waiting': '処理済みファイルを待機中',
        'loudness_meter_current_file': '最新：{file}',
        'loudness_meter_estimated': '推定値',
        'loudness_meter_help_text': '赤線は目標、青値は直前の出力を実際に再測定したラウドネスです。ファイルごとに上下します。スコアは直近8件の再測定結果を要約します。赤いパネルに「警告を確認」と表示されたら、処理を一時停止するか完了を待ち、［警告］を開いて対象ファイルを確認してください。',
        'loudness_meter_maximum': '最大 {value}',
        'loudness_meter_measured': '測定値',
        'loudness_meter_minimum': '最小 {value}',
        'loudness_meter_no_file': '解析待ち',
        'loudness_meter_target': '目標 {value} LUFS',
        'loudness_meter_title': 'ラウドネスメーター',
        'loudness_meter_tooltip': '赤が目標、青が直前の出力を実際に再測定した値です。',
        'loudness_meter_waiting': '音声ファイルを待機中',
        'loudness_meter_worst_file': '最大偏差：{file}',
        'loudness_meter_worst_file_detail': '直近8件の最大偏差：{file} — 目標 {expected} LUFS に対して {measured} LUFS、偏差 {deviation} '
                                            'LU。',
        'loudness_score_acceptable': '許容範囲',
        'loudness_score_check': '警告を確認',
        'loudness_score_excellent': '非常に良い',
        'loudness_score_good': '良い',
        'loudness_score_needs_qc': '目標スコア：品質チェックを有効にしてください',
        'loudness_score_not_applicable': '目標スコア：対象外',
        'loudness_score_tooltip': 'スコアは再測定した直近8件を使用します。100は一致、50はRMS偏差0.60 LU、0は1.20 '
                                  'LU以上です。赤いパネルは、［警告］ボタンで確認できるラウドネス警告が少なくとも1件あることを示します。',
        'loudness_score_value': '目標スコア：{score}/100\n{rating}\nRMS誤差：{deviation}\xa0LU',
        'loudness_score_waiting': '目標スコア：待機中',
        'measurement_unavailable': '測定できません。',
        'mp3_filter': '対応音声 (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'フォルダが選択されていません',
        'no_mp3': '対応音声ファイルが見つかりません。',
        'no_new_source': '有効なフォルダーまたは対応音声ファイルは追加されませんでした。',
        'not_performed': '未実行',
        'open_output_error': '出力先フォルダーを開けませんでした: {error}',
        'operation': '処理',
        'operation_analyze': '解析のみ — ファイル作成なし',
        'operation_analyze_label': '解析のみ',
        'operation_convert': '均一化 — 音声を実際にノーマライズ',
        'operation_convert_label': '音声ノーマライズ',
        'operation_help_text': 'ノーマライズは各ファイルを個別処理して出力を再測定します。ReplayGainはサンプルを変更しません。解析のみは測定と任意のCSVだけを作ります。',
        'operation_replaygain': 'ReplayGain — 再エンコードなし',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'ノーマライズは音声を実際に変更します。ReplayGainはストリームをコピーしてタグを追加します。解析のみは音声を作らず測定します。',
        'option_status_auto_start': '自動',
        'option_status_overwrite': '上書き',
        'option_status_quality_control': '品質',
        'option_status_report': 'CSV',
        'option_status_resume': '再開',
        'option_status_skip_compliant': '適合済',
        'options_tab': 'オプション',
        'output_lufs_log': '出力 {value} LUFS',
        'output_lufs_unavailable': '出力LUFSを取得できません',
        'overwrite': '既存ファイルを上書き',
        'overwrite_tooltip': '保存先に同名のMP3がある場合に置き換えます。元ファイルは上書きされません。',
        'parallel': '並列処理',
        'parallel_adjusted': '自動並列処理 — {active}プロセス、CPU {cpu:.0f}%。',
        'parallel_auto': '自動',
        'parallel_auto_log': '自動、最大 {maximum}',
        'parallel_tooltip': '同時に処理できるファイル数を決めます。\n'
                            '\n'
                            '• 自動は最大4タスクで開始します。CPU測定が利用できる場合は毎秒確認し、使用率70%未満で1タスク増やし、92%を超えると1タスク減らします。\n'
                            '• 自動は検出された論理プロセッサ数を超えず、絶対上限は16タスクです。\n'
                            '• CPU測定が利用できない場合、自動は検出された上限を動的調整なしで直接使用します。\n'
                            '• 数値を指定すると同時タスク数の最大値が固定されます。CPU使用率の目標値ではありません。\n'
                            '\n'
                            'タスク数を増やすと大きな一括処理が速くなる場合がありますが、負荷、温度、ディスク動作が増えます。自動が表示されるまで−を押してください。',
        'paste': '貼り付け',
        'path_left': 'パスの左側を表示',
        'path_right': 'パスの右側を表示',
        'pause': '一時停止',
        'peak': '最大トゥルーピーク',
        'peak_tooltip': '最大トゥルーピークは到達目標ではなく上限です。サンプル間ピークを含む、復元波形の最も高いピークをdBTPで制限し、エンコードや再エンコード後のクリッピングを減らします。\n'
                        '\n'
                        '• -1.0 dBTP — 一般的な納品上限で、出力ピークは最も高くなります。\n'
                        '• -1.5 dBTP — 既定値で、MP3向けの慎重な妥協点です。\n'
                        '• -2.0 dBTP — 再エンコードする可能性がある場合や高いラウドネス目標で役立つ追加の余裕です。\n'
                        '• 0 dBTP — 余裕がなく、MP3には推奨しません。\n'
                        '\n'
                        'より負の値ほど安全ですが、非常にダイナミックな曲がLUFS目標へ正確に到達できない場合があります。',
        'phase_summary': '合計時間の推定配分 — 解析 {analysis}、変換 {conversion}、品質チェック {quality}。',
        'pipeline_enabled': 'トラック処理 — 解析完了後、各変換を直ちに開始します。',
        'pre_measurement': '入力ファイルを測定中…',
        'preset': 'プリセット',
        'preset_dynamic': 'ダイナミックな音楽',
        'preset_library': '音楽ライブラリ — 推奨',
        'preset_streaming': '強めのストリーミング',
        'preset_tooltip': '目標ラウドネス、最大トゥルーピーク、MP3品質をまとめて設定します。手動で変更すると「カスタム」になります。',
        'processing_cancelled': '処理をキャンセルしました。',
        'processing_completed': '処理完了',
        'processing_in_progress': '処理中',
        'processing_paused': '処理を一時停止しました。',
        'processing_resumed': '処理を再開しました。',
        'progress_status': '{status}：{file}',
        'qc_impossible': '警告 — 品質チェックに失敗しました：{error}',
        'qc_log': ' — 品質チェック：{quality}',
        'qc_ok': '成功',
        'qc_warning': '警告 — {detail}',
        'quality': '音声品質',
        'quality_control': '自動品質チェック',
        'quality_control_tooltip': '各出力を再測定します。補正は±0.50 LUを目指し、ラウドネス警告は±0.60 '
                                   'LUを超えた場合だけ表示します。動的MP3は最大3回、WAV／AIFF／FLACはTrue '
                                   'Peakの余裕があれば元ファイルから最大2回再試行します。無効にすると確認、再試行、メーター表示を行いません。',
        'quality_tooltip': '圧縮形式の品質とファイルサイズのバランスを設定します。数値が小さいほど品質とビットレートが高くなります。この設定はLUFS目標値や最大トゥルーピークを変更しません。\n'
                           '\n'
                           '• 0 — 最高品質。細部を保つために推奨します。\n'
                           '• 1〜2 — 非常に高い品質。\n'
                           '• 3〜4 — 品質とサイズのよいバランス。\n'
                           '• 5〜9 — 損失が増える代わりに小さいファイル。\n'
                           '\n'
                           'FLACは値に関係なく可逆です。WAVとAIFFはこの設定を無視し、入力と互換性のあるPCMサンプルレートとビット深度を保ちます。MP3、M4A、OGG、Opusでは、小さい値が入力より高いビットレートを要求し、出力が大きくなる場合があります。大きい値は通常サイズを減らしますが、VBRがよく使われるため同じバイト数は保証されません。非可逆形式を再エンコードしても、すでに失われた情報は戻りません。',
        'ready': '準備完了',
        'recursive_scan': 'フォルダを再帰的に検索中…',
        'remove_all': 'すべて削除',
        'remove_selection': '選択項目を削除',
        'replaygain_help_text': 'ReplayGainは推奨ゲインを計算しREPLAYGAIN_TRACK_GAIN/PEAKを書きます。音声は再エンコードせずコピーされ、対応プレーヤーだけがタグを適用します。物理LUFSとTrue '
                                'Peakは変わりません。',
        'replaygain_levels_log': '音声は変更なし: {before} LUFS · メタデータのReplayGain {gain} dB · 設定目標 {target} LUFS（対応プレーヤーが必要）',
        'replaygain_log_help_text': 'ReplayGainでは、ログに変化していない物理ラウドネス、メタデータへ書き込んだゲイン、設定した目標を表示します。品質管理が有効な場合の「音声は不変、タグを確認済み」は、ラウドネスとピークを入力と比較しタグを再読込したという意味であり、ファイルが物理的に目標値で測定されるという意味ではありません。',
        'replaygain_operation': '再エンコードなしのReplayGain',
        'replaygain_qc_help_text': '品質管理が有効な場合、ReplayGainは出力ファイルを再測定して物理ラウドネスとピークが変わっていないことを確認し、Trackタグも検証します。成功は音声が保持されタグが存在することを示すだけで、目標ラウドネスへの物理的到達を示しません。',
        'replaygain_qc_ok': '成功 — 音声は不変、タグを確認済み',
        'replaygain_tags_missing': 'ReplayGainタグが見つかりません。',
        'replaygain_usefulness_text': 'ReplayGainは、対応プレーヤーで使うライブラリの再生音量を、再エンコードせず可逆的に揃える用途に適しています。すべてのプレーヤーで物理的に目標値を測定できるファイルを納品する場合は、ノーマライズを使用してください。',
        'report_destination': '保存先',
        'report_detail': '詳細',
        'report_error': '警告 — CSVレポートを作成できません：{error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'ゲイン_db',
        'report_input_dbtp': '入力_dbtp',
        'report_input_lufs': '入力_lufs',
        'report_log': 'CSVレポート — {path}',
        'report_mode': 'モード',
        'report_operation': '処理',
        'report_output_dbtp': '出力_dbtp',
        'report_output_lufs': '出力_lufs',
        'report_path': 'レポート：{path}',
        'report_qc': '品質チェック',
        'report_qc_engine': '品質チェック_測定方式',
        'report_seconds': '処理秒数',
        'report_source': '元ファイル',
        'report_status': '状態',
        'report_tooltip': '測定値、時間、警告を含むCSVだけを作成し、診断JSONは追加しません。',
        'resume': '中断後に再開',
        'resume_not_saved': ' 再開ポイントを保存できませんでした：{error}',
        'resume_processing': '再開',
        'resume_tooltip': '同じ設定で完了済みのファイルを認識し、再処理を省きます。',
        'resumed_progress': '再開：{file}',
        'save_dialog_cancel': 'キャンセル',
        'save_dialog_filename': 'ファイル名',
        'save_dialog_filetype': '形式',
        'save_dialog_location': '保存先',
        'save_dialog_overwrite': '置き換える',
        'save_dialog_overwrite_message': '「{file}」は既に存在します。',
        'save_dialog_overwrite_title': 'ファイルを置き換えますか？',
        'save_dialog_parent': '親フォルダ',
        'save_dialog_save': '保存',
        'save_issue_list': 'CSVで保存…',
        'save_issue_list_error': '一覧を保存できませんでした：{error}',
        'save_issue_list_error_title': '保存できません',
        'save_issue_list_title': 'CSV一覧を保存',
        'scan_error': 'エラー — {error}',
        'scanning_folders': 'フォルダーを走査中…',
        'settings': '設定',
        'open_folder': 'フォルダーを開く',
        'show_option_help': 'ヘルプを表示：{option}',
        'silent_copy': '無音または測定不能な音声をコピーしました。',
        'silent_copy_no_replaygain': '無音の音声をReplayGainタグなしでコピーしました。',
        'silent_unmeasurable': '無音または測定不能な音声です。',
        'simulation': 'シミュレーション',
        'skip_compliant': '適合済みファイルを再エンコードしない',
        'skip_compliant_tooltip': '目標±0.10 LU以内かつTrue Peak上限以下のファイルは再エンコードせずコピーします。',
        'skipped_progress': 'スキップ：{file}',
        'source_audio_count': 'ファイル：{count}',
        'source_list_more': '… ほか {count} 件のソースを保持',
        'source_safety': '元のファイルは移動も変更もしません。',
        'source_selection_tooltip': '複数選択：個別項目はCtrlクリック、範囲はShiftクリックで選択します。',
        'sources_added': '{count}件のソースを追加しました。',
        'start': '開始',
        'status_analyzed': '解析済み',
        'status_cancelled': 'キャンセル',
        'status_compliant': '適合',
        'status_error': 'エラー',
        'status_ok': '成功',
        'status_resumed': '再開',
        'status_skipped': 'スキップ',
        'status_warning': '警告',
        'switch_to_dark': 'ダークモード',
        'switch_to_light': 'ライトモード',
        'tagline': '知覚される音量を均一化',
        'target': '目標ラウドネス',
        'target_tooltip': 'ラウドネス目標は、曲全体の積分ラウドネスの目標値をLUFSで表したものです。負の値が小さいほどファイルは大きく聞こえ、-14 LUFSは-16 LUFSより大きくなります。2 '
                          'LUの差は、ピーク制限前ではおよそ2 dBのレベル差に相当します。\n'
                          '\n'
                          '目安：落ち着きとダイナミクスを重視するなら-18 LUFS、全体的なバランスなら-16 LUFS、ストリーミング風の大きめの音量なら-14 '
                          'LUFSです。配信サービス側で別の再生ノーマライズが行われる場合があります。\n'
                          '\n'
                          'この目標だけで曲内部の強弱が平坦になるわけではありません。最大トゥルーピークによりクリッピングなしで目標へ到達できない場合、結果は少し低くなることがあります。',
        'theme_accessible': 'アプリケーションの表示を変更します。選択は保存されます。',
        'total_time': '合計時間：{duration}',
        'track_two_pass': '2パスのトラックノーマライズ。',
        'true_peak_meter_exceeded': '超過 {margin} dB',
        'true_peak_meter_margin': '余裕 {margin} dB',
        'true_peak_meter_title': 'ピーク余裕',
        'true_peak_meter_tooltip': '最後の出力のトゥルーピークを設定上限と比較します。マーカーは最新値、三角は一連の最大ピークを保持します。緑は上限内、橙は0.25 '
                                   'dB以内の超過、赤はそれ以上です。橙の許容値はLUFScaleの品質管理用で、納品規格ではありません。新しい処理ごとにリセットします。',
        'true_peak_meter_waiting': 'dBTP測定待ち',
        'version_changes': '• Windows 10/11 x86-64向けの単一オフラインインストーラーです。\n'
                           '• Python、PySide6/Qt、FFmpeg、コーデック、ガイド、ライセンスを同梱し、インストール時のダウンロードやPowerShellコマンドは不要です。\n'
                           '• セットアップとSHA-256の作成前にloudnormと全エンコーダーを検証します。',
        'version_changes_title': 'バージョン {version} の新機能',
        'version_label': 'バージョン {version}',
        'volume': '音量',
        'volume_loud': '大きめ: -14 LUFS',
        'volume_normal': '標準: -16 LUFS',
        'volume_soft': '小さめ: -18 LUFS',
        'volume_tooltip': 'この設定はラウドネス目標の簡易選択です。システムの再生音量は変更しません。\n'
                          '\n'
                          '• 小さめ：-18 LUFS — 落ち着いた音量で、ダイナミックレンジの余裕が大きく、リミッターが動作しにくい設定です。\n'
                          '• 標準：-16 LUFS — バランスのよい妥協点で、個人ライブラリの出発点に適しています。\n'
                          '• 大きめ：-14 LUFS — Spotifyの「標準」再生目標に近い、存在感のある音量ですが、制限処理が必要になる可能性が高まります。\n'
                          '• カスタム — 別のLUFS目標を直接入力できます。\n'
                          '\n'
                          'これらは実用的な選択肢であり、世界共通の規格ではありません。',
        'warning_list_title': '処理の警告',
        'warnings_button': '警告 ({count})',
        'warnings_button_tooltip': 'ファイル名、パス、詳細を含む警告一覧を開きます。一時停止中または処理後に利用できます。',
        'warnings_dialog_title': '処理の警告'},
 'ko': {'activity_cancelled': '활동: 처리 취소',
        'activity_cancelling': '활동: 취소 중…',
        'activity_completed': '활동: 처리 완료',
        'activity_compliant': '적합: {count}',
        'activity_detected': '활동: {total}개 파일 감지',
        'activity_errors': '오류: {count}',
        'activity_files': '파일: {count}',
        'activity_idle': '활동: 대기',
        'activity_preparing': '활동: 파일 준비 중…',
        'activity_skipped': '재개/건너뜀: {count}',
        'activity_successes': '성공: {count}',
        'activity_warnings': '경고: {count}',
        'adaptive_disabled_log': '적응형 분석 — {sample}회 측정 후 빠른 검사를 중지했습니다(성공 {successes}회, 예상 절감 {percent:+.1f}%).',
        'add_folders': '폴더 추가…',
        'add_mp3': '오디오 파일 추가…',
        'add_replaygain': 'ReplayGain 추가',
        'add_source_files': '오디오 파일 추가',
        'add_source_folder': '원본 폴더 추가',
        'already_completed': '이전 실행에서 이미 완료되었습니다.',
        'already_compliant_badge': '적합',
        'already_compliant_copy': '이미 적합: 오디오를 다시 인코딩하지 않고 그대로 복사했습니다.',
        'already_compliant_log': '이미 적합, 재인코딩 없음',
        'analysis_cache_summary': '분석 캐시 — 측정 {hits}건을 재사용했습니다.',
        'analysis_impossible': '분석 실패: {error}',
        'analysis_measurement_progress': '분석 {current}/{total} — {file} — {value}',
        'analysis_method': '분석 방식',
        'analysis_method_adaptive': '적응형 — 효과가 없으면 중지',
        'analysis_method_fast': '빠른 방식 — 실험적',
        'analysis_method_historical': '전체 측정 — 기준 방식',
        'analysis_method_tooltip': '안정 버전은 기준 자료에서 검증된 전체 길이 분석 방식을 자동으로 사용합니다. 빠른 분석과 적응형 분석은 제공하지 않습니다.',
        'analysis_progress_help_text': '분석 전용에서는 각 측정이 끝날 때마다 처리 전 그래프, 로그, 진행률이 파일별로 갱신되고 처리 후는 움직이지 않습니다.',
        'analyze': '분석',
        'analyze_only_fresh_help_text': '분석만은 실행마다 FFmpeg로 각 원본 전체를 다시 측정합니다. 처리 전 그래프와 진행률은 파일별로 움직이며 출력과 출력 QC는 '
                                        '없습니다.',
        'analyze_operation': '분석/시뮬레이션',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': '오디오 스트림을 재인코딩 없이 복사하고 ReplayGain 태그를 추가했습니다.',
        'audio_tab': '오디오',
        'auto_start': '놓기 또는 붙여넣기 후 자동 시작',
        'auto_start_tooltip': '대상이 준비된 경우 소스를 추가하자마자 처리를 시작합니다.',
        'cancel': '취소',
        'cancelled_summary': '취소됨 — 성공 {success}, 오류 {failed}, 재개/건너뜀 {skipped}, 경고 {warnings}, 적합 {compliant} — '
                             '{duration}.',
        'cancelling': '취소 중…',
        'choose': '선택…',
        'choose_output': '대상 폴더 선택',
        'clipboard': '클립보드',
        'clipboard_empty': '클립보드에 지원되는 폴더나 오디오 파일 경로가 없습니다.',
        'close_button': '닫기',
        'close_question': '처리를 취소하고 응용 프로그램을 닫으시겠습니까?',
        'completed_dialog_summary': '상태: 완료\n'
                                    '파일: {files}\n'
                                    '성공: {success}\n'
                                    '오류: {failed}\n'
                                    '재개 또는 건너뜀: {skipped}\n'
                                    '경고: {warnings}\n'
                                    '적합: {compliant}\n'
                                    '총 시간: {duration}',
        'completed_summary': '완료 — 성공 {success}, 오류 {failed}, 재개/건너뜀 {skipped}, 경고 {warnings}, 적합 {compliant} — '
                             '{duration}.',
        'completed_with_errors': '경고와 함께 처리 완료',
        'convert': '정규화',
        'convert_operation': '오디오 정규화',
        'cpu_tooltip': '처리 중 시스템의 전체 CPU 사용량입니다.',
        'cpu_usage': 'CPU',
        'create_report': 'CSV 보고서 만들기',
        'csv_file_filter': 'CSV 파일 (*.csv)',
        'custom': '사용자 지정',
        'decrease_value': '값 줄이기',
        'description': '원본을 바꾸지 않고 파일별로 체감 음량을 균일화합니다.',
        'destination': '대상',
        'destination_error': '오류 — 대상 위치를 사용할 수 없습니다: {error}',
        'destination_path_tooltip': '경로는 선택하고 복사할 수 있지만 수정할 수 없습니다.',
        'destination_required_start': '처리를 시작하기 전에 대상 폴더를 선택하세요.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus · 하위 폴더 지원',
        'drop_title': '폴더나 오디오 파일을 여기에 놓으세요',
        'elapsed_time': '경과 시간: {duration}',
        'error_list_title': '처리 오류',
        'errors_button': '오류 ({count})',
        'errors_button_tooltip': '파일 이름, 경로와 상세 정보가 있는 오류 목록을 엽니다. 일시 정지 중이거나 처리 후 사용할 수 있습니다.',
        'errors_dialog_title': '처리 오류',
        'estimated_result': '예상 결과이며 파일을 만들지 않았습니다.',
        'estimated_total_calculating': '예상 총 시간: 계산 중…',
        'estimated_total_time': '예상 총 시간: {duration}',
        'estimated_total_time_with_day_finish': '예상 총 시간: {duration} — {days}일 {time}',
        'estimated_total_time_with_finish': '예상 총 시간: {duration} — 약 {time}에 완료',
        'estimated_total_unavailable': '예상 총 시간: 알 수 없음',
        'ffmpeg_download_button': 'FFmpeg 공식 웹사이트 열기',
        'ffmpeg_error_no_detail': '세부 정보가 없는 FFmpeg 오류입니다.',
        'ffmpeg_execution_error': 'FFmpeg를 실행할 수 없습니다: {error}',
        'ffmpeg_incompatible': '호환되지 않는 FFmpeg',
        'ffmpeg_missing': 'FFmpeg를 찾을 수 없음',
        'ffmpeg_missing_encoders': '이 FFmpeg 빌드에는 필요한 오디오 인코더가 모두 포함되어 있지 않습니다: {encoders}.',
        'ffmpeg_missing_message': 'FFmpeg를 설치하여 PATH에서 사용할 수 있게 하거나 프로그램 옆에 배치해야 합니다.',
        'ffmpeg_no_lame': '이 FFmpeg 빌드에는 libmp3lame MP3 인코더가 없습니다.',
        'ffmpeg_no_loudnorm': '이 FFmpeg 빌드에는 loudnorm 필터가 없습니다.',
        'ffmpeg_not_responding': 'FFmpeg가 올바르게 응답하지 않습니다.',
        'file_exists': '파일이 이미 존재합니다.',
        'files_found': '오디오 파일 {total}개 발견 — {operation} — 병렬 처리 {parallel}개.',
        'finalization_completed': '마무리 완료: {duration}.',
        'finalizing': '마무리 중 — 보고서, 분석 캐시 및 재개 데이터…',
        'folder': '폴더',
        'folder_unavailable': '폴더를 사용할 수 없음',
        'guide_analysis_method': 'LUFScale는 기준 자료에서 검증된 유일한 방식인 전체 길이 이력 측정을 자동으로 사용합니다.',
        'guide_analyze_prediction_body': '분석만은 결과를 예상할 수 있지만 오디오와 출력 QC를 만들지 않습니다.',
        'guide_analyze_prediction_title': '출력 없는 예상',
        'guide_build_body': 'Windows 10 1809 이상 또는 Windows 11 x86-64에서:\n'
                            '\n'
                            '1. “LUFScale-2.1.12-Setup-x64.exe”와 SHA-256 파일을 다운로드합니다.\n'
                            '2. SHA-256을 확인한 뒤 설치 파일을 두 번 클릭합니다.\n'
                            '3. GNU GPL 라이선스를 읽고 동의한 다음 마법사를 따릅니다.\n'
                            '4. 시작 메뉴에서 LUFScale를 실행합니다.\n'
                            '\n'
                            '앱, Python, PySide6/Qt, FFmpeg, 코덱, 안내서와 라이선스가 이미 포함되어 있습니다. 설치 과정에서 다운로드하거나 PowerShell 명령을 실행할 필요가 없으며 Windows 제거 프로그램이 자동으로 만들어집니다.\n'
                            '\n'
                            '배포판은 서명되지 않았습니다. 파일과 체크섬을 확인한 뒤 SmartScreen이 확인을 요구할 수 있습니다.',
        'guide_build_title': 'Windows x86-64에 LUFScale 설치',
        'guide_estimated_total_help': '예상 총 시간: 12분 - 약 14:30에 완료됩니다. ‘12분’은 예상 총 소요 시간이고 ‘14:30’은 예상 종료 시각입니다. 자정을 '
                                      '넘으면 시각 앞에 날짜 수가 자동으로 추가됩니다(예: ‘2일. 14:30’).',
        'guide_file_processing_body': '각 파일의 측정값과 개별 게인으로 True Peak 한도 안에서 목표 LUFS에 접근합니다.',
        'guide_file_processing_title': '파일별 처리',
        'guide_help_tooltip': '선택한 언어의 전체 PDF 안내서를 엽니다.',
        'guide_level_mode_body': '트랙(권장)은 각 파일을 목표에 맞춥니다. 앨범은 고급 특수 모드로 공통 게인을 적용해 곡 간 대비를 유지합니다. 순서대로 듣는 작품에는 앨범, '
                                 '셔플이나 파일별 일정한 음량에는 트랙을 사용합니다.',
        'guide_license_body': 'LUFScale는 GNU GPL-3.0-or-later로 배포되는 자유 소프트웨어입니다. 라이선스 조건에 따라 사용·연구·수정·재배포할 수 있습니다. 소스 '
                              '코드, 고지, 타사 라이선스가 배포본에 포함됩니다. 소프트웨어는 보증 없이 제공됩니다.',
        'guide_license_feature': '• GNU GPL-3.0-or-later 자유 소프트웨어로, 라이선스에 따라 사용·연구·수정·재배포할 수 있습니다.\n'
                                 '• Python, Qt, FFmpeg가 포함된 Windows x86-64 오프라인 설치 프로그램입니다. Windows 11을 권장합니다. Windows 10 '
                                 '1809 이상도 호환 대상이지만 Microsoft 표준 지원은 종료되었습니다.',
        'guide_license_title': '자유 소프트웨어와 재배포',
        'guide_log_legend_cancelled': '처리를 사용자가 중단했습니다. 오류가 아닙니다.',
        'guide_log_legend_compliant': '오디오를 변경하지 않고 복사했습니다. 원본이 이미 목표와 피크 한도를 충족했습니다.',
        'guide_log_legend_error': '해당 파일의 처리를 완료하지 못했습니다.',
        'guide_log_legend_success': '감지된 이상 없이 처리가 완료되었습니다.',
        'guide_log_legend_warning': '출력은 생성되었지만 측정값 하나가 허용 범위를 벗어났습니다.',
        'guide_missing_message': 'PDF 안내서를 찾을 수 없습니다: {path}',
        'guide_missing_title': '안내서 사용 불가',
        'guide_open_error': 'PDF 안내서를 열 수 없습니다: {path}',
        'guide_quality_priority_body': 'LUFScale는 파일의 라우드니스를 측정하고, 정규화 작업에서는 트루 피크를 제어하면서 체감 음량을 LUFS 목표로 실제 조정합니다. 각 '
                                       '원본의 전체 길이를 분석한 뒤 출력을 다시 측정하고 검증합니다. 결과는 태그나 호환 플레이어에 의존하지 않으며, 파일 간 음량이 더 일관되고 '
                                       '편차는 표시되며 원본은 변경되지 않습니다.',
        'guide_quality_priority_title': 'LUFScale의 기능',
        'help_button': '도움말',
        'help_overview': '• MP3, FLAC, WAV, AIFF, M4A, OGG, Opus의 균일화, ReplayGain 또는 분석.\n'
                         '• 각 파일을 따로 측정하고 선택한 목표로 처리합니다.\n'
                         '• 폴더 구조, 지원 메타데이터와 표지를 보존하며 원본은 바뀌지 않습니다.\n'
                         '• 병렬 처리, 캐시, 재개, QC, CSV, 진행률, CPU, LUFS 기록.\n'
                         '• 12개 언어의 화면과 PDF 안내서.',
        'help_title': '주요 기능',
        'increase_value': '값 늘리기',
        'input_lufs_log': '입력 {value} LUFS',
        'interface_ffmpeg_message': '내장 FFmpeg 오디오 엔진이 없거나 사용할 수 없습니다. 전체 배포 압축 파일에서 LUFScale을 다시 설치하십시오.',
        'internal_error': '내부 오류: {error}',
        'interrupted': '처리가 중단되었습니다.',
        'invalid_location': '잘못된 위치',
        'issue_detail_column': '세부 정보',
        'issue_file_column': '파일',
        'issue_path_column': '경로',
        'language': '언어',
        'language_tooltip': '인터페이스, 메시지와 이후 CSV 보고서의 언어를 즉시 바꿉니다.',
        'log_help_text': '각 줄은 파일 또는 일반 처리 단계를 설명합니다.\n'
                         '\n'
                         '• 성공한 줄은 파일 이름으로 바로 시작하며 ‘성공’을 반복하지 않습니다.\n'
                         '• 적합, 재개, 건너뜀, 취소, 오류는 유용한 정보를 더할 때 표시됩니다.\n'
                         '• 레벨은 입력 → 다시 측정한 출력, 이어서 품질 관리 결과를 표시합니다.\n'
                         '• 경고와 오류는 파일 이름, 경로, 세부 정보가 있는 별도 목록을 엽니다. 일시 정지 중이나 처리 후 사용할 수 있고 각 목록을 저장할 수 있습니다.\n'
                         '\n'
                         '색상: 녹색=성공, 주황=경고, 빨강=완료되지 않은 파일, 청보라=재개, 회색=정보·건너뜀·취소.\n'
                         '\n'
                         'QC 경고—라우드니스는 다시 측정한 출력이 예상값에서 ±0.60 LU보다 더 벗어났음을 뜻합니다. 더 음수인 값은 더 작고, 덜 음수인 값은 더 큽니다. 편차는 '
                         '절댓값으로, -14.00 대신 -14.69이면 0.69 LU입니다. 파일은 생성되며 변환 실패가 아닙니다. 듣기에 괜찮다면 조치가 필수는 아닙니다. 엄격한 목표가 '
                         '필요하면 세부 정보와 CSV를 확인하고 목표 및 True Peak 한계를 점검한 뒤 다시 처리하십시오. 이 메시지만으로 한계, 인코더 또는 보정 한계 중 원인을 '
                         '확정할 수 없습니다.\n'
                         '\n'
                         'QC 경고—피크는 다시 측정한 True Peak가 선택한 한계를 0.25 dB 넘었음을 뜻합니다. 파일은 생성됩니다. 계속되면 더 낮은 LUFS 목표나 -2.0 '
                         'dBTP 같은 더 안전한 피크 한계를 선택해 다시 처리하십시오.\n'
                         '\n'
                         '누적 시간은 모든 병렬 작업 시간을 합산합니다. 총 시간은 실제 경과 시간입니다.',
        'log_placeholder': '처리 기록이 여기에 표시됩니다.',
        'log_title': '처리 기록',
        'loudness_comparison_after': '처리 후',
        'loudness_comparison_analysis_only': '분석 전용 모드에서는 출력 없음',
        'loudness_comparison_before': '처리 전',
        'loudness_comparison_help_text': '파일마다 오른쪽에 점이 추가됩니다. 이전은 항상 측정한 원본입니다. 정규화의 이후는 실제로 다시 측정한 출력입니다. ReplayGain의 '
                                         '두 번째 점선 그래프는 원본 음량과 저장된 Track Gain으로 재생을 예상합니다. ≈ 기호와 호환 플레이어 안내는 전달 파일의 물리 '
                                         '측정이 아님을 뜻합니다. 비호환 플레이어는 원래 음량을 유지하며, 호환 플레이어도 프리앰프나 클리핑 방지에 따라 결과가 달라질 수 '
                                         '있습니다. 두 그래프는 동일한 고정 ±6 LU 눈금을 유지합니다. 분석 전용에는 이후 출력이 없습니다.',
        'loudness_comparison_increased': '차이 {value} LU 증가',
        'loudness_comparison_needs_qc': '비교하려면 품질 관리를 켜세요',
        'loudness_comparison_no_after': '이 작업에는 처리 후 곡선이 없습니다',
        'loudness_comparison_not_applicable': '이 작업에서는 비교할 수 없습니다',
        'loudness_comparison_reached': '목표 도달 · 차이 {value} LU',
        'loudness_comparison_reduced': '차이 {value} LU 감소',
        'loudness_comparison_replaygain_after': 'RG 재생 예상',
        'loudness_comparison_replaygain_note': '호환 플레이어 · 오디오 불변',
        'loudness_comparison_scale': '보기 ±{scale} LU · QC 허용 ±{tolerance} LU',
        'loudness_comparison_target': '목표 {value} LUFS',
        'loudness_comparison_title': '라우드니스 변화',
        'loudness_comparison_tooltip': '이전은 물리적 음량입니다. ReplayGain의 두 번째 그래프는 저장된 게인으로 호환 재생을 예상합니다.',
        'loudness_comparison_unchanged': '차이 변화 없음',
        'loudness_comparison_waiting': '처리된 파일을 기다리는 중',
        'loudness_meter_estimated': '예상값',
        'loudness_meter_help_text': '미터는 최근 다시 측정한 출력과 설정 목표를 비교합니다. 값과 곡선은 파일마다 업데이트되며 순간 재생 레벨이 아니라 파일 전체의 통합 '
                                    '라우드니스입니다. 자동 품질 관리가 꺼져 있거나 출력이 없는 분석 전용 작업에서는 비활성 상태가 정상입니다.',
        'loudness_meter_measured': '측정값',
        'loudness_meter_no_file': '분석 대기 중',
        'loudness_meter_title': '라우드니스 미터',
        'loudness_meter_tooltip': '빨간색은 목표이며 파란색은 최근 출력에서 실제로 다시 측정한 라우드니스입니다.',
        'loudness_meter_waiting': '오디오 파일 대기 중',
        'loudness_score_acceptable': '허용 가능',
        'loudness_score_check': '경고 보기',
        'loudness_score_excellent': '매우 좋음',
        'loudness_score_needs_qc': '목표 점수: 품질 관리 활성화 필요',
        'loudness_score_not_applicable': '목표 점수: 해당 없음',
        'loudness_score_tooltip': '점수는 실제로 다시 측정한 최근 출력 8개를 사용합니다. 100은 정확히 일치, 50은 RMS 오차 0.60 LU, 0은 1.20 LU 이상입니다. '
                                  '빨간 패널은 경고 버튼에서 확인할 라우드니스 경고가 있음을 뜻합니다.',
        'loudness_score_waiting': '목표 점수: 대기 중',
        'measurement_unavailable': '측정 불가',
        'mp3_filter': '지원 오디오 (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': '선택한 폴더 없음',
        'no_mp3': '지원되는 오디오 파일이 없습니다.',
        'no_new_source': '새 오디오 소스가 없습니다.',
        'not_performed': '수행하지 않음',
        'open_output_error': '대상 폴더를 열 수 없습니다: {error}',
        'operation': '작업',
        'operation_analyze': '분석만 — 파일 생성 안 함',
        'operation_analyze_label': '분석만 — 파일 생성 없이 시뮬레이션',
        'operation_convert': '균일화 — 오디오를 실제로 정규화',
        'operation_convert_label': '정규화 — 오디오를 실제로 조정',
        'operation_help_text': '정규화는 각 파일을 별도로 처리하고 True Peak 상한 아래에서 LUFS 목표를 맞춘 뒤 출력을 다시 측정합니다. ReplayGain은 오디오 샘플을 '
                               '바꾸지 않습니다. 분석만은 측정과 요청 시 CSV 보고서를 만들지만 오디오 파일은 만들지 않습니다.',
        'operation_replaygain': 'ReplayGain — 오디오 재인코딩 없음',
        'operation_replaygain_label': 'ReplayGain — 오디오 재인코딩 없음',
        'operation_tooltip': '균일화는 오디오를 실제로 바꿉니다. ReplayGain은 스트림을 복사하고 태그를 추가합니다. 분석만은 오디오를 만들지 않습니다.',
        'option_status_auto_start': '자동',
        'option_status_overwrite': '덮어',
        'option_status_quality_control': '품질',
        'option_status_report': 'CSV',
        'option_status_resume': '재개',
        'option_status_skip_compliant': '건너',
        'options_tab': '옵션',
        'output_lufs_unavailable': '출력 LUFS를 사용할 수 없음',
        'overwrite': '기존 파일 덮어쓰기',
        'overwrite_tooltip': '대상에 있는 기존 파일만 바꾸며 원본은 덮어쓰지 않습니다.',
        'parallel': '병렬 처리',
        'parallel_adjusted': '자동 병렬 처리 — {active}개 프로세스, CPU {cpu:.0f}%.',
        'parallel_auto': '자동',
        'parallel_auto_log': '자동, 최대 {maximum}',
        'parallel_tooltip': '동시에 처리할 수 있는 파일 수를 정합니다.\n'
                            '\n'
                            '• 자동은 최대 4개 작업으로 시작합니다. CPU 측정이 가능하면 매초 확인하여 사용률이 70% 아래일 때 작업 하나를 추가하고 92% 위일 때 하나를 '
                            '줄입니다.\n'
                            '• 자동은 감지된 논리 프로세서 수를 넘지 않으며 절대 상한은 16개 작업입니다.\n'
                            '• CPU 측정이 불가능하면 동적 조정 없이 감지된 상한을 바로 사용합니다.\n'
                            '• 숫자 값은 동시 작업의 최대 수이며 CPU 사용률 목표가 아닙니다.\n'
                            '\n'
                            '작업을 늘리면 큰 묶음이 빨라질 수 있지만 부하, 온도와 디스크 접근이 증가합니다. 자동이 나타날 때까지 −를 누르십시오.',
        'paste': '붙여넣기',
        'path_left': '경로의 왼쪽 부분 표시',
        'path_right': '경로의 오른쪽 부분 표시',
        'pause': '일시 정지',
        'peak': '최대 트루 피크',
        'peak_tooltip': '최대 트루 피크는 도달할 음량이 아니라 상한입니다. 샘플 사이의 피크를 포함해 복원된 파형의 가장 높은 피크를 dBTP로 제한하여 인코딩 또는 트랜스코딩 뒤 클리핑 '
                        '위험을 줄입니다.\n'
                        '\n'
                        '• -1.0 dBTP — 일반적인 배포 상한이며 출력 피크가 가장 높습니다.\n'
                        '• -1.5 dBTP — 기본값이며 MP3에 신중한 절충안입니다.\n'
                        '• -2.0 dBTP — 재인코딩될 파일이나 높은 라우드니스 목표에 유용한 추가 여유입니다.\n'
                        '• 0 dBTP — 여유가 없으므로 MP3에는 권장하지 않습니다.\n'
                        '\n'
                        '더 음수인 값은 보호를 늘리지만 매우 다이내믹한 트랙이 LUFS 목표에 정확히 도달하지 못하게 할 수 있습니다.',
        'phase_summary': '예상 총 시간 배분 — 분석 {analysis}, 변환 {conversion}, 품질 관리 {quality}.',
        'pipeline_enabled': '트랙 파이프라인 — 분석이 끝나는 즉시 각 변환을 시작합니다.',
        'pre_measurement': '입력 파일 측정 중…',
        'preset': '프리셋',
        'preset_dynamic': '다이내믹 음악',
        'preset_library': '음악 보관함 — 권장',
        'preset_streaming': '강한 스트리밍',
        'preset_tooltip': '라우드니스 목표, 최대 트루 피크와 오디오 품질을 일관된 조합으로 한 번에 적용합니다. 값을 수동으로 바꾸면 사용자 지정을 선택합니다.',
        'processing_cancelled': '처리가 취소되었습니다.',
        'processing_completed': '처리 완료',
        'processing_in_progress': '처리 중…',
        'processing_paused': '처리가 일시 정지되었습니다.',
        'processing_resumed': '처리를 계속합니다.',
        'qc_impossible': '품질 관리를 수행할 수 없음: {error}',
        'qc_log': ' — 품질 관리: {quality}',
        'qc_ok': '품질 관리: 적합',
        'qc_warning': '품질 관리 경고 — {detail}',
        'quality': '오디오 품질',
        'quality_control': '자동 품질 관리',
        'quality_control_tooltip': '각 출력을 다시 측정합니다. 보정은 계속 ±0.50 LU를 목표로 하며 라우드니스 경고는 ±0.60 LU를 넘을 때만 표시됩니다. 다이내믹 MP3는 '
                                   '최대 3회의 보정 시도를 유지합니다. WAV, AIFF, FLAC은 True Peak 여유가 허용하면 원본에서 최대 2회 다시 시도할 수 있습니다. '
                                   '이 옵션을 끄면 검증, 재시도와 미터 활동이 없어집니다.',
        'quality_tooltip': '압축 형식의 품질과 크기 사이의 균형을 정합니다. 숫자가 낮을수록 품질과 비트레이트가 높습니다. 이 설정은 LUFS 목표나 최대 트루 피크를 바꾸지 않습니다.\n'
                           '\n'
                           '• 0 — 세부 보존에 권장하는 최고 품질.\n'
                           '• 1~2 — 매우 높은 품질.\n'
                           '• 3~4 — 품질/크기의 좋은 균형.\n'
                           '• 5~9 — 손실이 더 큰 작은 파일.\n'
                           '\n'
                           'FLAC은 값과 관계없이 무손실입니다. WAV와 AIFF는 이 설정을 무시하고 원본과 호환되는 PCM 샘플레이트와 비트 깊이를 유지합니다. MP3, M4A, '
                           'OGG, Opus에서 낮은 값은 원본보다 높은 비트레이트를 요구하여 출력이 더 커질 수 있습니다. 높은 값은 보통 크기를 줄이지만 VBR을 자주 사용하므로 같은 '
                           '바이트 수를 보장하지 않습니다. 손실 형식을 재인코딩해도 이미 잃은 정보는 복원되지 않습니다.',
        'ready': '준비',
        'recursive_scan': '폴더를 재귀적으로 검색 중…',
        'remove_all': '모두 제거',
        'remove_selection': '선택 항목 제거',
        'replaygain_help_text': 'ReplayGain은 게인을 계산해 REPLAYGAIN_TRACK_GAIN/PEAK를 기록합니다. 오디오는 재인코딩 없이 복사되며(-c:a copy), '
                                '호환 플레이어만 태그를 적용합니다. 물리 LUFS와 True Peak는 바뀌지 않습니다.',
        'replaygain_levels_log': '오디오 변경 없음: {before} LUFS · 메타데이터 ReplayGain {gain} dB · 설정 목표 {target} LUFS(호환 플레이어 '
                                 '필요)',
        'replaygain_log_help_text': 'ReplayGain에서 로그는 변하지 않은 물리적 라우드니스, 메타데이터에 쓴 게인과 설정 목표를 표시합니다. 품질 관리가 켜진 상태의 ‘오디오 '
                                    '유지 및 태그 확인’은 라우드니스와 피크를 원본과 비교하고 태그를 다시 읽었다는 뜻이며 파일이 물리적으로 목표값에서 측정된다는 뜻은 아닙니다.',
        'replaygain_operation': '재인코딩 없는 ReplayGain',
        'replaygain_qc_help_text': '품질 관리가 켜지면 ReplayGain은 전달 파일을 다시 측정해 물리적 라우드니스와 피크가 그대로인지 확인하고 Track 태그를 검사합니다. '
                                   '성공은 오디오 보존과 태그 존재를 확인할 뿐 물리적으로 목표에 도달했다는 뜻은 아닙니다.',
        'replaygain_qc_ok': '성공 — 오디오 유지 및 태그 확인',
        'replaygain_tags_missing': 'ReplayGain 태그를 찾지 못했습니다.',
        'replaygain_usefulness_text': 'ReplayGain은 호환 플레이어에서 사용하는 라이브러리의 재생 음량을 재인코딩 없이 가역적으로 맞출 때 유용합니다. 모든 플레이어에서 '
                                      '물리적으로 목표값이 측정되는 파일을 제공하려면 정규화를 사용하십시오.',
        'report_destination': '대상',
        'report_detail': '상세',
        'report_error': '경고 — CSV 보고서를 만들 수 없습니다: {error}',
        'report_filename_prefix': 'LUFScale_보고서',
        'report_gain': '게인_dB',
        'report_input_dbtp': '입력_dBTP',
        'report_input_lufs': '입력_LUFS',
        'report_log': 'CSV 보고서 — {path}',
        'report_operation': '작업',
        'report_output_dbtp': '출력_dBTP',
        'report_output_lufs': '출력_LUFS',
        'report_path': '보고서: {path}',
        'report_qc': '품질_관리',
        'report_qc_engine': '품질_관리_엔진',
        'report_seconds': '경과_초',
        'report_source': '원본',
        'report_status': '상태',
        'report_tooltip': '측정값, 시간, 경고가 담긴 CSV만 만들고 진단 JSON은 추가하지 않습니다.',
        'resume': '중단 후 계속',
        'resume_not_saved': ' 재개 지점을 저장하지 못했습니다: {error}',
        'resume_processing': '계속',
        'resume_tooltip': '같은 설정으로 완료한 파일을 찾아 다시 처리하지 않습니다.',
        'save_dialog_cancel': '취소',
        'save_dialog_filename': '파일 이름',
        'save_dialog_filetype': '형식',
        'save_dialog_location': '폴더',
        'save_dialog_overwrite': '바꾸기',
        'save_dialog_overwrite_message': '“{file}” 파일이 이미 있습니다.',
        'save_dialog_overwrite_title': '파일을 바꾸시겠습니까?',
        'save_dialog_parent': '상위 폴더',
        'save_dialog_save': '저장',
        'save_issue_list': 'CSV로 저장…',
        'save_issue_list_error': '목록을 저장할 수 없습니다: {error}',
        'save_issue_list_error_title': '저장할 수 없음',
        'save_issue_list_title': 'CSV 목록 저장',
        'scan_error': '오류 — {error}',
        'scanning_folders': '폴더 검색 중…',
        'settings': '설정',
        'open_folder': '폴더 열기',
        'show_option_help': '도움말 표시: {option}',
        'silent_copy': '무음이거나 측정할 수 없는 오디오를 복사했습니다.',
        'silent_copy_no_replaygain': '무음 오디오를 ReplayGain 태그 없이 복사했습니다.',
        'silent_unmeasurable': '무음이거나 측정할 수 없는 오디오입니다.',
        'simulation': '시뮬레이션',
        'skip_compliant': '이미 적합한 파일 건너뛰기',
        'skip_compliant_tooltip': '목표 ±0.10 LU 이내이고 True Peak 한도 이하인 파일은 재인코딩 없이 복사됩니다.',
        'source_audio_count': '파일: {count}',
        'source_list_more': '… 원본 {count}개 더 유지',
        'source_safety': '원본 파일은 이동하거나 수정하지 않습니다.',
        'source_selection_tooltip': '여러 항목 선택: 개별 항목은 Ctrl-클릭, 범위는 Shift-클릭을 사용하세요.',
        'sources_added': '{count}개 소스를 추가했습니다.',
        'start': '시작',
        'status_analyzed': '분석됨',
        'status_cancelled': '취소됨',
        'status_compliant': '적합',
        'status_error': '오류',
        'status_ok': '성공',
        'status_resumed': '재개됨',
        'status_skipped': '건너뜀',
        'status_warning': '경고',
        'switch_to_dark': '어두운 모드',
        'switch_to_light': '밝은 모드',
        'tagline': '원본을 보존하면서 지각되는 음량을 균일하게 맞춥니다.',
        'target': '라우드니스 목표',
        'target_tooltip': '라우드니스 목표는 트랙 전체에 대해 원하는 통합 라우드니스이며 LUFS로 표시합니다. 덜 음수인 값이 더 크게 들립니다. -14 LUFS는 -16 LUFS보다 '
                          '큽니다. 피크 제한 전 2 LU 차이는 약 2 dB의 레벨 차이입니다.\n'
                          '\n'
                          '참고: 더 차분하고 다이내믹한 결과는 -18 LUFS, 일반적인 균형은 -16 LUFS, 스트리밍 스타일의 큰 결과는 -14 LUFS입니다. 플랫폼은 자체 재생 '
                          '정규화를 적용할 수 있습니다.\n'
                          '\n'
                          '이 목표만으로 트랙 내부의 다이내믹이 평탄해지지는 않습니다. 최대 트루 피크 때문에 클리핑 없이 목표에 도달할 수 없으면 결과가 조금 더 낮을 수 있습니다.',
        'theme_accessible': '밝은 모드와 어두운 모드 전환',
        'total_time': '총 시간: {duration}',
        'track_two_pass': '2패스 트랙 정규화.',
        'true_peak_meter_title': '트루 피크 여유',
        'true_peak_meter_tooltip': '최근 출력의 트루 피크와 지정 상한을 비교합니다. 표식은 최근 값, 삼각형은 배치의 최고 피크를 유지합니다. 초록색은 상한 충족, 주황색은 최대 '
                                   '0.25 dB 초과, 빨간색은 그보다 큰 초과를 뜻합니다. 주황색 허용치는 LUFScale 품질 관리용이며 배포 표준이 아닙니다. 그래프는 배치마다 '
                                   '초기화됩니다.',
        'true_peak_meter_waiting': 'dBTP 측정 대기 중',
        'version_changes': '• Windows 10/11 x86-64용 단일 오프라인 설치 프로그램입니다.\n'
                           '• Python, PySide6/Qt, FFmpeg, 코덱, 안내서와 라이선스가 포함되며 설치 중 다운로드나 PowerShell 명령이 필요 없습니다.\n'
                           '• 설치 파일과 SHA-256을 만들기 전에 loudnorm과 모든 인코더를 검증합니다.',
        'version_changes_title': '버전 {version}의 새로운 기능',
        'version_label': '버전 {version}',
        'volume': '음량',
        'volume_loud': '크게: -14 LUFS',
        'volume_normal': '보통: -16 LUFS',
        'volume_soft': '부드럽게: -18 LUFS',
        'volume_tooltip': '이 설정은 라우드니스 목표의 바로가기이며 시스템의 재생 음량을 바꾸지 않습니다.\n'
                          '\n'
                          '• 부드럽게: -18 LUFS — 더 차분하고 다이내믹 여유가 크며 리미터가 작동할 가능성이 낮습니다.\n'
                          '• 보통: -16 LUFS — 균형 잡힌 절충안으로 개인 라이브러리의 시작점에 적합합니다.\n'
                          '• 크게: -14 LUFS — Spotify 보통 재생 목표에 가까운 더 선명한 음량이지만 제한 처리가 더 필요할 수 있습니다.\n'
                          '• 사용자 지정 — 다른 LUFS 목표를 직접 입력합니다.\n'
                          '\n'
                          '이 값은 실용적인 선택이며 보편적 표준은 아닙니다.',
        'warning_list_title': '처리 경고',
        'warnings_button': '경고 ({count})',
        'warnings_button_tooltip': '파일 이름, 경로와 상세 정보가 있는 경고 목록을 엽니다. 일시 정지 중이거나 처리 후 사용할 수 있습니다.',
        'warnings_dialog_title': '처리 경고'},
 'pt': {'activity_cancelled': 'Atividade: processamento cancelado',
        'activity_cancelling': 'Atividade: a cancelar…',
        'activity_completed': 'Atividade: processamento concluído',
        'activity_compliant': 'Conformes: {count}',
        'activity_detected': 'Atividade: {total} ficheiro(s) detetado(s)',
        'activity_errors': 'Erros: {count}',
        'activity_files': 'Ficheiros: {count}',
        'activity_idle': 'Atividade: em espera',
        'activity_preparing': 'Atividade: a preparar ficheiros…',
        'activity_progress': '{total} ficheiros • concluídos {success} • alertas {warnings} • erros {failed} • '
                             'retomados/ignorados {skipped} • conformes {compliant}',
        'activity_skipped': 'Retomados/ignorados: {count}',
        'activity_successes': 'Concluídos: {count}',
        'activity_warnings': 'Alertas: {count}',
        'adaptive_disabled_log': 'Análise adaptativa — sondas rápidas paradas após {sample} medições ({successes} '
                                 'sucessos, poupança estimada {percent:+.1f}%).',
        'add_folders': 'Adicionar pastas…',
        'add_mp3': 'Adicionar ficheiros de áudio…',
        'add_replaygain': 'Adicionar ReplayGain',
        'add_source_files': 'Adicionar ficheiros de áudio',
        'add_source_folder': 'Adicionar uma pasta de origem',
        'already_completed': 'Já concluído durante uma execução anterior.',
        'already_compliant_badge': 'CONFORME',
        'already_compliant_copy': 'Já conforme: cópia idêntica sem recodificação de áudio.',
        'already_compliant_log': 'já conforme, sem recodificação',
        'analysis_cache_summary': 'Cache de análise — {hits} medição(ões) reutilizada(s).',
        'analysis_impossible': 'Falha na análise: {error}',
        'analysis_measurement_progress': 'Análise {current}/{total} — {file} — {value}',
        'analysis_method': 'Método de análise',
        'analysis_method_adaptive': 'Adaptativo — para se não compensar',
        'analysis_method_fast': 'Rápido — experimental',
        'analysis_method_historical': 'Histórico — referência',
        'analysis_method_log': 'Método de análise — {method}.',
        'analysis_method_tooltip': 'A versão estável usa automaticamente a medição histórica completa, o único método '
                                   'validado no corpus de referência. Rápido e Adaptativo deixaram de ser propostos.',
        'analysis_progress': 'Análise {current}/{total}: {file}',
        'analysis_progress_help_text': 'Em Apenas analisar, o gráfico Antes, o registo e a barra avançam ficheiro a '
                                       'ficheiro após cada medição; Depois permanece imóvel.',
        'analyze': 'Analisar',
        'analyze_only_fresh_help_text': 'Apenas analisar mede de novo cada origem completa com FFmpeg em cada '
                                        'execução. Antes e o progresso avançam ficheiro a ficheiro, sem saída nem QC '
                                        'de saída.',
        'analyze_operation': 'análise/simulação',
        'analyzed_progress': 'Analisado: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Fluxo de áudio copiado sem recodificação; etiquetas ReplayGain adicionadas.',
        'audio_tab': 'Áudio',
        'auto_start': 'Iniciar automaticamente após arrastar ou colar',
        'auto_start_tooltip': 'Inicia automaticamente o processamento após adicionar origens por arrastar e largar ou '
                              'colar, se já tiver sido escolhido um destino.',
        'cancel': 'Cancelar',
        'cancelled_summary': 'Cancelado — {success} concluído(s), {failed} erro(s), {skipped} retomado(s)/ignorado(s), '
                             '{warnings} aviso(s), {compliant} conforme(s) — {duration}.',
        'cancelling': 'A cancelar…',
        'choose': 'Escolher…',
        'choose_output': 'Escolher a pasta de destino',
        'clipboard': 'Área de transferência',
        'clipboard_empty': 'A área de transferência não contém um caminho válido de pasta ou ficheiro de áudio '
                           'compatível.',
        'close_button': 'Fechar',
        'close_question': 'Cancelar o processamento e fechar a aplicação?',
        'completed_dialog_summary': 'Estado: concluído\n'
                                    'Ficheiros: {files}\n'
                                    'Concluídos: {success}\n'
                                    'Erros: {failed}\n'
                                    'Retomados ou ignorados: {skipped}\n'
                                    'Avisos: {warnings}\n'
                                    'Conformes: {compliant}\n'
                                    'Tempo total: {duration}',
        'completed_summary': 'Concluído — {success} concluído(s), {failed} erro(s), {skipped} retomado(s)/ignorado(s), '
                             '{warnings} aviso(s), {compliant} conforme(s) — {duration}.',
        'completed_with_errors': 'Processamento concluído com avisos',
        'convert': 'Normalizar',
        'convert_operation': 'uniformização de áudio',
        'cpu_tooltip': 'Utilização total do processador do sistema, atualizada a cada segundo durante o processamento.',
        'cpu_unavailable': 'N/D',
        'cpu_usage': 'CPU',
        'create_report': 'Criar um relatório CSV',
        'csv_file_filter': 'Ficheiros CSV (*.csv)',
        'custom': 'Personalizado',
        'decrease_value': 'Diminuir o valor',
        'description': 'Uniformiza o volume percebido ficheiro a ficheiro sem alterar os originais.',
        'destination': 'Destino',
        'destination_error': 'ERRO — destino indisponível: {error}',
        'destination_path_tooltip': 'Clique no caminho e use as setas, Início/Fim ou a roda. O caminho pode ser '
                                    'selecionado e copiado, mas não alterado.',
        'destination_required_start': 'Escolha primeiro a pasta de destino com o botão «Escolher…».',
        'dialog_ok': 'OK',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — subpastas incluídas',
        'drop_title': 'Largue aqui pastas ou ficheiros de áudio',
        'elapsed_time': 'Tempo decorrido: {duration}',
        'error_list_title': 'Erros de processamento',
        'error_progress': 'Erro: {file}',
        'errors_button': 'Erros ({count})',
        'errors_button_tooltip': 'Abre a lista de erros com nome do ficheiro, caminho e detalhe. Disponível durante '
                                 'uma pausa ou após o processamento.',
        'errors_dialog_title': 'Erros do processamento',
        'estimated_result': 'Resultado estimado; nenhum ficheiro criado.',
        'estimated_total_calculating': 'Tempo total estimado: a calcular…',
        'estimated_total_time': 'Tempo total estimado: {duration}',
        'estimated_total_time_with_day_finish': 'Tempo total estimado: {duration} — {days} d. {time}',
        'estimated_total_time_with_finish': 'Tempo total estimado: {duration} — {time}',
        'estimated_total_unavailable': 'Tempo total estimado: indisponível',
        'ffmpeg_download_button': 'Abrir o site oficial do FFmpeg',
        'ffmpeg_error_no_detail': 'Erro do FFmpeg sem detalhes.',
        'ffmpeg_execution_error': 'Não foi possível executar o FFmpeg: {error}',
        'ffmpeg_incompatible': 'FFmpeg incompatível',
        'ffmpeg_missing': 'FFmpeg não encontrado',
        'ffmpeg_missing_encoders': 'Esta versão do FFmpeg não inclui todos os codificadores de áudio necessários: '
                                   '{encoders}.',
        'ffmpeg_missing_message': 'O FFmpeg deve estar instalado e disponível no PATH ou colocado junto ao programa.',
        'ffmpeg_no_lame': 'Esta versão do FFmpeg não inclui o codificador MP3 libmp3lame.',
        'ffmpeg_no_loudnorm': 'Esta versão do FFmpeg não inclui o filtro loudnorm.',
        'ffmpeg_not_responding': 'O FFmpeg não está a responder corretamente.',
        'file_exists': 'O ficheiro já existe.',
        'files_found': '{total} ficheiro(s) de áudio encontrado(s) — {operation} — {parallel} processo(s) paralelo(s).',
        'finalization_completed': 'Finalização concluída em {duration}.',
        'finalizing': 'Finalização — relatório, cache de análise e dados de retoma…',
        'folder': 'Pasta',
        'folder_unavailable': 'Pasta indisponível',
        'guide_analysis_method': 'O LUFScale utiliza automaticamente a medição histórica completa, o único método '
                                 'validado no corpus de referência.',
        'guide_analyze_prediction_body': 'Apenas analisar pode estimar o resultado, mas não cria áudio nem controlo de '
                                         'qualidade de saída.',
        'guide_analyze_prediction_title': 'Estimativa sem saída',
        'guide_build_body': 'No Windows 10 1809 ou posterior, ou Windows 11 x86-64:\n'
                            '\n'
                            '1. Transfira «LUFScale-2.1.12-Setup-x64.exe» e o respetivo ficheiro SHA-256.\n'
                            '2. Verifique o SHA-256 e faça duplo clique no instalador.\n'
                            '3. Leia e aceite a licença GNU GPL e siga o assistente.\n'
                            '4. Inicie o LUFScale pelo menu Iniciar.\n'
                            '\n'
                            'A aplicação, Python, PySide6/Qt, FFmpeg, codecs, guias e licenças já estão incluídos. A '
                            'instalação não transfere nada nem exige comandos PowerShell. É criado automaticamente um '
                            'desinstalador do Windows.\n'
                            '\n'
                            'A distribuição não é assinada; depois de verificar o ficheiro e a soma, o SmartScreen '
                            'pode pedir confirmação.',
        'guide_build_title': 'Instalar o LUFScale no Windows x86-64',
        'guide_estimated_total_help': 'Tempo total estimado: 12 min - fim por volta das 14:30. «12 min» é a duração '
                                      'total estimada e «14:30» a hora prevista de fim. Se ultrapassar a meia-noite, o '
                                      'número de dias é acrescentado automaticamente antes da hora, por exemplo «2 d. '
                                      '14:30».',
        'guide_file_processing_body': 'Cada ficheiro recebe medição e ganho próprios para se aproximar do alvo LUFS '
                                      'sob o limite True Peak.',
        'guide_file_processing_title': 'Tratamento por ficheiro',
        'guide_help_tooltip': 'Abre o guia PDF completo no idioma selecionado.',
        'guide_level_mode_body': 'Faixa - recomendado: aproxima cada ficheiro do alvo. Álbum - avançado e '
                                 'especializado: aplica um ganho comum e preserva contrastes. Use Álbum para uma obra '
                                 'ouvida pela ordem; Faixa para reprodução aleatória ou nível regular entre ficheiros.',
        'guide_license_body': 'O LUFScale é software livre distribuído sob GNU GPL-3.0-or-later. Esta licença permite '
                              'utilização, estudo, modificação e redistribuição segundo os seus termos. A distribuição '
                              'inclui fontes, avisos e licenças de terceiros. O software é fornecido sem garantia.',
        'guide_license_feature': '• Software livre GNU GPL-3.0-or-later: a licença permite utilização, estudo, '
                                 'modificação e redistribuição.\n'
                                 '• Instalador offline Windows x86-64 com Python, Qt e FFmpeg incluídos. '
                                 'Recomenda-se Windows 11; Windows 10 1809 ou posterior continua como alvo de '
                                 'compatibilidade, mas o suporte padrão da Microsoft terminou.',
        'guide_license_title': 'Software livre e redistribuição',
        'guide_log_legend_cancelled': 'O processamento foi interrompido voluntariamente; não é um erro.',
        'guide_log_legend_compliant': 'Cópia de áudio inalterada: a fonte já respeitava o alvo e o limite de pico.',
        'guide_log_legend_error': 'Não foi possível concluir o ficheiro afetado.',
        'guide_log_legend_success': 'Processamento concluído sem anomalias detetadas.',
        'guide_log_legend_warning': 'A saída existe, mas uma medição excede a tolerância prevista.',
        'guide_missing_message': 'O guia PDF não foi encontrado: {path}',
        'guide_missing_title': 'Guia indisponível',
        'guide_open_error': 'Não foi possível abrir o guia PDF: {path}',
        'guide_quality_priority_body': 'O LUFScale mede a sonoridade dos ficheiros e, com Normalizar, ajusta '
                                       'fisicamente o volume percebido para um alvo LUFS, controlando o pico '
                                       'verdadeiro. Cada fonte é analisada em toda a sua duração; a saída é depois '
                                       'novamente medida e verificada. O resultado não depende de etiquetas nem de um '
                                       'leitor compatível: os níveis ficam mais coerentes entre ficheiros, os desvios '
                                       'são assinalados e os originais permanecem intactos.',
        'guide_quality_priority_title': 'Para que serve o LUFScale?',
        'help_button': 'Ajuda',
        'help_overview': '• Normalização real, ReplayGain ou análise de MP3, FLAC, WAV, AIFF, M4A, OGG e Opus.\n'
                         '• Cada ficheiro é medido e tratado separadamente para o alvo escolhido.\n'
                         '• Estrutura, metadados e capas compatíveis são preservados; os originais não mudam.\n'
                         '• Paralelismo Auto, cache, retoma, controlo de qualidade, CSV, progresso, CPU e históricos '
                         'LUFS.\n'
                         '• Interface e guias PDF em 12 idiomas.',
        'help_title': 'Principais funcionalidades',
        'increase_value': 'Aumentar o valor',
        'input_lufs_log': 'entrada {value} LUFS',
        'interface_ffmpeg_message': 'O motor de áudio FFmpeg integrado está ausente ou inutilizável. Reinstale o '
                                    'LUFScale a partir do arquivo de distribuição completo.',
        'internal_error': 'Erro interno: {error}',
        'interrupted': 'Processamento interrompido.',
        'invalid_location': 'Localização inválida',
        'issue_detail_column': 'Detalhe',
        'issue_file_column': 'Ficheiro',
        'issue_path_column': 'Caminho',
        'language': 'Idioma',
        'language_tooltip': 'Altera imediatamente o idioma da interface, das mensagens e dos futuros relatórios CSV. A '
                            'escolha fica memorizada.',
        'log_help_text': 'Cada linha corresponde a um ficheiro ou a uma etapa geral.\n'
                         '\n'
                         '• Uma linha bem-sucedida começa diretamente pelo nome do ficheiro; SUCESSO deixa de ser '
                         'repetido.\n'
                         '• CONFORME, RETOMADO, IGNORADO, CANCELADO e ERRO permanecem quando acrescentam informação '
                         'útil.\n'
                         '• Os níveis mostram entrada → saída novamente medida e depois o eventual resultado do '
                         'controlo de qualidade.\n'
                         '• Alertas e Erros abrem listas separadas com nome, caminho e detalhe. Estão disponíveis '
                         'durante uma pausa ou no fim, e cada lista pode ser guardada.\n'
                         '\n'
                         'Cores: verde = sucesso; laranja = alerta; vermelho = ficheiro não concluído; violeta azulado '
                         '= retomado; cinzento = informação, item ignorado ou cancelamento.\n'
                         '\n'
                         'ALERTA QC — sonoridade significa que a saída medida difere do valor esperado mais de ±0,60 '
                         'LU. Um valor mais negativo é mais baixo; um menos negativo é mais alto. O desvio é a '
                         'diferença absoluta: -14,69 em vez de -14,00 corresponde a 0,69 LU. O ficheiro é criado na '
                         'mesma; não é uma falha de conversão. Se o resultado for aceitável ao ouvir, não é '
                         'obrigatório agir. Para um alvo rigoroso, consulte o detalhe e o CSV e verifique o alvo e o '
                         'limite True Peak antes de repetir. A mensagem, por si só, não prova se a causa é o limite, o '
                         'codificador ou um limite de correção.\n'
                         '\n'
                         'ALERTA QC — pico significa que o pico verdadeiro medido excede o limite escolhido em mais de '
                         '0,25 dB. O ficheiro é criado na mesma. Se persistir, escolha um alvo LUFS mais baixo ou um '
                         'limite mais prudente, por exemplo -2,0 dBTP, e repita.\n'
                         '\n'
                         'Os tempos acumulados somam o trabalho de todas as tarefas paralelas. O tempo total é a '
                         'duração realmente decorrida.',
        'log_placeholder': 'O relatório do processamento será apresentado aqui.',
        'log_title': 'Registo de processamento',
        'loudness_comparison_after': 'Depois',
        'loudness_comparison_analysis_only': 'Sem saída no modo Apenas analisar',
        'loudness_comparison_before': 'Antes',
        'loudness_comparison_help_text': 'Cada ficheiro acrescenta um ponto à direita. Antes mostra sempre a origem '
                                         'medida. Com Uniformizar, Depois mostra a saída realmente medida de novo. Com '
                                         'ReplayGain, o segundo gráfico tracejado estima a reprodução: sonoridade da '
                                         'origem mais ganho Track guardado. O sinal ≈ e a nota Leitor compatível '
                                         'indicam que não é uma medição física do ficheiro entregue. Um leitor '
                                         'incompatível mantém o nível original; um compatível pode alterar o resultado '
                                         'pelo pré-amplificador ou proteção contra recorte. Os gráficos mantêm a mesma '
                                         'escala fixa ±6 LU. Apenas analisar não tem saída Depois.',
        'loudness_comparison_increased': 'Desvio aumentado em {value} LU',
        'loudness_comparison_needs_qc': 'Ative o controlo de qualidade para comparar',
        'loudness_comparison_no_after': 'Sem curva Depois para esta operação',
        'loudness_comparison_not_applicable': 'Comparação indisponível para esta operação',
        'loudness_comparison_reached': 'Alvo atingido · desvio {value} LU',
        'loudness_comparison_reduced': 'Desvio reduzido em {value} LU',
        'loudness_comparison_replaygain_after': 'Reprodução RG estimada',
        'loudness_comparison_replaygain_note': 'Leitor compatível · áudio inalterado',
        'loudness_comparison_scale': 'Vista ±{scale} LU · tol. QC ±{tolerance} LU',
        'loudness_comparison_target': 'Alvo {value} LUFS',
        'loudness_comparison_title': 'Evolução da sonoridade',
        'loudness_comparison_tooltip': 'Antes mostra a sonoridade física. Em ReplayGain, o segundo gráfico estima a '
                                       'reprodução compatível a partir do ganho guardado.',
        'loudness_comparison_unchanged': 'Desvio inalterado',
        'loudness_comparison_waiting': 'A aguardar um ficheiro processado',
        'loudness_meter_current_file': 'Último: {file}',
        'loudness_meter_estimated': 'Estimado',
        'loudness_meter_help_text': 'A linha vermelha é o alvo e o valor azul é a sonoridade realmente medida da '
                                    'última saída. Sobe ou desce em cada ficheiro. A pontuação resume as últimas 8 '
                                    'saídas medidas. Se o painel vermelho indicar «Ver alertas», pause o processamento '
                                    'ou aguarde o fim e abra Alertas para identificar os ficheiros afetados.',
        'loudness_meter_maximum': 'Máx {value}',
        'loudness_meter_measured': 'Medido',
        'loudness_meter_minimum': 'Mín {value}',
        'loudness_meter_no_file': 'A aguardar uma análise',
        'loudness_meter_target': 'Alvo {value} LUFS',
        'loudness_meter_title': 'Medidor de sonoridade',
        'loudness_meter_tooltip': 'Alvo vermelho; última saída realmente medida em azul.',
        'loudness_meter_waiting': 'À espera de um ficheiro de áudio',
        'loudness_meter_worst_file': 'Maior desvio: {file}',
        'loudness_meter_worst_file_detail': 'Maior desvio das últimas 8 análises: {file} — {measured} LUFS para '
                                            '{expected} LUFS, desvio {deviation} LU.',
        'loudness_score_acceptable': 'Aceitável',
        'loudness_score_check': 'Ver alertas',
        'loudness_score_excellent': 'Excelente',
        'loudness_score_good': 'Boa',
        'loudness_score_needs_qc': 'Pontuação do alvo: ative o controlo de qualidade',
        'loudness_score_not_applicable': 'Pontuação do alvo: não aplicável',
        'loudness_score_tooltip': 'A pontuação usa as últimas 8 saídas medidas. 100 é exato, 50 equivale a um erro RMS '
                                  'de 0,60 LU e 0 a 1,20 LU ou mais. Um painel vermelho significa que pelo menos um '
                                  'alerta de sonoridade pode ser consultado no botão Alertas.',
        'loudness_score_value': 'Pontuação do alvo: {score}/100\n{rating}\nErro RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Pontuação do alvo: em espera',
        'measurement_unavailable': 'Medição indisponível.',
        'mp3': 'MP3',
        'mp3_filter': 'Áudio compatível (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Nenhuma pasta selecionada',
        'no_mp3': 'Nenhum ficheiro de áudio compatível encontrado.',
        'no_new_source': 'Não foi adicionada nenhuma pasta ou ficheiro de áudio compatível.',
        'not_performed': 'Não efetuado',
        'open_output_error': 'Não foi possível abrir a pasta de destino: {error}',
        'operation': 'Operação',
        'operation_analyze': 'Apenas analisar — nenhum ficheiro criado',
        'operation_analyze_label': 'Apenas análise',
        'operation_convert': 'Uniformizar — normalizar realmente o áudio',
        'operation_convert_label': 'Uniformização de áudio',
        'operation_help_text': 'Uniformizar trata cada ficheiro separadamente e volta a medir a saída. ReplayGain não '
                               'altera amostras. Apenas analisar produz medições e um CSV opcional, mas nenhum áudio.',
        'operation_replaygain': 'ReplayGain — sem recodificação de áudio',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Uniformizar altera o áudio para o alvo. ReplayGain copia o fluxo e adiciona etiquetas. '
                             'Apenas analisar mede sem criar áudio.',
        'option_status_auto_start': 'AUTO',
        'option_status_overwrite': 'SUB',
        'option_status_quality_control': 'QUAL',
        'option_status_report': 'CSV',
        'option_status_resume': 'RET',
        'option_status_skip_compliant': 'IGN',
        'options_tab': 'Opções',
        'output_lufs_log': 'saída {value} LUFS',
        'output_lufs_unavailable': 'LUFS de saída indisponível',
        'overwrite': 'Substituir ficheiros existentes',
        'overwrite_tooltip': 'Permite substituir um MP3 já existente no destino. Os ficheiros de origem nunca são '
                             'substituídos.',
        'parallel': 'Processos paralelos',
        'parallel_adjusted': 'Paralelismo automático — {active} processo(s), CPU {cpu:.0f} %.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automático, máximo {maximum}',
        'parallel_tooltip': 'Determina quantos ficheiros podem ser processados simultaneamente.\n'
                            '\n'
                            '• Auto começa com no máximo 4 tarefas. Quando a medição da CPU está disponível, '
                            'verifica-a a cada segundo: adiciona uma tarefa abaixo de 70% de utilização e retira uma '
                            'acima de 92%.\n'
                            '• Auto nunca excede o número de processadores lógicos detetados e tem um limite absoluto '
                            'de 16 tarefas.\n'
                            '• Se a medição da CPU não estiver disponível, Auto utiliza diretamente esse limite '
                            'detetado, sem adaptação dinâmica.\n'
                            '• Um valor numérico fixa o número máximo de tarefas simultâneas; não é um objetivo de '
                            'utilização da CPU.\n'
                            '\n'
                            'Mais tarefas podem acelerar um lote grande, mas aumentam a carga, a temperatura e a '
                            'atividade do disco. Prima − até aparecer Auto.',
        'paste': 'Colar',
        'path_left': 'Mostrar a parte esquerda do caminho',
        'path_right': 'Mostrar a parte direita do caminho',
        'pause': 'Pausa',
        'peak': 'Pico real máximo',
        'peak_tooltip': 'O pico verdadeiro máximo é um limite, não um nível a atingir. Limita em dBTP os picos mais '
                        'altos da forma de onda reconstruída, incluindo os que surgem entre amostras, para reduzir a '
                        'saturação após codificação ou transcodificação.\n'
                        '\n'
                        '• -1,0 dBTP — limite de entrega comum, com o pico de saída mais alto.\n'
                        '• -1,5 dBTP — valor predefinido e compromisso prudente para MP3.\n'
                        '• -2,0 dBTP — margem adicional, útil se o ficheiro puder ser novamente codificado ou com um '
                        'alvo de sonoridade alto.\n'
                        '• 0 dBTP — sem margem; não recomendado para MP3.\n'
                        '\n'
                        'Um valor mais negativo é mais seguro, mas pode impedir faixas muito dinâmicas de atingirem '
                        'exatamente o alvo LUFS.',
        'phase_summary': 'Distribuição estimada do tempo total — análise {analysis}, conversão {conversion}, controlo '
                         'de qualidade {quality}.',
        'pipeline_enabled': 'Pipeline de Faixa — cada conversão começa assim que a análise termina.',
        'pre_measurement': 'A medir os ficheiros de entrada…',
        'preset': 'Predefinição',
        'preset_dynamic': 'Música dinâmica',
        'preset_library': 'Biblioteca musical — recomendado',
        'preset_streaming': 'Streaming mais presente',
        'preset_tooltip': 'Aplica de uma vez um alvo de sonoridade, um pico real máximo e uma qualidade MP3 coerentes. '
                          'Qualquer alteração manual seleciona Personalizado.',
        'processing_cancelled': 'Processamento cancelado.',
        'processing_completed': 'Processamento concluído',
        'processing_in_progress': 'Processamento em curso',
        'processing_paused': 'Processamento em pausa.',
        'processing_resumed': 'Processamento retomado.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'AVISO — não foi possível efetuar o controlo de qualidade: {error}',
        'qc_log': ' — controlo de qualidade: {quality}',
        'qc_ok': 'SUCESSO',
        'qc_warning': 'AVISO — {detail}',
        'quality': 'Qualidade de áudio',
        'quality_control': 'Controlo de qualidade automático',
        'quality_control_tooltip': 'Volta a medir cada saída. As correções continuam a visar ±0,50 LU; o alerta de '
                                   'sonoridade só aparece fora de ±0,60 LU. Os MP3 dinâmicos mantêm até três '
                                   'tentativas; WAV, AIFF e FLAC podem ser refeitos da origem até duas vezes se houver '
                                   'margem True Peak. Desativar remove verificação, tentativas e atividade do medidor.',
        'quality_tooltip': 'Regula o compromisso entre qualidade e tamanho dos formatos comprimidos. Quanto menor for '
                           'o número, maiores serão a qualidade e o débito. Esta definição não altera o alvo LUFS nem '
                           'o pico verdadeiro máximo.\n'
                           '\n'
                           '• 0 — qualidade máxima, recomendada para preservar os detalhes.\n'
                           '• 1 a 2 — qualidade muito alta.\n'
                           '• 3 a 4 — bom compromisso qualidade/tamanho.\n'
                           '• 5 a 9 — ficheiros menores, com mais perdas.\n'
                           '\n'
                           'FLAC permanece sem perdas qualquer que seja o valor. WAV e AIFF ignoram esta definição e '
                           'conservam a frequência e a profundidade PCM compatíveis com a origem. Para MP3, M4A, OGG e '
                           'Opus, um valor baixo pode exigir um débito superior ao original e criar um ficheiro maior. '
                           'Um valor mais alto costuma reduzir o tamanho, sem garantir o mesmo número de bytes porque '
                           'estes codificadores usam frequentemente VBR. Recodificar um formato com perdas não '
                           'recupera informação já perdida.',
        'ready': 'Pronto',
        'recursive_scan': 'A analisar pastas recursivamente…',
        'remove_all': 'Remover tudo',
        'remove_selection': 'Remover seleção',
        'replaygain_help_text': 'ReplayGain calcula ganho e escreve REPLAYGAIN_TRACK_GAIN/PEAK. O fluxo é copiado sem '
                                'recodificação (-c:a copy); só um leitor compatível aplica as etiquetas. LUFS e True '
                                'Peak físicos não mudam.',
        'replaygain_levels_log': 'áudio inalterado: {before} LUFS · ReplayGain {gain} dB nos metadados · alvo '
                                 'configurado {target} LUFS (requer leitor compatível)',
        'replaygain_log_help_text': 'Em ReplayGain, o registo mostra a sonoridade física inalterada, o ganho escrito '
                                    'nos metadados e o alvo configurado. Com o controlo de qualidade ativo, «áudio '
                                    'inalterado e etiquetas verificadas» significa que sonoridade e pico foram '
                                    'comparados com a origem e que as etiquetas foram relidas; não significa que o '
                                    'ficheiro meça fisicamente o alvo.',
        'replaygain_operation': 'ReplayGain sem recodificação',
        'replaygain_qc_help_text': 'Com o controlo de qualidade ativo, o ReplayGain volta a medir o ficheiro entregue '
                                   'para confirmar que a sonoridade física e o pico ficaram inalterados e depois '
                                   'verifica as etiquetas Track. Um resultado positivo confirma áudio preservado e '
                                   'etiquetas presentes, não que o alvo físico tenha sido atingido.',
        'replaygain_qc_ok': 'SUCESSO — áudio inalterado e etiquetas verificadas',
        'replaygain_tags_missing': 'As etiquetas ReplayGain não foram encontradas.',
        'replaygain_usefulness_text': 'ReplayGain é útil para uniformizar a reprodução de forma reversível e sem '
                                      'recodificação numa biblioteca usada com um leitor compatível. Para entregar um '
                                      'ficheiro que meça fisicamente o alvo em todos os leitores, use Uniformizar.',
        'report_destination': 'destino',
        'report_detail': 'detalhe',
        'report_error': 'AVISO — não foi possível criar o relatório CSV: {error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'ganho_db',
        'report_input_dbtp': 'dbtp_entrada',
        'report_input_lufs': 'lufs_entrada',
        'report_log': 'Relatório CSV — {path}',
        'report_mode': 'modo',
        'report_operation': 'operação',
        'report_output_dbtp': 'dbtp_saída',
        'report_output_lufs': 'lufs_saída',
        'report_path': 'Relatório: {path}',
        'report_qc': 'controlo_qualidade',
        'report_qc_engine': 'motor_controlo_qualidade',
        'report_seconds': 'tempo_segundos',
        'report_source': 'origem',
        'report_status': 'estado',
        'report_tooltip': 'Cria apenas um relatório CSV com medições, tempos e alertas; não adiciona JSON de '
                          'diagnóstico.',
        'resume': 'Retomar após uma interrupção',
        'resume_not_saved': ' Ponto de retoma não guardado: {error}',
        'resume_processing': 'Retomar',
        'resume_tooltip': 'Os ficheiros já concluídos com as mesmas definições são reconhecidos e não são processados '
                          'novamente.',
        'resumed_progress': 'Retomado: {file}',
        'save_dialog_cancel': 'Cancelar',
        'save_dialog_filename': 'Nome do ficheiro',
        'save_dialog_filetype': 'Formato',
        'save_dialog_location': 'Localização',
        'save_dialog_overwrite': 'Substituir',
        'save_dialog_overwrite_message': 'O ficheiro «{file}» já existe.',
        'save_dialog_overwrite_title': 'Substituir o ficheiro?',
        'save_dialog_parent': 'Pasta superior',
        'save_dialog_save': 'Guardar',
        'save_issue_list': 'Guardar como CSV…',
        'save_issue_list_error': 'Não foi possível guardar a lista: {error}',
        'save_issue_list_error_title': 'Não foi possível guardar',
        'save_issue_list_title': 'Guardar a lista CSV',
        'scan_error': 'ERRO — {error}',
        'scanning_folders': 'A analisar pastas…',
        'settings': 'Definições',
        'open_folder': 'Abrir pasta',
        'show_option_help': 'Mostrar ajuda: {option}',
        'silent_copy': 'Áudio silencioso ou não mensurável copiado.',
        'silent_copy_no_replaygain': 'Áudio silencioso copiado sem etiquetas ReplayGain.',
        'silent_unmeasurable': 'Áudio silencioso ou não mensurável.',
        'simulation': 'Simulação',
        'skip_compliant': 'Não recodificar ficheiros já conformes',
        'skip_compliant_tooltip': 'Após a análise, um ficheiro a ±0,10 LU do alvo e abaixo do limite True Peak é '
                                  'copiado sem recodificação.',
        'skipped_progress': 'Ignorado: {file}',
        'source_audio_count': 'Ficheiros: {count}',
        'source_list_more': '… mais {count} fontes mantidas',
        'source_safety': 'Os ficheiros de origem nunca são movidos nem alterados.',
        'source_selection_tooltip': 'Seleção múltipla: Ctrl+clique para itens separados e Shift+clique para um intervalo.',
        'sources_added': '{count} origem(ns) adicionada(s).',
        'start': 'Iniciar',
        'status_analyzed': 'ANALISADO',
        'status_cancelled': 'CANCELADO',
        'status_compliant': 'CONFORME',
        'status_error': 'ERRO',
        'status_ok': 'SUCESSO',
        'status_resumed': 'RETOMADO',
        'status_skipped': 'IGNORADO',
        'status_warning': 'AVISO',
        'switch_to_dark': 'Modo escuro',
        'switch_to_light': 'Modo claro',
        'tagline': 'Uniformiza o volume de áudio percecionado',
        'target': 'Alvo de sonoridade',
        'target_tooltip': 'O alvo de sonoridade é a sonoridade integrada pretendida para toda a faixa, expressa em '
                          'LUFS. Um valor menos negativo produz um ficheiro mais alto: -14 LUFS é mais alto do que -16 '
                          'LUFS. Uma diferença de 2 LU corresponde aproximadamente a 2 dB de nível antes de eventual '
                          'limitação de pico.\n'
                          '\n'
                          'Referências: -18 LUFS para um resultado mais calmo e dinâmico; -16 LUFS para equilíbrio '
                          'geral; -14 LUFS para um resultado mais alto de tipo streaming. As plataformas podem depois '
                          'aplicar a sua própria normalização de reprodução.\n'
                          '\n'
                          'Este alvo não achata por si só a dinâmica interna da faixa. Se o pico verdadeiro máximo '
                          'impedir que o alvo seja atingido sem saturação, o resultado pode ficar ligeiramente mais '
                          'baixo.',
        'theme_accessible': 'Alterar o aspeto da aplicação. A escolha fica memorizada.',
        'total_time': 'Tempo total: {duration}',
        'track_two_pass': 'Normalização de faixa em duas passagens.',
        'true_peak_meter_exceeded': 'Excesso {margin} dB',
        'true_peak_meter_margin': 'Margem {margin} dB',
        'true_peak_meter_title': 'Margem de pico',
        'true_peak_meter_tooltip': 'Compara o true peak da última saída com o limite escolhido. O marcador mostra o '
                                   'último valor e o triângulo conserva o pico mais alto do lote. Verde: limite '
                                   'respeitado; laranja: excesso até 0,25 dB; vermelho: excesso maior. A tolerância '
                                   'laranja pertence ao controlo de qualidade LUFScale e não é uma norma de entrega. '
                                   'Reinicia em cada lote.',
        'true_peak_meter_waiting': 'A aguardar uma medição dBTP',
        'version_changes': '• Um único instalador offline para Windows 10/11 x86-64.\n'
                           '• Python, PySide6/Qt, FFmpeg, codecs, guias e licenças estão incluídos; a instalação não '
                           'transfere nada nem exige comandos PowerShell.\n'
                           '• A compilação valida loudnorm e os codificadores antes de criar o instalador e o SHA-256.',
        'version_changes_title': 'Novidades da versão {version}',
        'version_label': 'Versão {version}',
        'volume': 'Volume',
        'volume_loud': 'Forte: -14 LUFS',
        'volume_normal': 'Normal: -16 LUFS',
        'volume_soft': 'Suave: -18 LUFS',
        'volume_tooltip': 'Esta definição é um atalho para o alvo de sonoridade; não altera o volume de audição do '
                          'sistema.\n'
                          '\n'
                          '• Suave: -18 LUFS — nível mais calmo, maior margem dinâmica e menor probabilidade de '
                          'acionar o limitador.\n'
                          '• Normal: -16 LUFS — compromisso equilibrado e bom ponto de partida para uma biblioteca '
                          'pessoal.\n'
                          '• Forte: -14 LUFS — reprodução mais presente, próxima do alvo Normal do Spotify, mas com '
                          'maior probabilidade de exigir limitação.\n'
                          '• Personalizado — permite introduzir diretamente outro alvo LUFS.\n'
                          '\n'
                          'São escolhas práticas, não uma norma universal.',
        'warning_list_title': 'Alertas de processamento',
        'warnings_button': 'Alertas ({count})',
        'warnings_button_tooltip': 'Abre a lista de alertas com nome do ficheiro, caminho e detalhe. Disponível '
                                   'durante uma pausa ou após o processamento.',
        'warnings_dialog_title': 'Alertas do processamento'},
 'ru': {'activity_cancelled': 'Активность: обработка отменена',
        'activity_cancelling': 'Активность: отмена…',
        'activity_completed': 'Активность: обработка завершена',
        'activity_compliant': 'Соответствует: {count}',
        'activity_detected': 'Активность: обнаружено файлов: {total}',
        'activity_errors': 'Ошибки: {count}',
        'activity_files': 'Файлы: {count}',
        'activity_idle': 'Активность: ожидание',
        'activity_preparing': 'Активность: подготовка файлов…',
        'activity_progress': '{total} файлов • успешно {success} • предупреждения {warnings} • ошибки {failed} • '
                             'возобновлено/пропущено {skipped} • соответствует {compliant}',
        'activity_skipped': 'Возобн./пропущ.: {count}',
        'activity_successes': 'Успешно: {count}',
        'activity_warnings': 'Предупреждения: {count}',
        'adaptive_disabled_log': 'Адаптивный анализ — быстрые пробы остановлены после {sample} замеров ({successes} '
                                 'успешных, расчётная экономия {percent:+.1f}%).',
        'add_folders': 'Добавить папки…',
        'add_mp3': 'Добавить аудиофайлы…',
        'add_replaygain': 'Добавить ReplayGain',
        'add_source_files': 'Добавить аудиофайлы',
        'add_source_folder': 'Добавить исходную папку',
        'already_completed': 'Уже завершено во время предыдущего запуска.',
        'already_compliant_badge': 'СООТВЕТСТВУЕТ',
        'already_compliant_copy': 'Уже соответствует: скопирован без изменений и перекодирования аудио.',
        'already_compliant_log': 'уже соответствует, без перекодирования',
        'analysis_cache_summary': 'Кэш анализа — повторно использовано измерений: {hits}.',
        'analysis_impossible': 'Ошибка анализа: {error}',
        'analysis_measurement_progress': 'Анализ {current}/{total} — {file} — {value}',
        'analysis_method': 'Метод анализа',
        'analysis_method_adaptive': 'Адаптивный — остановка без выгоды',
        'analysis_method_fast': 'Быстрый — экспериментальный',
        'analysis_method_historical': 'Исторический — эталон',
        'analysis_method_log': 'Метод анализа — {method}.',
        'analysis_method_tooltip': 'Стабильная версия автоматически использует полный исторический эталонный замер — '
                                   'единственный метод, проверенный на эталонном наборе. Быстрый и адаптивный варианты '
                                   'больше не предлагаются.',
        'analysis_progress': 'Анализ {current}/{total}: {file}',
        'analysis_progress_help_text': 'При анализе график «До», журнал и индикатор выполнения обновляются после '
                                       'каждого файла; «После» остаётся неподвижным.',
        'analyze': 'Анализировать',
        'analyze_only_fresh_help_text': 'При каждом запуске анализ заново полностью измеряет каждый источник через '
                                        'FFmpeg. График «До» и прогресс обновляются по файлам; выхода и его QC нет.',
        'analyze_operation': 'анализ/моделирование',
        'analyzed_progress': 'Проанализировано: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Аудиопоток скопирован без перекодирования; добавлены теги ReplayGain.',
        'audio_tab': 'Аудио',
        'auto_start': 'Запускать после перетаскивания или вставки',
        'auto_start_tooltip': 'Автоматически запускает обработку после перетаскивания или вставки, если папка '
                              'назначения уже выбрана.',
        'cancel': 'Отмена',
        'cancelled_summary': 'Отменено — успешно {success}, ошибок {failed}, возобновлено/пропущено {skipped}, '
                             'предупреждений {warnings}, соответствует {compliant} — {duration}.',
        'cancelling': 'Отмена…',
        'choose': 'Выбрать…',
        'choose_output': 'Выбрать папку назначения',
        'clipboard': 'Буфер обмена',
        'clipboard_empty': 'Буфер обмена не содержит допустимого пути к папке или поддерживаемому аудиофайлу.',
        'close_button': 'Закрыть',
        'close_question': 'Отменить обработку и закрыть приложение?',
        'completed_dialog_summary': 'Состояние: завершено\n'
                                    'Файлы: {files}\n'
                                    'Успешно: {success}\n'
                                    'Ошибки: {failed}\n'
                                    'Возобновлено или пропущено: {skipped}\n'
                                    'Предупреждения: {warnings}\n'
                                    'Соответствует: {compliant}\n'
                                    'Общее время: {duration}',
        'completed_summary': 'Завершено — успешно {success}, ошибок {failed}, возобновлено/пропущено {skipped}, '
                             'предупреждений {warnings}, соответствует {compliant} — {duration}.',
        'completed_with_errors': 'Обработка завершена с предупреждениями',
        'convert': 'Нормализовать',
        'convert_operation': 'нормализация аудио',
        'cpu_tooltip': 'Общая загрузка CPU системы, обновляемая каждую секунду во время обработки.',
        'cpu_usage': 'ЦП',
        'create_report': 'Создать отчёт CSV',
        'csv_file_filter': 'Файлы CSV (*.csv)',
        'custom': 'Пользовательский',
        'decrease_value': 'Уменьшить значение',
        'description': 'Выравнивает воспринимаемую громкость каждого файла, не изменяя оригиналы.',
        'destination': 'Папка назначения',
        'destination_error': 'ОШИБКА — папка назначения недоступна: {error}',
        'destination_path_tooltip': 'Щёлкните путь и используйте стрелки, Home/End или колесо мыши. Путь можно '
                                    'выделить и скопировать, но нельзя изменить.',
        'destination_required_start': 'Сначала выберите папку назначения кнопкой «Выбрать…».',
        'dialog_ok': 'ОК',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — включая вложенные папки',
        'drop_title': 'Перетащите сюда папки или аудиофайлы',
        'elapsed_time': 'Прошло: {duration}',
        'error_list_title': 'Ошибки обработки',
        'error_progress': 'Ошибка: {file}',
        'errors_button': 'Ошибки ({count})',
        'errors_button_tooltip': 'Открывает список ошибок с именем файла, путём и подробностями. Доступен во время '
                                 'паузы или после обработки.',
        'errors_dialog_title': 'Ошибки обработки',
        'estimated_result': 'Расчётный результат; файл не создан.',
        'estimated_total_calculating': 'Общее расчётное время: вычисление…',
        'estimated_total_time': 'Общее расчётное время: {duration}',
        'estimated_total_time_with_day_finish': 'Общее расчётное время: {duration} — {days} д. {time}',
        'estimated_total_time_with_finish': 'Общее расчётное время: {duration} — {time}',
        'estimated_total_unavailable': 'Общее расчётное время: недоступно',
        'ffmpeg_download_button': 'Открыть официальный сайт FFmpeg',
        'ffmpeg_error_no_detail': 'Ошибка FFmpeg без подробностей.',
        'ffmpeg_execution_error': 'Не удалось запустить FFmpeg: {error}',
        'ffmpeg_incompatible': 'Несовместимая версия FFmpeg',
        'ffmpeg_missing': 'FFmpeg не найден',
        'ffmpeg_missing_encoders': 'Эта версия FFmpeg не содержит все необходимые аудиокодеры: {encoders}.',
        'ffmpeg_missing_message': 'FFmpeg должен быть установлен и доступен через PATH либо находиться рядом с '
                                  'программой.',
        'ffmpeg_no_lame': 'Эта сборка FFmpeg не содержит MP3-кодировщик libmp3lame.',
        'ffmpeg_no_loudnorm': 'В этой сборке FFmpeg отсутствует фильтр loudnorm.',
        'ffmpeg_not_responding': 'FFmpeg не отвечает должным образом.',
        'file_exists': 'Файл уже существует.',
        'files_found': 'Найдено аудиофайлов: {total} — {operation} — параллельных процессов: {parallel}.',
        'finalization_completed': 'Завершение выполнено за {duration}.',
        'finalizing': 'Завершение — отчёт, кэш анализа и данные возобновления…',
        'folder': 'Папка',
        'folder_unavailable': 'Папка недоступна',
        'guide_analysis_method': 'LUFScale автоматически использует полный исторический замер - единственный метод, '
                                 'проверенный на эталонном наборе.',
        'guide_analyze_prediction_body': 'Анализ может оценить результат, но не создаёт аудио и контроль качества '
                                         'выхода.',
        'guide_analyze_prediction_title': 'Оценка без выхода',
        'guide_build_body': 'В Windows 10 1809 или новее либо Windows 11 x86-64:\n'
                            '\n'
                            '1. Загрузите «LUFScale-2.1.12-Setup-x64.exe» и файл SHA-256.\n'
                            '2. Проверьте SHA-256 и дважды щёлкните установщик.\n'
                            '3. Прочтите и примите лицензию GNU GPL, затем следуйте указаниям мастера.\n'
                            '4. Запустите LUFScale из меню Пуск.\n'
                            '\n'
                            'Приложение, Python, PySide6/Qt, FFmpeg, кодеки, руководства и лицензии уже включены. '
                            'Установка ничего не загружает и не требует команд PowerShell. Деинсталлятор Windows '
                            'создаётся автоматически.\n'
                            '\n'
                            'Сборка не подписана; после проверки файла и контрольной суммы SmartScreen может '
                            'запросить подтверждение.',
        'guide_build_title': 'Установка LUFScale в Windows x86-64',
        'guide_estimated_total_help': 'Общее расчётное время: 12 мин - завершение около 14:30. «12 мин» - расчётная '
                                      'общая длительность, а «14:30» - ожидаемое время окончания. После полуночи перед '
                                      'временем автоматически добавляется число дней, например «2 д. 14:30».',
        'guide_file_processing_body': 'Для каждого файла отдельно рассчитываются измерение и усиление к цели LUFS с '
                                      'учётом True Peak.',
        'guide_file_processing_title': 'Обработка по файлам',
        'guide_help_tooltip': 'Открывает полное PDF-руководство на выбранном языке.',
        'guide_level_mode_body': 'Трек - рекомендуется: ведёт каждый файл к цели. Альбом - расширенный '
                                 'специализированный режим: применяет общее усиление и сохраняет контрасты. Альбом '
                                 'подходит для последовательного прослушивания, Трек - для случайного порядка и '
                                 'ровного уровня файлов.',
        'guide_license_body': 'LUFScale — свободное ПО под лицензией GNU GPL-3.0-or-later. Лицензия разрешает '
                              'использование, изучение, изменение и распространение на её условиях. В комплект входят '
                              'исходный код, уведомления и сторонние лицензии. Программа предоставляется без гарантий.',
        'guide_license_feature': '• Свободное ПО GNU GPL-3.0-or-later: лицензия разрешает использование, изучение, '
                                 'изменение и распространение.\n'
                                 '• Автономный установщик Windows x86-64 с Python, Qt и FFmpeg. Рекомендуется Windows 11; '
                                 'Windows 10 1809 или новее остаётся целью совместимости, но стандартная поддержка '
                                 'Microsoft завершена.',
        'guide_license_title': 'Свободное ПО и распространение',
        'guide_log_legend_cancelled': 'Обработка остановлена пользователем; это не ошибка.',
        'guide_log_legend_compliant': 'Аудио скопировано без изменений: источник уже соответствовал цели и пределу '
                                      'пика.',
        'guide_log_legend_error': 'Не удалось завершить обработку указанного файла.',
        'guide_log_legend_success': 'Обработка завершена без обнаруженных отклонений.',
        'guide_log_legend_warning': 'Выходной файл создан, но одно измерение вышло за допустимый предел.',
        'guide_missing_message': 'PDF-руководство не найдено: {path}',
        'guide_missing_title': 'Руководство недоступно',
        'guide_open_error': 'Не удалось открыть руководство PDF: {path}',
        'guide_quality_priority_body': 'LUFScale измеряет громкость файлов и в режиме нормализации физически '
                                       'корректирует воспринимаемый уровень до цели LUFS, контролируя истинный пик. '
                                       'Каждый источник анализируется целиком, после чего выход повторно измеряется и '
                                       'проверяется. Результат не зависит от тегов или совместимого проигрывателя: '
                                       'уровни файлов становятся согласованнее, отклонения отмечаются, а оригиналы '
                                       'остаются неизменными.',
        'guide_quality_priority_title': 'Для чего нужен LUFScale?',
        'help_button': 'Справка',
        'help_overview': '• Нормализация, ReplayGain или анализ MP3, FLAC, WAV, AIFF, M4A, OGG и Opus.\n'
                         '• Каждый файл измеряется и обрабатывается отдельно до выбранной цели.\n'
                         '• Структура, метаданные и обложки сохраняются; оригиналы не изменяются.\n'
                         '• Параллельная обработка, кэш, продолжение, контроль качества, CSV, прогресс, CPU и история '
                         'LUFS.\n'
                         '• Интерфейс и PDF на 12 языках.',
        'help_title': 'Основные возможности',
        'increase_value': 'Увеличить значение',
        'input_lufs_log': 'вход {value} LUFS',
        'interface_ffmpeg_message': 'Встроенный аудиодвижок FFmpeg отсутствует или непригоден. Переустановите LUFScale '
                                    'из полного архива дистрибутива.',
        'internal_error': 'Внутренняя ошибка: {error}',
        'interrupted': 'Обработка прервана.',
        'invalid_location': 'Недопустимое расположение',
        'issue_detail_column': 'Подробности',
        'issue_file_column': 'Файл',
        'issue_path_column': 'Путь',
        'language': 'Язык',
        'language_tooltip': 'Сразу меняет язык интерфейса. Выбор сохраняется; непереведённые технические сообщения '
                            'остаются на английском.',
        'log_help_text': 'Каждая строка относится к файлу или общему этапу обработки.\n'
                         '\n'
                         '• Успешная строка начинается с имени файла; УСПЕШНО больше не повторяется.\n'
                         '• СООТВЕТСТВУЕТ, ВОЗОБНОВЛЕНО, ПРОПУЩЕНО, ОТМЕНЕНО и ОШИБКА остаются, когда дают полезную '
                         'информацию.\n'
                         '• Уровни показывают вход → повторно измеренный выход, затем возможный результат контроля '
                         'качества.\n'
                         '• Предупреждения и Ошибки открывают отдельные списки с именем, путём и подробностями. Они '
                         'доступны во время паузы или после обработки; каждый список можно сохранить.\n'
                         '\n'
                         'Цвета: зелёный = успех; оранжевый = предупреждение; красный = незавершённый файл; '
                         'сине-фиолетовый = возобновление; серый = информация, пропуск или отмена.\n'
                         '\n'
                         'ПРЕДУПРЕЖДЕНИЕ QC — громкость означает, что повторно измеренный выход отличается от '
                         'ожидаемого более чем на ±0,60 LU. Более отрицательное значение тише, менее отрицательное — '
                         'громче. Отклонение — абсолютная разность: -14,69 вместо -14,00 даёт 0,69 LU. Файл всё равно '
                         'создан; это не ошибка преобразования. Если звучание устраивает, действие не обязательно. Для '
                         'строгой цели изучите детали и CSV, затем проверьте цель и предел True Peak перед повтором. '
                         'Одно сообщение не доказывает, вызвано ли отклонение пределом, кодировщиком или пределом '
                         'коррекции.\n'
                         '\n'
                         'ПРЕДУПРЕЖДЕНИЕ QC — пик означает превышение выбранного предела истинного пика более чем на '
                         '0,25 дБ. Файл всё равно создан. При повторяющемся предупреждении задайте более низкую цель '
                         'LUFS или более осторожный предел, например -2,0 dBTP, и повторите обработку.\n'
                         '\n'
                         'Накопленное время суммирует работу всех параллельных задач. Общее время — фактически '
                         'прошедшая длительность.',
        'log_placeholder': 'Здесь появится отчёт обработки.',
        'log_title': 'Журнал обработки',
        'loudness_comparison_after': 'После',
        'loudness_comparison_analysis_only': 'В режиме анализа выходной файл не создаётся',
        'loudness_comparison_before': 'До',
        'loudness_comparison_help_text': 'Каждый файл добавляет точку справа. «До» всегда показывает измеренный '
                                         'источник. При нормализации «После» показывает реально повторно измеренный '
                                         'результат. Для ReplayGain второй пунктирный график оценивает '
                                         'воспроизведение: громкость источника плюс записанный Track Gain. Знак ≈ и '
                                         'пометка о совместимом плеере означают, что это не физическое измерение '
                                         'выходного файла. Несовместимый плеер сохраняет исходный уровень; совместимый '
                                         'может изменить результат настройкой предусиления или защитой от клиппинга. '
                                         'Оба графика сохраняют общую фиксированную шкалу ±6 LU. У режима анализа нет '
                                         'выхода «После».',
        'loudness_comparison_increased': 'Отклонение увеличено на {value} LU',
        'loudness_comparison_needs_qc': 'Включите контроль качества для сравнения',
        'loudness_comparison_no_after': 'Для этой операции нет графика «После»',
        'loudness_comparison_not_applicable': 'Сравнение недоступно для этой операции',
        'loudness_comparison_reached': 'Цель достигнута · отклонение {value} LU',
        'loudness_comparison_reduced': 'Отклонение уменьшено на {value} LU',
        'loudness_comparison_replaygain_after': 'Оценка воспроизведения RG',
        'loudness_comparison_replaygain_note': 'Совместимый плеер · звук не изменён',
        'loudness_comparison_scale': 'Шкала ±{scale} LU · допуск QC ±{tolerance} LU',
        'loudness_comparison_target': 'Цель {value} LUFS',
        'loudness_comparison_title': 'Изменение громкости',
        'loudness_comparison_tooltip': '«До» показывает физическую громкость. Для ReplayGain второй график оценивает '
                                       'воспроизведение по записанному усилению.',
        'loudness_comparison_unchanged': 'Отклонение не изменилось',
        'loudness_comparison_waiting': 'Ожидание обработанного файла',
        'loudness_meter_current_file': 'Последний: {file}',
        'loudness_meter_estimated': 'Оценка',
        'loudness_meter_help_text': 'Красная линия — цель, синее значение — реально измеренная громкость последнего '
                                    'результата. Оно меняется для каждого файла. Оценка обобщает 8 последних повторно '
                                    'измеренных выходов. Если на красной панели указано «Открыть предупреждения», '
                                    'приостановите обработку или дождитесь её окончания, затем откройте Предупреждения '
                                    'и найдите затронутые файлы.',
        'loudness_meter_maximum': 'Макс {value}',
        'loudness_meter_measured': 'Измерено',
        'loudness_meter_minimum': 'Мин {value}',
        'loudness_meter_no_file': 'Ожидание анализа',
        'loudness_meter_target': 'Цель {value} LUFS',
        'loudness_meter_title': 'Измеритель громкости',
        'loudness_meter_tooltip': 'Красная цель; последний реально измеренный результат показан синим.',
        'loudness_meter_waiting': 'Ожидание аудиофайла',
        'loudness_meter_worst_file': 'Наибольшее отклонение: {file}',
        'loudness_meter_worst_file_detail': 'Наибольшее отклонение за последние 8 анализов: {file} — {measured} LUFS '
                                            'при цели {expected} LUFS, отклонение {deviation} LU.',
        'loudness_score_acceptable': 'Приемлемо',
        'loudness_score_check': 'Открыть предупреждения',
        'loudness_score_excellent': 'Отлично',
        'loudness_score_good': 'Хорошо',
        'loudness_score_needs_qc': 'Оценка цели: включите контроль качества',
        'loudness_score_not_applicable': 'Оценка цели: неприменимо',
        'loudness_score_tooltip': 'Оценка использует 8 последних повторно измеренных выходов. 100 — точное совпадение, '
                                  '50 — ошибка RMS 0,60 LU, 0 — 1,20 LU или больше. Красная панель означает, что '
                                  'кнопка Предупреждения содержит хотя бы одно предупреждение по громкости.',
        'loudness_score_value': 'Оценка цели: {score}/100\n{rating}\nОшибка RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Оценка цели: ожидание',
        'measurement_unavailable': 'Измерение недоступно.',
        'mp3_filter': 'Поддерживаемое аудио (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Папка не выбрана',
        'no_mp3': 'Поддерживаемые аудиофайлы не найдены.',
        'no_new_source': 'Не добавлено ни одной новой папки или поддерживаемого аудиофайла.',
        'not_performed': 'Не выполнено',
        'open_output_error': 'Не удалось открыть папку назначения: {error}',
        'operation': 'Операция',
        'operation_analyze': 'Только анализ — файл не создаётся',
        'operation_analyze_label': 'Только анализ',
        'operation_convert': 'Выровнять — нормализовать аудио',
        'operation_convert_label': 'Нормализация аудио',
        'operation_help_text': 'Нормализация обрабатывает каждый файл отдельно и повторно измеряет выход. ReplayGain '
                               'не меняет сэмплы. Анализ создаёт измерения и при необходимости CSV, но не аудио.',
        'operation_replaygain': 'ReplayGain — без перекодирования',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Нормализация физически меняет звук. ReplayGain копирует поток и добавляет теги. Анализ '
                             'измеряет без создания аудио.',
        'option_status_auto_start': 'АВТО',
        'option_status_overwrite': 'ПЕР',
        'option_status_quality_control': 'КАЧ',
        'option_status_report': 'CSV',
        'option_status_resume': 'ВОЗ',
        'option_status_skip_compliant': 'ПРО',
        'options_tab': 'Параметры',
        'output_lufs_log': 'выход {value} LUFS',
        'output_lufs_unavailable': 'LUFS выхода недоступен',
        'overwrite': 'Перезаписывать существующие файлы',
        'overwrite_tooltip': 'Разрешает заменить MP3, уже существующий в папке назначения. Исходные файлы никогда не '
                             'перезаписываются.',
        'parallel': 'Параллельные процессы',
        'parallel_adjusted': 'Автоматическая параллельность — процессов: {active}, CPU {cpu:.0f}%.',
        'parallel_auto': 'Авто',
        'parallel_auto_log': 'автоматически, максимум {maximum}',
        'parallel_tooltip': 'Определяет, сколько файлов можно обрабатывать одновременно.\n'
                            '\n'
                            '• «Авто» начинает максимум с 4 задач. Если измерение CPU доступно, оно проверяется каждую '
                            'секунду: ниже 70% добавляется одна задача, выше 92% одна задача убирается.\n'
                            '• «Авто» никогда не превышает обнаруженное число логических процессоров и имеет '
                            'абсолютный предел 16 задач.\n'
                            '• Если измерение CPU недоступно, «Авто» сразу использует обнаруженный предел без '
                            'динамической регулировки.\n'
                            '• Числовое значение задаёт максимальное число одновременных задач; это не целевая '
                            'загрузка CPU.\n'
                            '\n'
                            'Большее число задач может ускорить крупную партию, но увеличивает нагрузку, нагрев и '
                            'активность диска. Нажимайте − до появления «Авто».',
        'paste': 'Вставить',
        'path_left': 'Показать левую часть пути',
        'path_right': 'Показать правую часть пути',
        'pause': 'Пауза',
        'peak': 'Максимальный true peak',
        'peak_tooltip': 'Максимальный true peak — это предел, а не уровень, которого нужно достичь. Он ограничивает в '
                        'dBTP самые высокие пики восстановленной формы сигнала, включая межсемпловые, чтобы снизить '
                        'риск перегрузки после кодирования или транскодирования.\n'
                        '\n'
                        '• -1,0 dBTP — распространённый предел поставки с самым высоким выходным пиком.\n'
                        '• -1,5 dBTP — значение по умолчанию и осторожный компромисс для MP3.\n'
                        '• -2,0 dBTP — дополнительный запас, полезный при повторном кодировании или высокой целевой '
                        'громкости.\n'
                        '• 0 dBTP — запас отсутствует; для MP3 не рекомендуется.\n'
                        '\n'
                        'Более отрицательное значение безопаснее, но может не позволить очень динамичным трекам точно '
                        'достичь цели LUFS.',
        'phase_summary': 'Расчётное распределение общего времени — анализ {analysis}, преобразование {conversion}, '
                         'контроль качества {quality}.',
        'pipeline_enabled': 'Конвейер треков — преобразование начинается сразу после завершения анализа.',
        'pre_measurement': 'Измерение входных файлов…',
        'preset': 'Предустановка',
        'preset_dynamic': 'Динамичная музыка',
        'preset_library': 'Музыкальная библиотека — рекомендуется',
        'preset_streaming': 'Более громкий стриминг',
        'preset_tooltip': 'Одновременно задаёт согласованные целевую громкость, максимальный true peak и качество MP3. '
                          'Любое ручное изменение выбирает режим «Пользовательский».',
        'processing_cancelled': 'Обработка отменена.',
        'processing_completed': 'Обработка завершена',
        'processing_in_progress': 'Выполняется обработка',
        'processing_paused': 'Обработка приостановлена.',
        'processing_resumed': 'Обработка продолжена.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'ПРЕДУПРЕЖДЕНИЕ — контроль качества не выполнен: {error}',
        'qc_log': ' — контроль качества: {quality}',
        'qc_ok': 'УСПЕШНО',
        'qc_warning': 'ПРЕДУПРЕЖДЕНИЕ — {detail}',
        'quality': 'Качество аудио',
        'quality_control': 'Автоматический контроль качества',
        'quality_control_tooltip': 'Повторно измеряет каждый выход. Коррекция по-прежнему стремится к ±0,50 LU; '
                                   'предупреждение появляется только за пределами ±0,60 LU. Для динамических MP3 '
                                   'сохраняется до трёх попыток; WAV, AIFF и FLAC могут быть повторены из источника до '
                                   'двух раз при наличии запаса True Peak. Отключение убирает проверку, повторы и '
                                   'работу индикатора.',
        'quality_tooltip': 'Задаёт компромисс между качеством и размером для сжатых форматов. Чем меньше число, тем '
                           'выше качество и битрейт. Эта настройка не меняет цель LUFS и максимальный True Peak.\n'
                           '\n'
                           '• 0 — максимальное качество, рекомендуется для сохранения деталей.\n'
                           '• 1-2 — очень высокое качество.\n'
                           '• 3-4 — хороший баланс качества и размера.\n'
                           '• 5-9 — меньшие файлы с большими потерями.\n'
                           '\n'
                           'FLAC остаётся форматом без потерь при любом значении. WAV и AIFF игнорируют настройку и '
                           'сохраняют совместимые с источником частоту и разрядность PCM. Для MP3, M4A, OGG и Opus '
                           'малое значение может потребовать битрейт выше исходного и увеличить файл. Большее значение '
                           'обычно уменьшает размер, но не гарантирует одинаковое число байтов, поскольку эти кодеки '
                           'часто используют VBR. Повторное кодирование формата с потерями не восстанавливает уже '
                           'утраченную информацию.',
        'ready': 'Готово',
        'recursive_scan': 'Рекурсивное сканирование папок…',
        'remove_all': 'Удалить всё',
        'remove_selection': 'Удалить выбранное',
        'replaygain_help_text': 'ReplayGain вычисляет усиление и пишет REPLAYGAIN_TRACK_GAIN/PEAK. Поток копируется '
                                'без перекодирования (-c:a copy); теги применяет только совместимый проигрыватель. '
                                'Физические LUFS и True Peak не меняются.',
        'replaygain_levels_log': 'аудио без изменений: {before} LUFS · ReplayGain {gain} дБ в метаданных · заданная '
                                 'цель {target} LUFS (нужен совместимый проигрыватель)',
        'replaygain_log_help_text': 'В режиме ReplayGain журнал показывает неизменную физическую громкость, усиление, '
                                    'записанное в метаданные, и заданную цель. При включённом контроле качества '
                                    'сообщение «аудио не изменено, теги проверены» означает сравнение громкости и пика '
                                    'с источником и повторное чтение тегов; оно не означает, что файл физически '
                                    'измеряется на целевом уровне.',
        'replaygain_operation': 'ReplayGain без перекодирования',
        'replaygain_qc_help_text': 'При включённом контроле качества ReplayGain повторно измеряет итоговый файл, чтобы '
                                   'подтвердить неизменность физической громкости и пика, затем проверяет теги Track. '
                                   'Успех подтверждает сохранность аудио и наличие тегов, а не физическое достижение '
                                   'цели.',
        'replaygain_qc_ok': 'УСПЕШНО — аудио не изменено, теги проверены',
        'replaygain_tags_missing': 'Теги ReplayGain не найдены.',
        'replaygain_usefulness_text': 'ReplayGain полезен для обратимого выравнивания громкости при воспроизведении '
                                      'без перекодирования, если библиотека используется в совместимом проигрывателе. '
                                      'Для файла, физически измеряемого на цели в любом проигрывателе, выберите '
                                      'Нормализацию.',
        'report_destination': 'назначение',
        'report_detail': 'подробности',
        'report_error': 'ПРЕДУПРЕЖДЕНИЕ — не удалось создать отчёт CSV: {error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'усиление_дб',
        'report_input_dbtp': 'вход_dbtp',
        'report_input_lufs': 'вход_lufs',
        'report_log': 'Отчёт CSV — {path}',
        'report_mode': 'режим',
        'report_operation': 'операция',
        'report_output_dbtp': 'выход_dbtp',
        'report_output_lufs': 'выход_lufs',
        'report_path': 'Отчёт: {path}',
        'report_qc': 'контроль_качества',
        'report_qc_engine': 'движок_контроля_качества',
        'report_seconds': 'время_секунды',
        'report_source': 'источник',
        'report_status': 'статус',
        'report_tooltip': 'Создаёт только CSV с измерениями, временем и предупреждениями; диагностический JSON не '
                          'добавляется.',
        'resume': 'Возобновить после прерывания',
        'resume_not_saved': ' Точка возобновления не сохранена: {error}',
        'resume_processing': 'Продолжить',
        'resume_tooltip': 'Ранее завершённые с теми же настройками файлы распознаются и не обрабатываются повторно.',
        'resumed_progress': 'Возобновлено: {file}',
        'save_dialog_cancel': 'Отмена',
        'save_dialog_filename': 'Имя файла',
        'save_dialog_filetype': 'Формат',
        'save_dialog_location': 'Папка',
        'save_dialog_overwrite': 'Заменить',
        'save_dialog_overwrite_message': 'Файл «{file}» уже существует.',
        'save_dialog_overwrite_title': 'Заменить файл?',
        'save_dialog_parent': 'Родительская папка',
        'save_dialog_save': 'Сохранить',
        'save_issue_list': 'Сохранить как CSV…',
        'save_issue_list_error': 'Не удалось сохранить список: {error}',
        'save_issue_list_error_title': 'Сохранение невозможно',
        'save_issue_list_title': 'Сохранить список CSV',
        'scan_error': 'ОШИБКА — {error}',
        'scanning_folders': 'Сканирование папок…',
        'settings': 'Настройки',
        'open_folder': 'Открыть папку',
        'show_option_help': 'Показать справку: {option}',
        'silent_copy': 'Тихий или неизмеримый звук скопирован.',
        'silent_copy_no_replaygain': 'Тихий звук скопирован без тегов ReplayGain.',
        'silent_unmeasurable': 'Тихий или неизмеримый звук.',
        'simulation': 'Моделирование',
        'skip_compliant': 'Не перекодировать уже соответствующие файлы',
        'skip_compliant_tooltip': 'Файл в пределах ±0,10 LU от цели и ниже лимита True Peak копируется без '
                                  'перекодирования.',
        'skipped_progress': 'Пропущено: {file}',
        'source_audio_count': 'Файлы: {count}',
        'source_list_more': '… сохранено ещё источников: {count}',
        'source_safety': 'Исходные файлы никогда не перемещаются и не изменяются.',
        'source_selection_tooltip': 'Множественный выбор: Ctrl-щелчок для отдельных элементов, Shift-щелчок для '
                                    'диапазона.',
        'sources_added': 'Добавлено источников: {count}.',
        'start': 'Запустить',
        'status_analyzed': 'ПРОАНАЛИЗИРОВАНО',
        'status_cancelled': 'ОТМЕНЕНО',
        'status_compliant': 'СООТВЕТСТВУЕТ',
        'status_error': 'ОШИБКА',
        'status_ok': 'УСПЕШНО',
        'status_resumed': 'ВОЗОБНОВЛЕНО',
        'status_skipped': 'ПРОПУЩЕНО',
        'status_warning': 'ПРЕДУПРЕЖДЕНИЕ',
        'switch_to_dark': 'Тёмная тема',
        'switch_to_light': 'Светлая тема',
        'tagline': 'Выравнивает воспринимаемую громкость звука',
        'target': 'Целевая громкость',
        'target_tooltip': 'Целевая громкость — это требуемая интегральная громкость всего трека в LUFS. Менее '
                          'отрицательное значение даёт более громкий файл: -14 LUFS громче, чем -16 LUFS. Разница 2 LU '
                          'примерно соответствует разнице уровня 2 дБ до возможного ограничения пиков.\n'
                          '\n'
                          'Ориентиры: -18 LUFS для более спокойного и динамичного результата; -16 LUFS для общего '
                          'баланса; -14 LUFS для более громкого результата в стиле стриминга. Платформы могут затем '
                          'применять собственную нормализацию воспроизведения.\n'
                          '\n'
                          'Сама цель не выравнивает внутреннюю динамику трека. Если максимальный true peak не '
                          'позволяет достичь цели без перегрузки, результат может остаться немного ниже.',
        'theme_accessible': 'Изменить оформление приложения. Выбор сохраняется.',
        'total_time': 'Общее время: {duration}',
        'track_two_pass': 'Двухпроходная нормализация трека.',
        'true_peak_meter_exceeded': 'Превышение {margin} дБ',
        'true_peak_meter_margin': 'Запас {margin} дБ',
        'true_peak_meter_title': 'Запас пика',
        'true_peak_meter_tooltip': 'Сравнивает истинный пик последнего результата с выбранным пределом. Метка '
                                   'показывает последнее значение, треугольник сохраняет наивысший пик серии. Зелёный: '
                                   'предел соблюдён; оранжевый: превышение до 0,25 дБ; красный: больше. Оранжевый '
                                   'допуск относится к контролю качества LUFScale и не является стандартом передачи. '
                                   'Сбрасывается для каждой серии.',
        'true_peak_meter_waiting': 'Ожидание измерения dBTP',
        'version_changes': '• Единый автономный установщик для Windows 10/11 x86-64.\n'
                           '• Включены Python, PySide6/Qt, FFmpeg, кодеки, руководства и лицензии; установка не '
                           'загружает файлы и не требует команд PowerShell.\n'
                           '• Перед созданием установщика и SHA-256 проверяются loudnorm и все кодировщики.',
        'version_changes_title': 'Новое в версии {version}',
        'version_label': 'Версия {version}',
        'volume': 'Громкость',
        'volume_loud': 'Громко: -14 LUFS',
        'volume_normal': 'Обычно: -16 LUFS',
        'volume_soft': 'Тихо: -18 LUFS',
        'volume_tooltip': 'Эта настройка служит быстрым выбором целевой громкости; она не меняет громкость '
                          'воспроизведения системы.\n'
                          '\n'
                          '• Тихо: -18 LUFS — более спокойный уровень, больший динамический запас и меньшая '
                          'вероятность работы лимитера.\n'
                          '• Нормально: -16 LUFS — сбалансированный компромисс и удобная отправная точка для личной '
                          'библиотеки.\n'
                          '• Громко: -14 LUFS — более выразительное звучание, близкое к цели Spotify «Нормально», но '
                          'чаще требующее ограничения.\n'
                          '• Пользовательский — позволяет напрямую ввести другую цель LUFS.\n'
                          '\n'
                          'Это практические варианты, а не универсальный стандарт.',
        'warning_list_title': 'Предупреждения обработки',
        'warnings_button': 'Предупреждения ({count})',
        'warnings_button_tooltip': 'Открывает список предупреждений с именем файла, путём и подробностями. Доступен во '
                                   'время паузы или после обработки.',
        'warnings_dialog_title': 'Предупреждения обработки'},
 'tr': {'activity_cancelled': 'Etkinlik: iptal edildi',
        'activity_cancelling': 'Etkinlik: iptal ediliyor…',
        'activity_completed': 'Etkinlik: tamamlandı',
        'activity_compliant': 'Uygun: {count}',
        'activity_detected': 'Etkinlik: {total} dosya bulundu',
        'activity_errors': 'Hatalar: {count}',
        'activity_files': 'Dosyalar: {count}',
        'activity_idle': 'Etkinlik: bekliyor',
        'activity_preparing': 'Etkinlik: dosyalar hazırlanıyor…',
        'activity_skipped': 'Sürdürülen/atlanan: {count}',
        'activity_successes': 'Başarılı: {count}',
        'activity_warnings': 'Uyarılar: {count}',
        'adaptive_disabled_log': 'Uyarlamalı analiz — {sample} ölçümden sonra hızlı yoklamalar durduruldu ({successes} '
                                 'başarılı, tahmini kazanç %{percent:+.1f}).',
        'add_folders': 'Klasör ekle…',
        'add_mp3': 'Ses dosyası ekle…',
        'add_replaygain': 'ReplayGain ekle',
        'add_source_files': 'Ses dosyaları ekle',
        'add_source_folder': 'Kaynak klasör ekle',
        'already_completed': 'Önceki bir çalışmada zaten tamamlandı.',
        'already_compliant_badge': 'UYGUN',
        'already_compliant_copy': 'Zaten uygun: ses yeniden kodlanmadan, değiştirilmeden kopyalandı.',
        'already_compliant_log': 'zaten uygun, yeniden kodlama yok',
        'analysis_cache_summary': 'Analiz önbelleği — {hits} ölçüm yeniden kullanıldı.',
        'analysis_impossible': 'Analiz başarısız: {error}',
        'analysis_measurement_progress': 'Analiz {current}/{total} — {file} — {value}',
        'analysis_method': 'Analiz yöntemi',
        'analysis_method_adaptive': 'Uyarlamalı — yarar sağlamazsa durur',
        'analysis_method_fast': 'Hızlı — deneysel',
        'analysis_method_historical': 'Tam ölçüm — başvuru yöntemi',
        'analysis_method_tooltip': 'Kararlı sürüm, referans derlem üzerinde doğrulanan tek yöntem olan tam tarihsel '
                                   'ölçümü otomatik olarak kullanır. Hızlı ve Uyarlanabilir yöntemler sunulmaz.',
        'analysis_progress_help_text': 'Yalnızca analizde her ölçüm bittiğinde Önce grafiği, günlük ve ilerleme çubuğu '
                                       'dosya dosya ilerler; Sonra sabit kalır.',
        'analyze': 'Analiz et',
        'analyze_only_fresh_help_text': 'Yalnızca analiz her çalıştırmada her kaynağı FFmpeg ile baştan sona yeniden '
                                        'ölçer. Önce grafiği ve ilerleme dosya dosya gider; çıktı ve çıktı QC yoktur.',
        'analyze_operation': 'analiz/benzetim',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Ses akışı yeniden kodlanmadan kopyalandı; ReplayGain etiketleri eklendi.',
        'audio_tab': 'Ses',
        'auto_start': 'Bırakma veya yapıştırmadan sonra otomatik başlat',
        'auto_start_tooltip': 'Hedef hazırsa kaynak eklenince işlemi başlatır.',
        'cancel': 'İptal',
        'cancelled_summary': 'İptal edildi — {success} başarılı, {failed} hata, {skipped} sürdürüldü/atlandı, '
                             '{warnings} uyarı, {compliant} uygun — {duration}.',
        'cancelling': 'İptal ediliyor…',
        'choose': 'Seç…',
        'choose_output': 'Hedef klasörü seç',
        'clipboard': 'Pano',
        'clipboard_empty': 'Panoda desteklenen bir klasör veya ses yolu yok.',
        'close_button': 'Kapat',
        'close_question': 'İşlemi iptal edip uygulamayı kapatmak istiyor musunuz?',
        'completed_dialog_summary': 'Durum: tamamlandı\n'
                                    'Dosyalar: {files}\n'
                                    'Başarılı: {success}\n'
                                    'Hatalar: {failed}\n'
                                    'Sürdürülen veya atlanan: {skipped}\n'
                                    'Uyarılar: {warnings}\n'
                                    'Uygun: {compliant}\n'
                                    'Toplam süre: {duration}',
        'completed_summary': 'Tamamlandı — {success} başarılı, {failed} hata, {skipped} sürdürüldü/atlandı, {warnings} '
                             'uyarı, {compliant} uygun — {duration}.',
        'completed_with_errors': 'İşlem uyarılarla tamamlandı',
        'convert': 'Normalleştir',
        'convert_operation': 'ses normalleştirme',
        'cpu_tooltip': 'İşlem sırasında sistemin toplam CPU kullanımı.',
        'cpu_usage': 'CPU',
        'create_report': 'CSV raporu oluştur',
        'csv_file_filter': 'CSV dosyaları (*.csv)',
        'custom': 'Özel',
        'decrease_value': 'Değeri azalt',
        'description': 'Orijinalleri değiştirmeden algılanan sesi dosya bazında eşitler.',
        'destination': 'Hedef',
        'destination_error': 'HATA — hedef kullanılamıyor: {error}',
        'destination_path_tooltip': 'Yol seçilebilir ve kopyalanabilir, ancak değiştirilemez.',
        'destination_required_start': 'Başlamadan önce bir hedef klasör seçin.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus · alt klasörler desteklenir',
        'drop_title': 'Klasörleri veya ses dosyalarını buraya bırakın',
        'elapsed_time': 'Geçen süre: {duration}',
        'error_list_title': 'İşlem hataları',
        'errors_button': 'Hatalar ({count})',
        'errors_button_tooltip': 'Dosya adı, yol ve ayrıntıları içeren hata listesini açar. Duraklatıldığında veya '
                                 'işlemden sonra kullanılabilir.',
        'errors_dialog_title': 'İşlem hataları',
        'estimated_result': 'Tahmini sonuç; dosya oluşturulmadı.',
        'estimated_total_calculating': 'Tahmini toplam süre: hesaplanıyor…',
        'estimated_total_time': 'Tahmini toplam süre: {duration}',
        'estimated_total_time_with_day_finish': 'Tahmini toplam süre: {duration} — {days} gün {time}',
        'estimated_total_time_with_finish': 'Tahmini toplam süre: {duration} — yaklaşık {time} biter',
        'estimated_total_unavailable': 'Tahmini toplam süre: kullanılamıyor',
        'ffmpeg_download_button': 'Resmî FFmpeg sitesini aç',
        'ffmpeg_error_no_detail': 'Ayrıntısız FFmpeg hatası.',
        'ffmpeg_execution_error': 'FFmpeg çalıştırılamadı: {error}',
        'ffmpeg_incompatible': 'Uyumsuz FFmpeg',
        'ffmpeg_missing': 'FFmpeg bulunamadı',
        'ffmpeg_missing_encoders': 'Bu FFmpeg yapısı gerekli ses kodlayıcılarının tümünü içermiyor: {encoders}.',
        'ffmpeg_missing_message': 'FFmpeg kurulmalı ve PATH üzerinden erişilebilir olmalı ya da programın yanına '
                                  'yerleştirilmelidir.',
        'ffmpeg_no_lame': 'Bu FFmpeg derlemesinde libmp3lame MP3 kodlayıcısı yok.',
        'ffmpeg_no_loudnorm': 'Bu FFmpeg yapısı loudnorm filtresini içermiyor.',
        'ffmpeg_not_responding': 'FFmpeg doğru yanıt vermiyor.',
        'file_exists': 'Dosya zaten var.',
        'files_found': '{total} ses dosyası bulundu — {operation} — {parallel} paralel işlem.',
        'finalization_completed': 'Sonlandırma {duration} içinde tamamlandı.',
        'finalizing': 'Sonlandırılıyor — rapor, analiz önbelleği ve devam verileri…',
        'folder': 'Klasör',
        'folder_unavailable': 'Klasör kullanılamıyor',
        'guide_analysis_method': 'LUFScale, referans derlem üzerinde doğrulanan tek yöntem olan tam tarihsel ölçümü '
                                 'otomatik olarak kullanır.',
        'guide_analyze_prediction_body': 'Yalnızca analiz sonucu tahmin edebilir ancak ses veya çıktı QC oluşturmaz.',
        'guide_analyze_prediction_title': 'Çıktısız tahmin',
        'guide_build_body': 'Windows 10 1809 veya üzeri ya da Windows 11 x86-64 üzerinde:\n'
                            '\n'
                            '1. “LUFScale-2.1.12-Setup-x64.exe” ve SHA-256 dosyasını indirin.\n'
                            '2. SHA-256 değerini doğrulayın ve yükleyiciye çift tıklayın.\n'
                            '3. GNU GPL lisansını okuyup kabul edin ve sihirbazı izleyin.\n'
                            '4. Başlat menüsünden LUFScale’i çalıştırın.\n'
                            '\n'
                            'Uygulama, Python, PySide6/Qt, FFmpeg, codec bileşenleri, kılavuzlar ve lisanslar zaten '
                            'dahildir. Kurulum hiçbir şey indirmez ve PowerShell komutu gerektirmez. Windows kaldırıcı '
                            'otomatik oluşturulur.\n'
                            '\n'
                            'Dağıtım imzasızdır; dosya ve sağlama toplamını doğruladıktan sonra SmartScreen onay '
                            'isteyebilir.',
        'guide_build_title': 'LUFScale’i Windows x86-64’e kurma',
        'guide_estimated_total_help': 'Tahmini toplam süre: 12 dk - yaklaşık 14:30’da biter. ‘12 dk’ tahmini toplam '
                                      'süre, ‘14:30’ beklenen bitiş saatidir. Gece yarısı aşılırsa gün sayısı saatin '
                                      'önüne otomatik eklenir; örneğin ‘2 g. 14:30’.',
        'guide_file_processing_body': 'Her dosya kendi ölçüm ve kazancıyla True Peak sınırı içinde hedef LUFS’e '
                                      'yaklaşır.',
        'guide_file_processing_title': 'Dosya bazında işlem',
        'guide_help_tooltip': 'Seçilen dilde tam PDF kılavuzunu açar.',
        'guide_level_mode_body': 'Parça - önerilen: her dosyayı hedefe yaklaştırır. Albüm - gelişmiş ve özel: ortak '
                                 'kazanç uygular ve karşıtlıkları korur. Sırayla dinlenen eser için Albüm; karışık '
                                 'çalma veya dosyalar arası düzenli düzey için Parça kullanın.',
        'guide_license_body': 'LUFScale, GNU GPL-3.0-or-later altında dağıtılan özgür yazılımdır. Lisans koşulları '
                              'uyarınca kullanılabilir, incelenebilir, değiştirilebilir ve yeniden dağıtılabilir. '
                              'Kaynak kod, bildirimler ve üçüncü taraf lisansları dağıtıma dahildir. Yazılım '
                              'garantisiz sunulur.',
        'guide_license_feature': '• GNU GPL-3.0-or-later özgür yazılım: lisans kullanım, inceleme, değiştirme ve '
                                 'yeniden dağıtıma izin verir.\n'
                                 '• Python, Qt ve FFmpeg içeren çevrimdışı Windows x86-64 yükleyici. Windows 11 '
                                 'önerilir; Windows 10 1809 veya üzeri uyumluluk hedefidir ancak Microsoft standart '
                                 'desteği sona ermiştir.',
        'guide_license_title': 'Özgür yazılım ve yeniden dağıtım',
        'guide_log_legend_cancelled': 'İşlem kullanıcı tarafından durduruldu; bu bir hata değildir.',
        'guide_log_legend_compliant': 'Ses değiştirilmeden kopyalandı: kaynak hedefi ve tepe sınırını zaten '
                                      'karşılıyordu.',
        'guide_log_legend_error': 'İlgili dosyanın işlemi tamamlanamadı.',
        'guide_log_legend_success': 'İşlem, algılanan bir sorun olmadan tamamlandı.',
        'guide_log_legend_warning': 'Çıkış oluşturuldu, ancak bir ölçüm beklenen toleransın dışında.',
        'guide_missing_message': 'PDF kılavuzu bulunamadı: {path}',
        'guide_missing_title': 'Kılavuz kullanılamıyor',
        'guide_open_error': 'PDF kılavuzu açılamadı: {path}',
        'guide_quality_priority_body': 'LUFScale dosyaların ses yüksekliğini ölçer ve Normalleştir ile gerçek tepeyi '
                                       'denetlerken algılanan düzeyi LUFS hedefine fiziksel olarak ayarlar. Her kaynak '
                                       'baştan sona analiz edilir; ardından çıktı yeniden ölçülür ve doğrulanır. Sonuç '
                                       'etiketlere veya uyumlu bir oynatıcıya bağlı değildir: dosyalar arasındaki '
                                       'düzeyler daha tutarlı olur, sapmalar bildirilir ve özgün dosyalar değişmeden '
                                       'kalır.',
        'guide_quality_priority_title': 'LUFScale ne yapar?',
        'help_button': 'Yardım',
        'help_overview': '• MP3, FLAC, WAV, AIFF, M4A, OGG ve Opus normalleştirme, ReplayGain veya analiz.\n'
                         '• Her dosya ayrı ölçülür ve seçilen hedefe işlenir.\n'
                         '• Klasör yapısı, uyumlu meta veri ve kapak korunur; orijinaller değişmez.\n'
                         '• Paralel işlem, önbellek, sürdürme, QC, CSV, ilerleme, CPU ve LUFS geçmişi.\n'
                         '• 12 dilde arayüz ve PDF kılavuzu.',
        'help_title': 'Temel özellikler',
        'increase_value': 'Değeri artır',
        'input_lufs_log': 'Giriş {value} LUFS',
        'interface_ffmpeg_message': 'Yerleşik FFmpeg ses motoru eksik veya kullanılamıyor. LUFScale’i eksiksiz dağıtım '
                                    'arşivinden yeniden kurun.',
        'internal_error': 'Dahili hata: {error}',
        'interrupted': 'İşlem kesildi.',
        'invalid_location': 'Geçersiz konum',
        'issue_detail_column': 'Ayrıntı',
        'issue_file_column': 'Dosya',
        'issue_path_column': 'Yol',
        'language': 'Dil',
        'language_tooltip': 'Arayüzün, iletilerin ve sonraki CSV raporlarının dilini hemen değiştirir.',
        'log_help_text': 'Her satır bir dosyayı veya genel işlem adımını açıklar.\n'
                         '\n'
                         '• Başarılı satır doğrudan dosya adıyla başlar; BAŞARILI tekrarlanmaz.\n'
                         '• UYUMLU, SÜRDÜRÜLDÜ, ATLANDI, İPTAL EDİLDİ ve HATA yararlı bilgi kattığında gösterilir.\n'
                         '• Düzeyler giriş → yeniden ölçülen çıkış ve ardından varsa kalite kontrol sonucunu '
                         'gösterir.\n'
                         '• Uyarılar ve Hatalar; ad, yol ve ayrıntı içeren ayrı listeler açar. Duraklatma sırasında '
                         'veya işlem sonrasında kullanılabilir ve her liste kaydedilebilir.\n'
                         '\n'
                         'Renkler: yeşil=başarı; turuncu=uyarı; kırmızı=tamamlanmamış dosya; mavi-mor=sürdürme; '
                         'gri=bilgi, atlama veya iptal.\n'
                         '\n'
                         'QC UYARISI—ses yüksekliği, yeniden ölçülen çıkışın beklenen değerden ±0,60 LU’dan fazla '
                         'saptığını belirtir. Daha negatif değer daha kısık, daha az negatif değer daha yüksektir. '
                         'Sapma mutlak farktır: -14,00 yerine -14,69 değeri 0,69 LU farktır. Dosya yine oluşturulur; '
                         'bu bir dönüştürme hatası değildir. Dinleme sonucu uygunsa işlem zorunlu değildir. Kesin '
                         'hedef gerekiyorsa ayrıntıyı ve CSV’yi inceleyin; yeniden denemeden önce hedefi ve True Peak '
                         'tavanını kontrol edin. Mesaj tek başına nedenin tavan, kodlayıcı veya düzeltme sınırı '
                         'olduğunu kanıtlamaz.\n'
                         '\n'
                         'QC UYARISI—tepe, yeniden ölçülen True Peak’in seçilen sınırı 0,25 dB’den fazla aştığını '
                         'belirtir. Dosya yine oluşturulur. Uyarı sürerse daha düşük LUFS hedefi veya örneğin -2,0 '
                         'dBTP gibi daha güvenli bir tepe sınırı seçip yeniden işleyin.\n'
                         '\n'
                         'Birikimli süreler tüm paralel görevlerin çalışmasını toplar. Toplam süre gerçekten geçen '
                         'süredir.',
        'log_placeholder': 'İşlem günlüğü burada görünür.',
        'log_title': 'İşlem günlüğü',
        'loudness_comparison_after': 'Sonra',
        'loudness_comparison_analysis_only': 'Yalnızca analiz modunda çıkış yok',
        'loudness_comparison_before': 'Önce',
        'loudness_comparison_help_text': 'Her dosya sağa bir nokta ekler. Önce her zaman ölçülen kaynağı gösterir. '
                                         'Normalleştir’de Sonra gerçekten yeniden ölçülen çıktıdır. ReplayGain’de '
                                         'kesikli ikinci grafik oynatmayı tahmin eder: kaynak ses düzeyi artı kayıtlı '
                                         'Track Gain. ≈ işareti ve Uyumlu oynatıcı notu bunun teslim edilen dosyanın '
                                         'fiziksel ölçümü olmadığını belirtir. Uyumsuz oynatıcı özgün düzeyi korur; '
                                         'uyumlu oynatıcı da preamp veya kırpma önleme nedeniyle sonucu '
                                         'değiştirebilir. İki grafik aynı sabit ±6 LU ölçeğini korur. Yalnızca Analiz '
                                         'modunda Sonra çıktısı yoktur.',
        'loudness_comparison_increased': 'Fark {value} LU arttı',
        'loudness_comparison_needs_qc': 'Karşılaştırmak için kalite kontrolünü açın',
        'loudness_comparison_no_after': 'Bu işlem için Sonra eğrisi yok',
        'loudness_comparison_not_applicable': 'Bu işlem için karşılaştırma kullanılamaz',
        'loudness_comparison_reached': 'Hedefe ulaşıldı · fark {value} LU',
        'loudness_comparison_reduced': 'Fark {value} LU azaldı',
        'loudness_comparison_replaygain_after': 'Tahmini RG oynatma',
        'loudness_comparison_replaygain_note': 'Uyumlu oynatıcı · ses değişmedi',
        'loudness_comparison_scale': 'Görünüm ±{scale} LU · QC tol. ±{tolerance} LU',
        'loudness_comparison_target': 'Hedef {value} LUFS',
        'loudness_comparison_title': 'Ses yüksekliği değişimi',
        'loudness_comparison_tooltip': 'Önce fiziksel ses düzeyini gösterir. ReplayGain’de ikinci grafik kayıtlı '
                                       'kazançtan uyumlu oynatmayı tahmin eder.',
        'loudness_comparison_unchanged': 'Fark değişmedi',
        'loudness_comparison_waiting': 'İşlenmiş dosya bekleniyor',
        'loudness_meter_estimated': 'Tahmini',
        'loudness_meter_help_text': 'Ölçer, son yeniden ölçülen çıkışı ayarlı hedefle karşılaştırır. Değer ve eğri '
                                    'dosya başına güncellenir; anlık oynatma düzeyi değil, dosyanın tümleşik ses '
                                    'yüksekliğidir. Otomatik kalite kontrol kapalıysa veya çıkış üretmeyen Yalnızca '
                                    'analiz işleminde etkin olmaması normaldir.',
        'loudness_meter_measured': 'Ölçülen',
        'loudness_meter_no_file': 'Analiz bekleniyor',
        'loudness_meter_title': 'Ses yüksekliği ölçeri',
        'loudness_meter_tooltip': 'Kırmızı hedefi, mavi ise son çıktının gerçekten yeniden ölçülen ses yüksekliğini '
                                  'gösterir.',
        'loudness_meter_waiting': 'Ses dosyası bekleniyor',
        'loudness_score_acceptable': 'Kabul edilebilir',
        'loudness_score_check': 'Uyarıları görüntüle',
        'loudness_score_excellent': 'Mükemmel',
        'loudness_score_needs_qc': 'Hedef puanı: kalite kontrolünü etkinleştirin',
        'loudness_score_not_applicable': 'Hedef puanı: uygulanamaz',
        'loudness_score_tooltip': 'Puan, gerçekten yeniden ölçülen son 8 çıktıyı kullanır. 100 tam eşleşme, 50 değeri '
                                  '0,60 LU RMS hatası, 0 ise 1,20 LU veya üzeridir. Kırmızı panel, Uyarılar düğmesiyle '
                                  'incelenebilecek en az bir ses yüksekliği uyarısı olduğunu gösterir.',
        'loudness_score_waiting': 'Hedef puanı: bekleniyor',
        'measurement_unavailable': 'Ölçüm kullanılamıyor',
        'mp3_filter': 'Desteklenen ses (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Klasör seçilmedi',
        'no_mp3': 'Desteklenen ses dosyası bulunamadı.',
        'no_new_source': 'Yeni ses kaynağı yok.',
        'not_performed': 'Yapılmadı',
        'open_output_error': 'Hedef klasör açılamadı: {error}',
        'operation': 'İşlem',
        'operation_analyze': 'Yalnızca analiz — dosya oluşturmaz',
        'operation_analyze_label': 'Yalnızca analiz — dosyasız benzetim',
        'operation_convert': 'Eşitle — sesi gerçekten normalleştir',
        'operation_convert_label': 'Normalleştir — sesi gerçekten ayarla',
        'operation_help_text': 'Normalleştirme her dosyayı ayrı işler, True Peak sınırı altında LUFS hedefini amaçlar '
                               've çıktıyı yeniden ölçer. ReplayGain ses örneklerini değiştirmez. Yalnızca analiz '
                               'ölçümler ve istenirse CSV raporu üretir, ses dosyası oluşturmaz.',
        'operation_replaygain': 'ReplayGain — sesi yeniden kodlamaz',
        'operation_replaygain_label': 'ReplayGain — sesi yeniden kodlama',
        'operation_tooltip': 'Normalleştirme sesi değiştirir. ReplayGain akışı kopyalayıp etiket ekler. Yalnızca '
                             'analiz ses dosyası oluşturmaz.',
        'option_status_auto_start': 'OTO',
        'option_status_overwrite': 'ÜZER',
        'option_status_quality_control': 'KAL',
        'option_status_report': 'CSV',
        'option_status_resume': 'SÜR',
        'option_status_skip_compliant': 'ATLA',
        'options_tab': 'Seçenekler',
        'output_lufs_unavailable': 'çıkış LUFS değeri kullanılamıyor',
        'overwrite': 'Var olan dosyaların üzerine yaz',
        'overwrite_tooltip': 'Yalnızca hedef dosyaları değiştirir, kaynaklara dokunmaz.',
        'parallel': 'Paralel işlemler',
        'parallel_adjusted': 'Otomatik paralellik — {active} işlem, CPU %{cpu:.0f}.',
        'parallel_auto': 'Otomatik',
        'parallel_auto_log': 'otomatik, en çok {maximum}',
        'parallel_tooltip': 'Aynı anda kaç dosyanın işlenebileceğini belirler.\n'
                            '\n'
                            '• Otomatik en fazla 4 görevle başlar. CPU ölçümü varsa her saniye denetler: kullanım '
                            '%70’in altındayken bir görev ekler, %92’nin üstündeyken bir görev çıkarır.\n'
                            '• Otomatik, algılanan mantıksal işlemci sayısını aşmaz ve mutlak sınır 16 görevdir.\n'
                            '• CPU ölçümü yoksa algılanan sınırı dinamik uyarlama olmadan doğrudan kullanır.\n'
                            '• Sayısal değer eşzamanlı görevlerin üst sınırıdır; CPU kullanım hedefi değildir.\n'
                            '\n'
                            'Daha fazla görev büyük grubu hızlandırabilir, ancak yükü, sıcaklığı ve disk erişimini '
                            'artırır. Otomatik görünene kadar − düğmesine basın.',
        'paste': 'Yapıştır',
        'path_left': 'Yolun sol bölümünü göster',
        'path_right': 'Yolun sağ bölümünü göster',
        'pause': 'Duraklat',
        'peak': 'En yüksek true peak',
        'peak_tooltip': 'Maksimum true peak ulaşılacak bir seviye değil, üst sınırdır. Kodlama veya dönüştürme sonrası '
                        'kırpma riskini azaltmak için örnekler arasındaki tepeler dahil yeniden oluşturulan dalganın '
                        'en yüksek noktalarını dBTP olarak sınırlar.\n'
                        '\n'
                        '• -1,0 dBTP — en yüksek çıkış tepe seviyesine sahip yaygın teslim sınırı.\n'
                        '• -1,5 dBTP — varsayılan ve MP3 için temkinli uzlaşma.\n'
                        '• -2,0 dBTP — yeniden kodlanacak dosyalar veya yüksek ses hedefi için ek pay.\n'
                        '• 0 dBTP — hiç pay yok; MP3 için önerilmez.\n'
                        '\n'
                        'Daha negatif değer daha fazla korur, ancak çok dinamik parçaların LUFS hedefine tam '
                        'ulaşmasını engelleyebilir.',
        'phase_summary': 'Tahmini toplam süre dağılımı — analiz {analysis}, dönüştürme {conversion}, kalite kontrolü '
                         '{quality}.',
        'pipeline_enabled': 'Parça işlem hattı — her dönüştürme kendi analizi biter bitmez başlar.',
        'pre_measurement': 'Girdi dosyaları ölçülüyor…',
        'preset': 'Ön ayar',
        'preset_dynamic': 'Dinamik müzik',
        'preset_library': 'Müzik arşivi — önerilen',
        'preset_streaming': 'Daha güçlü akış',
        'preset_tooltip': 'Tutarlı bir ses yüksekliği hedefini, maksimum true peak değerini ve ses kalitesini tek '
                          'seferde uygular. Her elle değişiklik Özel seçeneğini seçer.',
        'processing_cancelled': 'İşlem iptal edildi.',
        'processing_completed': 'İşlem tamamlandı',
        'processing_in_progress': 'İşleniyor…',
        'processing_paused': 'İşlem duraklatıldı.',
        'processing_resumed': 'İşlem sürdürülüyor.',
        'qc_impossible': 'Kalite kontrolü yapılamadı: {error}',
        'qc_log': ' — kalite kontrolü: {quality}',
        'qc_ok': 'Kalite kontrolü: uygun',
        'qc_warning': 'Kalite kontrolü UYARISI — {detail}',
        'quality': 'Ses kalitesi',
        'quality_control': 'Otomatik kalite kontrolü',
        'quality_control_tooltip': 'Her çıktıyı yeniden ölçer. Düzeltmeler ±0,50 LU değerini hedeflemeyi sürdürür; ses '
                                   'yüksekliği uyarısı yalnız ±0,60 LU dışına çıkıldığında görünür. Dinamik MP3 '
                                   'dosyalarında en fazla 3 düzeltme denemesi vardır; True Peak payı izin verirse WAV, '
                                   'AIFF ve FLAC kaynaktan en fazla 2 kez yeniden denenebilir. Bu seçeneği kapatmak '
                                   'doğrulamayı, yeniden denemeleri ve ölçer etkinliğini kaldırır.',
        'quality_tooltip': 'Sıkıştırılmış biçimlerde kalite/boyut dengesini ayarlar. Sayı küçüldükçe kalite ve bitrate '
                           'yükselir. Bu ayar LUFS hedefini veya maksimum true peak değerini değiştirmez.\n'
                           '\n'
                           '• 0 — ayrıntıları korumak için önerilen maksimum kalite.\n'
                           '• 1-2 — çok yüksek kalite.\n'
                           '• 3-4 — iyi kalite/boyut dengesi.\n'
                           '• 5-9 — daha fazla kayıpla daha küçük dosyalar.\n'
                           '\n'
                           'FLAC her değerde kayıpsız kalır. WAV ve AIFF bu ayarı yok sayar, kaynakla uyumlu PCM '
                           'örnekleme hızını ve bit derinliğini korur. MP3, M4A, OGG ve Opus için düşük değer '
                           'kaynaktan daha yüksek bitrate isteyip çıktıyı büyütebilir. Yüksek değer çoğunlukla boyutu '
                           'düşürür; ancak bu kodlayıcılar sıkça VBR kullandığından aynı byte sayısını garanti etmez. '
                           'Kayıplı biçimi yeniden kodlamak daha önce kaybolan bilgiyi geri getirmez.',
        'ready': 'Hazır',
        'recursive_scan': 'Klasörler özyinelemeli taranıyor…',
        'remove_all': 'Tümünü kaldır',
        'remove_selection': 'Seçimi kaldır',
        'replaygain_help_text': 'ReplayGain kazanç hesaplayıp REPLAYGAIN_TRACK_GAIN/PEAK yazar. Ses yeniden '
                                'kodlanmadan kopyalanır (-c:a copy); etiketleri yalnız uyumlu oynatıcı uygular. '
                                'Fiziksel LUFS ve True Peak değişmez.',
        'replaygain_levels_log': 'ses değişmedi: {before} LUFS · meta veride ReplayGain {gain} dB · ayarlanan hedef '
                                 '{target} LUFS (uyumlu oynatıcı gerekir)',
        'replaygain_log_help_text': 'ReplayGain’de günlük değişmeyen fiziksel ses yüksekliğini, metaveriye yazılan '
                                    'kazancı ve ayarlanan hedefi gösterir. Kalite kontrolü açıkken ‘ses değişmedi ve '
                                    'etiketler doğrulandı’, ses yüksekliği ile tepenin kaynakla karşılaştırıldığı ve '
                                    'etiketlerin yeniden okunduğu anlamına gelir; dosyanın fiziksel olarak hedefte '
                                    'ölçüldüğü anlamına gelmez.',
        'replaygain_operation': 'Yeniden kodlamasız ReplayGain',
        'replaygain_qc_help_text': 'Kalite kontrolü açıkken ReplayGain teslim edilen dosyayı yeniden ölçerek fiziksel '
                                   'ses yüksekliği ile tepenin değişmediğini doğrular, ardından Track etiketlerini '
                                   'denetler. Başarı, sesin korunduğunu ve etiketlerin bulunduğunu doğrular; fiziksel '
                                   'hedefe ulaşıldığını değil.',
        'replaygain_qc_ok': 'BAŞARILI — ses değişmedi ve etiketler doğrulandı',
        'replaygain_tags_missing': 'ReplayGain etiketleri bulunamadı.',
        'replaygain_usefulness_text': 'ReplayGain, uyumlu bir oynatıcıyla kullanılan arşivde yeniden kodlama olmadan, '
                                      'geri alınabilir çalma düzeyi eşitlemesi için yararlıdır. Her oynatıcıda '
                                      'fiziksel olarak hedefte ölçülen bir dosya teslim etmek için Normalleştirme '
                                      'kullanın.',
        'report_destination': 'hedef',
        'report_detail': 'ayrıntı',
        'report_error': 'UYARI — CSV raporu oluşturulamadı: {error}',
        'report_filename_prefix': 'LUFScale_Raporu',
        'report_gain': 'kazanç_dB',
        'report_input_dbtp': 'giriş_dBTP',
        'report_input_lufs': 'giriş_LUFS',
        'report_log': 'CSV raporu — {path}',
        'report_operation': 'işlem',
        'report_output_dbtp': 'çıkış_dBTP',
        'report_output_lufs': 'çıkış_LUFS',
        'report_path': 'Rapor: {path}',
        'report_qc': 'kalite_kontrolü',
        'report_qc_engine': 'kalite_kontrol_motoru',
        'report_seconds': 'geçen_saniye',
        'report_source': 'kaynak',
        'report_status': 'durum',
        'report_tooltip': 'Yalnız ölçüm, süre ve uyarı içeren CSV oluşturur; tanı JSON’u eklemez.',
        'resume': 'Kesintiden sonra sürdür',
        'resume_not_saved': ' Devam noktası kaydedilmedi: {error}',
        'resume_processing': 'Sürdür',
        'resume_tooltip': 'Aynı ayarlarla tamamlanan dosyaları tanır.',
        'save_dialog_cancel': 'İptal',
        'save_dialog_filename': 'Dosya adı',
        'save_dialog_filetype': 'Biçim',
        'save_dialog_location': 'Klasör',
        'save_dialog_overwrite': 'Değiştir',
        'save_dialog_overwrite_message': '“{file}” dosyası zaten var.',
        'save_dialog_overwrite_title': 'Dosya değiştirilsin mi?',
        'save_dialog_parent': 'Üst klasör',
        'save_dialog_save': 'Kaydet',
        'save_issue_list': 'CSV olarak kaydet…',
        'save_issue_list_error': 'Liste kaydedilemedi: {error}',
        'save_issue_list_error_title': 'Kaydedilemedi',
        'save_issue_list_title': 'CSV listesini kaydet',
        'scan_error': 'HATA — {error}',
        'scanning_folders': 'Klasörler taranıyor…',
        'settings': 'Ayarlar',
        'open_folder': 'Klasörü aç',
        'show_option_help': 'Yardımı göster: {option}',
        'silent_copy': 'Sessiz veya ölçülemeyen ses kopyalandı.',
        'silent_copy_no_replaygain': 'Sessiz ses, ReplayGain etiketi olmadan kopyalandı.',
        'silent_unmeasurable': 'Sessiz veya ölçülemeyen ses.',
        'simulation': 'Benzetim',
        'skip_compliant': 'Zaten uygun dosyaları atla',
        'skip_compliant_tooltip': 'Hedefin ±0,10 LU aralığında ve True Peak sınırı altında olan dosya yeniden '
                                  'kodlanmadan kopyalanır.',
        'source_audio_count': 'Dosyalar: {count}',
        'source_list_more': '… {count} kaynak daha korundu',
        'source_safety': 'Kaynak dosyalar taşınmaz veya değiştirilmez.',
        'source_selection_tooltip': 'Birden çok seçim: ayrı öğeler için Ctrl-tıklama, aralık için Shift-tıklama kullanın.',
        'sources_added': '{count} kaynak eklendi.',
        'start': 'Başlat',
        'status_analyzed': 'ANALİZ EDİLDİ',
        'status_cancelled': 'İPTAL',
        'status_compliant': 'UYGUN',
        'status_error': 'HATA',
        'status_ok': 'BAŞARILI',
        'status_resumed': 'SÜRDÜRÜLDÜ',
        'status_skipped': 'ATLANDI',
        'status_warning': 'UYARI',
        'switch_to_dark': 'Koyu mod',
        'switch_to_light': 'Açık mod',
        'tagline': 'Kaynakları koruyarak algılanan ses yüksekliğini eşitler.',
        'target': 'Ses yüksekliği hedefi',
        'target_tooltip': 'Ses yüksekliği hedefi, tüm parçanın LUFS cinsinden istenen tümleşik ses yüksekliğidir. Daha '
                          'az negatif değer daha yüksek bir dosya üretir: -14 LUFS, -16 LUFS’tan daha yüksektir. 2 LU '
                          'fark, tepe sınırlamasından önce yaklaşık 2 dB seviye farkıdır.\n'
                          '\n'
                          'Kılavuz: daha sakin ve dinamik sonuç için -18 LUFS; genel denge için -16 LUFS; streaming '
                          'tarzı daha yüksek sonuç için -14 LUFS. Platformlar daha sonra kendi çalma '
                          'normalizasyonlarını uygulayabilir.\n'
                          '\n'
                          'Bu hedef parçanın iç dinamiklerini tek başına düzleştirmez. Maksimum true peak kırpma '
                          'olmadan hedefe ulaşmayı engellerse sonuç biraz daha düşük kalabilir.',
        'theme_accessible': 'Açık ve koyu mod arasında geçiş yap',
        'total_time': 'Toplam süre: {duration}',
        'track_two_pass': 'İki geçişli parça normalleştirmesi.',
        'true_peak_meter_title': 'Gerçek tepe payı',
        'true_peak_meter_tooltip': 'Son çıktının gerçek tepesini seçilen üst sınırla karşılaştırır. İşaret son değeri, '
                                   'üçgen ise grubun en yüksek tepesini tutar. Yeşil sınırın karşılandığını, kehribar '
                                   'en çok 0,25 dB aşımı, kırmızı daha büyük aşımı gösterir. Kehribar tolerans '
                                   'LUFScale kalite kontrolüne aittir ve teslim standardı değildir. Grafik her grupta '
                                   'sıfırlanır.',
        'true_peak_meter_waiting': 'dBTP ölçümü bekleniyor',
        'version_changes': '• Windows 10/11 x86-64 için tek dosyalı çevrimdışı yükleyici.\n'
                           '• Python, PySide6/Qt, FFmpeg, codec bileşenleri, kılavuzlar ve lisanslar dahildir; kurulum '
                           'sırasında indirme veya PowerShell komutu gerekmez.\n'
                           '• Setup ve SHA-256 oluşturulmadan önce loudnorm ve tüm kodlayıcılar doğrulanır.',
        'version_changes_title': '{version} sürümündeki yenilikler',
        'version_label': 'Sürüm {version}',
        'volume': 'Ses düzeyi',
        'volume_loud': 'Güçlü: -14 LUFS',
        'volume_normal': 'Normal: -16 LUFS',
        'volume_soft': 'Yumuşak: -18 LUFS',
        'volume_tooltip': 'Bu ayar ses yüksekliği hedefinin kısayoludur; sistemin çalma sesini değiştirmez.\n'
                          '\n'
                          '• Yumuşak: -18 LUFS — daha sakin seviye, daha fazla dinamik pay ve limiterin devreye girme '
                          'olasılığı daha düşük.\n'
                          '• Normal: -16 LUFS — dengeli bir uzlaşma ve kişisel arşiv için iyi bir başlangıç.\n'
                          '• Yüksek: -14 LUFS — Spotify Normal çalma hedefine yakın, daha belirgin bir seviye; ancak '
                          'daha fazla sınırlama gerekebilir.\n'
                          '• Özel — başka bir LUFS hedefini doğrudan girmeyi sağlar.\n'
                          '\n'
                          'Bunlar pratik seçimlerdir, evrensel bir standart değildir.',
        'warning_list_title': 'İşlem uyarıları',
        'warnings_button': 'Uyarılar ({count})',
        'warnings_button_tooltip': 'Dosya adı, yol ve ayrıntıları içeren uyarı listesini açar. Duraklatıldığında veya '
                                   'işlemden sonra kullanılabilir.',
        'warnings_dialog_title': 'İşlem uyarıları'},
 'zh': {'activity_cancelled': '活动：处理已取消',
        'activity_cancelling': '活动：正在取消…',
        'activity_completed': '活动：处理完成',
        'activity_compliant': '合规：{count}',
        'activity_detected': '活动：检测到 {total} 个文件',
        'activity_errors': '错误：{count}',
        'activity_files': '文件：{count}',
        'activity_idle': '活动：等待中',
        'activity_preparing': '活动：正在准备文件…',
        'activity_progress': '{total} 个文件 • 成功 {success} • 警告 {warnings} • 错误 {failed} • 已续传/跳过 {skipped} • 合规 '
                             '{compliant}',
        'activity_skipped': '已续传/跳过：{count}',
        'activity_successes': '成功：{count}',
        'activity_warnings': '警告：{count}',
        'adaptive_disabled_log': '自适应分析 — 在{sample}次测量后停止快速探测（成功{successes}次，估算节省{percent:+.1f}%）。',
        'add_folders': '添加文件夹…',
        'add_mp3': '添加音频文件…',
        'add_replaygain': '添加 ReplayGain',
        'add_source_files': '添加音频文件',
        'add_source_folder': '添加来源文件夹',
        'already_completed': '已在上一次运行中完成。',
        'already_compliant_badge': '已符合',
        'already_compliant_copy': '已符合要求：原样复制，不重新编码音频。',
        'already_compliant_log': '已符合要求，未重新编码',
        'analysis_cache_summary': '分析缓存 — 重用了 {hits} 个测量结果。',
        'analysis_impossible': '分析失败：{error}',
        'analysis_measurement_progress': '分析 {current}/{total} — {file} — {value}',
        'analysis_method': '分析方法',
        'analysis_method_adaptive': '自适应 — 无收益时停止',
        'analysis_method_fast': '快速方式 — 实验',
        'analysis_method_historical': '历史方式 — 基准',
        'analysis_method_log': '分析方法 — {method}。',
        'analysis_method_tooltip': '稳定版自动使用完整的历史参考测量，这是唯一经过参考语料验证的方法。快速和自适应方式不再提供。',
        'analysis_progress': '分析 {current}/{total}：{file}',
        'analysis_progress_help_text': '仅分析时，每完成一个文件，处理前图表、日志和进度条都会更新；处理后图表保持不动。',
        'analyze': '分析',
        'analyze_only_fresh_help_text': '仅分析每次都用FFmpeg完整复测每个源文件。处理前图和进度逐文件更新；没有输出文件和输出质检。',
        'analyze_operation': '分析/模拟',
        'analyzed_progress': '已分析：{file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': '音频流未经重新编码已复制；已添加 ReplayGain 标签。',
        'audio_tab': '音频',
        'auto_start': '拖放或粘贴后自动开始',
        'auto_start_tooltip': '已选择目标位置时，通过拖放或粘贴添加来源后自动开始处理。',
        'cancel': '取消',
        'cancelled_summary': '已取消 — 成功 {success}，错误 {failed}，续传/跳过 {skipped}，警告 {warnings}，合规 {compliant} — '
                             '{duration}。',
        'cancelling': '正在取消…',
        'choose': '选择…',
        'choose_output': '选择目标文件夹',
        'clipboard': '剪贴板',
        'clipboard_empty': '剪贴板中没有有效的文件夹或受支持音频文件路径。',
        'close_button': '关闭',
        'close_question': '取消处理并关闭应用？',
        'completed_dialog_summary': '状态：已完成\n'
                                    '文件数：{files}\n'
                                    '成功：{success}\n'
                                    '错误：{failed}\n'
                                    '续传或跳过：{skipped}\n'
                                    '警告：{warnings}\n'
                                    '合规：{compliant}\n'
                                    '总时间：{duration}',
        'completed_summary': '已完成 — 成功 {success}，错误 {failed}，续传/跳过 {skipped}，警告 {warnings}，合规 {compliant} — '
                             '{duration}。',
        'completed_with_errors': '处理完成，但有警告',
        'convert': '统一响度',
        'convert_operation': '音频标准化',
        'cpu_tooltip': '处理期间每秒更新一次的 系统总 CPU 使用率。',
        'cpu_unavailable': '不可用',
        'cpu_usage': 'CPU',
        'create_report': '创建 CSV 报告',
        'csv_file_filter': 'CSV 文件 (*.csv)',
        'custom': '自定义',
        'decrease_value': '减小数值',
        'description': '不改动原文件，逐个文件统一感知响度。',
        'destination': '目标位置',
        'destination_error': '错误 — 目标位置不可用：{error}',
        'destination_path_tooltip': '单击路径，然后使用方向键、Home/End 或鼠标滚轮浏览。路径可以选择和复制，但不能修改。',
        'destination_required_start': '请先用“选择…”按钮选择目标文件夹。',
        'dialog_ok': '确定',
        'drop_subtitle': 'MP3、FLAC、WAV、AIFF、M4A、OGG、Opus — 支持子文件夹',
        'drop_title': '将文件夹或音频文件拖放到这里',
        'elapsed_time': '已用时间：{duration}',
        'error_list_title': '处理错误',
        'error_progress': '错误：{file}',
        'errors_button': '错误 ({count})',
        'errors_button_tooltip': '打开错误列表，其中包含文件名、路径和详情。暂停期间或处理结束后可用。',
        'errors_dialog_title': '处理错误',
        'estimated_result': '估算结果；未创建文件。',
        'estimated_total_calculating': '预计总时间：正在计算…',
        'estimated_total_time': '预计总时间：{duration}',
        'estimated_total_time_with_day_finish': '预计总时间：{duration} — {days} 天。{time}',
        'estimated_total_time_with_finish': '预计总时间：{duration} — {time}',
        'estimated_total_unavailable': '预计总时间：不可用',
        'ffmpeg_download_button': '打开 FFmpeg 官方网站',
        'ffmpeg_error_no_detail': 'FFmpeg 错误，无详细信息。',
        'ffmpeg_execution_error': '无法运行 FFmpeg：{error}',
        'ffmpeg_incompatible': 'FFmpeg 不兼容',
        'ffmpeg_missing': '找不到 FFmpeg',
        'ffmpeg_missing_encoders': '此 FFmpeg 未包含全部所需音频编码器：{encoders}。',
        'ffmpeg_missing_message': '必须安装 FFmpeg 并使其可从 PATH 访问，或将其放在程序旁边。',
        'ffmpeg_no_lame': '此 FFmpeg 版本不包含 libmp3lame MP3 编码器。',
        'ffmpeg_no_loudnorm': '此 FFmpeg 版本不包含 loudnorm 滤镜。',
        'ffmpeg_not_responding': 'FFmpeg 未正确响应。',
        'file_exists': '文件已经存在。',
        'files_found': '找到 {total} 个音频文件 — {operation} — {parallel} 个并行进程。',
        'finalization_completed': '最终处理在 {duration} 内完成。',
        'finalizing': '最终处理 — 报告、分析缓存和恢复数据…',
        'folder': '文件夹',
        'folder_unavailable': '文件夹不可用',
        'guide_analysis_method': 'LUFScale 自动使用完整的历史测量方法，这是唯一在参考语料上验证过的方法。',
        'guide_analyze_prediction_body': '仅分析可估算结果，但不创建音频或输出质检。',
        'guide_analyze_prediction_title': '无输出估算',
        'guide_build_body': '在 Windows 10 1809 或更高版本、或 Windows 11 x86-64 上：\n'
                            '\n'
                            '1. 下载“LUFScale-2.1.12-Setup-x64.exe”及其 SHA-256 文件。\n'
                            '2. 验证 SHA-256，然后双击安装程序。\n'
                            '3. 阅读并接受 GNU GPL 许可证，然后按向导操作。\n'
                            '4. 从开始菜单启动 LUFScale。\n'
                            '\n'
                            '应用程序、Python、PySide6/Qt、FFmpeg、编解码器、指南和许可证均已包含。安装过程不会下载任何内容，也不需要 PowerShell 命令，并会自动创建 Windows 卸载程序。\n'
                            '\n'
                            '社区版未签名；检查文件及其校验和后，SmartScreen 可能要求确认。',
        'guide_build_title': '在 Windows x86-64 上安装 LUFScale',
        'guide_estimated_total_help': '预计总时间：12分钟 - '
                                      '约14:30完成。“12分钟”是预计总时长，“14:30”是预计结束时刻。跨过午夜时，会自动在时刻前加入天数，例如“2天。14:30”。',
        'guide_file_processing_body': '每个文件按自身测量计算增益，在True Peak上限内接近目标LUFS。',
        'guide_file_processing_title': '逐文件处理',
        'guide_help_tooltip': '打开所选语言的完整 PDF 指南。',
        'guide_level_mode_body': '单曲（推荐）让每个文件接近目标。专辑是高级专用模式，用共同增益保留曲目对比。按顺序聆听完整作品时用专辑；随机播放或要求文件间音量稳定时用单曲。',
        'guide_license_body': 'LUFScale是依据GNU '
                              'GPL-3.0-or-later发布的自由软件。用户可按许可证条款使用、研究、修改和再分发。发行包包含源代码、声明及第三方许可证。本软件不提供担保。',
        'guide_license_feature': '• GNU GPL-3.0-or-later 自由软件：许可允许使用、研究、修改和再分发。\n'
                                 '• Windows x86-64 离线安装程序，内含 Python、Qt 和 FFmpeg。建议使用 Windows 11；Windows 10 1809 '
                                 '或更高版本仍为兼容目标，但 Microsoft 标准支持已结束。',
        'guide_license_title': '自由软件与再分发',
        'guide_log_legend_cancelled': '处理由用户主动停止；这不是错误。',
        'guide_log_legend_compliant': '音频未改动并直接复制：源文件已满足目标值和峰值上限。',
        'guide_log_legend_error': '无法完成相关文件的处理。',
        'guide_log_legend_success': '处理完成，未检测到异常。',
        'guide_log_legend_warning': '输出文件已生成，但有一项测量超出预期容差。',
        'guide_missing_message': '找不到 PDF 指南：{path}',
        'guide_missing_title': '指南不可用',
        'guide_open_error': '无法打开 PDF 指南：{path}',
        'guide_quality_priority_body': 'LUFScale 测量文件响度；使用“标准化”时，它会在控制真峰值的同时，把感知音量实际调整到 LUFS '
                                       '目标。每个源文件都会进行全时长分析，输出随后会被重新测量和验证。结果不依赖标签或兼容播放器：文件之间的音量更一致，偏差会被标出，原文件保持不变。',
        'guide_quality_priority_title': 'LUFScale 有什么作用？',
        'help_button': '帮助',
        'help_overview': '• 支持MP3、FLAC、WAV、AIFF、M4A、OGG和Opus的均一化、ReplayGain或分析。\n'
                         '• 每个文件单独测量并处理到所选目标。\n'
                         '• 保留目录、兼容元数据和封面；原文件不变。\n'
                         '• 并行处理、缓存、续传、质检、CSV、进度、CPU和LUFS历史。\n'
                         '• 十二种语言的界面与PDF指南。',
        'help_title': '主要功能',
        'increase_value': '增大数值',
        'input_lufs_log': '输入 {value} LUFS',
        'interface_ffmpeg_message': '内置 FFmpeg 音频引擎缺失或无法使用。请从完整发行压缩包重新安装 LUFScale。',
        'internal_error': '内部错误：{error}',
        'interrupted': '处理已中断。',
        'invalid_location': '位置无效',
        'issue_detail_column': '详情',
        'issue_file_column': '文件',
        'issue_path_column': '路径',
        'language': '语言',
        'language_tooltip': '立即更改界面、消息和后续 CSV 报告的语言，并记住所选语言。',
        'log_help_text': '每一行描述一个文件或一般处理步骤。\n'
                         '\n'
                         '• 成功行直接以文件名开头，不再重复“成功”。\n'
                         '• 合规、已续传、已跳过、已取消和错误只在能提供有用信息时显示。\n'
                         '• 电平显示输入 → 重新测量的输出，随后显示可能的质量控制结果。\n'
                         '• “警告”和“错误”分别打开含文件名、路径和详情的列表；暂停期间或处理结束后可用，每个列表都能保存。\n'
                         '\n'
                         '颜色：绿色＝成功；橙色＝警告；红色＝文件未完成；蓝紫色＝续传；灰色＝信息、跳过或取消。\n'
                         '\n'
                         'QC 警告—响度表示重新测量的输出与预期值相差超过 ±0.60 LU。数值越负越安静，越不负越响。偏差取绝对值：目标 -14.00、结果 -14.69 的偏差为 0.69 '
                         'LU。文件仍会创建，这不是转换失败。若听感可接受，无需强制处理；若目标必须严格，请查看详情和 CSV，核对目标与 True Peak '
                         '上限后重试。仅凭这条消息不能确定原因是上限、编码器还是修正能力限制。\n'
                         '\n'
                         'QC 警告—峰值表示重新测量的 True Peak 超出所选上限 0.25 dB 以上。文件仍会创建。若警告持续，请选择更低的 LUFS 目标或更稳妥的峰值上限（例如 -2.0 '
                         'dBTP），再重新处理。\n'
                         '\n'
                         '累计时间是所有并行任务工作量之和；总时间是实际经过的时长。',
        'log_placeholder': '处理日志将显示在此处。',
        'log_title': '处理日志',
        'loudness_comparison_after': '处理后',
        'loudness_comparison_analysis_only': '仅分析模式不生成输出',
        'loudness_comparison_before': '处理前',
        'loudness_comparison_help_text': '每个文件都会在右侧添加一个点。“之前”始终显示测得的源文件。使用标准化时，“之后”显示实际复测的输出。使用 ReplayGain '
                                         '时，第二个虚线图表估算播放效果：源响度加上写入的 Track Gain。≈ '
                                         '符号和“兼容播放器”说明表明这不是交付文件的物理测量。播放器不兼容时仍使用原始音量；兼容播放器也可能因前置增益或削波保护而改变结果。两个图表保持相同的固定 '
                                         '±6 LU 标尺。仅分析模式没有“之后”输出。',
        'loudness_comparison_increased': '偏差增加 {value} LU',
        'loudness_comparison_needs_qc': '启用质量控制后才能比较',
        'loudness_comparison_no_after': '此操作不显示处理后曲线',
        'loudness_comparison_not_applicable': '此操作无法进行前后比较',
        'loudness_comparison_reached': '达到目标 · 偏差 {value} LU',
        'loudness_comparison_reduced': '偏差减少 {value} LU',
        'loudness_comparison_replaygain_after': 'RG 播放估算',
        'loudness_comparison_replaygain_note': '兼容播放器 · 音频未改变',
        'loudness_comparison_scale': '显示 ±{scale} LU · QC容差 ±{tolerance} LU',
        'loudness_comparison_target': '目标 {value} LUFS',
        'loudness_comparison_title': '响度变化',
        'loudness_comparison_tooltip': '“之前”显示物理响度。ReplayGain 的第二个图表根据写入的增益估算兼容播放器的播放效果。',
        'loudness_comparison_unchanged': '偏差未变化',
        'loudness_comparison_waiting': '等待已处理文件',
        'loudness_meter_current_file': '最新：{file}',
        'loudness_meter_estimated': '估算',
        'loudness_meter_help_text': '红线是目标，蓝色数值是最后一个输出实际复测的响度，并会随每个文件上下移动。评分汇总最近8个复测输出。如果红色面板显示“查看警告”，请暂停处理或等待完成，然后打开“警告”以确定相关文件。',
        'loudness_meter_maximum': '最大 {value}',
        'loudness_meter_measured': '实测',
        'loudness_meter_minimum': '最小 {value}',
        'loudness_meter_no_file': '等待分析',
        'loudness_meter_target': '目标 {value} LUFS',
        'loudness_meter_title': '响度表',
        'loudness_meter_tooltip': '红色为目标，蓝色为最后一个输出的实际复测值。',
        'loudness_meter_waiting': '等待音频文件',
        'loudness_meter_worst_file': '最大偏差：{file}',
        'loudness_meter_worst_file_detail': '最近 8 次分析中的最大偏差：{file} — 目标 {expected} LUFS，实测 {measured} LUFS，偏差 '
                                            '{deviation} LU。',
        'loudness_score_acceptable': '可接受',
        'loudness_score_check': '查看警告',
        'loudness_score_excellent': '优秀',
        'loudness_score_good': '良好',
        'loudness_score_needs_qc': '目标评分：请启用质量控制',
        'loudness_score_not_applicable': '目标评分：不适用',
        'loudness_score_tooltip': '评分使用最近8个实际复测输出。100表示完全一致，50表示RMS偏差0.60 LU，0表示1.20 LU或更大。红色面板表示“警告”按钮中至少有一项响度警告可供查看。',
        'loudness_score_value': '目标评分：{score}/100\n{rating}\nRMS 误差：{deviation}\xa0LU',
        'loudness_score_waiting': '目标评分：等待',
        'measurement_unavailable': '测量不可用。',
        'mp3': 'MP3',
        'mp3_filter': '支持的音频 (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': '未选择文件夹',
        'no_mp3': '未找到受支持的音频文件。',
        'no_new_source': '未添加新的有效文件夹或受支持的音频文件。',
        'not_performed': '未执行',
        'open_output_error': '无法打开目标文件夹：{error}',
        'operation': '操作',
        'operation_analyze': '仅分析 — 不创建文件',
        'operation_analyze_label': '仅分析',
        'operation_convert': '均衡 — 实际标准化音频',
        'operation_convert_label': '音频标准化',
        'operation_help_text': '均一化逐个处理文件并复测输出。ReplayGain不改变采样。仅分析生成测量和可选CSV，不生成音频。',
        'operation_replaygain': 'ReplayGain — 不重新编码音频',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': '均一化会实际改变音频；ReplayGain复制音频流并添加标签；仅分析不创建音频。',
        'option_status_auto_start': '自动',
        'option_status_overwrite': '覆盖',
        'option_status_quality_control': '质控',
        'option_status_report': 'CSV',
        'option_status_resume': '继续',
        'option_status_skip_compliant': '合规',
        'options_tab': '选项',
        'output_lufs_log': '输出 {value} LUFS',
        'output_lufs_unavailable': '输出 LUFS 不可用',
        'overwrite': '覆盖现有文件',
        'overwrite_tooltip': '允许替换目标位置中已经存在的 MP3。源文件绝不会被覆盖。',
        'parallel': '并行进程',
        'parallel_adjusted': '自动并行 — {active} 个进程，CPU {cpu:.0f}%。',
        'parallel_auto': 'Auto',
        'parallel_auto_log': '自动，最多 {maximum}',
        'parallel_tooltip': '决定可以同时处理多少个文件。\n'
                            '\n'
                            '• Auto 最多从 4 个任务开始。有 CPU 测量时，每秒检查一次：使用率低于 70% 时增加一个任务，高于 92% 时减少一个。\n'
                            '• Auto 不会超过检测到的逻辑 CPU 数，绝对上限为 16。\n'
                            '• 无法测量 CPU 时，直接使用检测到的上限，不做动态调整。\n'
                            '• 数字值固定并发任务的最大数量，并不是 CPU 使用率目标。\n'
                            '\n'
                            '按 − 直到显示 Auto。',
        'paste': '粘贴',
        'path_left': '显示路径左侧',
        'path_right': '显示路径右侧',
        'pause': '暂停',
        'peak': '最大真峰值',
        'peak_tooltip': '最大真峰值是上限，而不是要达到的电平。它以 dBTP 限制重建波形的最高峰值，包括采样点之间的峰值，以减少编码或转码后的削波。\n'
                        '\n'
                        '• -1.0 dBTP — 常见交付上限。\n'
                        '• -1.5 dBTP — MP3 的谨慎默认值。\n'
                        '• -2.0 dBTP — 为再次编码或较高响度目标提供额外余量。\n'
                        '• 0 dBTP — 没有余量，不建议用于 MP3。\n'
                        '\n'
                        '更负的值更安全，但可能使高动态曲目无法精确达到 LUFS 目标。',
        'phase_summary': '预计总时间分配 — 分析 {analysis}，转换 {conversion}，质量控制 {quality}。',
        'pipeline_enabled': '单曲流水线 — 每个转换在其分析完成后立即开始。',
        'pre_measurement': '正在测量输入文件…',
        'preset': '预设',
        'preset_dynamic': '动态音乐',
        'preset_library': '音乐库 — 推荐',
        'preset_streaming': '更响亮的流媒体',
        'preset_tooltip': '一次应用一致的响度目标、最大真峰值和 MP3 质量。任何手动修改都会选择“自定义”。',
        'processing_cancelled': '处理已取消。',
        'processing_completed': '处理完成',
        'processing_in_progress': '正在处理',
        'processing_paused': '处理已暂停。',
        'processing_resumed': '处理已继续。',
        'progress_status': '{status}：{file}',
        'qc_impossible': '警告 — 质量控制失败：{error}',
        'qc_log': ' — 质量控制：{quality}',
        'qc_ok': '成功',
        'qc_warning': '警告 — {detail}',
        'quality': '音频质量',
        'quality_control': '自动质量控制',
        'quality_control_tooltip': '重新测量每个输出。校正仍以±0.50 LU为目标；只有超出±0.60 LU才显示响度警告。动态MP3保留最多三次尝试；True '
                                   'Peak余量允许时，WAV、AIFF和FLAC可从源文件最多重试两次。关闭后将取消验证、重试和响度表活动。',
        'quality_tooltip': '设置压缩格式在质量与大小之间的取舍。数字越小，质量和码率越高。此设置不会改变 LUFS 目标或最大 True Peak。\n'
                           '\n'
                           '• 0 — 最高质量，建议用于保留细节。\n'
                           '• 1 到 2 — 很高质量。\n'
                           '• 3 到 4 — 质量/大小的良好平衡。\n'
                           '• 5 到 9 — 文件更小，但损失更多。\n'
                           '\n'
                           '无论数值如何，FLAC 始终无损。WAV 和 AIFF 会忽略此设置，并保留与源文件兼容的 PCM 采样率和位深。对于 MP3、M4A、OGG 和 '
                           'Opus，较小数值可能要求高于源文件的码率，使输出更大。较大数值通常会减小文件，但这些编码器常使用 VBR，因此不能保证字节数相同。重新编码有损格式无法恢复已经丢失的信息。',
        'ready': '就绪',
        'recursive_scan': '正在递归扫描文件夹…',
        'remove_all': '全部移除',
        'remove_selection': '移除所选项',
        'replaygain_help_text': 'ReplayGain计算增益并写入REPLAYGAIN_TRACK_GAIN/PEAK。音频不重编码（-c:a '
                                'copy），只有兼容播放器会应用标签，因此物理LUFS和True Peak不变。',
        'replaygain_levels_log': '音频不变：{before} LUFS · 元数据ReplayGain {gain} dB · 设置目标 {target} LUFS（需要兼容播放器）',
        'replaygain_log_help_text': '在 ReplayGain '
                                    '模式下，日志会显示未改变的物理响度、写入元数据的增益以及设定目标。启用质量控制时，“音频未改变且标签已验证”表示已将响度和峰值与源文件比较，并重新读取了标签；这不表示文件的物理测量值达到了目标。',
        'replaygain_operation': '无需重新编码的 ReplayGain',
        'replaygain_qc_help_text': '启用质量控制后，ReplayGain 会重新测量交付文件，确认其物理响度和峰值没有变化，然后检查 Track '
                                   '标签。成功表示音频得到保留且标签存在，并不表示物理响度达到了目标。',
        'replaygain_qc_ok': '成功 — 音频未改变且标签已验证',
        'replaygain_tags_missing': '未找到 ReplayGain 标签。',
        'replaygain_usefulness_text': 'ReplayGain适合在兼容播放器中对资料库进行可逆、无重编码的播放音量统一。若要交付在所有播放器中都能实际测得目标值的文件，请使用标准化。',
        'report_destination': '目标',
        'report_detail': '详情',
        'report_error': '警告 — 无法创建 CSV 报告：{error}',
        'report_filename_prefix': 'LUFScale_报告',
        'report_gain': '增益_db',
        'report_input_dbtp': '输入_dbtp',
        'report_input_lufs': '输入_lufs',
        'report_log': 'CSV 报告 — {path}',
        'report_mode': '模式',
        'report_operation': '操作',
        'report_output_dbtp': '输出_dbtp',
        'report_output_lufs': '输出_lufs',
        'report_path': '报告：{path}',
        'report_qc': '质量控制',
        'report_qc_engine': '质量控制_测量引擎',
        'report_seconds': '已用秒数',
        'report_source': '来源',
        'report_status': '状态',
        'report_tooltip': '只创建包含测量、耗时和警告的CSV，不再附加诊断JSON。',
        'resume': '中断后继续',
        'resume_not_saved': ' 未保存续传检查点：{error}',
        'resume_processing': '继续',
        'resume_tooltip': '识别使用相同设置已经完成的文件，不再重复处理。',
        'resumed_progress': '已续传：{file}',
        'save_dialog_cancel': '取消',
        'save_dialog_filename': '文件名',
        'save_dialog_filetype': '格式',
        'save_dialog_location': '位置',
        'save_dialog_overwrite': '替换',
        'save_dialog_overwrite_message': '文件“{file}”已存在。',
        'save_dialog_overwrite_title': '替换文件？',
        'save_dialog_parent': '上级文件夹',
        'save_dialog_save': '保存',
        'save_issue_list': '另存为 CSV…',
        'save_issue_list_error': '无法保存列表：{error}',
        'save_issue_list_error_title': '无法保存',
        'save_issue_list_title': '保存 CSV 列表',
        'scan_error': '错误 — {error}',
        'scanning_folders': '正在扫描文件夹…',
        'settings': '设置',
        'open_folder': '打开文件夹',
        'show_option_help': '显示帮助：{option}',
        'silent_copy': '静音或无法测量的音频已复制。',
        'silent_copy_no_replaygain': '静音音频已复制，但未添加 ReplayGain 标签。',
        'silent_unmeasurable': '音频静音或无法测量。',
        'simulation': '模拟',
        'skip_compliant': '不重新编码已符合要求的文件',
        'skip_compliant_tooltip': '目标±0.10 LU内且不超过True Peak上限的文件直接复制，不重编码。',
        'skipped_progress': '已跳过：{file}',
        'source_audio_count': '文件：{count}',
        'source_list_more': '… 另保留 {count} 个来源',
        'source_safety': '源文件绝不会被移动或修改。',
        'source_selection_tooltip': '多选：按住 Ctrl 单击选择分散项目，按住 Shift 单击选择连续范围。',
        'sources_added': '已添加 {count} 个来源。',
        'start': '开始',
        'status_analyzed': '已分析',
        'status_cancelled': '已取消',
        'status_compliant': '合规',
        'status_error': '错误',
        'status_ok': '成功',
        'status_resumed': '已续传',
        'status_skipped': '已跳过',
        'status_warning': '警告',
        'switch_to_dark': '深色模式',
        'switch_to_light': '浅色模式',
        'tagline': '统一感知音量',
        'target': '响度目标',
        'target_tooltip': '响度目标是整首曲目的目标综合响度，以 LUFS 表示。数值越不负，文件听起来越响：-14 LUFS 比 -16 LUFS 响。2 LU 的差值在峰值限制前约等于 2 dB '
                          '的电平差。\n'
                          '\n'
                          '参考：-18 LUFS 更平静、更有动态；-16 LUFS 适合一般均衡；-14 LUFS 适合较响亮的流媒体风格。平台之后可能应用自己的播放标准化。\n'
                          '\n'
                          '目标本身不会压平曲目内部的动态。如果最大真峰值不允许在不削波的情况下达到目标，结果可能略低。',
        'theme_accessible': '更改应用程序外观。选择会被记住。',
        'total_time': '总时间：{duration}',
        'track_two_pass': '两遍单曲标准化。',
        'true_peak_meter_exceeded': '超出 {margin} dB',
        'true_peak_meter_margin': '余量 {margin} dB',
        'true_peak_meter_title': '峰值余量',
        'true_peak_meter_tooltip': '将上一输出的真峰值与所选上限比较。标记显示最新值，三角形保留本批次最高峰值。绿色表示符合上限；橙色表示超出不超过 0.25 dB；红色表示超出更多。橙色容差仅用于 '
                                   'LUFScale 质量控制，并非交付标准。每批任务都会重置。',
        'true_peak_meter_waiting': '等待 dBTP 测量',
        'version_changes': '• 面向 Windows 10/11 x86-64 的单文件离线安装程序。\n'
                           '• 内含 Python、PySide6/Qt、FFmpeg、编解码器、指南和许可证；安装时无需下载或 PowerShell 命令。\n'
                           '• 创建安装程序及 SHA-256 前会验证 loudnorm 和所有编码器。',
        'version_changes_title': '版本 {version} 的新增内容',
        'version_label': '版本 {version}',
        'volume': '音量',
        'volume_loud': '响亮: -14 LUFS',
        'volume_normal': '标准: -16 LUFS',
        'volume_soft': '柔和: -18 LUFS',
        'volume_tooltip': '此设置是响度目标的快捷方式，不会改变 系统的播放音量。\n'
                          '\n'
                          '• 柔和：-18 LUFS — 更平静，动态余量更大，较少触发限制器。\n'
                          '• 标准：-16 LUFS — 均衡折中，适合作为个人音乐库的起点。\n'
                          '• 响亮：-14 LUFS — 播放更突出，但更可能需要限制。\n'
                          '• 自定义 — 直接输入其他 LUFS 目标。\n'
                          '\n'
                          '这些是实用选择，并非通用标准。',
        'warning_list_title': '处理警告',
        'warnings_button': '警告 ({count})',
        'warnings_button_tooltip': '打开警告列表，其中包含文件名、路径和详情。暂停期间或处理结束后可用。',
        'warnings_dialog_title': '处理警告'}}

EXTRA_CORE_TEXTS = {'es': {'album_unmeasurable': 'No se puede medir la sonoridad del álbum.',
        'empty_album': 'Un álbum debe contener al menos un archivo de audio compatible.',
        'incomplete_measurements': 'Mediciones de FFmpeg incompletas: {fields}',
        'loudness_changed': 'sonoridad modificada en {value:+.2f} LU',
        'loudness_unmeasurable': 'No se puede medir la sonoridad.',
        'measurements_ok': 'Mediciones correctas.',
        'no_inputs': 'Añade al menos una carpeta o un archivo de audio compatible.',
        'no_measurements': 'FFmpeg no devolvió mediciones de sonoridad utilizables.',
        'output_contains_source': 'La carpeta de destino seleccionada ya contiene el archivo de origen. Elige otra '
                                  'ubicación.',
        'output_inside_source': 'La carpeta de destino no puede estar dentro de una carpeta de origen. Elige una '
                                'ubicación fuera de las carpetas añadidas.',
        'output_not_silent': 'La salida ya no es silenciosa.',
        'output_recreates_source': 'Esta carpeta de destino volvería a crear los archivos directamente en el origen. '
                                   'Elige otra ubicación.',
        'output_unmeasurable': 'La salida no tiene una sonoridad medible.',
        'peak_above_limit': 'pico {value:.2f} dBTP por encima del límite',
        'peak_changed': 'pico modificado en {value:+.2f} dB',
        'silent_preserved': 'Audio silencioso conservado.',
        'unexpected_loudness': '{actual:.2f} LUFS en lugar de {expected:.2f}'},
 'hi': {'album_unmeasurable': 'एल्बम की ध्वनि-तीव्रता मापी नहीं जा सकती।',
        'empty_album': 'एल्बम में कम से कम एक समर्थित ऑडियो फ़ाइल होनी चाहिए।',
        'incomplete_measurements': 'अपूर्ण FFmpeg मापन: {fields}',
        'loudness_changed': 'ध्वनि-तीव्रता {value:+.2f} LU बदली',
        'loudness_unmeasurable': 'ध्वनि-तीव्रता मापी नहीं जा सकती।',
        'measurements_ok': 'मापन अनुरूप हैं।',
        'no_inputs': 'कम से कम एक फ़ोल्डर या समर्थित ऑडियो फ़ाइल जोड़ें।',
        'no_measurements': 'FFmpeg ने उपयोगी ध्वनि-तीव्रता मापन नहीं दिया।',
        'output_contains_source': 'चुने गए आउटपुट फ़ोल्डर में स्रोत फ़ाइल पहले से है। कोई दूसरा स्थान चुनें।',
        'output_inside_source': 'आउटपुट फ़ोल्डर स्रोत फ़ोल्डर के अंदर नहीं हो सकता। जोड़े गए फ़ोल्डरों के बाहर कोई '
                                'स्थान चुनें।',
        'output_not_silent': 'आउटपुट अब मौन नहीं है।',
        'output_recreates_source': 'यह आउटपुट फ़ोल्डर फ़ाइलों को सीधे स्रोत में फिर बनाएगा। कोई दूसरा स्थान चुनें।',
        'output_unmeasurable': 'आउटपुट में मापने योग्य ध्वनि-तीव्रता नहीं है।',
        'peak_above_limit': 'पीक {value:.2f} dBTP सीमा से ऊपर',
        'peak_changed': 'पीक {value:+.2f} dB बदला',
        'silent_preserved': 'मौन ऑडियो सुरक्षित रखा गया।',
        'unexpected_loudness': '{expected:.2f} के बजाय {actual:.2f} LUFS'},
 'it': {'album_unmeasurable': 'La sonorità dell’album non può essere misurata.',
        'empty_album': 'Un album deve contenere almeno un file audio supportato.',
        'incomplete_measurements': 'Misurazioni FFmpeg incomplete: {fields}',
        'loudness_changed': 'sonorità modificata di {value:+.2f} LU',
        'loudness_unmeasurable': 'La sonorità non può essere misurata.',
        'measurements_ok': 'Misurazioni conformi.',
        'no_inputs': 'Aggiungi almeno una cartella o un file audio supportato.',
        'no_measurements': 'FFmpeg non ha restituito misurazioni di sonorità utilizzabili.',
        'output_contains_source': 'La cartella di destinazione selezionata contiene già il file sorgente. Scegli '
                                  'un’altra posizione.',
        'output_inside_source': 'La cartella di destinazione non può trovarsi dentro una cartella sorgente. Scegli una '
                                'posizione esterna alle cartelle aggiunte.',
        'output_not_silent': 'L’uscita non è più silenziosa.',
        'output_recreates_source': 'Questa cartella di destinazione ricreerebbe i file direttamente nella sorgente. '
                                   'Scegli un’altra posizione.',
        'output_unmeasurable': 'L’uscita non ha una sonorità misurabile.',
        'peak_above_limit': 'picco {value:.2f} dBTP oltre il limite',
        'peak_changed': 'picco modificato di {value:+.2f} dB',
        'silent_preserved': 'Audio silenzioso conservato.',
        'unexpected_loudness': '{actual:.2f} LUFS invece di {expected:.2f}'},
 'ja': {'album_unmeasurable': 'アルバムのラウドネスを測定できません。',
        'empty_album': 'アルバムには対応音声ファイルが1つ以上必要です。',
        'incomplete_measurements': 'FFmpegの測定値が不完全です：{fields}',
        'loudness_changed': 'ラウドネスが{value:+.2f} LU変化',
        'loudness_unmeasurable': 'ラウドネスを測定できません。',
        'measurements_ok': '測定値は基準内です。',
        'no_inputs': 'フォルダーまたは対応音声ファイルを1つ以上追加してください。',
        'no_measurements': 'FFmpegから利用可能なラウドネス測定値が返されませんでした。',
        'output_contains_source': '選択した保存先には元ファイルがすでに含まれています。別の場所を選んでください。',
        'output_inside_source': '保存先を元フォルダの内側に置くことはできません。追加したフォルダの外を選んでください。',
        'output_not_silent': '出力は無音ではありません。',
        'output_recreates_source': 'この保存先では元の場所に直接ファイルが作成されます。別の場所を選んでください。',
        'output_unmeasurable': '出力に測定可能なラウドネスがありません。',
        'peak_above_limit': 'ピーク{value:.2f} dBTPが上限を超過',
        'peak_changed': 'ピークが{value:+.2f} dB変化',
        'silent_preserved': '無音の音声を保持しました。',
        'unexpected_loudness': '{expected:.2f}ではなく{actual:.2f} LUFS'},
 'pt': {'album_unmeasurable': 'Não é possível medir a sonoridade do álbum.',
        'empty_album': 'Um álbum deve conter pelo menos um ficheiro de áudio compatível.',
        'incomplete_measurements': 'Medições FFmpeg incompletas: {fields}',
        'loudness_changed': 'sonoridade alterada em {value:+.2f} LU',
        'loudness_unmeasurable': 'Não é possível medir a sonoridade.',
        'measurements_ok': 'Medições conformes.',
        'no_inputs': 'Adicione pelo menos uma pasta ou um ficheiro de áudio compatível.',
        'no_measurements': 'O FFmpeg não devolveu medições de sonoridade utilizáveis.',
        'output_contains_source': 'A pasta de destino selecionada já contém o ficheiro de origem. Escolha outra '
                                  'localização.',
        'output_inside_source': 'A pasta de destino não pode estar dentro de uma pasta de origem. Escolha uma '
                                'localização fora das pastas adicionadas.',
        'output_not_silent': 'A saída deixou de ser silenciosa.',
        'output_recreates_source': 'Esta pasta de destino voltaria a criar os ficheiros diretamente na origem. Escolha '
                                   'outra localização.',
        'output_unmeasurable': 'A saída não tem sonoridade mensurável.',
        'peak_above_limit': 'pico {value:.2f} dBTP acima do limite',
        'peak_changed': 'pico alterado em {value:+.2f} dB',
        'silent_preserved': 'Áudio silencioso preservado.',
        'unexpected_loudness': '{actual:.2f} LUFS em vez de {expected:.2f}'},
 'ru': {'album_unmeasurable': 'Громкость альбома невозможно измерить.',
        'empty_album': 'Альбом должен содержать хотя бы один поддерживаемый аудиофайл.',
        'incomplete_measurements': 'Неполные измерения FFmpeg: {fields}',
        'loudness_changed': 'громкость изменилась на {value:+.2f} LU',
        'loudness_unmeasurable': 'Громкость невозможно измерить.',
        'measurements_ok': 'Измерения соответствуют требованиям.',
        'no_inputs': 'Добавьте хотя бы одну папку или поддерживаемый аудиофайл.',
        'no_measurements': 'FFmpeg не вернул пригодные измерения громкости.',
        'output_contains_source': 'Выбранная папка назначения уже содержит исходный файл. Выберите другое место.',
        'output_inside_source': 'Папка назначения не может находиться внутри исходной папки. Выберите место вне '
                                'добавленных папок.',
        'output_not_silent': 'Выходной сигнал больше не является тихим.',
        'output_recreates_source': 'Эта папка назначения привела бы к созданию файлов прямо в источнике. Выберите '
                                   'другое место.',
        'output_unmeasurable': 'Выходной сигнал не имеет измеримой громкости.',
        'peak_above_limit': 'пик {value:.2f} dBTP выше предела',
        'peak_changed': 'пиковый уровень изменился на {value:+.2f} дБ',
        'silent_preserved': 'Тихий звук сохранён.',
        'unexpected_loudness': '{actual:.2f} LUFS вместо {expected:.2f}'},
 'zh': {'album_unmeasurable': '无法测量专辑响度。',
        'empty_album': '专辑必须至少包含一个受支持的音频文件。',
        'incomplete_measurements': 'FFmpeg 测量不完整：{fields}',
        'loudness_changed': '响度变化 {value:+.2f} LU',
        'loudness_unmeasurable': '无法测量响度。',
        'measurements_ok': '测量符合要求。',
        'no_inputs': '请至少添加一个文件夹或受支持的音频文件。',
        'no_measurements': 'FFmpeg 未返回可用的响度测量结果。',
        'output_contains_source': '所选输出文件夹已经包含源文件。请选择其他位置。',
        'output_inside_source': '输出文件夹不能位于来源文件夹内。请选择已添加文件夹之外的位置。',
        'output_not_silent': '输出不再静音。',
        'output_recreates_source': '此输出文件夹会直接在来源中重新创建文件。请选择其他位置。',
        'output_unmeasurable': '输出没有可测量的响度。',
        'peak_above_limit': '峰值 {value:.2f} dBTP 超过限制',
        'peak_changed': '峰值变化 {value:+.2f} dB',
        'silent_preserved': '已保留静音音频。',
        'unexpected_loudness': '实际 {actual:.2f} LUFS，目标 {expected:.2f}'}}

TEXTS.update(
    {
        "official_website": ("Site officiel", "Official website"),
        "official_website_tooltip": (
            "Ouvrir le site officiel de LUFScale",
            "Open the official LUFScale website",
        ),
    }
)

_WEBSITE_TEXTS = {
    "es": {
        "official_website": "Sitio web oficial",
        "official_website_tooltip": "Abrir el sitio web oficial de LUFScale",
    },
    "it": {
        "official_website": "Sito web ufficiale",
        "official_website_tooltip": "Apri il sito web ufficiale di LUFScale",
    },
    "pt": {
        "official_website": "Site oficial",
        "official_website_tooltip": "Abrir o site oficial do LUFScale",
    },
    "ru": {
        "official_website": "Официальный сайт",
        "official_website_tooltip": "Открыть официальный сайт LUFScale",
    },
    "ja": {
        "official_website": "公式サイト",
        "official_website_tooltip": "LUFScaleの公式サイトを開く",
    },
    "hi": {
        "official_website": "आधिकारिक वेबसाइट",
        "official_website_tooltip": "LUFScale की आधिकारिक वेबसाइट खोलें",
    },
    "zh": {
        "official_website": "官方网站",
        "official_website_tooltip": "打开 LUFScale 官方网站",
    },
    "ko": {
        "official_website": "공식 웹사이트",
        "official_website_tooltip": "LUFScale 공식 웹사이트 열기",
    },
    "id": {
        "official_website": "Situs web resmi",
        "official_website_tooltip": "Buka situs web resmi LUFScale",
    },
    "tr": {
        "official_website": "Resmî web sitesi",
        "official_website_tooltip": "LUFScale resmî web sitesini aç",
    },
}
for _language, _updates in _WEBSITE_TEXTS.items():
    EXTRA_TEXTS[_language].update(_updates)


_LOG_SPACING_CHANGE = {
    "fr": "• L’interligne du journal de traitement est maintenant uniforme dans toutes les langues ; les polices japonaises, chinoises, coréennes et devanagari n’ajoutent plus d’espace vertical excessif.",
    "en": "• Processing-log line spacing is now uniform in every language; Japanese, Chinese, Korean and Devanagari fonts no longer add excessive vertical space.",
    "es": "• El interlineado del registro de procesamiento ahora es uniforme en todos los idiomas; las fuentes de japonés, chino, coreano y devanagari ya no añaden un espacio vertical excesivo.",
    "it": "• L’interlinea del registro di elaborazione è ora uniforme in tutte le lingue; i caratteri giapponesi, cinesi, coreani e devanagari non aggiungono più uno spazio verticale eccessivo.",
    "pt": "• O espaçamento entre linhas do registo de processamento é agora uniforme em todos os idiomas; as fontes japonesas, chinesas, coreanas e devanágari já não acrescentam espaço vertical excessivo.",
    "ru": "• Межстрочный интервал журнала обработки теперь одинаков для всех языков; японские, китайские, корейские шрифты и деванагари больше не добавляют избыточное вертикальное пространство.",
    "ja": "• 処理ログの行間を全言語で統一し、日本語・中国語・韓国語・デーヴァナーガリー文字のフォントで過剰な縦方向の余白が生じないようにしました。",
    "hi": "• प्रसंस्करण लॉग की पंक्ति-दूरी अब सभी भाषाओं में समान है; जापानी, चीनी, कोरियाई और देवनागरी फ़ॉन्ट अब अतिरिक्त ऊर्ध्वाधर खाली स्थान नहीं जोड़ते।",
    "zh": "• 处理日志的行距现在在所有语言中保持一致；日文、中文、韩文和天城文字体不再产生过大的垂直间距。",
    "ko": "• 처리 로그의 줄 간격을 모든 언어에서 동일하게 맞췄으며 일본어, 중국어, 한국어 및 데바나가리 글꼴이 더 이상 과도한 세로 여백을 추가하지 않습니다.",
    "id": "• Jarak baris log pemrosesan kini seragam dalam semua bahasa; font Jepang, Tionghoa, Korea, dan Dewanagari tidak lagi menambahkan ruang vertikal berlebihan.",
    "tr": "• İşlem günlüğünün satır aralığı artık tüm dillerde aynıdır; Japonca, Çince, Korece ve Devanagari yazı tipleri artık aşırı dikey boşluk eklemez.",
}
_previous_french_changes, _previous_english_changes = TEXTS["version_changes"]
TEXTS["version_changes"] = (
    _LOG_SPACING_CHANGE["fr"] + "\n" + _previous_french_changes,
    _LOG_SPACING_CHANGE["en"] + "\n" + _previous_english_changes,
)
for _language in _LOG_SPACING_CHANGE:
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language]["version_changes"] = (
            _LOG_SPACING_CHANGE[_language]
            + "\n"
            + EXTRA_TEXTS[_language]["version_changes"]
        )


__all__ = ["EXTRA_CORE_TEXTS", "EXTRA_TEXTS", "LANGUAGES", "TEXTS"]
