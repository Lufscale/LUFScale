from __future__ import annotations

# Effective translations for the current interface.
EXTRA_TEXTS: dict[str, dict[str, str]] = {'de': {'activity_cancelled': 'Aktivität: Verarbeitung abgebrochen',
        'activity_cancelling': 'Aktivität: Abbruch läuft…',
        'activity_completed': 'Aktivität: Verarbeitung abgeschlossen',
        'activity_compliant': 'Konform: {count}',
        'activity_detected': 'Aktivität: {total} Datei(en) erkannt',
        'activity_errors': 'Fehler: {count}',
        'activity_files': 'Dateien: {count}',
        'activity_idle': 'Aktivität: wartet',
        'activity_preparing': 'Aktivität: Dateien werden vorbereitet…',
        'activity_progress': '{total} Dateien • erfolgreich {success} • Warnungen {warnings} • '
                             'Fehler {failed} • fortgesetzt/übersprungen {skipped} • konform '
                             '{compliant}',
        'activity_skipped': 'Fortgesetzt/übersprungen: {count}',
        'activity_successes': 'Erfolgreich: {count}',
        'activity_warnings': 'Warnungen: {count}',
        'adaptive_disabled_log': 'Adaptive Analyse — schnelle Sonden nach {sample} Messungen '
                                 'gestoppt ({successes} Erfolge, geschätzte Einsparung '
                                 '{percent:+.1f} %).',
        'add_folders': 'Ordner hinzufügen…',
        'add_mp3': 'Audiodateien hinzufügen…',
        'add_replaygain': 'ReplayGain hinzufügen',
        'add_source_files': 'Audiodateien hinzufügen',
        'add_source_folder': 'Quellordner hinzufügen',
        'album_gain_detail': 'Gemeinsame Albumverstärkung {gain:+.2f} dB.',
        'album_gain_log': 'Album „{album}“ — gemeinsame Verstärkung {gain:+.2f} dB.',
        'album_measurement_error': 'Albummessung fehlgeschlagen: {error}',
        'album_mode_log': 'Albummodus — jeder Ordner mit Audiodateien bildet ein Album.',
        'albums_measurement': '{count} Album/Alben werden gemessen…',
        'already_completed': 'Bereits bei einer früheren Ausführung abgeschlossen.',
        'already_compliant_badge': 'PASSEND',
        'already_compliant_copy': 'Bereits passend: unverändert und ohne Audio-Neucodierung '
                                  'kopiert.',
        'already_compliant_log': 'bereits passend, ohne Neucodierung',
        'analysis_cache_summary': 'Analyse-Cache — {hits} Messung(en) wiederverwendet.',
        'analysis_impossible': 'Analyse fehlgeschlagen: {error}',
        'analysis_method': 'Analysemethode',
        'analysis_method_adaptive': 'Adaptiv — stoppt ohne Vorteil',
        'analysis_method_fast': 'Schnell — experimentell',
        'analysis_method_historical': 'Bisherig — Referenz',
        'analysis_method_log': 'Analysemethode — {method}.',
        'analysis_method_tooltip': 'Bisherig verwendet ausschließlich die in 1.22.13 validierte '
                                   'vollständige Referenzmessung. Schnell testet bei jeder Datei '
                                   'die lineare Sonde und fällt bei Bedarf auf die bisherige '
                                   'Messung zurück. Adaptiv beginnt wie Schnell; nach mindestens '
                                   '12 Messungen und 3 Rückfällen vergleicht es die gemessenen '
                                   'Zeiten und deaktiviert die Sonden, wenn die geschätzte '
                                   'Einsparung unter 5 % bleibt. Endqualität und '
                                   'Qualitätskontrolle werden nicht reduziert.',
        'analysis_progress': 'Analyse {current}/{total}: {file}',
        'analyze': 'Analysieren',
        'analyze_operation': 'Analyse/Simulation',
        'analyzed_progress': 'Analysiert: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Audiostream ohne Neukodierung kopiert; ReplayGain-Tags '
                                 'hinzugefügt.',
        'audio_tab': 'Audio',
        'auto_start': 'Nach Ablegen oder Einfügen automatisch starten',
        'auto_start_tooltip': 'Startet die Verarbeitung nach dem Hinzufügen von Quellen per '
                              'Drag-and-drop oder Einfügen automatisch, wenn bereits ein Ziel '
                              'gewählt wurde.',
        'cancel': 'Abbrechen',
        'cancelled_summary': 'Abgebrochen — {success} erfolgreich, {failed} Fehler, {skipped} '
                             'fortgesetzt/übersprungen, {warnings} Warnung(en), {compliant} '
                             'konform — {duration}.',
        'cancelling': 'Wird abgebrochen…',
        'choose': 'Auswählen…',
        'choose_output': 'Zielordner auswählen',
        'clipboard': 'Zwischenablage',
        'clipboard_empty': 'Die Zwischenablage enthält keinen gültigen Pfad zu einem Ordner oder '
                           'einer unterstützten Audiodatei.',
        'close_question': 'Verarbeitung abbrechen und Anwendung schließen?',
        'completed_dialog_summary': 'Status: abgeschlossen\n'
                                    'Dateien: {files}\n'
                                    'Erfolgreich: {success}\n'
                                    'Fehler: {failed}\n'
                                    'Fortgesetzt oder übersprungen: {skipped}\n'
                                    'Warnungen: {warnings}\n'
                                    'Konform: {compliant}\n'
                                    'Gesamtzeit: {duration}',
        'completed_summary': 'Abgeschlossen — {success} erfolgreich, {failed} Fehler, {skipped} '
                             'fortgesetzt/übersprungen, {warnings} Warnung(en), {compliant} '
                             'konform — {duration}.',
        'completed_with_errors': 'Verarbeitung mit Warnungen abgeschlossen',
        'convert': 'Normalisieren',
        'convert_operation': 'Audionormalisierung',
        'cpu_tooltip': 'Gesamte CPU-Auslastung des Macs, während der Verarbeitung jede Sekunde '
                       'aktualisiert.',
        'cpu_unavailable': 'N/V',
        'cpu_usage': 'CPU',
        'create_report': 'CSV-Bericht erstellen',
        'custom': 'Benutzerdefiniert',
        'decrease_value': 'Wert verringern',
        'description': 'Gleicht die wahrgenommene Lautstärke im Titel- oder Albummodus an, ohne '
                       'die Originale zu verändern.',
        'destination': 'Ziel',
        'destination_error': 'FEHLER — Ziel nicht verfügbar: {error}',
        'destination_path_tooltip': 'Klicken Sie in den Pfad und verwenden Sie Pfeiltasten, '
                                    'Pos1/Ende oder das Mausrad. Der Pfad kann ausgewählt und '
                                    'kopiert, aber nicht geändert werden.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — Unterordner unterstützt',
        'drop_title': 'Ordner oder Audiodateien hier ablegen',
        'elapsed_time': 'Verstrichene Zeit: {duration}',
        'error_progress': 'Fehler: {file}',
        'estimated_result': 'Geschätztes Ergebnis; keine Datei erstellt.',
        'estimated_total_calculating': 'Geschätzte Gesamtzeit: wird berechnet…',
        'estimated_total_time': 'Geschätzte Gesamtzeit: {duration}',
        'estimated_total_time_with_finish': 'Geschätzte Gesamtzeit: {duration} — Ende gegen {time}',
        'estimated_total_unavailable': 'Geschätzte Gesamtzeit: nicht verfügbar',
        'ffmpeg_download_button': 'Offizielle FFmpeg-Website öffnen',
        'ffmpeg_error_no_detail': 'FFmpeg-Fehler ohne Details.',
        'ffmpeg_execution_error': 'FFmpeg kann nicht ausgeführt werden: {error}',
        'ffmpeg_incompatible': 'FFmpeg nicht kompatibel',
        'ffmpeg_missing': 'FFmpeg nicht gefunden',
        'ffmpeg_missing_encoders': 'Diese FFmpeg-Version enthält nicht alle benötigten '
                                   'Audio-Encoder: {encoders}.',
        'ffmpeg_missing_message': 'FFmpeg muss installiert und über PATH erreichbar sein oder '
                                  'neben dem Programm liegen.',
        'ffmpeg_no_lame': 'Diese FFmpeg-Version enthält den MP3-Encoder libmp3lame nicht.',
        'ffmpeg_no_loudnorm': 'Diese FFmpeg-Version enthält den Filter loudnorm nicht.',
        'ffmpeg_not_responding': 'FFmpeg antwortet nicht ordnungsgemäß.',
        'file_exists': 'Die Datei ist bereits vorhanden.',
        'files_found': '{total} Audiodatei(en) gefunden — {operation} — {parallel} parallele '
                       'Verarbeitung(en).',
        'folder': 'Ordner',
        'folder_unavailable': 'Ordner nicht verfügbar',
        'guide_help_tooltip': 'Öffnet die vollständige PDF-Anleitung in der ausgewählten Sprache.',
        'guide_missing_message': 'Die PDF-Anleitung wurde nicht gefunden: {path}',
        'guide_missing_title': 'Anleitung nicht verfügbar',
        'guide_open_error': 'macOS konnte die PDF-Anleitung nicht öffnen: {path}',
        'help_button': 'Hilfe',
        'help_overview': '• Echte Normalisierung, ReplayGain oder Analyse ohne MP3-Erstellung.\n'
                         '• Titel- und Albummodus mit Erhalt der Unterschiede zwischen Titeln.\n'
                         '• Ordnerstruktur, Metadaten und Cover bleiben erhalten, wenn FFmpeg sie '
                         'kopieren kann.\n'
                         '• Originale werden niemals verschoben oder verändert.\n'
                         '• Auto-Parallelität, Analyse-Cache und Fortsetzen nach Unterbrechung.\n'
                         '• Qualitätskontrolle, CSV-Bericht, Fortschritt, CPU, Lautheitsmesser und '
                         'geschätzte Gesamtdauer.\n'
                         '• Oberfläche in zwölf Sprachen und PDF-Anleitungen in zwölf Sprachen.',
        'help_title': 'Wichtigste Funktionen',
        'increase_value': 'Wert erhöhen',
        'interface_ffmpeg_message': 'Die Oberfläche ist verfügbar, für die Konvertierung wird '
                                    'jedoch FFmpeg benötigt. Installieren Sie FFmpeg und starten '
                                    'Sie die Anwendung neu.',
        'internal_error': 'Interner Fehler: {error}',
        'interrupted': 'Verarbeitung unterbrochen.',
        'invalid_location': 'Ungültiger Speicherort',
        'language': 'Sprache',
        'language_tooltip': 'Ändert sofort die Sprache der Oberfläche, der Meldungen und künftiger '
                            'CSV-Berichte. Die Auswahl wird gespeichert.',
        'level_mode': 'Lautstärkemodus',
        'log_help_text': 'Jede Zeile beschreibt eine Datei oder einen allgemeinen '
                         'Verarbeitungsschritt.\n'
                         '\n'
                         '• Anfang: Verarbeitungsstatus (OK, WARNUNG, FEHLER, fortgesetzt oder '
                         'übersprungen).\n'
                         '• Danach: MP3-Name und für diese Datei benötigte Zeit.\n'
                         '• LUFS-Feld: gemessener Pegel vorher → erreichter Pegel nach der '
                         'Verarbeitung.\n'
                         '• Ende: Ergebnis der Qualitätskontrolle und gegebenenfalls weitere '
                         'Details.\n'
                         '\n'
                         'Farben: Grün = Erfolg; Orange = Warnung; Rot = nicht fertiggestellte '
                         'Datei; Blauviolett = Fortsetzung; Grau = Information, übersprungenes '
                         'Element oder Abbruch.\n'
                         '\n'
                         'Die kumulierten Zeiten addieren die Arbeit aller parallelen Aufgaben. '
                         'Die Gesamtzeit ist die tatsächlich verstrichene Dauer.\n'
                         '\n'
                         'QC-WARNUNG — Peak bedeutet, dass der erneut gemessene True Peak der '
                         'Ausgabe den gewählten Grenzwert um mehr als 0,25 dB überschreitet. Die '
                         'Datei wird trotzdem erstellt: Es handelt sich nicht um einen '
                         'Konvertierungsfehler. Sie hält jedoch die verlangte Obergrenze nicht '
                         'genau ein und bietet weniger Reserve für eine weitere Kodierung oder '
                         'bestimmte Konverter. Je näher der dBTP-Wert an 0 liegt, desto größer ist '
                         'das Risiko von Inter-Sample-Peaks. Wählen Sie bei einer wiederkehrenden '
                         'Warnung ein leiseres LUFS-Ziel oder einen vorsichtigeren maximalen Peak, '
                         'etwa −2,0 dBTP, und verarbeiten Sie die Datei erneut.',
        'log_placeholder': 'Das Verarbeitungsprotokoll erscheint hier.',
        'log_title': 'Verarbeitungsprotokoll',
        'loudness_meter_estimated': 'Geschätzt',
        'loudness_meter_help_text': 'Dieses Messgerät kontrolliert die Gleichmäßigkeit der '
                                    'Normalisierung. Es vergleicht die letzte Audiodatei mit dem '
                                    'Ziel und berechnet fortlaufend Minimum und Maximum der '
                                    'letzten 100 Dateien. Ältere Werte verlassen dieses Fenster '
                                    'schrittweise, damit große Stapel dynamisch bleiben. Die '
                                    'Zielbewertung umfasst weiterhin den gesamten Stapel; die '
                                    'Anzeige ändert keine Einstellung.',
        'loudness_meter_maximum': 'Max {value}',
        'loudness_meter_measured': 'Gemessen',
        'loudness_meter_minimum': 'Min {value}',
        'loudness_meter_target': 'Ziel {value} LUFS',
        'loudness_meter_title': 'Lautheitsmesser',
        'loudness_meter_tooltip': 'Die rote Linie zeigt das Ziel. Der blaue Wert links folgt der '
                                  'letzten Audiodatei. Die grauen und dunkelvioletten Linien und '
                                  'Werte rechts zeigen Minimum und Maximum der letzten 100 '
                                  'Dateien. Die Skala vergrößert kleine Abweichungen; bei jedem '
                                  'neuen Stapel wird das Messgerät zurückgesetzt.',
        'loudness_meter_waiting': 'Warten auf eine Audiodatei',
        'loudness_score_acceptable': 'Akzeptabel',
        'loudness_score_check': 'Prüfen',
        'loudness_score_excellent': 'Ausgezeichnet',
        'loudness_score_good': 'Gut',
        'loudness_score_needs_qc': 'Zielwert: Qualitätskontrolle aktivieren',
        'loudness_score_not_applicable': 'Zielwert: nicht anwendbar',
        'loudness_score_tooltip': 'Der Wert verwendet nur Ausgaben, die tatsächlich erneut '
                                  'gemessen wurden. Er basiert auf der quadratischen mittleren '
                                  'Abweichung zwischen erreichter und erwarteter Lautheit: 100 = '
                                  'exaktes Ergebnis, 50 = Gesamtabweichung von 0,5 LU, der '
                                  'Toleranz der Qualitätskontrolle, und 0 = Abweichung von 1 LU '
                                  'oder mehr. Im Albummodus berücksichtigt der erwartete Wert '
                                  'jedes Titels die gemeinsame Verstärkung, damit die gewünschten '
                                  'Unterschiede erhalten bleiben. Die RMS-Abweichung '
                                  '(Quadratwurzel aus dem Mittelwert der quadrierten Abweichungen) '
                                  'fasst den Gesamtabstand zwischen den erreichten Lautheiten und '
                                  'ihren Zielwerten zusammen. Je näher sie bei 0 LU liegt, desto '
                                  'genauer ist der Stapel.',
        'loudness_score_value': 'Zielwert: {score}/100\n'
                                '{rating}\n'
                                'RMS-Abweichung: {deviation}\xa0LU',
        'loudness_score_waiting': 'Zielwert: wartet',
        'measurement_unavailable': 'Messung nicht verfügbar.',
        'mode_album': 'Album — Unterschiede zwischen Titeln beibehalten',
        'mode_album_label': 'Album',
        'mode_tooltip': 'Titel passt jede MP3-Datei einzeln an. Album berechnet eine gemeinsame '
                        'Verstärkung pro Ordner, damit die Lautstärkeunterschiede zwischen den '
                        'Titeln erhalten bleiben.',
        'mode_track': 'Track — gleicher Pegel für jede Datei',
        'mode_track_label': 'Titel',
        'mp3': 'MP3',
        'mp3_filter': 'Unterstützte Audiodateien (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg '
                      '*.opus)',
        'no_folder': 'Kein Ordner ausgewählt',
        'no_mp3': 'Keine unterstützten Audiodateien gefunden.',
        'no_new_source': 'Es wurde kein neuer gültiger Ordner und keine unterstützte Audiodatei '
                         'hinzugefügt.',
        'not_performed': 'Nicht durchgeführt',
        'open_output_error': 'Der Zielordner kann nicht geöffnet werden: {error}',
        'operation': 'Vorgang',
        'operation_analyze': 'Nur analysieren — Simulation ohne neue Datei',
        'operation_analyze_label': 'Nur Analyse',
        'operation_convert': 'Normalisieren — Audiodaten wirklich bearbeiten',
        'operation_convert_label': 'Audionormalisierung',
        'operation_replaygain': 'ReplayGain — ohne Audiokodierung',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Normalisieren verarbeitet das Audio wirklich. MP3, M4A/AAC, OGG und '
                             'Opus müssen neu codiert werden; die Größe hängt von der Qualität ab '
                             'und kann steigen. FLAC wird verlustfrei neu codiert, doch die '
                             'Kompression kann sich mit den Samples ändern. WAV und AIFF behalten '
                             'kompatible Quellrate, Kanäle und Bittiefe. ReplayGain codiert nicht '
                             'neu; Analysieren erstellt keine Datei.',
        'options_tab': 'Optionen',
        'overwrite': 'Vorhandene Dateien überschreiben',
        'overwrite_tooltip': 'Erlaubt das Ersetzen einer bereits im Ziel vorhandenen MP3-Datei. '
                             'Quelldateien werden niemals überschrieben.',
        'parallel': 'Parallele Prozesse',
        'parallel_adjusted': 'Automatische Parallelität — {active} Prozess(e), CPU {cpu:.0f} %.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automatisch, maximal {maximum}',
        'parallel_tooltip': 'Bestimmt, wie viele Dateien gleichzeitig verarbeitet werden können.\n'
                            '\n'
                            '• Auto startet mit höchstens 4 Aufgaben. Ist die CPU-Messung '
                            'verfügbar, wird sie jede Sekunde geprüft: Unter 70 % Auslastung kommt '
                            'eine Aufgabe hinzu, über 92 % wird eine entfernt.\n'
                            '• Auto überschreitet nie die erkannte Zahl logischer Prozessoren und '
                            'hat eine absolute Obergrenze von 16 Aufgaben.\n'
                            '• Ist keine CPU-Messung verfügbar, verwendet Auto diese erkannte '
                            'Obergrenze direkt und ohne dynamische Anpassung.\n'
                            '• Ein Zahlenwert legt die maximale Zahl gleichzeitiger Aufgaben fest; '
                            'er ist kein Zielwert für die CPU-Auslastung.\n'
                            '\n'
                            'Mehr Aufgaben können große Stapel beschleunigen, erhöhen aber Last, '
                            'Temperatur und Festplattenaktivität. Drücken Sie −, bis Auto '
                            'erscheint.',
        'paste': 'Einfügen',
        'path_left': 'Linken Teil des Pfads anzeigen',
        'path_right': 'Rechten Teil des Pfads anzeigen',
        'pause': 'Pause',
        'peak': 'Maximaler True Peak',
        'peak_tooltip': 'Der maximale True Peak ist eine Obergrenze, kein zu erreichender Pegel. '
                        'Er begrenzt die höchsten rekonstruierten Wellenformspitzen einschließlich '
                        'der Spitzen zwischen Abtastwerten in dBTP, um Übersteuerung nach dem '
                        'Kodieren oder Transkodieren zu verringern.\n'
                        '\n'
                        '• -1,0 dBTP — übliche Auslieferungsgrenze mit dem höchsten '
                        'Ausgangsspitzenpegel.\n'
                        '• -1,5 dBTP — Standardwert und vorsichtiger Kompromiss für MP3.\n'
                        '• -2,0 dBTP — zusätzliche Reserve, sinnvoll bei späterer Neukodierung '
                        'oder hohem Lautheitsziel.\n'
                        '• 0 dBTP — keine Reserve; für MP3 nicht empfohlen.\n'
                        '\n'
                        'Ein negativerer Wert ist sicherer, kann aber verhindern, dass sehr '
                        'dynamische Titel das LUFS-Ziel genau erreichen.',
        'phase_summary': 'Geschätzte Aufteilung der Gesamtzeit — Analyse {analysis}, Konvertierung '
                         '{conversion}, Qualitätskontrolle {quality}.',
        'pipeline_enabled': 'Titel-Pipeline — jede Konvertierung beginnt direkt nach ihrer '
                            'Analyse.',
        'pre_measurement': 'Eingabedateien werden gemessen…',
        'preset': 'Voreinstellung',
        'preset_dynamic': 'Dynamische Musik',
        'preset_library': 'Musikbibliothek — empfohlen',
        'preset_streaming': 'Präsenteres Streaming',
        'preset_tooltip': 'Wendet gleichzeitig ein abgestimmtes Lautheitsziel, einen maximalen '
                          'True Peak und eine MP3-Qualität an. Jede manuelle Änderung wählt '
                          'Benutzerdefiniert.',
        'processing_cancelled': 'Verarbeitung abgebrochen.',
        'processing_completed': 'Verarbeitung abgeschlossen',
        'processing_in_progress': 'Verarbeitung läuft',
        'processing_paused': 'Verarbeitung pausiert.',
        'processing_resumed': 'Verarbeitung fortgesetzt.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'WARNUNG — Qualitätskontrolle nicht möglich: {error}',
        'qc_log': ' — QC {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'WARNUNG — {detail}',
        'quality': 'Audioqualität',
        'quality_control': 'Automatische Qualitätskontrolle',
        'quality_control_tooltip': 'Misst jede Ausgabe erneut. Bei dynamischen MP3-Dateien kann '
                                   'die Messung bis zu drei korrigierende Neukodierungen auslösen. '
                                   'Das Deaktivieren ändert die Encoderqualität nicht, entfernt '
                                   'aber Abschlussprüfung, Korrekturen und Messgeräteaktivität.',
        'quality_tooltip': 'Steuert Qualität und Größe komprimierter Formate: eine kleine Zahl '
                           'bedeutet höhere Qualität und Bitrate. Liegt die gewählte Bitrate über '
                           'der Quelle, wächst die Datei. Eine größere Zahl verkleinert sie meist, '
                           'VBR garantiert jedoch keine identische Bytezahl. FLAC bleibt '
                           'verlustfrei; WAV und AIFF ignorieren diese Einstellung und behalten '
                           'ihre PCM-Eigenschaften. Bereiche: 0 = höchste Qualität; 1-2 = sehr '
                           'hoch; 3-4 = ausgewogen; 5-9 = kleinere Datei.',
        'ready': 'Bereit',
        'recursive_scan': 'Ordner werden rekursiv durchsucht…',
        'remove_all': 'Alle entfernen',
        'remove_selection': 'Auswahl entfernen',
        'replaygain_operation': 'ReplayGain ohne Neukodierung',
        'replaygain_tags_missing': 'ReplayGain-Tags wurden nicht gefunden.',
        'report_album_dbtp': 'album_eingang_dbtp',
        'report_album_lufs': 'album_eingang_lufs',
        'report_destination': 'ziel',
        'report_detail': 'details',
        'report_error': 'WARNUNG — CSV-Bericht konnte nicht erstellt werden: {error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'verstärkung_db',
        'report_input_dbtp': 'eingang_dbtp',
        'report_input_lufs': 'eingang_lufs',
        'report_log': 'CSV-Bericht — {path}',
        'report_mode': 'modus',
        'report_operation': 'vorgang',
        'report_output_dbtp': 'ausgang_dbtp',
        'report_output_lufs': 'ausgang_lufs',
        'report_path': 'Bericht: {path}',
        'report_qc': 'qualitätskontrolle',
        'report_seconds': 'dauer_sekunden',
        'report_source': 'quelle',
        'report_status': 'status',
        'report_tooltip': 'Erstellt im Ziel einen ausführlichen Bericht mit Messwerten, Zeiten und '
                          'Warnungen.',
        'resume': 'Nach Unterbrechung fortsetzen',
        'resume_not_saved': ' Fortsetzungspunkt nicht gespeichert: {error}',
        'resume_processing': 'Fortsetzen',
        'resume_tooltip': 'Bereits abgeschlossene Dateien mit denselben Einstellungen werden '
                          'erkannt und nicht erneut verarbeitet.',
        'resumed_progress': 'Fortgesetzt: {file}',
        'scan_error': 'FEHLER — {error}',
        'scanning_folders': 'Ordner werden analysiert…',
        'settings': 'Einstellungen',
        'show_finder': 'Im Finder anzeigen',
        'show_option_help': 'Hilfe anzeigen: {option}',
        'silent_album_copy': 'Stilles oder nicht messbares Album kopiert.',
        'silent_copy': 'Stilles oder nicht messbares Audio kopiert.',
        'silent_copy_no_replaygain': 'Stilles Audio ohne ReplayGain-Tags kopiert.',
        'silent_unmeasurable': 'Stilles oder nicht messbares Audio.',
        'simulation': 'Simulation',
        'skip_compliant': 'Bereits passende Dateien nicht neu codieren',
        'skip_compliant_tooltip': 'Standardmäßig aktiviert. Nach der Analyse wird eine Datei '
                                  'unverändert kopiert, wenn ihre Lautheit höchstens ±0,5 LU vom '
                                  'Ziel abweicht und der True Peak den Grenzwert nicht '
                                  'überschreitet. Im Albummodus wird die Lautheit für das ganze '
                                  'Album bewertet. Qualität und Größe bleiben exakt erhalten; das '
                                  'Protokoll weist darauf hin.',
        'skipped_progress': 'Übersprungen: {file}',
        'source_audio_count': 'Zu verarbeitende Audiodateien: {count}',
        'source_list_more': '… {count} weitere Quellen bleiben erhalten',
        'source_safety': 'Quelldateien werden niemals verschoben oder verändert.',
        'source_selection_tooltip': 'Mehrfachauswahl: ⌘-Klick für einzelne Elemente und '
                                    'Umschalt-Klick für einen Bereich.',
        'sources_added': '{count} Quelle(n) hinzugefügt.',
        'start': 'Starten',
        'status_analyzed': 'ANALYSIERT',
        'status_cancelled': 'ABGEBROCHEN',
        'status_error': 'FEHLER',
        'status_ok': 'OK',
        'status_resumed': 'FORTGESETZT',
        'status_skipped': 'ÜBERSPRUNGEN',
        'switch_to_dark': 'Dunkler Modus',
        'switch_to_light': 'Heller Modus',
        'tagline': 'Gleicht die wahrgenommene Audiolautstärke an',
        'target': 'Lautheitsziel',
        'target_tooltip': 'Das Lautheitsziel ist die angestrebte integrierte Lautheit des gesamten '
                          'Titels in LUFS. Ein weniger negativer Wert erzeugt eine lautere Datei: '
                          '-14 LUFS ist lauter als -16 LUFS. Ein Unterschied von 2 LU entspricht '
                          'vor einer möglichen Spitzenbegrenzung ungefähr 2 dB Pegeldifferenz.\n'
                          '\n'
                          'Orientierung: -18 LUFS für ein ruhigeres, dynamischeres Ergebnis; -16 '
                          'LUFS für eine allgemeine Balance; -14 LUFS für ein lauteres Ergebnis im '
                          'Streaming-Stil. Plattformen können bei der Wiedergabe eine eigene '
                          'Normalisierung anwenden.\n'
                          '\n'
                          'Das Ziel glättet nicht von selbst die Dynamik innerhalb des Titels. '
                          'Verhindert der maximale True Peak das verzerrungsfreie Erreichen des '
                          'Ziels, kann das Ergebnis etwas leiser bleiben.',
        'theme_accessible': 'Darstellung der Anwendung ändern. Die Auswahl wird gespeichert.',
        'total_time': 'Gesamtzeit: {duration}',
        'track_mode_log': 'Trackmodus — jede Audiodatei wird separat verarbeitet.',
        'track_two_pass': 'Titel-Normalisierung in zwei Durchläufen.',
        'true_peak_meter_exceeded': 'Überschreitung {margin} dB',
        'true_peak_meter_margin': 'Spielraum {margin} dB',
        'true_peak_meter_title': 'Peak-Spielraum',
        'true_peak_meter_tooltip': 'Vergleicht den True Peak der letzten Ausgabe mit dem gewählten '
                                   'Grenzwert. Die Markierung zeigt den letzten Wert, das Dreieck '
                                   'behält den höchsten Peak des Stapels. Grün: eingehalten; '
                                   'Orange: bis 0,25 dB darüber; Rot: stärker überschritten. Die '
                                   'orange Toleranz gehört zur LUFScale-Qualitätskontrolle und ist '
                                   'keine Liefernorm. Wird bei jedem Stapel zurückgesetzt.',
        'true_peak_meter_waiting': 'Warte auf eine dBTP-Messung',
        'version_changes': '• Die Gesamtzahl der Audiodateien wird beim Hinzufügen oder Entfernen '
                           'von Quellen aktualisiert.\n'
                           '• Messgerät und Abstand entsprechen wieder Version 1.21.25; ohne '
                           'Qualitätskontrolle bleibt es inaktiv.\n'
                           '• Die Schätzung zeigt nun auch die ungefähre Endzeit.\n'
                           '• Frühere interne Testwerkzeuge wurden entfernt.',
        'version_changes_title': 'Neu in Version {version}',
        'version_label': 'Version {version}',
        'volume': 'Lautstärke',
        'volume_loud': 'Laut: -14 LUFS',
        'volume_normal': 'Normal: -16 LUFS',
        'volume_soft': 'Leise: -18 LUFS',
        'volume_tooltip': 'Diese Einstellung ist eine Abkürzung zum Lautheitsziel; sie ändert '
                          'nicht die Wiedergabelautstärke des Macs.\n'
                          '\n'
                          '• Leise: -18 LUFS — ruhigerer Pegel, mehr dynamische Reserve und '
                          'geringere Wahrscheinlichkeit, den Limiter zu beanspruchen.\n'
                          '• Normal: -16 LUFS — ausgewogener Kompromiss und sinnvoller '
                          'Ausgangspunkt für eine persönliche Musiksammlung.\n'
                          '• Laut: -14 LUFS — präsentere Wiedergabe nahe Spotifys Ziel für '
                          '„Normal“, kann jedoch häufiger eine Begrenzung erfordern.\n'
                          '• Benutzerdefiniert — ermöglicht die direkte Eingabe eines anderen '
                          'LUFS-Ziels.\n'
                          '\n'
                          'Dies sind praktische Wahlmöglichkeiten, keine allgemeingültige Norm.',
        'zero_album_gain': 'Albumverstärkung null; Audio kopiert.'},
 'es': {'activity_cancelled': 'Actividad: proceso cancelado',
        'activity_cancelling': 'Actividad: cancelando…',
        'activity_completed': 'Actividad: proceso finalizado',
        'activity_compliant': 'Conformes: {count}',
        'activity_detected': 'Actividad: {total} archivo(s) detectado(s)',
        'activity_errors': 'Errores: {count}',
        'activity_files': 'Archivos: {count}',
        'activity_idle': 'Actividad: en espera',
        'activity_preparing': 'Actividad: preparando archivos…',
        'activity_progress': '{total} archivos • correctos {success} • alertas {warnings} • '
                             'errores {failed} • reanudados/omitidos {skipped} • conformes '
                             '{compliant}',
        'activity_skipped': 'Reanudados/omitidos: {count}',
        'activity_successes': 'Correctos: {count}',
        'activity_warnings': 'Alertas: {count}',
        'adaptive_disabled_log': 'Análisis adaptativo — sondas rápidas detenidas tras {sample} '
                                 'mediciones ({successes} éxitos, ahorro estimado {percent:+.1f} '
                                 '%).',
        'add_folders': 'Añadir carpetas…',
        'add_mp3': 'Añadir archivos de audio…',
        'add_replaygain': 'Añadir ReplayGain',
        'add_source_files': 'Añadir archivos de audio',
        'add_source_folder': 'Añadir una carpeta de origen',
        'album_gain_detail': 'Ganancia común del álbum: {gain:+.2f} dB.',
        'album_gain_log': 'Álbum «{album}» — ganancia común {gain:+.2f} dB.',
        'album_measurement_error': 'No se pudo medir el álbum: {error}',
        'album_mode_log': 'Modo Álbum — cada carpeta con archivos de audio forma un álbum.',
        'albums_measurement': 'Midiendo {count} álbum(es)…',
        'already_completed': 'Ya finalizado durante una ejecución anterior.',
        'already_compliant_badge': 'CONFORME',
        'already_compliant_copy': 'Ya conforme: copia idéntica sin recodificar el audio.',
        'already_compliant_log': 'ya conforme, sin recodificación',
        'analysis_cache_summary': 'Caché de análisis — {hits} medición(es) reutilizada(s).',
        'analysis_impossible': 'No se pudo analizar: {error}',
        'analysis_method': 'Método de análisis',
        'analysis_method_adaptive': 'Adaptativo — se detiene si no compensa',
        'analysis_method_fast': 'Rápido — experimental',
        'analysis_method_historical': 'Histórico — referencia',
        'analysis_method_log': 'Método de análisis — {method}.',
        'analysis_method_tooltip': 'Histórico usa únicamente la medición completa de referencia '
                                   'validada en 1.22.13. Rápido prueba la sonda lineal en cada '
                                   'archivo y vuelve a la medición histórica cuando es necesario. '
                                   'Adaptativo comienza como Rápido; tras al menos 12 mediciones y '
                                   '3 retornos, compara los tiempos observados y desactiva las '
                                   'sondas si el ahorro estimado sigue por debajo del 5 %. La '
                                   'calidad final y el control de calidad no se reducen.',
        'analysis_progress': 'Análisis {current}/{total}: {file}',
        'analyze': 'Analizar',
        'analyze_operation': 'análisis/simulación',
        'analyzed_progress': 'Analizado: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Flujo de audio copiado sin recodificar; etiquetas ReplayGain '
                                 'añadidas.',
        'audio_tab': 'Audio',
        'auto_start': 'Iniciar automáticamente después de soltar o pegar',
        'auto_start_tooltip': 'Inicia automáticamente el proceso después de añadir fuentes '
                              'mediante arrastrar y soltar o pegar, si ya se ha elegido un '
                              'destino.',
        'cancel': 'Cancelar',
        'cancelled_summary': 'Cancelado — {success} correcto(s), {failed} error(es), {skipped} '
                             'reanudado(s)/omitido(s), {warnings} aviso(s), {compliant} '
                             'conforme(s) — {duration}.',
        'cancelling': 'Cancelando…',
        'choose': 'Elegir…',
        'choose_output': 'Elegir la carpeta de destino',
        'clipboard': 'Portapapeles',
        'clipboard_empty': 'El portapapeles no contiene una ruta válida de carpeta o archivo de '
                           'audio compatible.',
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
                             'reanudado(s)/omitido(s), {warnings} aviso(s), {compliant} '
                             'conforme(s) — {duration}.',
        'completed_with_errors': 'Proceso finalizado con avisos',
        'convert': 'Normalizar',
        'convert_operation': 'uniformización de audio',
        'cpu_tooltip': 'Uso total del procesador del Mac, actualizado cada segundo durante el '
                       'proceso.',
        'cpu_unavailable': 'N/D',
        'cpu_usage': 'CPU',
        'create_report': 'Crear un informe CSV',
        'custom': 'Personalizado',
        'decrease_value': 'Disminuir el valor',
        'description': 'Uniformiza el volumen percibido en modo Pista o Álbum sin modificar los '
                       'originales.',
        'destination': 'Destino',
        'destination_error': 'ERROR — destino no disponible: {error}',
        'destination_path_tooltip': 'Haz clic en la ruta y usa las flechas, Inicio/Fin o la rueda. '
                                    'Se puede seleccionar y copiar, pero no modificar.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — se admiten subcarpetas',
        'drop_title': 'Suelta aquí tus carpetas o archivos de audio',
        'elapsed_time': 'Tiempo transcurrido: {duration}',
        'error_progress': 'Error: {file}',
        'estimated_result': 'Resultado estimado; no se creó ningún archivo.',
        'estimated_total_calculating': 'Tiempo total estimado: calculando…',
        'estimated_total_time': 'Tiempo total estimado: {duration}',
        'estimated_total_time_with_finish': 'Tiempo total estimado: {duration} — fin aproximado a '
                                            'las {time}',
        'estimated_total_unavailable': 'Tiempo total estimado: no disponible',
        'ffmpeg_download_button': 'Abrir el sitio oficial de FFmpeg',
        'ffmpeg_error_no_detail': 'Error de FFmpeg sin detalles.',
        'ffmpeg_execution_error': 'No se puede ejecutar FFmpeg: {error}',
        'ffmpeg_incompatible': 'FFmpeg incompatible',
        'ffmpeg_missing': 'No se encuentra FFmpeg',
        'ffmpeg_missing_encoders': 'Esta versión de FFmpeg no incluye todos los codificadores de '
                                   'audio necesarios: {encoders}.',
        'ffmpeg_missing_message': 'FFmpeg debe estar instalado y disponible en PATH, o situado '
                                  'junto al programa.',
        'ffmpeg_no_lame': 'Esta compilación de FFmpeg no incluye el codificador MP3 libmp3lame.',
        'ffmpeg_no_loudnorm': 'Esta compilación de FFmpeg no incluye el filtro loudnorm.',
        'ffmpeg_not_responding': 'FFmpeg no responde correctamente.',
        'file_exists': 'El archivo ya existe.',
        'files_found': '{total} archivo(s) de audio encontrado(s) — {operation} — {parallel} '
                       'proceso(s) paralelo(s).',
        'folder': 'Carpeta',
        'folder_unavailable': 'Carpeta no disponible',
        'guide_help_tooltip': 'Abre la guía PDF completa en el idioma seleccionado.',
        'guide_missing_message': 'No se ha encontrado la guía PDF: {path}',
        'guide_missing_title': 'Guía no disponible',
        'guide_open_error': 'macOS no ha podido abrir la guía PDF: {path}',
        'help_button': 'Ayuda',
        'help_overview': '• Normalización real, ReplayGain o análisis sin crear MP3.\n'
                         '• Modos Pista y Álbum que conservan las diferencias entre pistas.\n'
                         '• Estructura de carpetas, metadatos y carátulas conservados cuando '
                         'FFmpeg puede copiarlos.\n'
                         '• Los originales nunca se mueven ni se modifican.\n'
                         '• Paralelismo Auto, caché de análisis y reanudación tras una '
                         'interrupción.\n'
                         '• Control de calidad, informe CSV, progreso, CPU, medidor de sonoridad y '
                         'duración total estimada.\n'
                         '• Interfaz disponible en doce idiomas y guías PDF en doce idiomas.',
        'help_title': 'Características principales',
        'increase_value': 'Aumentar el valor',
        'interface_ffmpeg_message': 'La interfaz está disponible, pero la conversión necesita '
                                    'FFmpeg. Instala FFmpeg y reinicia la aplicación.',
        'internal_error': 'Error interno: {error}',
        'interrupted': 'Proceso interrumpido.',
        'invalid_location': 'Ubicación no válida',
        'language': 'Idioma',
        'language_tooltip': 'Cambia inmediatamente el idioma de la interfaz, los mensajes y los '
                            'futuros informes CSV. La elección se guarda.',
        'level_mode': 'Modo de sonoridad',
        'log_help_text': 'Cada línea corresponde a un archivo o a una etapa general.\n'
                         '\n'
                         '• Inicio: estado del proceso (OK, ALERTA, ERROR, reanudado u omitido).\n'
                         '• Después: nombre del MP3 y tiempo dedicado al archivo.\n'
                         '• Cartucho LUFS: nivel medido antes → nivel obtenido después del '
                         'proceso.\n'
                         '• Final: resultado del control de calidad y posible detalle.\n'
                         '\n'
                         'Colores: verde = éxito; naranja = alerta; rojo = archivo no terminado; '
                         'violeta azulado = reanudación; gris = información, elemento omitido o '
                         'cancelación.\n'
                         '\n'
                         'Los tiempos acumulados suman el trabajo de todas las tareas paralelas. '
                         'El tiempo total es la duración real transcurrida.\n'
                         '\n'
                         'QC ALERTA — pico significa que el pico verdadero vuelto a medir en la '
                         'salida supera en más de 0,25 dB el límite elegido. El archivo se crea '
                         'igualmente: no es un error de conversión. Sin embargo, no respeta '
                         'estrictamente el techo solicitado y deja menos margen para otra '
                         'codificación o algunos conversores. Cuanto más se acerca el valor dBTP a '
                         '0, mayor es el riesgo de picos entre muestras. Para corregir una alerta '
                         'persistente, elija un objetivo LUFS más bajo o un pico máximo más '
                         'prudente, por ejemplo −2,0 dBTP, y vuelva a procesar el archivo.',
        'log_placeholder': 'El informe del proceso aparecerá aquí.',
        'log_title': 'Registro de procesamiento',
        'loudness_meter_estimated': 'Estimado',
        'loudness_meter_help_text': 'Este medidor comprueba visualmente la regularidad de la '
                                    'normalización. Compara el último archivo de audio con el '
                                    'objetivo y calcula continuamente el mínimo y el máximo de los '
                                    'últimos 100 archivos. Los valores antiguos salen '
                                    'progresivamente de esta ventana para mantener dinámicos los '
                                    'lotes grandes. La puntuación del objetivo sigue abarcando '
                                    'todo el lote y el indicador no cambia ningún ajuste.',
        'loudness_meter_maximum': 'Máx {value}',
        'loudness_meter_measured': 'Medido',
        'loudness_meter_minimum': 'Mín {value}',
        'loudness_meter_target': 'Objetivo {value} LUFS',
        'loudness_meter_title': 'Medidor de sonoridad',
        'loudness_meter_tooltip': 'La línea roja representa el objetivo. El valor azul de la '
                                  'izquierda sigue el último archivo de audio. Las líneas y los '
                                  'valores gris y violeta oscuro muestran a la derecha el mínimo y '
                                  'el máximo de los últimos 100 archivos. La escala amplía las '
                                  'pequeñas diferencias y el medidor se reinicia con cada lote.',
        'loudness_meter_waiting': 'Esperando un archivo de audio',
        'loudness_score_acceptable': 'Aceptable',
        'loudness_score_check': 'Revisar',
        'loudness_score_excellent': 'Excelente',
        'loudness_score_good': 'Buena',
        'loudness_score_needs_qc': 'Puntuación objetivo: active el control de calidad',
        'loudness_score_not_applicable': 'Puntuación objetivo: no aplicable',
        'loudness_score_tooltip': 'La puntuación utiliza únicamente las salidas realmente medidas '
                                  'de nuevo. Se basa en el error cuadrático medio entre la '
                                  'sonoridad obtenida y la esperada: 100 = resultado exacto, 50 = '
                                  'error global de 0,5 LU, que es la tolerancia del control de '
                                  'calidad, y 0 = error de 1 LU o más. En modo Álbum, el valor '
                                  'esperado de cada pista incluye la ganancia común para conservar '
                                  'las diferencias previstas. El error RMS (raíz cuadrada de la '
                                  'media de los errores al cuadrado) resume la distancia global '
                                  'entre los niveles obtenidos y sus objetivos. Cuanto más se '
                                  'acerca a 0 LU, más precisa es la serie.',
        'loudness_score_value': 'Puntuación objetivo: {score}/100\n'
                                '{rating}\n'
                                'Error RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Puntuación objetivo: en espera',
        'measurement_unavailable': 'Medición no disponible.',
        'mode_album': 'Álbum — conserva las diferencias entre pistas',
        'mode_album_label': 'Álbum',
        'mode_tooltip': 'Pista ajusta cada MP3 por separado. Álbum calcula una ganancia común por '
                        'carpeta para conservar las diferencias de volumen entre sus pistas.',
        'mode_track': 'Pista — mismo nivel para cada archivo',
        'mode_track_label': 'Pista',
        'mp3': 'MP3',
        'mp3_filter': 'Audio compatible (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Ninguna carpeta seleccionada',
        'no_mp3': 'No se encontraron archivos de audio compatibles.',
        'no_new_source': 'No se añadió ninguna carpeta ni archivo de audio compatible.',
        'not_performed': 'No realizado',
        'open_output_error': 'No se puede abrir la carpeta de destino: {error}',
        'operation': 'Operación',
        'operation_analyze': 'Solo analizar — simulación sin crear archivos',
        'operation_analyze_label': 'Solo análisis',
        'operation_convert': 'Uniformizar — normalizar realmente el audio',
        'operation_convert_label': 'Uniformización de audio',
        'operation_replaygain': 'ReplayGain — sin recodificar el audio',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Uniformizar procesa realmente el audio. MP3, M4A/AAC, OGG y Opus '
                             'deben recodificarse: el tamaño depende de la calidad y puede '
                             'aumentar. FLAC se recodifica sin pérdida, pero su compresión puede '
                             'variar porque cambian las muestras. WAV y AIFF conservan frecuencia, '
                             'canales y profundidad compatibles con el origen. ReplayGain no '
                             'recodifica; Analizar no crea archivos.',
        'options_tab': 'Opciones',
        'overwrite': 'Sobrescribir archivos existentes',
        'overwrite_tooltip': 'Permite reemplazar un MP3 que ya existe en el destino. Los archivos '
                             'de origen nunca se sobrescriben.',
        'parallel': 'Procesos en paralelo',
        'parallel_adjusted': 'Paralelismo automático — {active} proceso(s), CPU {cpu:.0f} %.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automático, máximo {maximum}',
        'parallel_tooltip': 'Determina cuántos archivos pueden procesarse simultáneamente.\n'
                            '\n'
                            '• Auto comienza con un máximo de 4 tareas. Cuando se puede medir la '
                            'CPU, la comprueba cada segundo: añade una tarea por debajo del 70 % '
                            'de uso y retira una por encima del 92 %.\n'
                            '• Auto nunca supera el número de procesadores lógicos detectados y '
                            'tiene un límite absoluto de 16 tareas.\n'
                            '• Si no se puede medir la CPU, Auto utiliza directamente ese límite '
                            'detectado sin adaptación dinámica.\n'
                            '• Un valor numérico fija el número máximo de tareas simultáneas; no '
                            'es un objetivo de uso de CPU.\n'
                            '\n'
                            'Más tareas pueden acelerar un lote grande, pero aumentan la carga, la '
                            'temperatura y la actividad del disco. Pulsa − hasta que aparezca '
                            'Auto.',
        'paste': 'Pegar',
        'path_left': 'Ver la parte izquierda de la ruta',
        'path_right': 'Ver la parte derecha de la ruta',
        'pause': 'Pausa',
        'peak': 'Pico real máximo',
        'peak_tooltip': 'El pico real máximo es un límite, no un nivel que se deba alcanzar. '
                        'Limita en dBTP los picos más altos de la onda reconstruida, incluidos los '
                        'que aparecen entre muestras, para reducir la saturación después de '
                        'codificar o transcodificar.\n'
                        '\n'
                        '• -1,0 dBTP — límite habitual de entrega, con el pico de salida más '
                        'alto.\n'
                        '• -1,5 dBTP — valor predeterminado y compromiso prudente para MP3.\n'
                        '• -2,0 dBTP — margen adicional, útil si el archivo puede volver a '
                        'codificarse o si se usa un objetivo de sonoridad alto.\n'
                        '• 0 dBTP — sin margen; no recomendado para MP3.\n'
                        '\n'
                        'Un valor más negativo es más seguro, pero puede impedir que pistas muy '
                        'dinámicas alcancen exactamente el objetivo LUFS.',
        'phase_summary': 'Distribución estimada del tiempo total — análisis {analysis}, conversión '
                         '{conversion}, control de calidad {quality}.',
        'pipeline_enabled': 'Canalización de pistas — cada conversión comienza en cuanto termina '
                            'su análisis.',
        'pre_measurement': 'Midiendo los archivos de entrada…',
        'preset': 'Preajuste',
        'preset_dynamic': 'Música dinámica',
        'preset_library': 'Biblioteca musical — recomendado',
        'preset_streaming': 'Streaming más intenso',
        'preset_tooltip': 'Aplica de una vez un objetivo de sonoridad, un pico real máximo y una '
                          'calidad MP3 coherentes. Cualquier cambio manual selecciona '
                          'Personalizado.',
        'processing_cancelled': 'Proceso cancelado.',
        'processing_completed': 'Proceso finalizado',
        'processing_in_progress': 'Proceso en curso',
        'processing_paused': 'Proceso en pausa.',
        'processing_resumed': 'Proceso reanudado.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'AVISO — no se pudo realizar el control de calidad: {error}',
        'qc_log': ' — CC {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'AVISO — {detail}',
        'quality': 'Calidad de audio',
        'quality_control': 'Control de calidad automático',
        'quality_control_tooltip': 'Vuelve a medir cada salida. Para los MP3 de ruta dinámica, la '
                                   'medición puede activar hasta tres recodificaciones '
                                   'correctivas. Desactivarlo no cambia la calidad del '
                                   'codificador, pero elimina la verificación final, las '
                                   'correcciones y la actividad del medidor.',
        'quality_tooltip': 'Controla calidad y tamaño de los formatos comprimidos: un número bajo '
                           'usa mayor calidad y caudal. Si el caudal elegido supera el original, '
                           'el archivo aumenta. Un número alto suele reducirlo, pero VBR no '
                           'garantiza el mismo número de bytes. FLAC siempre es sin pérdida; WAV y '
                           'AIFF ignoran este ajuste y conservan sus propiedades PCM. Rangos: 0 = '
                           'máxima calidad; 1-2 = muy alta; 3-4 = equilibrio; 5-9 = tamaño menor.',
        'ready': 'Listo',
        'recursive_scan': 'Analizando carpetas de forma recursiva…',
        'remove_all': 'Quitar todo',
        'remove_selection': 'Quitar selección',
        'replaygain_operation': 'ReplayGain sin recodificación',
        'replaygain_tags_missing': 'No se encontraron las etiquetas ReplayGain.',
        'report_album_dbtp': 'dbtp_entrada_album',
        'report_album_lufs': 'lufs_entrada_album',
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
        'report_seconds': 'tiempo_segundos',
        'report_source': 'origen',
        'report_status': 'estado',
        'report_tooltip': 'Crea en el destino un informe detallado con mediciones, duraciones y '
                          'avisos.',
        'resume': 'Reanudar después de una interrupción',
        'resume_not_saved': ' No se guardó el punto de reanudación: {error}',
        'resume_processing': 'Reanudar',
        'resume_tooltip': 'Los archivos ya terminados con los mismos ajustes se reconocen y no se '
                          'vuelven a procesar.',
        'resumed_progress': 'Reanudado: {file}',
        'scan_error': 'ERROR — {error}',
        'scanning_folders': 'Analizando carpetas…',
        'settings': 'Ajustes',
        'show_finder': 'Mostrar en Finder',
        'show_option_help': 'Mostrar ayuda: {option}',
        'silent_album_copy': 'Álbum silencioso o no medible copiado.',
        'silent_copy': 'Audio silencioso o no medible copiado.',
        'silent_copy_no_replaygain': 'Audio silencioso copiado sin etiquetas ReplayGain.',
        'silent_unmeasurable': 'Audio silencioso o no medible.',
        'simulation': 'Simulación',
        'skip_compliant': 'No recodificar los archivos ya conformes',
        'skip_compliant_tooltip': 'Activado por defecto. Tras el análisis, un archivo situado a '
                                  '±0,5 LU del objetivo y cuyo pico real no supera el límite se '
                                  'copia sin cambios ni recodificación. En modo Álbum, la '
                                  'sonoridad se evalúa para el álbum completo. Así se conservan '
                                  'exactamente calidad y tamaño; el registro lo indica.',
        'skipped_progress': 'Omitido: {file}',
        'source_audio_count': 'Archivos de audio por procesar: {count}',
        'source_list_more': '… se conservan {count} fuentes más',
        'source_safety': 'Los archivos de origen nunca se mueven ni se modifican.',
        'source_selection_tooltip': 'Selección múltiple: ⌘ clic para elementos separados y Mayús '
                                    'clic para un intervalo.',
        'sources_added': '{count} fuente(s) añadida(s).',
        'start': 'Iniciar',
        'status_analyzed': 'ANALIZADO',
        'status_cancelled': 'CANCELADO',
        'status_error': 'ERROR',
        'status_ok': 'OK',
        'status_resumed': 'REANUDADO',
        'status_skipped': 'OMITIDO',
        'switch_to_dark': 'Modo oscuro',
        'switch_to_light': 'Modo claro',
        'tagline': 'Uniformiza el volumen de audio percibido',
        'target': 'Objetivo de sonoridad',
        'target_tooltip': 'El objetivo de sonoridad es la sonoridad integrada deseada para toda la '
                          'pista, expresada en LUFS. Un valor menos negativo produce un archivo '
                          'más fuerte: -14 LUFS es más fuerte que -16 LUFS. Una diferencia de 2 LU '
                          'equivale aproximadamente a 2 dB de nivel antes de una eventual '
                          'limitación de pico.\n'
                          '\n'
                          'Referencias: -18 LUFS para un resultado más tranquilo y dinámico; -16 '
                          'LUFS para un equilibrio general; -14 LUFS para un resultado más fuerte '
                          'de tipo streaming. Las plataformas pueden aplicar después su propia '
                          'normalización de reproducción.\n'
                          '\n'
                          'Este objetivo no aplana por sí solo la dinámica interna de la pista. Si '
                          'el pico real máximo impide alcanzar el objetivo sin saturación, el '
                          'resultado puede quedar ligeramente más bajo.',
        'theme_accessible': 'Cambiar la apariencia de la aplicación. La elección se guarda.',
        'total_time': 'Tiempo total: {duration}',
        'track_mode_log': 'Modo Pista — cada archivo de audio se procesa por separado.',
        'track_two_pass': 'Normalización de pista en dos pasadas.',
        'true_peak_meter_exceeded': 'Exceso {margin} dB',
        'true_peak_meter_margin': 'Margen {margin} dB',
        'true_peak_meter_title': 'Margen de pico',
        'true_peak_meter_tooltip': 'Compara el pico real de la última salida con el límite '
                                   'elegido. El marcador muestra el último valor y el triángulo '
                                   'conserva el pico más alto del lote. Verde: límite respetado; '
                                   'naranja: exceso de hasta 0,25 dB; rojo: exceso mayor. La '
                                   'tolerancia naranja pertenece al control de calidad de LUFScale '
                                   'y no es una norma de entrega. Se reinicia con cada lote.',
        'true_peak_meter_waiting': 'Esperando una medición dBTP',
        'version_changes': '• El número total de archivos de audio se actualiza al añadir o '
                           'retirar fuentes.\n'
                           '• El medidor recupera las dimensiones y la separación de la versión '
                           '1.21.25 y permanece inactivo sin control de calidad.\n'
                           '• La estimación indica también la hora aproximada de finalización.\n'
                           '• Se han retirado las antiguas herramientas internas de prueba.',
        'version_changes_title': 'Novedades de la versión {version}',
        'version_label': 'Versión {version}',
        'volume': 'Volumen',
        'volume_loud': 'Fuerte: -14 LUFS',
        'volume_normal': 'Normal: -16 LUFS',
        'volume_soft': 'Suave: -18 LUFS',
        'volume_tooltip': 'Este ajuste es un acceso directo al objetivo de sonoridad; no cambia el '
                          'volumen de escucha del Mac.\n'
                          '\n'
                          '• Suave: -18 LUFS — nivel más tranquilo, más margen dinámico y menos '
                          'riesgo de activar el limitador.\n'
                          '• Normal: -16 LUFS — compromiso equilibrado y buen punto de partida '
                          'para una biblioteca personal.\n'
                          '• Fuerte: -14 LUFS — reproducción más presente, cercana al objetivo '
                          'Normal de Spotify, pero con más probabilidad de necesitar limitación.\n'
                          '• Personalizado — permite introducir directamente otro objetivo LUFS.\n'
                          '\n'
                          'Son opciones prácticas, no una norma universal.',
        'zero_album_gain': 'Ganancia de álbum nula; audio copiado.'},
 'hi': {'activity_cancelled': 'गतिविधि: प्रसंस्करण रद्द',
        'activity_cancelling': 'गतिविधि: रद्द किया जा रहा है…',
        'activity_completed': 'गतिविधि: प्रसंस्करण पूरा',
        'activity_compliant': 'अनुरूप: {count}',
        'activity_detected': 'गतिविधि: {total} फ़ाइल मिलीं',
        'activity_errors': 'त्रुटि: {count}',
        'activity_files': 'फ़ाइलें: {count}',
        'activity_idle': 'गतिविधि: प्रतीक्षा में',
        'activity_preparing': 'गतिविधि: फ़ाइलें तैयार हो रही हैं…',
        'activity_progress': '{total} फ़ाइलें • सफल {success} • चेतावनी {warnings} • त्रुटि '
                             '{failed} • जारी/छोड़े {skipped} • अनुरूप {compliant}',
        'activity_skipped': 'जारी/छोड़े: {count}',
        'activity_successes': 'सफल: {count}',
        'activity_warnings': 'चेतावनी: {count}',
        'adaptive_disabled_log': 'अनुकूली विश्लेषण — {sample} माप के बाद तेज़ जाँच बंद '
                                 '({successes} सफल, अनुमानित बचत {percent:+.1f}%)।',
        'add_folders': 'फ़ोल्डर जोड़ें…',
        'add_mp3': 'ऑडियो फ़ाइलें जोड़ें…',
        'add_replaygain': 'ReplayGain जोड़ें',
        'add_source_files': 'ऑडियो फ़ाइलें जोड़ें',
        'add_source_folder': 'स्रोत फ़ोल्डर जोड़ें',
        'album_gain_detail': 'साझा एल्बम गेन {gain:+.2f} dB।',
        'album_gain_log': 'एल्बम “{album}” — साझा गेन {gain:+.2f} dB।',
        'album_measurement_error': 'एल्बम मापन विफल: {error}',
        'album_mode_log': 'एल्बम मोड — ऑडियो फ़ाइलों वाला हर फ़ोल्डर एक एल्बम है।',
        'albums_measurement': '{count} एल्बम मापे जा रहे हैं…',
        'already_completed': 'पिछले रन में पहले ही पूरा।',
        'already_compliant_badge': 'अनुरूप',
        'already_compliant_copy': 'पहले से अनुरूप: ऑडियो पुनः एनकोड किए बिना समान कॉपी।',
        'already_compliant_log': 'पहले से अनुरूप, पुनः एनकोड नहीं',
        'analysis_cache_summary': 'विश्लेषण कैश — {hits} मापन पुनः उपयोग हुए।',
        'analysis_impossible': 'विश्लेषण विफल: {error}',
        'analysis_method': 'विश्लेषण विधि',
        'analysis_method_adaptive': 'अनुकूली — लाभ न हो तो बंद',
        'analysis_method_fast': 'तेज़ — प्रायोगिक',
        'analysis_method_historical': 'पुरानी — संदर्भ',
        'analysis_method_log': 'विश्लेषण विधि — {method}।',
        'analysis_method_tooltip': 'पुरानी विधि केवल 1.22.13 में सत्यापित पूर्ण संदर्भ माप का '
                                   'उपयोग करती है। तेज़ विधि हर फ़ाइल पर रैखिक जाँच करती है और '
                                   'आवश्यकता होने पर पुरानी माप पर लौटती है। अनुकूली विधि तेज़ की '
                                   'तरह शुरू होती है; कम से कम 12 माप और 3 वापसी के बाद यह '
                                   'वास्तविक समय की तुलना करती है और अनुमानित बचत 5% से कम रहने पर '
                                   'जाँच बंद कर देती है। अंतिम गुणवत्ता और गुणवत्ता नियंत्रण कम '
                                   'नहीं किए जाते।',
        'analysis_progress': 'विश्लेषण {current}/{total}: {file}',
        'analyze': 'विश्लेषण करें',
        'analyze_operation': 'विश्लेषण/अनुकरण',
        'analyzed_progress': 'विश्लेषित: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'ऑडियो स्ट्रीम बिना पुनः एन्कोडिंग कॉपी हुई; ReplayGain टैग जोड़े '
                                 'गए।',
        'audio_tab': 'ऑडियो',
        'auto_start': 'ड्रॉप या पेस्ट के बाद स्वतः शुरू करें',
        'auto_start_tooltip': 'गंतव्य चुना होने पर ड्रैग-एंड-ड्रॉप या पेस्ट से स्रोत जुड़ते ही '
                              'प्रसंस्करण शुरू करता है।',
        'cancel': 'रद्द करें',
        'cancelled_summary': 'रद्द — {success} सफल, {failed} त्रुटि, {skipped} जारी/छोड़े, '
                             '{warnings} चेतावनी, {compliant} अनुरूप — {duration}।',
        'cancelling': 'रद्द किया जा रहा है…',
        'choose': 'चुनें…',
        'choose_output': 'गंतव्य फ़ोल्डर चुनें',
        'clipboard': 'क्लिपबोर्ड',
        'clipboard_empty': 'क्लिपबोर्ड में किसी फ़ोल्डर या समर्थित ऑडियो फ़ाइल का मान्य पथ नहीं '
                           'है।',
        'close_question': 'प्रसंस्करण रद्द कर अनुप्रयोग बंद करें?',
        'completed_dialog_summary': 'स्थिति: पूर्ण\n'
                                    'फ़ाइलें: {files}\n'
                                    'सफल: {success}\n'
                                    'त्रुटियाँ: {failed}\n'
                                    'जारी या छोड़े गए: {skipped}\n'
                                    'चेतावनियाँ: {warnings}\n'
                                    'अनुरूप: {compliant}\n'
                                    'कुल समय: {duration}',
        'completed_summary': 'पूरा — {success} सफल, {failed} त्रुटि, {skipped} जारी/छोड़े, '
                             '{warnings} चेतावनी, {compliant} अनुरूप — {duration}।',
        'completed_with_errors': 'प्रसंस्करण चेतावनियों के साथ पूरा',
        'convert': 'समान करें',
        'convert_operation': 'ऑडियो सामान्यीकरण',
        'cpu_tooltip': 'प्रसंस्करण के दौरान हर सेकंड अपडेट होने वाला Mac का कुल CPU उपयोग।',
        'cpu_unavailable': 'उपलब्ध नहीं',
        'cpu_usage': 'CPU',
        'create_report': 'CSV रिपोर्ट बनाएँ',
        'custom': 'कस्टम',
        'decrease_value': 'मान घटाएँ',
        'description': 'मूल फ़ाइलों को बदले बिना ट्रैक या एल्बम मोड में सुनाई देने वाली '
                       'ध्वनि-तीव्रता समान करता है।',
        'destination': 'गंतव्य',
        'destination_error': 'त्रुटि — गंतव्य उपलब्ध नहीं: {error}',
        'destination_path_tooltip': 'पथ पर क्लिक करें, फिर तीर कुंजियों, Home/End या माउस व्हील का '
                                    'उपयोग करें। पथ चुना और कॉपी किया जा सकता है, लेकिन बदला नहीं '
                                    'जा सकता।',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — उप-फ़ोल्डर सहित',
        'drop_title': 'फ़ोल्डर या ऑडियो फ़ाइलें यहाँ छोड़ें',
        'elapsed_time': 'बीता समय: {duration}',
        'error_progress': 'त्रुटि: {file}',
        'estimated_result': 'अनुमानित परिणाम; कोई फ़ाइल नहीं बनी।',
        'estimated_total_calculating': 'अनुमानित कुल समय: गणना जारी…',
        'estimated_total_time': 'अनुमानित कुल समय: {duration}',
        'estimated_total_time_with_finish': 'अनुमानित कुल समय: {duration} — लगभग {time} पर समाप्ति',
        'estimated_total_unavailable': 'अनुमानित कुल समय: उपलब्ध नहीं',
        'ffmpeg_download_button': 'FFmpeg की आधिकारिक वेबसाइट खोलें',
        'ffmpeg_error_no_detail': 'बिना विवरण की FFmpeg त्रुटि।',
        'ffmpeg_execution_error': 'FFmpeg नहीं चल सका: {error}',
        'ffmpeg_incompatible': 'असंगत FFmpeg',
        'ffmpeg_missing': 'FFmpeg नहीं मिला',
        'ffmpeg_missing_encoders': 'इस FFmpeg में सभी आवश्यक ऑडियो एनकोडर नहीं हैं: {encoders}।',
        'ffmpeg_missing_message': 'FFmpeg स्थापित और PATH में उपलब्ध होना चाहिए, या प्रोग्राम के '
                                  'पास रखा होना चाहिए।',
        'ffmpeg_no_lame': 'इस FFmpeg बिल्ड में libmp3lame MP3 एन्कोडर नहीं है।',
        'ffmpeg_no_loudnorm': 'इस FFmpeg बिल्ड में loudnorm फ़िल्टर नहीं है।',
        'ffmpeg_not_responding': 'FFmpeg सही उत्तर नहीं दे रहा है।',
        'file_exists': 'फ़ाइल पहले से मौजूद है।',
        'files_found': '{total} ऑडियो फ़ाइलें मिलीं — {operation} — {parallel} समानांतर '
                       'प्रक्रियाएँ।',
        'folder': 'फ़ोल्डर',
        'folder_unavailable': 'फ़ोल्डर उपलब्ध नहीं',
        'guide_help_tooltip': 'चुनी हुई भाषा में पूरा PDF मार्गदर्शक खोलता है।',
        'guide_missing_message': 'PDF मार्गदर्शक नहीं मिला: {path}',
        'guide_missing_title': 'मार्गदर्शक उपलब्ध नहीं',
        'guide_open_error': 'macOS PDF मार्गदर्शक नहीं खोल सका: {path}',
        'help_button': 'सहायता',
        'help_overview': '• वास्तविक ऑडियो सामान्यीकरण, ReplayGain या MP3 बनाए बिना विश्लेषण।\n'
                         '• ट्रैक और एल्बम मोड, जिनमें ट्रैकों के बीच अंतर सुरक्षित रहता है।\n'
                         '• जहाँ FFmpeg प्रतिलिपि कर सके वहाँ फ़ोल्डर संरचना, मेटाडेटा और आवरण '
                         'सुरक्षित रहते हैं।\n'
                         '• मूल फ़ाइलें कभी स्थानांतरित या संशोधित नहीं होतीं।\n'
                         '• स्वचालित समानांतरता, विश्लेषण कैश और रुकावट के बाद पुनः आरंभ।\n'
                         '• गुणवत्ता नियंत्रण, CSV रिपोर्ट, प्रगति, CPU, ध्वनि-तीव्रता मीटर और '
                         'अनुमानित कुल समय।\n'
                         '• इंटरफ़ेस और PDF मार्गदर्शक बारह भाषाओं में उपलब्ध हैं।',
        'help_title': 'मुख्य विशेषताएँ',
        'increase_value': 'मान बढ़ाएँ',
        'interface_ffmpeg_message': 'इंटरफ़ेस उपलब्ध है, लेकिन परिवर्तन के लिए FFmpeg चाहिए। '
                                    'FFmpeg स्थापित कर अनुप्रयोग फिर शुरू करें।',
        'internal_error': 'आंतरिक त्रुटि: {error}',
        'interrupted': 'प्रसंस्करण बाधित।',
        'invalid_location': 'अमान्य स्थान',
        'language': 'भाषा',
        'language_tooltip': 'इंटरफ़ेस, संदेशों और भविष्य की CSV रिपोर्ट की भाषा तुरंत बदलता है। '
                            'चयन सहेजा जाता है।',
        'level_mode': 'ध्वनि-तीव्रता मोड',
        'log_help_text': 'हर पंक्ति किसी फ़ाइल या सामान्य प्रसंस्करण चरण का वर्णन करती है।\n'
                         '\n'
                         '• शुरुआत: स्थिति (OK, चेतावनी, त्रुटि, जारी या छोड़ा गया)।\n'
                         '• फिर: MP3 नाम और उस फ़ाइल पर लगा समय।\n'
                         '• LUFS चिह्न: प्रसंस्करण से पहले का स्तर → बाद का स्तर।\n'
                         '• अंत: गुणवत्ता-नियंत्रण परिणाम और अतिरिक्त विवरण।\n'
                         '\n'
                         'रंग: हरा = सफलता; नारंगी = चेतावनी; लाल = अधूरी फ़ाइल; नीला-बैंगनी = '
                         'जारी; धूसर = सूचना, छोड़ा गया या रद्द।\n'
                         '\n'
                         'संचयी समय सभी समानांतर कार्यों का योग है। कुल समय वास्तविक बीता समय है।\n'
                         '\n'
                         'QC चेतावनी — पीक का अर्थ है कि आउटपुट की दोबारा मापी गई ट्रू पीक चुनी गई '
                         'सीमा से 0.25 dB से अधिक ऊपर है। फ़ाइल फिर भी बनती है: यह रूपांतरण त्रुटि '
                         'नहीं है। लेकिन यह मांगी गई ऊपरी सीमा का पूरी तरह पालन नहीं करती और '
                         'दोबारा एन्कोडिंग या कुछ कन्वर्टरों के लिए कम गुंजाइश छोड़ती है। dBTP मान '
                         '0 के जितना पास होगा, इंटर-सैंपल पीक का जोखिम उतना अधिक होगा। लगातार '
                         'चेतावनी सुधारने के लिए कम LUFS लक्ष्य या −2.0 dBTP जैसी अधिक सुरक्षित '
                         'अधिकतम पीक चुनकर फ़ाइल फिर चलाएँ।',
        'log_placeholder': 'प्रसंस्करण लॉग यहाँ दिखाई देगा।',
        'log_title': 'प्रसंस्करण लॉग',
        'loudness_meter_estimated': 'अनुमानित',
        'loudness_meter_help_text': 'यह मीटर सामान्यीकरण की नियमितता की दृश्य जाँच करता है। यह '
                                    'नवीनतम ऑडियो फ़ाइल की लक्ष्य से तुलना करता है और पिछली 100 '
                                    'फ़ाइलों का न्यूनतम तथा अधिकतम लगातार निकालता है। पुराने मान '
                                    'धीरे-धीरे इस विंडो से बाहर हो जाते हैं, इसलिए बड़े बैच में '
                                    'प्रदर्शन गतिशील रहता है। लक्ष्य स्कोर पूरे बैच पर बना रहता है '
                                    'और यह संकेतक कोई सेटिंग नहीं बदलता।',
        'loudness_meter_maximum': 'अधिक {value}',
        'loudness_meter_measured': 'मापा गया',
        'loudness_meter_minimum': 'न्यून {value}',
        'loudness_meter_target': 'लक्ष्य {value} LUFS',
        'loudness_meter_title': 'ध्वनि-तीव्रता मीटर',
        'loudness_meter_tooltip': 'लाल रेखा लक्ष्य दिखाती है। बाईं नीली संख्या नवीनतम ऑडियो फ़ाइल '
                                  'का स्तर दिखाती है। दाईं ओर की धूसर और गहरी बैंगनी रेखाएँ तथा '
                                  'मान पिछली 100 फ़ाइलों का न्यूनतम और अधिकतम दिखाते हैं। पैमाना '
                                  'छोटे अंतर बढ़ाकर दिखाता है और हर नए बैच पर रीसेट होता है।',
        'loudness_meter_waiting': 'ऑडियो फ़ाइल की प्रतीक्षा',
        'loudness_score_acceptable': 'स्वीकार्य',
        'loudness_score_check': 'जाँचें',
        'loudness_score_excellent': 'उत्कृष्ट',
        'loudness_score_good': 'अच्छा',
        'loudness_score_needs_qc': 'लक्ष्य स्कोर: गुणवत्ता नियंत्रण चालू करें',
        'loudness_score_not_applicable': 'लक्ष्य स्कोर: लागू नहीं',
        'loudness_score_tooltip': 'स्कोर केवल वास्तव में दोबारा मापे गए आउटपुट उपयोग करता है। RMS '
                                  'त्रुटि (वर्गीकृत अंतरों के औसत का वर्गमूल) प्राप्त '
                                  'ध्वनि-तीव्रताओं और लक्ष्यों के कुल अंतर को बताती है। 0 LU के '
                                  'जितना निकट, बैच उतना सटीक: 100 = ठीक लक्ष्य, 50 = 0.5 LU RMS, '
                                  'और 0 = 1 LU या अधिक। एल्बम मोड में हर ट्रैक का अपेक्षित मान '
                                  'साझा गेन शामिल करता है।',
        'loudness_score_value': 'लक्ष्य स्कोर: {score}/100\n'
                                '{rating}\n'
                                'RMS त्रुटि: {deviation}\xa0LU',
        'loudness_score_waiting': 'लक्ष्य स्कोर: प्रतीक्षा',
        'measurement_unavailable': 'मापन उपलब्ध नहीं।',
        'mode_album': 'एल्बम — ट्रैकों के बीच अंतर सुरक्षित',
        'mode_album_label': 'एल्बम',
        'mode_tooltip': 'ट्रैक प्रत्येक MP3 को अलग समायोजित करता है। एल्बम हर फ़ोल्डर के लिए एक '
                        'साझा गेन गणना करता है ताकि ट्रैकों के बीच ध्वनि-अंतर बना रहे।',
        'mode_track': 'ट्रैक — हर फ़ाइल के लिए समान स्तर',
        'mode_track_label': 'ट्रैक',
        'mp3': 'MP3',
        'mp3_filter': 'समर्थित ऑडियो (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'कोई फ़ोल्डर नहीं चुना गया',
        'no_mp3': 'कोई समर्थित ऑडियो फ़ाइल नहीं मिली।',
        'no_new_source': 'कोई नया मान्य फ़ोल्डर या समर्थित ऑडियो फ़ाइल नहीं जोड़ी गई।',
        'not_performed': 'नहीं किया गया',
        'open_output_error': 'गंतव्य फ़ोल्डर नहीं खुल सका: {error}',
        'operation': 'क्रिया',
        'operation_analyze': 'केवल विश्लेषण — फ़ाइल बनाए बिना सिमुलेशन',
        'operation_analyze_label': 'केवल विश्लेषण',
        'operation_convert': 'समान करें — ऑडियो को वास्तव में सामान्य करें',
        'operation_convert_label': 'ऑडियो सामान्यीकरण',
        'operation_replaygain': 'ReplayGain — ऑडियो पुनः एन्कोड नहीं',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'समान करना ऑडियो को वास्तव में संसाधित करता है। MP3, M4A/AAC, OGG और '
                             'Opus को फिर एन्कोड करना पड़ता है; आकार गुणवत्ता पर निर्भर है और बढ़ '
                             'सकता है। FLAC दोषरहित फिर एन्कोड होता है, पर बदले नमूनों से संपीड़न '
                             'बदल सकता है। WAV/AIFF स्रोत-संगत दर, चैनल और बिट गहराई रखते हैं। '
                             'ReplayGain फिर एन्कोड नहीं करता; विश्लेषण फ़ाइल नहीं बनाता।',
        'options_tab': 'विकल्प',
        'overwrite': 'मौजूदा फ़ाइलें अधिलेखित करें',
        'overwrite_tooltip': 'गंतव्य में पहले से मौजूद MP3 को बदलने देता है। स्रोत फ़ाइलें कभी '
                             'अधिलेखित नहीं होतीं।',
        'parallel': 'समानांतर प्रक्रियाएँ',
        'parallel_adjusted': 'स्वचालित समानांतरता — {active} प्रक्रियाएँ, CPU {cpu:.0f}%।',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'स्वचालित, अधिकतम {maximum}',
        'parallel_tooltip': 'एक समय में संसाधित होने वाली फ़ाइलों की संख्या तय करता है।\n'
                            '\n'
                            '• Auto अधिकतम 4 कार्यों से शुरू होता है। CPU मापन उपलब्ध होने पर 70% '
                            'से कम उपयोग पर एक कार्य जोड़ता और 92% से अधिक पर एक हटाता है।\n'
                            '• यह मिले लॉजिकल CPU की संख्या और 16 की पूर्ण सीमा से अधिक नहीं '
                            'जाता।\n'
                            '• CPU मापन न हो तो मिली सीमा सीधे उपयोग होती है।\n'
                            '• संख्या एक साथ चलने वाले कार्यों की अधिकतम सीमा तय करती है; यह CPU '
                            'उपयोग का लक्ष्य नहीं है।\n'
                            '\n'
                            'Auto दिखने तक − दबाएँ।',
        'paste': 'चिपकाएँ',
        'path_left': 'पथ का बायाँ भाग दिखाएँ',
        'path_right': 'पथ का दायाँ भाग दिखाएँ',
        'pause': 'रोकें',
        'peak': 'अधिकतम ट्रू पीक',
        'peak_tooltip': 'अधिकतम ट्रू पीक एक सीमा है, प्राप्त करने का लक्ष्य नहीं। यह नमूनों के बीच '
                        'की चोटियों सहित पुनर्निर्मित तरंग की सबसे ऊँची चोटियों को dBTP में सीमित '
                        'करता है।\n'
                        '\n'
                        '• -1.0 dBTP — सामान्य वितरण सीमा।\n'
                        '• -1.5 dBTP — MP3 के लिए सावधान डिफ़ॉल्ट।\n'
                        '• -2.0 dBTP — पुनः एन्कोडिंग या ऊँचे लक्ष्य के लिए अतिरिक्त हेडरूम।\n'
                        '• 0 dBTP — कोई हेडरूम नहीं; MP3 के लिए अनुशंसित नहीं।\n'
                        '\n'
                        'अधिक ऋणात्मक मान सुरक्षित है, पर बहुत डायनेमिक ट्रैक को लक्ष्य तक पहुँचने '
                        'से रोक सकता है।',
        'phase_summary': 'अनुमानित कुल-समय विभाजन — विश्लेषण {analysis}, परिवर्तन {conversion}, '
                         'गुणवत्ता नियंत्रण {quality}।',
        'pipeline_enabled': 'ट्रैक पाइपलाइन — विश्लेषण पूरा होते ही प्रत्येक परिवर्तन शुरू होता '
                            'है।',
        'pre_measurement': 'इनपुट फ़ाइलें मापी जा रही हैं…',
        'preset': 'प्रीसेट',
        'preset_dynamic': 'डायनेमिक संगीत',
        'preset_library': 'संगीत लाइब्रेरी — अनुशंसित',
        'preset_streaming': 'अधिक तेज़ स्ट्रीमिंग',
        'preset_tooltip': 'ध्वनि-तीव्रता लक्ष्य, अधिकतम ट्रू पीक और MP3 गुणवत्ता का सुसंगत समूह एक '
                          'साथ लागू करता है। कोई मैन्युअल बदलाव कस्टम चुनता है।',
        'processing_cancelled': 'प्रसंस्करण रद्द।',
        'processing_completed': 'प्रसंस्करण पूरा',
        'processing_in_progress': 'प्रसंस्करण जारी',
        'processing_paused': 'प्रसंस्करण रुका हुआ है।',
        'processing_resumed': 'प्रसंस्करण फिर शुरू हुआ।',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'चेतावनी — गुणवत्ता नियंत्रण विफल: {error}',
        'qc_log': ' — गुणवत्ता {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'चेतावनी — {detail}',
        'quality': 'ऑडियो गुणवत्ता',
        'quality_control': 'स्वचालित गुणवत्ता नियंत्रण',
        'quality_control_tooltip': 'हर आउटपुट को दोबारा मापता है। डायनेमिक-पथ MP3 में माप अधिकतम '
                                   'तीन सुधारात्मक री-एन्कोड शुरू कर सकता है। इसे बंद करने से '
                                   'एन्कोडर गुणवत्ता नहीं बदलती, लेकिन अंतिम जाँच, सुधार और मीटर '
                                   'गतिविधि हट जाती है।',
        'quality_tooltip': 'संपीड़ित प्रारूपों की गुणवत्ता और आकार नियंत्रित करता है। छोटी संख्या '
                           'अधिक गुणवत्ता और बिटरेट देती है। चुना बिटरेट स्रोत से बड़ा हो तो फ़ाइल '
                           'बढ़ती है। बड़ी संख्या आम तौर पर आकार घटाती है, लेकिन VBR समान बाइटों '
                           'की गारंटी नहीं देता। FLAC दोषरहित रहता है; WAV/AIFF अपने PCM गुण रखते '
                           'हैं। स्तर: 0 = सर्वोच्च गुणवत्ता; 1-2 = बहुत उच्च; 3-4 = संतुलन; 5-9 = '
                           'छोटा आकार।',
        'ready': 'तैयार',
        'recursive_scan': 'फ़ोल्डर पुनरावर्ती रूप से स्कैन हो रहे हैं…',
        'remove_all': 'सभी हटाएँ',
        'remove_selection': 'चयन हटाएँ',
        'replaygain_operation': 'बिना पुनः एन्कोडिंग ReplayGain',
        'replaygain_tags_missing': 'ReplayGain टैग नहीं मिले।',
        'report_album_dbtp': 'एल्बम_इनपुट_dbtp',
        'report_album_lufs': 'एल्बम_इनपुट_lufs',
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
        'report_seconds': 'बीता_समय_सेकंड',
        'report_source': 'स्रोत',
        'report_status': 'स्थिति',
        'report_tooltip': 'गंतव्य में माप, अवधि और चेतावनियों वाली विस्तृत रिपोर्ट बनाता है।',
        'resume': 'रुकावट के बाद जारी रखें',
        'resume_not_saved': ' पुनः आरंभ बिंदु सहेजा नहीं गया: {error}',
        'resume_processing': 'जारी रखें',
        'resume_tooltip': 'उसी सेटिंग से पूरी हुई फ़ाइलें पहचान ली जाती हैं और फिर संसाधित नहीं '
                          'होतीं।',
        'resumed_progress': 'जारी: {file}',
        'scan_error': 'त्रुटि — {error}',
        'scanning_folders': 'फ़ोल्डर स्कैन हो रहे हैं…',
        'settings': 'सेटिंग्स',
        'show_finder': 'Finder में दिखाएँ',
        'show_option_help': 'सहायता दिखाएँ: {option}',
        'silent_album_copy': 'मौन या माप न सकने योग्य एल्बम कॉपी हुआ।',
        'silent_copy': 'मौन या माप न सकने योग्य ऑडियो कॉपी हुआ।',
        'silent_copy_no_replaygain': 'मौन ऑडियो ReplayGain टैग के बिना कॉपी हुआ।',
        'silent_unmeasurable': 'मौन या माप न सकने योग्य ऑडियो।',
        'simulation': 'अनुकरण',
        'skip_compliant': 'पहले से अनुरूप फ़ाइलों को दोबारा एनकोड न करें',
        'skip_compliant_tooltip': 'डिफ़ॉल्ट रूप से चालू। विश्लेषण के बाद लक्ष्य से ±0.5 LU के भीतर '
                                  'और true peak सीमा से नीचे वाली फ़ाइल बिना बदले और बिना पुनः '
                                  'एनकोड किए कॉपी होती है। एल्बम मोड में लाउडनेस पूरे एल्बम पर '
                                  'जाँची जाती है। गुणवत्ता और आकार बिल्कुल सुरक्षित रहते हैं; लॉग '
                                  'इसे बताता है।',
        'skipped_progress': 'छोड़ा: {file}',
        'source_audio_count': 'प्रोसेस की जाने वाली ऑडियो फ़ाइलें: {count}',
        'source_list_more': '… {count} और स्रोत सुरक्षित हैं',
        'source_safety': 'स्रोत फ़ाइलें कभी स्थानांतरित या संशोधित नहीं होतीं।',
        'source_selection_tooltip': 'एकाधिक चयन: अलग वस्तुओं के लिए Command-क्लिक और श्रेणी के लिए '
                                    'Shift-क्लिक।',
        'sources_added': '{count} स्रोत जोड़े गए।',
        'start': 'शुरू करें',
        'status_analyzed': 'विश्लेषित',
        'status_cancelled': 'रद्द',
        'status_error': 'त्रुटि',
        'status_ok': 'OK',
        'status_resumed': 'जारी',
        'status_skipped': 'छोड़ा',
        'switch_to_dark': 'गहरा मोड',
        'switch_to_light': 'हल्का मोड',
        'tagline': 'सुनाई देने वाली ऑडियो ध्वनि-तीव्रता को समान करता है',
        'target': 'ध्वनि-तीव्रता लक्ष्य',
        'target_tooltip': 'ध्वनि-तीव्रता लक्ष्य पूरे ट्रैक की अपेक्षित समेकित ध्वनि-तीव्रता है, '
                          'जिसे LUFS में व्यक्त किया जाता है। कम ऋणात्मक मान अधिक तेज़ फ़ाइल बनाता '
                          'है: -14 LUFS, -16 LUFS से तेज़ है। 2 LU का अंतर पीक सीमितकरण से पहले '
                          'लगभग 2 dB के स्तर-अंतर के बराबर है।\n'
                          '\n'
                          'मार्गदर्शन: अधिक शांत और डायनेमिक परिणाम के लिए -18 LUFS; सामान्य '
                          'संतुलन के लिए -16 LUFS; अधिक तेज़ स्ट्रीमिंग-जैसे परिणाम के लिए -14 '
                          'LUFS।\n'
                          '\n'
                          'यह लक्ष्य ट्रैक की आंतरिक डायनेमिक्स को स्वयं सपाट नहीं करता। अधिकतम '
                          'ट्रू पीक लक्ष्य तक बिना क्लिपिंग पहुँचना रोक सकता है।',
        'theme_accessible': 'ऐप का रूप बदलें। यह चुनाव याद रखा जाएगा।',
        'total_time': 'कुल समय: {duration}',
        'track_mode_log': 'ट्रैक मोड — हर ऑडियो फ़ाइल अलग संसाधित होती है।',
        'track_two_pass': 'दो-पास ट्रैक सामान्यीकरण।',
        'true_peak_meter_exceeded': 'अधिक {margin} dB',
        'true_peak_meter_margin': 'हेडरूम {margin} dB',
        'true_peak_meter_title': 'पीक हेडरूम',
        'true_peak_meter_tooltip': 'अंतिम आउटपुट के true peak की चुनी सीमा से तुलना करता है। चिह्न '
                                   'अंतिम मान और त्रिकोण बैच का सबसे ऊँचा पीक रखता है। हरा: सीमा '
                                   'पूरी; नारंगी: 0.25 dB तक अधिक; लाल: इससे अधिक। नारंगी सहनशीलता '
                                   'LUFScale गुणवत्ता जाँच की है, वितरण मानक नहीं। हर बैच पर रीसेट '
                                   'होता है।',
        'true_peak_meter_waiting': 'dBTP माप की प्रतीक्षा',
        'version_changes': '• स्रोत जोड़ने या हटाने पर ऑडियो फ़ाइलों की कुल संख्या अपडेट होती है।\n'
                           '• मीटर का आकार और अंतर 1.21.25 जैसा है और गुणवत्ता जाँच बंद होने पर '
                           'निष्क्रिय रहता है।\n'
                           '• अनुमान अब समाप्ति का लगभग समय भी दिखाता है।\n'
                           '• पुराने आंतरिक परीक्षण उपकरण हटा दिए गए हैं।',
        'version_changes_title': 'संस्करण {version} में नया',
        'version_label': 'संस्करण {version}',
        'volume': 'वॉल्यूम',
        'volume_loud': 'तेज़: -14 LUFS',
        'volume_normal': 'सामान्य: -16 LUFS',
        'volume_soft': 'हल्का: -18 LUFS',
        'volume_tooltip': 'यह ध्वनि-तीव्रता लक्ष्य का शॉर्टकट है; यह Mac का प्लेबैक वॉल्यूम नहीं '
                          'बदलता।\n'
                          '\n'
                          '• हल्का: -18 LUFS — शांत स्तर, अधिक डायनेमिक हेडरूम और लिमिटर सक्रिय '
                          'होने की कम संभावना।\n'
                          '• सामान्य: -16 LUFS — निजी लाइब्रेरी के लिए संतुलित शुरुआती विकल्प।\n'
                          '• तेज़: -14 LUFS — अधिक प्रमुख ध्वनि, लेकिन सीमितकरण की अधिक संभावना।\n'
                          '• कस्टम — कोई दूसरा LUFS लक्ष्य सीधे दर्ज करें।\n'
                          '\n'
                          'ये व्यावहारिक विकल्प हैं, सार्वभौमिक मानक नहीं।',
        'zero_album_gain': 'एल्बम गेन शून्य; ऑडियो कॉपी हुआ।'},
 'it': {'activity_cancelled': 'Attività: elaborazione annullata',
        'activity_cancelling': 'Attività: annullamento in corso…',
        'activity_completed': 'Attività: elaborazione completata',
        'activity_compliant': 'Conformi: {count}',
        'activity_detected': 'Attività: {total} file rilevato/i',
        'activity_errors': 'Errori: {count}',
        'activity_files': 'File: {count}',
        'activity_idle': 'Attività: in attesa',
        'activity_preparing': 'Attività: preparazione dei file…',
        'activity_progress': '{total} file • riusciti {success} • avvisi {warnings} • errori '
                             '{failed} • ripresi/ignorati {skipped} • conformi {compliant}',
        'activity_skipped': 'Ripresi/ignorati: {count}',
        'activity_successes': 'Riusciti: {count}',
        'activity_warnings': 'Avvisi: {count}',
        'adaptive_disabled_log': 'Analisi adattiva — sonde rapide arrestate dopo {sample} '
                                 'misurazioni ({successes} successi, risparmio stimato '
                                 '{percent:+.1f}%).',
        'add_folders': 'Aggiungi cartelle…',
        'add_mp3': 'Aggiungi file audio…',
        'add_replaygain': 'Aggiungi ReplayGain',
        'add_source_files': 'Aggiungi file audio',
        'add_source_folder': 'Aggiungi una cartella sorgente',
        'album_gain_detail': 'Guadagno comune dell’album {gain:+.2f} dB.',
        'album_gain_log': 'Album «{album}» — guadagno comune {gain:+.2f} dB.',
        'album_measurement_error': 'Misurazione dell’album non riuscita: {error}',
        'album_mode_log': 'Modalità Album — ogni cartella con file audio forma un album.',
        'albums_measurement': 'Misurazione di {count} album…',
        'already_completed': 'Già completato durante un’esecuzione precedente.',
        'already_compliant_badge': 'CONFORME',
        'already_compliant_copy': 'Già conforme: copia identica senza ricodifica audio.',
        'already_compliant_log': 'già conforme, senza ricodifica',
        'analysis_cache_summary': 'Cache di analisi — {hits} misurazione/i riutilizzata/i.',
        'analysis_impossible': 'Analisi non riuscita: {error}',
        'analysis_method': 'Metodo di analisi',
        'analysis_method_adaptive': 'Adattivo — si arresta se non conviene',
        'analysis_method_fast': 'Rapido — sperimentale',
        'analysis_method_historical': 'Storico — riferimento',
        'analysis_method_log': 'Metodo di analisi — {method}.',
        'analysis_method_tooltip': 'Storico usa soltanto la misurazione completa di riferimento '
                                   'convalidata nella 1.22.13. Rapido prova la sonda lineare su '
                                   'ogni file e torna alla misurazione storica quando necessario. '
                                   'Adattivo inizia come Rapido; dopo almeno 12 misurazioni e 3 '
                                   'ripieghi confronta i tempi osservati e disattiva le sonde se '
                                   'il risparmio stimato resta inferiore al 5%. La qualità finale '
                                   'e il controllo qualità non vengono ridotti.',
        'analysis_progress': 'Analisi {current}/{total}: {file}',
        'analyze': 'Analizza',
        'analyze_operation': 'analisi/simulazione',
        'analyzed_progress': 'Analizzato: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Flusso audio copiato senza ricodifica; tag ReplayGain aggiunti.',
        'audio_tab': 'Audio',
        'auto_start': 'Avvia automaticamente dopo il trascinamento o l’incolla',
        'auto_start_tooltip': 'Avvia automaticamente l’elaborazione dopo l’aggiunta di sorgenti '
                              'tramite trascinamento o incolla, se è già stata scelta una '
                              'destinazione.',
        'cancel': 'Annulla',
        'cancelled_summary': 'Annullato — {success} riuscito/i, {failed} errore/i, {skipped} '
                             'ripreso/i/ignorato/i, {warnings} avviso/i, {compliant} conforme/i — '
                             '{duration}.',
        'cancelling': 'Annullamento in corso…',
        'choose': 'Scegli…',
        'choose_output': 'Scegli la cartella di destinazione',
        'clipboard': 'Appunti',
        'clipboard_empty': 'Gli appunti non contengono un percorso valido di cartella o file audio '
                           'supportato.',
        'close_question': 'Annullare l’elaborazione e chiudere l’applicazione?',
        'completed_dialog_summary': 'Stato: completato\n'
                                    'File: {files}\n'
                                    'Riusciti: {success}\n'
                                    'Errori: {failed}\n'
                                    'Ripresi o ignorati: {skipped}\n'
                                    'Avvisi: {warnings}\n'
                                    'Conformi: {compliant}\n'
                                    'Tempo totale: {duration}',
        'completed_summary': 'Completato — {success} riuscito/i, {failed} errore/i, {skipped} '
                             'ripreso/i/ignorato/i, {warnings} avviso/i, {compliant} conforme/i — '
                             '{duration}.',
        'completed_with_errors': 'Elaborazione completata con avvisi',
        'convert': 'Normalizza',
        'convert_operation': 'uniformazione audio',
        'cpu_tooltip': 'Utilizzo totale della CPU del Mac, aggiornato ogni secondo durante '
                       'l’elaborazione.',
        'cpu_unavailable': 'N/D',
        'cpu_usage': 'CPU',
        'create_report': 'Crea un rapporto CSV',
        'custom': 'Personalizzato',
        'decrease_value': 'Diminuire il valore',
        'description': 'Uniforma il volume percepito in modalità Traccia o Album senza modificare '
                       'gli originali.',
        'destination': 'Destinazione',
        'destination_error': 'ERRORE — destinazione non disponibile: {error}',
        'destination_path_tooltip': 'Fai clic sul percorso, quindi usa le frecce, Inizio/Fine o la '
                                    'rotellina. Il percorso può essere selezionato e copiato, ma '
                                    'non modificato.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — sottocartelle incluse',
        'drop_title': 'Trascina qui cartelle o file audio',
        'elapsed_time': 'Tempo trascorso: {duration}',
        'error_progress': 'Errore: {file}',
        'estimated_result': 'Risultato stimato; nessun file creato.',
        'estimated_total_calculating': 'Tempo totale stimato: calcolo in corso…',
        'estimated_total_time': 'Tempo totale stimato: {duration}',
        'estimated_total_time_with_finish': 'Tempo totale stimato: {duration} — fine verso le '
                                            '{time}',
        'estimated_total_unavailable': 'Tempo totale stimato: non disponibile',
        'ffmpeg_download_button': 'Apri il sito ufficiale di FFmpeg',
        'ffmpeg_error_no_detail': 'Errore FFmpeg senza dettagli.',
        'ffmpeg_execution_error': 'Impossibile eseguire FFmpeg: {error}',
        'ffmpeg_incompatible': 'FFmpeg incompatibile',
        'ffmpeg_missing': 'FFmpeg non trovato',
        'ffmpeg_missing_encoders': 'Questa versione di FFmpeg non include tutti gli encoder audio '
                                   'richiesti: {encoders}.',
        'ffmpeg_missing_message': 'FFmpeg deve essere installato e disponibile nel PATH, oppure '
                                  'collocato accanto al programma.',
        'ffmpeg_no_lame': 'Questa versione di FFmpeg non include il codificatore MP3 libmp3lame.',
        'ffmpeg_no_loudnorm': 'Questa versione di FFmpeg non include il filtro loudnorm.',
        'ffmpeg_not_responding': 'FFmpeg non risponde correttamente.',
        'file_exists': 'Il file esiste già.',
        'files_found': 'Trovati {total} file audio — {operation} — {parallel} processi paralleli.',
        'folder': 'Cartella',
        'folder_unavailable': 'Cartella non disponibile',
        'guide_help_tooltip': 'Apre la guida PDF completa nella lingua selezionata.',
        'guide_missing_message': 'La guida PDF non è stata trovata: {path}',
        'guide_missing_title': 'Guida non disponibile',
        'guide_open_error': 'macOS non ha potuto aprire la guida PDF: {path}',
        'help_button': 'Aiuto',
        'help_overview': '• Normalizzazione reale, ReplayGain o analisi senza creare MP3.\n'
                         '• Modalità Traccia e Album con conservazione delle differenze tra le '
                         'tracce.\n'
                         '• Struttura delle cartelle, metadati e copertine conservati quando '
                         'FFmpeg può copiarli.\n'
                         '• Gli originali non vengono mai spostati o modificati.\n'
                         '• Parallelismo Auto, cache di analisi e ripresa dopo un’interruzione.\n'
                         '• Controllo qualità, rapporto CSV, avanzamento, CPU, misuratore di '
                         'sonorità e durata totale stimata.\n'
                         '• Interfaccia disponibile in dodici lingue e guide PDF in dodici lingue.',
        'help_title': 'Caratteristiche principali',
        'increase_value': 'Aumentare il valore',
        'interface_ffmpeg_message': 'L’interfaccia è disponibile, ma la conversione richiede '
                                    'FFmpeg. Installa FFmpeg e riavvia l’applicazione.',
        'internal_error': 'Errore interno: {error}',
        'interrupted': 'Elaborazione interrotta.',
        'invalid_location': 'Posizione non valida',
        'language': 'Lingua',
        'language_tooltip': 'Cambia immediatamente la lingua dell’interfaccia, dei messaggi e dei '
                            'futuri rapporti CSV. La scelta viene memorizzata.',
        'level_mode': 'Modalità volume',
        'log_help_text': 'Ogni riga riguarda un file o una fase generale.\n'
                         '\n'
                         '• Inizio: stato dell’elaborazione (OK, AVVISO, ERRORE, ripreso o '
                         'ignorato).\n'
                         '• Poi: nome dell’MP3 e tempo dedicato al file.\n'
                         '• Riquadro LUFS: livello misurato prima → livello ottenuto dopo '
                         'l’elaborazione.\n'
                         '• Fine: risultato del controllo qualità ed eventuali dettagli.\n'
                         '\n'
                         'Colori: verde = riuscito; arancione = avviso; rosso = file non '
                         'completato; viola bluastro = ripresa; grigio = informazione, elemento '
                         'ignorato o annullamento.\n'
                         '\n'
                         'I tempi cumulativi sommano il lavoro di tutte le attività parallele. Il '
                         'tempo totale è la durata effettivamente trascorsa.\n'
                         '\n'
                         'QC AVVISO — picco significa che il true peak rimisurato in uscita supera '
                         'di oltre 0,25 dB il limite scelto. Il file viene comunque creato: non è '
                         'un errore di conversione. Tuttavia non rispetta rigorosamente il limite '
                         'richiesto e lascia meno margine per una nuova codifica o per alcuni '
                         'convertitori. Più il valore dBTP si avvicina a 0, maggiore è il rischio '
                         'di picchi inter-campione. Per correggere un avviso persistente, '
                         'scegliere un obiettivo LUFS più basso o un picco massimo più prudente, '
                         'per esempio −2,0 dBTP, quindi elaborare nuovamente il file.',
        'log_placeholder': 'Il resoconto dell’elaborazione verrà visualizzato qui.',
        'log_title': 'Registro di elaborazione',
        'loudness_meter_estimated': 'Stimato',
        'loudness_meter_help_text': 'Questo misuratore controlla visivamente la regolarità della '
                                    'normalizzazione. Confronta l’ultimo file audio con '
                                    'l’obiettivo e calcola continuamente il minimo e il massimo '
                                    'degli ultimi 100 file. I valori più vecchi escono '
                                    'progressivamente da questa finestra, mantenendo dinamici i '
                                    'lotti grandi. Il punteggio dell’obiettivo resta calcolato '
                                    'sull’intero lotto e l’indicatore non modifica le '
                                    'impostazioni.',
        'loudness_meter_maximum': 'Max {value}',
        'loudness_meter_measured': 'Misurato',
        'loudness_meter_minimum': 'Min {value}',
        'loudness_meter_target': 'Obiettivo {value} LUFS',
        'loudness_meter_title': 'Misuratore di sonorità',
        'loudness_meter_tooltip': 'La linea rossa rappresenta l’obiettivo. Il valore blu a '
                                  'sinistra segue l’ultimo file audio. Le linee e i valori grigio '
                                  'e viola scuro mostrano a destra il minimo e il massimo degli '
                                  'ultimi 100 file. La scala amplifica le piccole differenze e il '
                                  'misuratore si azzera a ogni nuovo lotto.',
        'loudness_meter_waiting': 'In attesa di un file audio',
        'loudness_score_acceptable': 'Accettabile',
        'loudness_score_check': 'Da verificare',
        'loudness_score_excellent': 'Eccellente',
        'loudness_score_good': 'Buono',
        'loudness_score_needs_qc': 'Punteggio obiettivo: attivare il controllo qualità',
        'loudness_score_not_applicable': 'Punteggio obiettivo: non applicabile',
        'loudness_score_tooltip': 'Il punteggio usa soltanto le uscite effettivamente misurate di '
                                  'nuovo. Si basa sull’errore quadratico medio tra la sonorità '
                                  'ottenuta e quella prevista: 100 = risultato esatto, 50 = errore '
                                  'complessivo di 0,5 LU, cioè la tolleranza del controllo '
                                  'qualità, e 0 = errore di 1 LU o più. In modalità Album, il '
                                  'valore previsto di ogni traccia include il guadagno comune per '
                                  'conservare le differenze desiderate. L’errore RMS (radice '
                                  'quadrata della media degli scarti al quadrato) riassume la '
                                  'distanza complessiva tra le sonorità ottenute e i rispettivi '
                                  'obiettivi. Più è vicino a 0 LU, più precisa è la serie.',
        'loudness_score_value': 'Punteggio obiettivo: {score}/100\n'
                                '{rating}\n'
                                'Errore RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Punteggio obiettivo: in attesa',
        'measurement_unavailable': 'Misurazione non disponibile.',
        'mode_album': 'Album — conserva le differenze tra le tracce',
        'mode_album_label': 'Album',
        'mode_tooltip': 'Traccia regola ogni MP3 separatamente. Album calcola un guadagno comune '
                        'per cartella per conservare le differenze di volume tra le tracce.',
        'mode_track': 'Traccia — stesso livello per ogni file',
        'mode_track_label': 'Traccia',
        'mp3': 'MP3',
        'mp3_filter': 'Audio supportato (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Nessuna cartella selezionata',
        'no_mp3': 'Nessun file audio supportato trovato.',
        'no_new_source': 'Non è stata aggiunta alcuna cartella o file audio supportato.',
        'not_performed': 'Non eseguito',
        'open_output_error': 'Impossibile aprire la cartella di destinazione: {error}',
        'operation': 'Operazione',
        'operation_analyze': 'Solo analisi — simulazione senza creare file',
        'operation_analyze_label': 'Solo analisi',
        'operation_convert': 'Uniforma — normalizza realmente l’audio',
        'operation_convert_label': 'Uniformazione audio',
        'operation_replaygain': 'ReplayGain — senza ricodifica audio',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Uniforma elabora realmente l’audio. MP3, M4A/AAC, OGG e Opus devono '
                             'essere ricodificati: la dimensione dipende dalla qualità e può '
                             'aumentare. FLAC viene ricodificato senza perdita, ma la compressione '
                             'può variare con i campioni. WAV e AIFF conservano frequenza, canali '
                             'e profondità compatibili con la sorgente. ReplayGain non ricodifica; '
                             'Analizza non crea file.',
        'options_tab': 'Opzioni',
        'overwrite': 'Sovrascrivi i file esistenti',
        'overwrite_tooltip': 'Consente di sostituire un MP3 già presente nella destinazione. I '
                             'file sorgente non vengono mai sovrascritti.',
        'parallel': 'Processi paralleli',
        'parallel_adjusted': 'Parallelismo automatico — {active} processo/i, CPU {cpu:.0f} %.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automatico, massimo {maximum}',
        'parallel_tooltip': 'Determina quanti file possono essere elaborati contemporaneamente.\n'
                            '\n'
                            '• Auto parte con al massimo 4 attività. Quando la misurazione CPU è '
                            'disponibile, la controlla ogni secondo: aggiunge un’attività sotto il '
                            '70% di utilizzo e ne rimuove una sopra il 92%.\n'
                            '• Auto non supera mai il numero di processori logici rilevati, con un '
                            'limite assoluto di 16 attività.\n'
                            '• Se la misurazione CPU non è disponibile, Auto usa direttamente quel '
                            'limite rilevato senza adattamento dinamico.\n'
                            '• Un valore numerico fissa il numero massimo di attività simultanee; '
                            'non è un obiettivo di utilizzo CPU.\n'
                            '\n'
                            'Più attività possono accelerare un lotto grande, ma aumentano carico, '
                            'temperatura e attività del disco. Premi − finché non compare Auto.',
        'paste': 'Incolla',
        'path_left': 'Mostra la parte sinistra del percorso',
        'path_right': 'Mostra la parte destra del percorso',
        'pause': 'Pausa',
        'peak': 'Picco reale massimo',
        'peak_tooltip': 'Il picco reale massimo è un limite, non un livello da raggiungere. Limita '
                        'in dBTP i picchi più alti della forma d’onda ricostruita, compresi quelli '
                        'tra i campioni, per ridurre il clipping dopo la codifica o la '
                        'transcodifica.\n'
                        '\n'
                        '• -1,0 dBTP — limite di consegna comune, con il picco di uscita più '
                        'alto.\n'
                        '• -1,5 dBTP — valore predefinito e compromesso prudente per gli MP3.\n'
                        '• -2,0 dBTP — margine aggiuntivo, utile se il file verrà ricodificato o '
                        'con un obiettivo di sonorità elevato.\n'
                        '• 0 dBTP — nessun margine; sconsigliato per MP3.\n'
                        '\n'
                        'Un valore più negativo è più sicuro, ma può impedire alle tracce molto '
                        'dinamiche di raggiungere esattamente l’obiettivo LUFS.',
        'phase_summary': 'Ripartizione stimata del tempo totale — analisi {analysis}, conversione '
                         '{conversion}, controllo qualità {quality}.',
        'pipeline_enabled': 'Pipeline Traccia — ogni conversione inizia appena termina la sua '
                            'analisi.',
        'pre_measurement': 'Misurazione dei file di ingresso…',
        'preset': 'Preimpostazione',
        'preset_dynamic': 'Musica dinamica',
        'preset_library': 'Libreria musicale — consigliata',
        'preset_streaming': 'Streaming più presente',
        'preset_tooltip': 'Applica insieme un obiettivo di sonorità, un picco reale massimo e una '
                          'qualità MP3 coerenti. Ogni modifica manuale seleziona Personalizzato.',
        'processing_cancelled': 'Elaborazione annullata.',
        'processing_completed': 'Elaborazione completata',
        'processing_in_progress': 'Elaborazione in corso',
        'processing_paused': 'Elaborazione in pausa.',
        'processing_resumed': 'Elaborazione ripresa.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'AVVISO — controllo qualità impossibile: {error}',
        'qc_log': ' — CQ {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'AVVISO — {detail}',
        'quality': 'Qualità audio',
        'quality_control': 'Controllo qualità automatico',
        'quality_control_tooltip': 'Rimisura ogni uscita. Per gli MP3 del percorso dinamico, la '
                                   'misura può avviare fino a tre ricodifiche correttive. '
                                   'Disattivarlo non cambia la qualità dell’encoder, ma elimina '
                                   'verifica finale, correzioni e attività del misuratore.',
        'quality_tooltip': 'Controlla qualità e dimensione dei formati compressi: un numero basso '
                           'usa qualità e bitrate maggiori. Se il bitrate scelto supera quello '
                           'originale, il file cresce. Un numero alto di solito lo riduce, ma il '
                           'VBR non garantisce gli stessi byte. FLAC resta senza perdita; WAV e '
                           'AIFF ignorano l’impostazione e conservano le proprietà PCM. '
                           'Intervalli: 0 = qualità massima; 1-2 = molto alta; 3-4 = equilibrio; '
                           '5-9 = dimensione minore.',
        'ready': 'Pronto',
        'recursive_scan': 'Analisi ricorsiva delle cartelle…',
        'remove_all': 'Rimuovi tutto',
        'remove_selection': 'Rimuovi selezione',
        'replaygain_operation': 'ReplayGain senza ricodifica',
        'replaygain_tags_missing': 'Tag ReplayGain non trovati.',
        'report_album_dbtp': 'dbtp_ingresso_album',
        'report_album_lufs': 'lufs_ingresso_album',
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
        'report_seconds': 'tempo_secondi',
        'report_source': 'sorgente',
        'report_status': 'stato',
        'report_tooltip': 'Crea nella destinazione un rapporto dettagliato con misure, durate e '
                          'avvisi.',
        'resume': 'Riprendi dopo un’interruzione',
        'resume_not_saved': ' Punto di ripresa non salvato: {error}',
        'resume_processing': 'Riprendi',
        'resume_tooltip': 'I file già completati con le stesse impostazioni vengono riconosciuti e '
                          'non vengono elaborati di nuovo.',
        'resumed_progress': 'Ripreso: {file}',
        'scan_error': 'ERRORE — {error}',
        'scanning_folders': 'Analisi delle cartelle…',
        'settings': 'Impostazioni',
        'show_finder': 'Mostra nel Finder',
        'show_option_help': 'Mostra aiuto: {option}',
        'silent_album_copy': 'Album silenzioso o non misurabile copiato.',
        'silent_copy': 'Audio silenzioso o non misurabile copiato.',
        'silent_copy_no_replaygain': 'Audio silenzioso copiato senza tag ReplayGain.',
        'silent_unmeasurable': 'Audio silenzioso o non misurabile.',
        'simulation': 'Simulazione',
        'skip_compliant': 'Non ricodificare i file già conformi',
        'skip_compliant_tooltip': 'Attiva per impostazione predefinita. Dopo l’analisi, un file '
                                  'entro ±0,5 LU dall’obiettivo e con true peak non superiore al '
                                  'limite viene copiato identico, senza ricodifica. In modalità '
                                  'Album la conformità della sonorità è valutata sull’intero '
                                  'album. Qualità e dimensione restano identiche; il registro lo '
                                  'segnala.',
        'skipped_progress': 'Ignorato: {file}',
        'source_audio_count': 'File audio da elaborare: {count}',
        'source_list_more': '… altre {count} sorgenti conservate',
        'source_safety': 'I file sorgente non vengono mai spostati né modificati.',
        'source_selection_tooltip': 'Selezione multipla: ⌘ clic per elementi separati e Maiusc '
                                    'clic per un intervallo.',
        'sources_added': '{count} sorgente/i aggiunta/e.',
        'start': 'Avvia',
        'status_analyzed': 'ANALIZZATO',
        'status_cancelled': 'ANNULLATO',
        'status_error': 'ERRORE',
        'status_ok': 'OK',
        'status_resumed': 'RIPRESO',
        'status_skipped': 'IGNORATO',
        'switch_to_dark': 'Modalità scura',
        'switch_to_light': 'Modalità chiara',
        'tagline': 'Uniforma il volume audio percepito',
        'target': 'Obiettivo di sonorità',
        'target_tooltip': 'L’obiettivo di sonorità è la sonorità integrata desiderata sull’intera '
                          'traccia, espressa in LUFS. Un valore meno negativo produce un file più '
                          'forte: -14 LUFS è più forte di -16 LUFS. Una differenza di 2 LU '
                          'corrisponde approssimativamente a 2 dB di livello prima di un’eventuale '
                          'limitazione dei picchi.\n'
                          '\n'
                          'Riferimenti: -18 LUFS per un risultato più tranquillo e dinamico; -16 '
                          'LUFS per un equilibrio generale; -14 LUFS per un risultato più forte in '
                          'stile streaming. Le piattaforme possono poi applicare la propria '
                          'normalizzazione in riproduzione.\n'
                          '\n'
                          'Questo obiettivo non appiattisce da solo la dinamica interna della '
                          'traccia. Se il picco reale massimo impedisce di raggiungerlo senza '
                          'clipping, il risultato può rimanere leggermente più basso.',
        'theme_accessible': 'Cambia l’aspetto dell’applicazione. La scelta viene memorizzata.',
        'total_time': 'Tempo totale: {duration}',
        'track_mode_log': 'Modalità Traccia — ogni file audio viene elaborato separatamente.',
        'track_two_pass': 'Normalizzazione della traccia in due passaggi.',
        'true_peak_meter_exceeded': 'Superamento {margin} dB',
        'true_peak_meter_margin': 'Margine {margin} dB',
        'true_peak_meter_title': 'Margine di picco',
        'true_peak_meter_tooltip': 'Confronta il true peak dell’ultima uscita con il limite '
                                   'scelto. Il marcatore mostra l’ultimo valore e il triangolo '
                                   'conserva il picco più alto del lotto. Verde: limite '
                                   'rispettato; arancione: superamento fino a 0,25 dB; rosso: '
                                   'superiore. La tolleranza arancione è del controllo qualità '
                                   'LUFScale, non una norma di consegna. Si azzera a ogni lotto.',
        'true_peak_meter_waiting': 'In attesa di una misura dBTP',
        'version_changes': '• Il totale dei file audio si aggiorna quando si aggiungono o '
                           'rimuovono sorgenti.\n'
                           '• Il misuratore riprende dimensioni e separazione della versione '
                           '1.21.25 e resta inattivo senza controllo qualità.\n'
                           '• La stima indica anche l’ora approssimativa di fine.\n'
                           '• I precedenti strumenti interni di prova sono stati rimossi.',
        'version_changes_title': 'Novità della versione {version}',
        'version_label': 'Versione {version}',
        'volume': 'Volume',
        'volume_loud': 'Forte: -14 LUFS',
        'volume_normal': 'Normale: -16 LUFS',
        'volume_soft': 'Basso: -18 LUFS',
        'volume_tooltip': 'Questa impostazione è una scorciatoia per l’obiettivo di sonorità; non '
                          'modifica il volume di ascolto del Mac.\n'
                          '\n'
                          '• Basso: -18 LUFS — livello più tranquillo, maggiore margine dinamico e '
                          'minore probabilità di attivare il limiter.\n'
                          '• Normale: -16 LUFS — compromesso equilibrato e buon punto di partenza '
                          'per una raccolta personale.\n'
                          '• Alto: -14 LUFS — riproduzione più presente, vicina all’obiettivo '
                          'Normale di Spotify, ma con maggiore probabilità di richiedere '
                          'limitazione.\n'
                          '• Personalizzato — consente di inserire direttamente un altro obiettivo '
                          'LUFS.\n'
                          '\n'
                          'Sono scelte pratiche, non uno standard universale.',
        'zero_album_gain': 'Guadagno album nullo; audio copiato.'},
 'ja': {'activity_cancelled': '動作状況：処理をキャンセル',
        'activity_cancelling': '動作状況：キャンセル中…',
        'activity_completed': '動作状況：処理完了',
        'activity_compliant': '適合：{count}',
        'activity_detected': '動作状況：{total}件のファイルを検出',
        'activity_errors': 'エラー：{count}',
        'activity_files': 'ファイル：{count}',
        'activity_idle': '動作状況：待機中',
        'activity_preparing': '動作状況：ファイルを準備中…',
        'activity_progress': '{total} ファイル • 成功 {success} • 警告 {warnings} • エラー {failed} • 再開/スキップ '
                             '{skipped} • 適合 {compliant}',
        'activity_skipped': '再開/スキップ：{count}',
        'activity_successes': '成功：{count}',
        'activity_warnings': '警告：{count}',
        'adaptive_disabled_log': '適応解析 — '
                                 '{sample}回の測定後に高速プローブを停止しました（成功{successes}回、推定短縮率{percent:+.1f}%）。',
        'add_folders': 'フォルダを追加…',
        'add_mp3': '音声ファイルを追加…',
        'add_replaygain': 'ReplayGainを追加',
        'add_source_files': '音声ファイルを追加',
        'album_gain_detail': 'アルバム共通ゲイン {gain:+.2f} dB。',
        'album_gain_log': 'アルバム「{album}」— 共通ゲイン {gain:+.2f} dB。',
        'album_measurement_error': 'アルバムを測定できませんでした：{error}',
        'album_mode_log': 'アルバムモード — 音声ファイルを含む各フォルダーをアルバムとして扱います。',
        'albums_measurement': '{count}件のアルバムを測定中…',
        'already_completed': '前回の実行ですでに完了しています。',
        'already_compliant_badge': '適合済み',
        'already_compliant_copy': '適合済み：音声を再エンコードせず同一コピー。',
        'already_compliant_log': '適合済み、再エンコードなし',
        'analysis_cache_summary': '解析キャッシュ — {hits}件の測定値を再利用しました。',
        'analysis_impossible': '解析に失敗しました：{error}',
        'analysis_method': '解析方法',
        'analysis_method_adaptive': '適応方式 — 効果がなければ停止',
        'analysis_method_fast': '高速方式 — 実験用',
        'analysis_method_historical': '従来方式 — 基準',
        'analysis_method_log': '解析方法 — {method}。',
        'analysis_method_tooltip': '従来方式は1.22.13で検証された完全な基準測定のみを使用します。高速方式は各ファイルで線形プローブを試し、必要なら従来の測定に戻ります。適応方式は高速方式として開始し、12回以上の測定と3回以上のフォールバック後に実測時間を比較し、推定短縮率が5%未満ならプローブを停止します。最終品質と品質管理は簡略化しません。',
        'analysis_progress': '解析 {current}/{total}：{file}',
        'analyze': '解析',
        'analyzed_progress': '解析済み：{file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': '再エンコードせず音声をコピーし、ReplayGainタグを追加しました。',
        'audio_tab': 'オーディオ',
        'auto_start': 'ドロップまたは貼り付け後に自動開始',
        'auto_start_tooltip': '保存先が選択済みの場合、ドラッグ＆ドロップまたは貼り付け後に自動で処理を開始します。',
        'cancel': 'キャンセル',
        'cancelled_summary': 'キャンセル — 成功 {success}、エラー {failed}、再開/スキップ {skipped}、警告 {warnings}、適合 '
                             '{compliant} — {duration}。',
        'choose': '選択…',
        'clipboard_empty': 'クリップボードに有効なフォルダーまたは対応音声ファイルのパスがありません。',
        'completed_dialog_summary': '状態：完了\n'
                                    'ファイル数：{files}\n'
                                    '成功：{success}\n'
                                    'エラー：{failed}\n'
                                    '再開またはスキップ：{skipped}\n'
                                    '警告：{warnings}\n'
                                    '適合：{compliant}\n'
                                    '合計時間：{duration}',
        'completed_summary': '完了 — 成功 {success}、エラー {failed}、再開/スキップ {skipped}、警告 {warnings}、適合 '
                             '{compliant} — {duration}。',
        'convert': 'ノーマライズ',
        'convert_operation': '音声ノーマライズ',
        'cpu_tooltip': '処理中のMac全体のCPU使用率を1秒ごとに更新します。',
        'cpu_usage': 'CPU',
        'create_report': 'CSVレポートを作成',
        'custom': 'カスタム',
        'description': '元のファイルを変更せず、トラックまたはアルバム単位で聴感上の音量をそろえます。',
        'destination': '保存先',
        'destination_error': 'エラー — 保存先を使用できません：{error}',
        'destination_path_tooltip': 'パスをクリックし、矢印キー、Home/End、またはマウスホイールで移動します。選択とコピーはできますが、変更はできません。',
        'drop_subtitle': 'MP3、FLAC、WAV、AIFF、M4A、OGG、Opus — サブフォルダー対応',
        'drop_title': 'フォルダーまたは音声ファイルをここにドロップ',
        'elapsed_time': '経過時間：{duration}',
        'error_progress': 'エラー：{file}',
        'estimated_result': '推定結果です。ファイルは作成されません。',
        'estimated_total_calculating': '推定合計時間：計算中…',
        'estimated_total_time': '推定合計時間：{duration}',
        'estimated_total_time_with_finish': '推定合計時間：{duration} — {time}頃に完了',
        'estimated_total_unavailable': '推定合計時間：利用不可',
        'ffmpeg_download_button': 'FFmpeg公式サイトを開く',
        'ffmpeg_missing_encoders': 'この FFmpeg には必要な音声エンコーダーがすべて含まれていません: {encoders}。',
        'file_exists': 'ファイルはすでに存在します。',
        'files_found': '{total} 個の音声ファイル — {operation} — {parallel} 並列処理。',
        'guide_help_tooltip': '選択した言語の完全なPDFガイドを開きます。',
        'guide_missing_message': 'PDFガイドが見つかりません：{path}',
        'guide_missing_title': 'ガイドを利用できません',
        'guide_open_error': 'macOSでPDFガイドを開けませんでした：{path}',
        'help_button': 'ヘルプ',
        'help_overview': '• ノーマライズ、ReplayGain、または解析のみ。\n'
                         '• トラックモードとアルバムモード。\n'
                         '• FFmpegでコピー可能なフォルダ構成、メタデータ、アートワークを保持。\n'
                         '• 元のファイルは移動も変更もしません。\n'
                         '• 自動並列処理、解析キャッシュ、再開機能。\n'
                         '• インターフェースは12言語、PDFガイドは12言語に対応。',
        'help_title': '主な機能',
        'internal_error': '内部エラー：{error}',
        'interrupted': '処理が中断されました。',
        'language_tooltip': 'インターフェースの言語をすぐに変更して保存します。未翻訳の技術メッセージは英語で表示されます。',
        'level_mode': '音量モード',
        'log_help_text': '各行は、ファイルまたは処理全体の段階を示します。\n'
                         '\n'
                         '• 先頭：処理状態（OK、警告、エラー、再開、スキップ）。\n'
                         '• 続き：MP3名とそのファイルに要した時間。\n'
                         '• LUFS表示：処理前の測定レベル → 処理後に得られたレベル。\n'
                         '• 末尾：品質チェックの結果と追加情報。\n'
                         '\n'
                         '色：緑 = 成功、オレンジ = 警告、赤 = 未完了、青紫 = 再開、灰色 = 情報、スキップ、キャンセル。\n'
                         '\n'
                         '累積時間は、並列タスクすべての作業時間を合計したものです。合計時間は実際に経過した時間です。\n'
                         '\n'
                         'QC警告 — ピークは、出力を再測定したトゥルーピークが選択した上限を0.25 '
                         'dB以上超えたことを示します。ファイルは作成されるため、変換エラーではありません。ただし指定した上限を厳密には満たさず、再エンコードや一部のコンバーターに対する余裕が少なくなります。dBTP値が0に近いほど、インターサンプルピークの危険が高まります。警告が続く場合は、より低いLUFS目標または−2.0 '
                         'dBTPなどの安全な最大ピークを選び、再処理してください。',
        'log_placeholder': '処理結果がここに表示されます。',
        'log_title': '処理ログ',
        'loudness_meter_help_text': 'このメーターはノーマライズの均一性を目で確認するためのものです。直前の音声ファイルを目標値と比較し、直近100ファイルの最小値と最大値を継続して計算します。古い値はこの範囲から順次外れるため、大規模な処理でも表示が動き続けます。目標スコアは処理全体を対象とし、この表示は設定を変更しません。',
        'loudness_meter_maximum': '最大 {value}',
        'loudness_meter_minimum': '最小 {value}',
        'loudness_meter_target': '目標 {value} LUFS',
        'loudness_meter_title': 'ラウドネスメーター',
        'loudness_meter_tooltip': '赤線は目標値です。左の青い値は直前の音声ファイルを示します。右の灰色と濃紫色の線と値は、直近100ファイルの最小値と最大値を示します。小さな差が見やすい尺度で、新しい処理ごとにリセットされます。',
        'loudness_meter_waiting': '音声ファイルを待機中',
        'loudness_score_acceptable': '許容範囲',
        'loudness_score_check': '要確認',
        'loudness_score_excellent': '非常に良い',
        'loudness_score_good': '良い',
        'loudness_score_needs_qc': '目標スコア：品質チェックを有効にしてください',
        'loudness_score_not_applicable': '目標スコア：対象外',
        'loudness_score_tooltip': 'このスコアは、実際に再測定された出力だけを使用します。得られたラウドネスと期待値の二乗平均平方根誤差に基づき、100は完全一致、50は品質チェックの許容値である全体誤差0.5 '
                                  'LU、0は1 LU以上の誤差を表します。アルバムモードでは、意図した曲間差を保つため、各曲の期待値に共通ゲインを反映します。 '
                                  'RMS誤差（差を二乗した平均の平方根）は、実測ラウドネスと各目標値との全体的なずれを1つの値で示します。0 '
                                  'LUに近いほど、処理結果は目標に正確です。',
        'loudness_score_value': '目標スコア：{score}/100\n{rating}\nRMS誤差：{deviation}\xa0LU',
        'loudness_score_waiting': '目標スコア：待機中',
        'measurement_unavailable': '測定できません。',
        'mode_album': 'アルバム — トラック間の差を保持',
        'mode_tooltip': 'トラックは各MP3を個別に調整します。アルバムはフォルダごとに共通ゲインを計算し、曲間の音量差を保持します。',
        'mode_track': 'トラック — 各ファイルを同じレベルにする',
        'mp3_filter': '対応音声 (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'フォルダが選択されていません',
        'no_mp3': '対応音声ファイルが見つかりません。',
        'no_new_source': '有効なフォルダーまたは対応音声ファイルは追加されませんでした。',
        'not_performed': '未実行',
        'operation': '処理',
        'operation_analyze': '解析のみ — ファイルを作らないシミュレーション',
        'operation_analyze_label': '解析のみ',
        'operation_convert': '均一化 — 音声を実際にノーマライズ',
        'operation_convert_label': '音声ノーマライズ',
        'operation_replaygain': 'ReplayGain — 再エンコードなし',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': '均一化は音声を実際に処理します。MP3、M4A/AAC、OGG、Opus '
                             'は再エンコードが必要で、サイズは品質設定により増える場合があります。FLAC '
                             'は可逆で再エンコードされますが、サンプルが変わるため圧縮率は変動します。WAV/AIFF '
                             'は元と互換のサンプルレート、チャンネル、ビット深度を保持します。ReplayGain '
                             'は再エンコードせず、解析のみではファイルを作りません。',
        'options_tab': 'オプション',
        'overwrite': '既存ファイルを上書き',
        'overwrite_tooltip': '保存先に同名のMP3がある場合に置き換えます。元ファイルは上書きされません。',
        'parallel': '並列処理',
        'parallel_adjusted': '自動並列処理 — {active}プロセス、CPU {cpu:.0f}%。',
        'parallel_auto': '自動',
        'parallel_auto_log': '自動、最大 {maximum}',
        'parallel_tooltip': '同時に処理できるファイル数を決めます。\n'
                            '\n'
                            '• '
                            '自動は最大4タスクで開始します。CPU測定が利用できる場合は毎秒確認し、使用率70%未満で1タスク増やし、92%を超えると1タスク減らします。\n'
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
        'processing_paused': '処理を一時停止しました。',
        'processing_resumed': '処理を再開しました。',
        'progress_status': '{status}：{file}',
        'qc_impossible': '警告 — 品質チェックに失敗しました：{error}',
        'qc_log': ' — 品質 {quality}',
        'qc_ok': 'OK',
        'qc_warning': '警告 — {detail}',
        'quality': '音声品質',
        'quality_control': '自動品質チェック',
        'quality_control_tooltip': '各出力を再測定します。ダイナミック経路のMP3では、測定結果により最大3回の補正再エンコードを行うことがあります。無効にしてもエンコーダー品質は変わりませんが、最終確認、補正、メーター表示は行われません。',
        'quality_tooltip': '圧縮形式の品質とサイズを調整します。小さい数値ほど高品質・高ビットレートです。設定ビットレートが元より高ければファイルは大きくなります。大きい数値ほど通常は小さくなりますが、VBR '
                           'では同じバイト数を保証できません。FLAC は常に可逆で、WAV/AIFF は PCM 属性を保持します。 目安: 0 = 最高品質、1-2 '
                           '= 非常に高い、3-4 = バランス、5-9 = 小さいサイズ。',
        'ready': '準備完了',
        'recursive_scan': 'フォルダを再帰的に検索中…',
        'remove_all': 'すべて削除',
        'remove_selection': '選択項目を削除',
        'replaygain_tags_missing': 'ReplayGainタグが見つかりません。',
        'report_album_dbtp': 'アルバム入力_dbtp',
        'report_album_lufs': 'アルバム入力_lufs',
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
        'report_seconds': '処理秒数',
        'report_source': '元ファイル',
        'report_status': '状態',
        'report_tooltip': '測定値、処理時間、警告を含む詳細なレポートを保存先に作成します。',
        'resume': '中断後に再開',
        'resume_not_saved': ' 再開ポイントを保存できませんでした：{error}',
        'resume_processing': '再開',
        'resume_tooltip': '同じ設定で完了済みのファイルを認識し、再処理を省きます。',
        'resumed_progress': '再開：{file}',
        'scan_error': 'エラー — {error}',
        'settings': '設定',
        'show_finder': 'Finderに表示',
        'show_option_help': 'ヘルプを表示：{option}',
        'silent_album_copy': '無音または測定不能なアルバムをコピーしました。',
        'silent_copy': '無音または測定不能な音声をコピーしました。',
        'silent_copy_no_replaygain': '無音の音声をReplayGainタグなしでコピーしました。',
        'silent_unmeasurable': '無音または測定不能な音声です。',
        'simulation': 'シミュレーション',
        'skip_compliant': '適合済みファイルを再エンコードしない',
        'skip_compliant_tooltip': '既定で有効です。解析後、ラウドネスが目標の±0.5 '
                                  'LU以内でトゥルーピークが上限以下なら、音声を再エンコードせず同一のままコピーします。アルバムモードではアルバム全体のラウドネスで判定します。品質とサイズを完全に維持し、ログにも表示します。',
        'skipped_progress': 'スキップ：{file}',
        'source_audio_count': '処理する音声ファイル：{count}',
        'source_list_more': '… ほか {count} 件のソースを保持',
        'source_safety': '元のファイルは移動も変更もしません。',
        'source_selection_tooltip': '複数選択：個別項目はCommandクリック、範囲はShiftクリックで選択します。',
        'start': '開始',
        'status_analyzed': '解析済み',
        'status_cancelled': 'キャンセル',
        'status_error': 'エラー',
        'status_ok': 'OK',
        'status_resumed': '再開',
        'status_skipped': 'スキップ',
        'switch_to_dark': 'ダークモード',
        'switch_to_light': 'ライトモード',
        'tagline': '知覚される音量を均一化',
        'target': '目標ラウドネス',
        'target_tooltip': 'ラウドネス目標は、曲全体の積分ラウドネスの目標値をLUFSで表したものです。負の値が小さいほどファイルは大きく聞こえ、-14 LUFSは-16 '
                          'LUFSより大きくなります。2 LUの差は、ピーク制限前ではおよそ2 dBのレベル差に相当します。\n'
                          '\n'
                          '目安：落ち着きとダイナミクスを重視するなら-18 LUFS、全体的なバランスなら-16 LUFS、ストリーミング風の大きめの音量なら-14 '
                          'LUFSです。配信サービス側で別の再生ノーマライズが行われる場合があります。\n'
                          '\n'
                          'この目標だけで曲内部の強弱が平坦になるわけではありません。最大トゥルーピークによりクリッピングなしで目標へ到達できない場合、結果は少し低くなることがあります。',
        'theme_accessible': 'アプリケーションの表示を変更します。選択は保存されます。',
        'total_time': '合計時間：{duration}',
        'track_mode_log': 'トラックモード — 各音声ファイルを個別に処理します。',
        'track_two_pass': '2パスのトラックノーマライズ。',
        'true_peak_meter_exceeded': '超過 {margin} dB',
        'true_peak_meter_margin': '余裕 {margin} dB',
        'true_peak_meter_title': 'ピーク余裕',
        'true_peak_meter_tooltip': '最後の出力のトゥルーピークを設定上限と比較します。マーカーは最新値、三角は一連の最大ピークを保持します。緑は上限内、橙は0.25 '
                                   'dB以内の超過、赤はそれ以上です。橙の許容値はLUFScaleの品質管理用で、納品規格ではありません。新しい処理ごとにリセットします。',
        'true_peak_meter_waiting': 'dBTP測定待ち',
        'version_changes': '• ソースの追加・削除時に音声ファイル総数を更新します。\n'
                           '• メーターの寸法と間隔を1.21.25に戻し、品質管理が無効な場合は動作しません。\n'
                           '• 推定表示に完了予定時刻を追加しました。\n'
                           '• 以前の内部テストツールを削除しました。',
        'version_changes_title': 'バージョン {version} の新機能',
        'version_label': 'バージョン {version}',
        'volume': '音量',
        'volume_loud': '大きめ: -14 LUFS',
        'volume_normal': '標準: -16 LUFS',
        'volume_soft': '小さめ: -18 LUFS',
        'volume_tooltip': 'この設定はラウドネス目標の簡易選択です。Macの再生音量は変更しません。\n'
                          '\n'
                          '• 小さめ：-18 LUFS — 落ち着いた音量で、ダイナミックレンジの余裕が大きく、リミッターが動作しにくい設定です。\n'
                          '• 標準：-16 LUFS — バランスのよい妥協点で、個人ライブラリの出発点に適しています。\n'
                          '• 大きめ：-14 LUFS — Spotifyの「標準」再生目標に近い、存在感のある音量ですが、制限処理が必要になる可能性が高まります。\n'
                          '• カスタム — 別のLUFS目標を直接入力できます。\n'
                          '\n'
                          'これらは実用的な選択肢であり、世界共通の規格ではありません。',
        'zero_album_gain': 'アルバムゲインは0です。音声をコピーしました。'},
 'nl': {'activity_cancelled': 'Activiteit: verwerking geannuleerd',
        'activity_cancelling': 'Activiteit: annuleren…',
        'activity_completed': 'Activiteit: verwerking voltooid',
        'activity_compliant': 'Conform: {count}',
        'activity_detected': 'Activiteit: {total} bestand(en) gevonden',
        'activity_errors': 'Fouten: {count}',
        'activity_files': 'Bestanden: {count}',
        'activity_idle': 'Activiteit: wacht',
        'activity_preparing': 'Activiteit: bestanden voorbereiden…',
        'activity_progress': '{total} bestanden • geslaagd {success} • waarschuwingen {warnings} • '
                             'fouten {failed} • hervat/overgeslagen {skipped} • conform '
                             '{compliant}',
        'activity_skipped': 'Hervat/overgeslagen: {count}',
        'activity_successes': 'Geslaagd: {count}',
        'activity_warnings': 'Waarschuwingen: {count}',
        'adaptive_disabled_log': 'Adaptieve analyse — snelle sondes gestopt na {sample} metingen '
                                 '({successes} successen, geschatte besparing {percent:+.1f}%).',
        'add_folders': 'Mappen toevoegen…',
        'add_mp3': 'Audiobestanden toevoegen…',
        'add_replaygain': 'ReplayGain toevoegen',
        'add_source_files': 'Audiobestanden toevoegen',
        'album_gain_detail': 'Gedeelde albumversterking {gain:+.2f} dB.',
        'album_gain_log': 'Album ‘{album}’ — gedeelde versterking {gain:+.2f} dB.',
        'album_measurement_error': 'Album kon niet worden gemeten: {error}',
        'album_mode_log': 'Albummodus — elke map met audiobestanden vormt een album.',
        'albums_measurement': '{count} album(s) meten…',
        'already_completed': 'Al voltooid tijdens een eerdere uitvoering.',
        'already_compliant_badge': 'CONFORM',
        'already_compliant_copy': 'Al conform: ongewijzigd gekopieerd zonder audiohercodering.',
        'already_compliant_log': 'al conform, zonder hercodering',
        'analysis_cache_summary': 'Analysecache — {hits} meting(en) hergebruikt.',
        'analysis_impossible': 'Analyse mislukt: {error}',
        'analysis_method': 'Analysemethode',
        'analysis_method_adaptive': 'Adaptief — stopt zonder voordeel',
        'analysis_method_fast': 'Snel — experimenteel',
        'analysis_method_historical': 'Historisch — referentie',
        'analysis_method_log': 'Analysemethode — {method}.',
        'analysis_method_tooltip': 'Historisch gebruikt alleen de volledige referentiemeting die '
                                   'in 1.22.13 is gevalideerd. Snel probeert de lineaire sonde bij '
                                   'elk bestand en valt zo nodig terug op de historische meting. '
                                   'Adaptief begint als Snel; na minstens 12 metingen en 3 '
                                   'terugvallen vergelijkt het de gemeten tijden en schakelt het '
                                   'de sondes uit als de geschatte besparing onder 5% blijft. '
                                   'Eindkwaliteit en kwaliteitscontrole worden niet verminderd.',
        'analysis_progress': 'Analyse {current}/{total}: {file}',
        'analyze': 'Analyseren',
        'analyzed_progress': 'Geanalyseerd: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Audiostream zonder hercodering gekopieerd; ReplayGain-tags '
                                 'toegevoegd.',
        'audio_tab': 'Audio',
        'auto_start': 'Automatisch starten na slepen of plakken',
        'auto_start_tooltip': 'Start de verwerking automatisch na slepen of plakken wanneer al een '
                              'doelmap is gekozen.',
        'cancel': 'Annuleren',
        'cancelled_summary': 'Geannuleerd — {success} geslaagd, {failed} fout(en), {skipped} '
                             'hervat/overgeslagen, {warnings} waarschuwing(en), {compliant} '
                             'conform — {duration}.',
        'choose': 'Kiezen…',
        'clipboard_empty': 'Het klembord bevat geen geldig pad naar een map of ondersteund '
                           'audiobestand.',
        'completed_dialog_summary': 'Status: voltooid\n'
                                    'Bestanden: {files}\n'
                                    'Geslaagd: {success}\n'
                                    'Fouten: {failed}\n'
                                    'Hervat of overgeslagen: {skipped}\n'
                                    'Waarschuwingen: {warnings}\n'
                                    'Conform: {compliant}\n'
                                    'Totale tijd: {duration}',
        'completed_summary': 'Voltooid — {success} geslaagd, {failed} fout(en), {skipped} '
                             'hervat/overgeslagen, {warnings} waarschuwing(en), {compliant} '
                             'conform — {duration}.',
        'convert': 'Normaliseren',
        'convert_operation': 'audionormalisatie',
        'cpu_tooltip': 'Totale CPU-belasting van de Mac, elke seconde bijgewerkt tijdens de '
                       'verwerking.',
        'cpu_usage': 'CPU',
        'create_report': 'CSV-rapport maken',
        'custom': 'Aangepast',
        'description': 'Maakt het waargenomen volume gelijk in Track- of Albummodus zonder de '
                       'originelen te wijzigen.',
        'destination': 'Doelmap',
        'destination_error': 'FOUT — doelmap niet beschikbaar: {error}',
        'destination_path_tooltip': 'Klik in het pad en gebruik de pijltjestoetsen, Home/End of '
                                    'het muiswiel. Het pad kan worden geselecteerd en gekopieerd, '
                                    'maar niet gewijzigd.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — submappen ondersteund',
        'drop_title': 'Sleep mappen of audiobestanden hierheen',
        'elapsed_time': 'Verstreken tijd: {duration}',
        'error_progress': 'Fout: {file}',
        'estimated_result': 'Geschat resultaat; geen bestand gemaakt.',
        'estimated_total_calculating': 'Geschatte totale tijd: berekenen…',
        'estimated_total_time': 'Geschatte totale tijd: {duration}',
        'estimated_total_time_with_finish': 'Geschatte totale tijd: {duration} — klaar rond {time}',
        'estimated_total_unavailable': 'Geschatte totale tijd: niet beschikbaar',
        'ffmpeg_download_button': 'Officiële FFmpeg-website openen',
        'ffmpeg_missing_encoders': 'Deze FFmpeg-versie bevat niet alle vereiste audio-encoders: '
                                   '{encoders}.',
        'file_exists': 'Het bestand bestaat al.',
        'files_found': '{total} audiobestand(en) gevonden — {operation} — {parallel} parallelle '
                       'processen.',
        'guide_help_tooltip': 'Opent de volledige PDF-handleiding in de gekozen taal.',
        'guide_missing_message': 'De PDF-handleiding is niet gevonden: {path}',
        'guide_missing_title': 'Handleiding niet beschikbaar',
        'guide_open_error': 'macOS kon de PDF-handleiding niet openen: {path}',
        'help_button': 'Help',
        'help_overview': '• Echte normalisatie, ReplayGain of alleen analyse.\n'
                         '• Track- en Albummodus.\n'
                         '• Mappenstructuur, metadata en albumhoezen blijven behouden wanneer '
                         'FFmpeg ze kan kopiëren.\n'
                         '• Originelen worden nooit verplaatst of gewijzigd.\n'
                         '• Automatische parallelisatie, analysecache en hervatten.\n'
                         '• Interface in twaalf talen en PDF-handleidingen in twaalf talen.',
        'help_title': 'Belangrijkste functies',
        'internal_error': 'Interne fout: {error}',
        'interrupted': 'Verwerking onderbroken.',
        'language_tooltip': 'Wijzigt direct de taal van de interface. De keuze wordt onthouden; '
                            'niet-vertaalde technische meldingen blijven Engels.',
        'level_mode': 'Luidheidsmodus',
        'log_help_text': 'Elke regel beschrijft een bestand of een algemene verwerkingsstap.\n'
                         '\n'
                         '• Begin: verwerkingsstatus (OK, WAARSCHUWING, FOUT, hervat of '
                         'overgeslagen).\n'
                         '• Daarna: MP3-naam en tijd besteed aan dat bestand.\n'
                         '• LUFS-vak: gemeten niveau vóór → bereikt niveau na verwerking.\n'
                         '• Einde: resultaat van de kwaliteitscontrole en eventuele details.\n'
                         '\n'
                         'Kleuren: groen = geslaagd; oranje = waarschuwing; rood = niet voltooid '
                         'bestand; blauwviolet = hervatting; grijs = informatie, overgeslagen item '
                         'of annulering.\n'
                         '\n'
                         'De cumulatieve tijden tellen het werk van alle parallelle taken op. De '
                         'totale tijd is de werkelijk verstreken duur.\n'
                         '\n'
                         'QC-WAARSCHUWING — piek betekent dat de opnieuw gemeten true peak van de '
                         'uitvoer meer dan 0,25 dB boven de gekozen grens ligt. Het bestand wordt '
                         'toch aangemaakt: dit is geen conversiefout. Het voldoet echter niet '
                         'strikt aan het gevraagde plafond en laat minder speelruimte voor een '
                         'nieuwe codering of sommige converters. Hoe dichter de dBTP-waarde bij 0 '
                         'komt, hoe groter het risico op intersamplepieken. Kies bij een '
                         'aanhoudende waarschuwing een lager LUFS-doel of een voorzichtiger '
                         'maximale piek, bijvoorbeeld −2,0 dBTP, en verwerk het bestand opnieuw.',
        'log_placeholder': 'Het verwerkingsverslag verschijnt hier.',
        'log_title': 'Verwerkingslogboek',
        'loudness_meter_help_text': 'Deze meter controleert visueel of de normalisatie gelijkmatig '
                                    'is. Hij vergelijkt het laatste audiobestand met het doel en '
                                    'berekent voortdurend het minimum en maximum van de laatste '
                                    '100 bestanden. Oudere waarden verlaten dit venster '
                                    'geleidelijk, zodat grote reeksen dynamisch blijven. De '
                                    'doelscore blijft over de hele reeks berekend en de indicator '
                                    'wijzigt geen instellingen.',
        'loudness_meter_maximum': 'Max {value}',
        'loudness_meter_minimum': 'Min {value}',
        'loudness_meter_target': 'Doel {value} LUFS',
        'loudness_meter_title': 'Luidheidsmeter',
        'loudness_meter_tooltip': 'De rode lijn is het doel. De blauwe waarde links volgt het '
                                  'laatste audiobestand. De grijze en donkerpaarse lijnen en '
                                  'waarden rechts tonen het minimum en maximum van de laatste 100 '
                                  'bestanden. De schaal vergroot kleine verschillen en de meter '
                                  'wordt voor elke nieuwe reeks hersteld.',
        'loudness_meter_waiting': 'Wachten op een audiobestand',
        'loudness_score_acceptable': 'Aanvaardbaar',
        'loudness_score_check': 'Controleren',
        'loudness_score_excellent': 'Uitstekend',
        'loudness_score_good': 'Goed',
        'loudness_score_needs_qc': 'Doelscore: schakel kwaliteitscontrole in',
        'loudness_score_not_applicable': 'Doelscore: niet van toepassing',
        'loudness_score_tooltip': 'De score gebruikt alleen uitvoer die werkelijk opnieuw is '
                                  'gemeten. Hij is gebaseerd op de kwadratisch gemiddelde '
                                  'afwijking tussen bereikte en verwachte luidheid: 100 = exact '
                                  'resultaat, 50 = een totale afwijking van 0,5 LU, de tolerantie '
                                  'van de kwaliteitscontrole, en 0 = een afwijking van 1 LU of '
                                  'meer. In Albummodus houdt de verwachte waarde van elk nummer '
                                  'rekening met de gedeelde versterking, zodat de bedoelde '
                                  'verschillen behouden blijven. De RMS-afwijking (de '
                                  'vierkantswortel van het gemiddelde van de gekwadrateerde '
                                  'verschillen) vat de totale afstand tussen de bereikte luidheden '
                                  'en hun doelen samen. Hoe dichter bij 0 LU, hoe nauwkeuriger de '
                                  'reeks.',
        'loudness_score_value': 'Doelscore: {score}/100\n'
                                '{rating}\n'
                                'RMS-afwijking: {deviation}\xa0LU',
        'loudness_score_waiting': 'Doelscore: wachten',
        'measurement_unavailable': 'Meting niet beschikbaar.',
        'mode_album': 'Album — behoudt verschillen tussen tracks',
        'mode_tooltip': 'Track past elke MP3 afzonderlijk aan. Album berekent één gezamenlijke '
                        'versterking per map om de volumeverschillen tussen tracks te behouden.',
        'mode_track': 'Track — hetzelfde niveau voor elk bestand',
        'mp3_filter': 'Ondersteunde audio (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Geen map geselecteerd',
        'no_mp3': 'Geen ondersteunde audiobestanden gevonden.',
        'no_new_source': 'Er is geen nieuwe geldige map of ondersteund audiobestand toegevoegd.',
        'not_performed': 'Niet uitgevoerd',
        'operation': 'Bewerking',
        'operation_analyze': 'Alleen analyseren — simulatie zonder bestand',
        'operation_analyze_label': 'Alleen analyse',
        'operation_convert': 'Normaliseren — audio werkelijk verwerken',
        'operation_convert_label': 'Audionormalisatie',
        'operation_replaygain': 'ReplayGain — zonder hercodering',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Normaliseren verwerkt de audio echt. MP3, M4A/AAC, OGG en Opus '
                             'moeten opnieuw worden gecodeerd; de grootte hangt van de kwaliteit '
                             'af en kan toenemen. FLAC wordt verliesvrij hercodeerd, maar de '
                             'compressie kan door gewijzigde samples variëren. WAV en AIFF '
                             'behouden compatibele bronfrequentie, kanalen en bitdiepte. '
                             'ReplayGain hercodeert niet; Analyseren maakt geen bestand.',
        'options_tab': 'Opties',
        'overwrite': 'Bestaande bestanden overschrijven',
        'overwrite_tooltip': 'Staat toe dat een MP3 die al in de doelmap staat wordt vervangen. '
                             'Bronbestanden worden nooit overschreven.',
        'parallel': 'Parallelle processen',
        'parallel_adjusted': 'Automatische parallelisatie — {active} proces(sen), CPU {cpu:.0f}%.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automatisch, maximaal {maximum}',
        'parallel_tooltip': 'Bepaalt hoeveel bestanden tegelijk kunnen worden verwerkt.\n'
                            '\n'
                            '• Auto begint met maximaal 4 taken. Als CPU-meting beschikbaar is, '
                            'controleert het programma die elke seconde: onder 70% belasting komt '
                            'er één taak bij en boven 92% gaat er één af.\n'
                            '• Auto overschrijdt nooit het gedetecteerde aantal logische '
                            'processors en heeft een absolute grens van 16 taken.\n'
                            '• Is CPU-meting niet beschikbaar, dan gebruikt Auto die gedetecteerde '
                            'grens direct, zonder dynamische aanpassing.\n'
                            '• Een numerieke waarde stelt het maximale aantal gelijktijdige taken '
                            'vast; het is geen doel voor CPU-belasting.\n'
                            '\n'
                            'Meer taken kunnen een grote reeks versnellen, maar verhogen '
                            'belasting, temperatuur en schijfactiviteit. Druk op − tot Auto '
                            'verschijnt.',
        'paste': 'Plakken',
        'path_left': 'Linkerdeel van het pad tonen',
        'path_right': 'Rechterdeel van het pad tonen',
        'pause': 'Pauze',
        'peak': 'Maximale true peak',
        'peak_tooltip': 'De maximale true peak is een plafond, geen niveau dat bereikt moet '
                        'worden. Hij begrenst de hoogste gereconstrueerde golfvormpieken in dBTP, '
                        'ook pieken tussen samples, om oversturing na codering of transcodering te '
                        'verminderen.\n'
                        '\n'
                        '• -1,0 dBTP — gebruikelijk afleverplafond met het hoogste '
                        'uitgangspiekniveau.\n'
                        '• -1,5 dBTP — standaardwaarde en voorzichtig compromis voor MP3.\n'
                        '• -2,0 dBTP — extra ruimte, nuttig als het bestand opnieuw kan worden '
                        'gecodeerd of bij een hoog luidheidsdoel.\n'
                        '• 0 dBTP — geen ruimte; niet aanbevolen voor MP3.\n'
                        '\n'
                        'Een negatievere waarde is veiliger, maar kan voorkomen dat zeer '
                        'dynamische tracks het LUFS-doel exact bereiken.',
        'phase_summary': 'Geschatte verdeling van de totale tijd — analyse {analysis}, conversie '
                         '{conversion}, kwaliteitscontrole {quality}.',
        'pipeline_enabled': 'Track-pijplijn — elke conversie start zodra de analyse klaar is.',
        'pre_measurement': 'Invoerbestanden meten…',
        'preset': 'Voorinstelling',
        'preset_dynamic': 'Dynamische muziek',
        'preset_library': 'Muziekbibliotheek — aanbevolen',
        'preset_streaming': 'Krachtiger streamen',
        'preset_tooltip': 'Past in één keer een samenhangend luidheidsdoel, een maximale true peak '
                          'en MP3-kwaliteit toe. Elke handmatige wijziging kiest Aangepast.',
        'processing_cancelled': 'Verwerking geannuleerd.',
        'processing_paused': 'Verwerking gepauzeerd.',
        'processing_resumed': 'Verwerking hervat.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'WAARSCHUWING — kwaliteitscontrole mislukt: {error}',
        'qc_log': ' — KC {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'WAARSCHUWING — {detail}',
        'quality': 'Audiokwaliteit',
        'quality_control': 'Automatische kwaliteitscontrole',
        'quality_control_tooltip': 'Meet elke uitvoer opnieuw. Bij dynamische MP3-bestanden kan '
                                   'deze meting maximaal drie corrigerende hercoderingen starten. '
                                   'Uitschakelen verandert de encoderkwaliteit niet, maar '
                                   'verwijdert eindcontrole, correcties en meteractiviteit.',
        'quality_tooltip': 'Regelt kwaliteit en grootte van gecomprimeerde formaten: een laag '
                           'getal gebruikt hogere kwaliteit en bitrate. Is de gekozen bitrate '
                           'hoger dan de bron, dan groeit het bestand. Een hoger getal verkleint '
                           'het meestal, maar VBR garandeert niet hetzelfde aantal bytes. FLAC '
                           'blijft verliesvrij; WAV en AIFF negeren deze instelling en behouden '
                           'hun PCM-eigenschappen. Bereiken: 0 = maximale kwaliteit; 1-2 = zeer '
                           'hoog; 3-4 = evenwicht; 5-9 = kleiner bestand.',
        'ready': 'Gereed',
        'recursive_scan': 'Mappen recursief doorzoeken…',
        'remove_all': 'Alles verwijderen',
        'remove_selection': 'Selectie verwijderen',
        'replaygain_tags_missing': 'ReplayGain-tags zijn niet gevonden.',
        'report_album_dbtp': 'album_invoer_dbtp',
        'report_album_lufs': 'album_invoer_lufs',
        'report_destination': 'doel',
        'report_detail': 'details',
        'report_error': 'WAARSCHUWING — CSV-rapport kan niet worden gemaakt: {error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'versterking_db',
        'report_input_dbtp': 'invoer_dbtp',
        'report_input_lufs': 'invoer_lufs',
        'report_log': 'CSV-rapport — {path}',
        'report_mode': 'modus',
        'report_operation': 'bewerking',
        'report_output_dbtp': 'uitvoer_dbtp',
        'report_output_lufs': 'uitvoer_lufs',
        'report_path': 'Rapport: {path}',
        'report_qc': 'kwaliteitscontrole',
        'report_seconds': 'verstreken_seconden',
        'report_source': 'bron',
        'report_status': 'status',
        'report_tooltip': 'Maakt in de doelmap een gedetailleerd rapport met metingen, tijden en '
                          'waarschuwingen.',
        'resume': 'Hervatten na een onderbreking',
        'resume_not_saved': ' Hervattingspunt niet opgeslagen: {error}',
        'resume_processing': 'Hervatten',
        'resume_tooltip': 'Bestanden die met dezelfde instellingen al zijn voltooid, worden '
                          'herkend en niet opnieuw verwerkt.',
        'resumed_progress': 'Hervat: {file}',
        'scan_error': 'FOUT — {error}',
        'settings': 'Instellingen',
        'show_finder': 'Toon in Finder',
        'show_option_help': 'Help tonen: {option}',
        'silent_album_copy': 'Stil of niet-meetbaar album gekopieerd.',
        'silent_copy': 'Stille of niet-meetbare audio gekopieerd.',
        'silent_copy_no_replaygain': 'Stille audio zonder ReplayGain-tags gekopieerd.',
        'silent_unmeasurable': 'Stille of niet-meetbare audio.',
        'simulation': 'Simulatie',
        'skip_compliant': 'Conforme bestanden niet opnieuw coderen',
        'skip_compliant_tooltip': 'Standaard ingeschakeld. Na analyse wordt een bestand '
                                  'ongewijzigd gekopieerd als de luidheid binnen ±0,5 LU van het '
                                  'doel ligt en de true peak de grens niet overschrijdt. In '
                                  'Albummodus geldt de luidheidscontrole voor het hele album. '
                                  'Kwaliteit en grootte blijven exact gelijk; het logboek vermeldt '
                                  'dit.',
        'skipped_progress': 'Overgeslagen: {file}',
        'source_audio_count': 'Te verwerken audiobestanden: {count}',
        'source_list_more': '… nog {count} bronnen behouden',
        'source_safety': 'Bronbestanden worden nooit verplaatst of gewijzigd.',
        'source_selection_tooltip': 'Meervoudige selectie: Command-klik voor losse items en '
                                    'Shift-klik voor een bereik.',
        'start': 'Starten',
        'status_analyzed': 'GEANALYSEERD',
        'status_cancelled': 'GEANNULEERD',
        'status_error': 'FOUT',
        'status_ok': 'OK',
        'status_resumed': 'HERVAT',
        'status_skipped': 'OVERGESLAGEN',
        'switch_to_dark': 'Donkere modus',
        'switch_to_light': 'Lichte modus',
        'tagline': 'Maakt het waargenomen audiovolume gelijk',
        'target': 'Luidheidsdoel',
        'target_tooltip': 'Het luidheidsdoel is de gewenste geïntegreerde luidheid over de hele '
                          'track, uitgedrukt in LUFS. Een minder negatieve waarde levert een '
                          'luider bestand op: -14 LUFS is luider dan -16 LUFS. Een verschil van 2 '
                          'LU komt vóór eventuele piekbegrenzing ongeveer overeen met 2 dB '
                          'niveauverschil.\n'
                          '\n'
                          'Richtwaarden: -18 LUFS voor een rustiger en dynamischer resultaat; -16 '
                          'LUFS voor algemene balans; -14 LUFS voor een luider streamingachtig '
                          'resultaat. Platforms kunnen daarna hun eigen afspeelnormalisatie '
                          'toepassen.\n'
                          '\n'
                          'Dit doel vlakt de dynamiek binnen de track niet vanzelf af. Als de '
                          'maximale true peak verhindert dat het doel zonder oversturing wordt '
                          'bereikt, kan het resultaat iets lager blijven.',
        'theme_accessible': 'Wijzig het uiterlijk van de toepassing. De keuze wordt onthouden.',
        'total_time': 'Totale tijd: {duration}',
        'track_mode_log': 'Trackmodus — elk audiobestand wordt apart verwerkt.',
        'track_two_pass': 'Tracknormalisatie in twee doorgangen.',
        'true_peak_meter_exceeded': 'Overschrijding {margin} dB',
        'true_peak_meter_margin': 'Marge {margin} dB',
        'true_peak_meter_title': 'Piekmarge',
        'true_peak_meter_tooltip': 'Vergelijkt de true peak van de laatste uitvoer met de gekozen '
                                   'grens. De markering toont de laatste waarde en de driehoek '
                                   'bewaart de hoogste piek van de reeks. Groen: binnen de grens; '
                                   'oranje: tot 0,25 dB erboven; rood: meer. De oranje tolerantie '
                                   'hoort bij LUFScale-kwaliteitscontrole en is geen '
                                   'leveringsnorm. Wordt per reeks gewist.',
        'true_peak_meter_waiting': 'Wachten op een dBTP-meting',
        'version_changes': '• Het totale aantal audiobestanden wordt bijgewerkt bij toevoegen of '
                           'verwijderen van bronnen.\n'
                           '• De meter gebruikt weer de afmetingen en afstand van versie 1.21.25 '
                           'en blijft zonder kwaliteitscontrole inactief.\n'
                           '• De schatting toont ook het verwachte eindtijdstip.\n'
                           '• De oude interne testhulpmiddelen zijn verwijderd.',
        'version_changes_title': 'Nieuw in versie {version}',
        'version_label': 'Versie {version}',
        'volume': 'Volume',
        'volume_loud': 'Luid: -14 LUFS',
        'volume_normal': 'Normaal: -16 LUFS',
        'volume_soft': 'Zacht: -18 LUFS',
        'volume_tooltip': 'Deze instelling is een snelkeuze voor het luidheidsdoel; zij verandert '
                          'niet het afspeelvolume van de Mac.\n'
                          '\n'
                          '• Zacht: -18 LUFS — rustiger niveau, meer dynamische ruimte en minder '
                          'kans dat de limiter ingrijpt.\n'
                          '• Normaal: -16 LUFS — evenwichtig compromis en goed beginpunt voor een '
                          'persoonlijke muziekbibliotheek.\n'
                          '• Luid: -14 LUFS — nadrukkelijkere weergave, dicht bij Spotify’s doel '
                          'voor Normaal, maar met meer kans op begrenzing.\n'
                          '• Aangepast — hiermee voert u rechtstreeks een ander LUFS-doel in.\n'
                          '\n'
                          'Dit zijn praktische keuzes, geen universele norm.',
        'zero_album_gain': 'Albumversterking nul; audio gekopieerd.'},
 'pl': {'activity_cancelled': 'Aktywność: przetwarzanie anulowane',
        'activity_cancelling': 'Aktywność: anulowanie…',
        'activity_completed': 'Aktywność: przetwarzanie zakończone',
        'activity_compliant': 'Zgodne: {count}',
        'activity_detected': 'Aktywność: wykryto {total} plik(ów)',
        'activity_errors': 'Błędy: {count}',
        'activity_files': 'Pliki: {count}',
        'activity_idle': 'Aktywność: oczekiwanie',
        'activity_preparing': 'Aktywność: przygotowywanie plików…',
        'activity_progress': '{total} plików • udane {success} • ostrzeżenia {warnings} • błędy '
                             '{failed} • wznowione/pominięte {skipped} • zgodne {compliant}',
        'activity_skipped': 'Wznowione/pominięte: {count}',
        'activity_successes': 'Udane: {count}',
        'activity_warnings': 'Ostrzeżenia: {count}',
        'adaptive_disabled_log': 'Analiza adaptacyjna — szybkie sondy zatrzymane po {sample} '
                                 'pomiarach ({successes} sukcesów, szacowana oszczędność '
                                 '{percent:+.1f}%).',
        'add_folders': 'Dodaj foldery…',
        'add_mp3': 'Dodaj pliki audio…',
        'add_replaygain': 'Dodaj ReplayGain',
        'add_source_files': 'Dodaj pliki audio',
        'album_gain_detail': 'Wspólne wzmocnienie albumu {gain:+.2f} dB.',
        'album_gain_log': 'Album „{album}” — wspólne wzmocnienie {gain:+.2f} dB.',
        'album_measurement_error': 'Nie udało się zmierzyć albumu: {error}',
        'album_mode_log': 'Tryb Album — każdy folder z plikami audio tworzy album.',
        'albums_measurement': 'Pomiar albumów: {count}…',
        'already_completed': 'Ukończono już podczas wcześniejszego uruchomienia.',
        'already_compliant_badge': 'ZGODNY',
        'already_compliant_copy': 'Już zgodny: skopiowano bez zmian i bez ponownego kodowania '
                                  'audio.',
        'already_compliant_log': 'już zgodny, bez ponownego kodowania',
        'analysis_cache_summary': 'Pamięć analiz — ponownie użyto {hits} pomiarów.',
        'analysis_impossible': 'Analiza nie powiodła się: {error}',
        'analysis_method': 'Metoda analizy',
        'analysis_method_adaptive': 'Adaptacyjna — zatrzymuje się bez zysku',
        'analysis_method_fast': 'Szybka — eksperymentalna',
        'analysis_method_historical': 'Historyczna — odniesienie',
        'analysis_method_log': 'Metoda analizy — {method}.',
        'analysis_method_tooltip': 'Historyczna używa wyłącznie pełnego pomiaru referencyjnego '
                                   'zatwierdzonego w 1.22.13. Szybka sprawdza sondę liniową dla '
                                   'każdego pliku i w razie potrzeby wraca do pomiaru '
                                   'historycznego. Adaptacyjna zaczyna jak Szybka; po co najmniej '
                                   '12 pomiarach i 3 powrotach porównuje zmierzone czasy i wyłącza '
                                   'sondy, jeśli szacowana oszczędność pozostaje poniżej 5%. '
                                   'Jakość końcowa i kontrola jakości nie są ograniczane.',
        'analysis_progress': 'Analiza {current}/{total}: {file}',
        'analyze': 'Analizuj',
        'analyzed_progress': 'Przeanalizowano: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Strumień audio skopiowano bez ponownego kodowania; dodano '
                                 'znaczniki ReplayGain.',
        'audio_tab': 'Audio',
        'auto_start': 'Uruchom automatycznie po upuszczeniu lub wklejeniu',
        'auto_start_tooltip': 'Automatycznie uruchamia przetwarzanie po przeciągnięciu lub '
                              'wklejeniu źródeł, jeśli wybrano folder docelowy.',
        'cancel': 'Anuluj',
        'cancelled_summary': 'Anulowano — {success} udane, {failed} błędów, {skipped} '
                             'wznowione/pominięte, {warnings} ostrzeżeń, {compliant} zgodne — '
                             '{duration}.',
        'choose': 'Wybierz…',
        'clipboard_empty': 'Schowek nie zawiera prawidłowej ścieżki do folderu lub obsługiwanego '
                           'pliku audio.',
        'completed_dialog_summary': 'Stan: zakończono\n'
                                    'Pliki: {files}\n'
                                    'Udane: {success}\n'
                                    'Błędy: {failed}\n'
                                    'Wznowione lub pominięte: {skipped}\n'
                                    'Ostrzeżenia: {warnings}\n'
                                    'Zgodne: {compliant}\n'
                                    'Łączny czas: {duration}',
        'completed_summary': 'Zakończono — {success} udane, {failed} błędów, {skipped} '
                             'wznowione/pominięte, {warnings} ostrzeżeń, {compliant} zgodne — '
                             '{duration}.',
        'convert': 'Normalizuj',
        'convert_operation': 'normalizacja audio',
        'cpu_tooltip': 'Całkowite użycie CPU komputera Mac, aktualizowane co sekundę podczas '
                       'przetwarzania.',
        'cpu_usage': 'CPU',
        'create_report': 'Utwórz raport CSV',
        'custom': 'Niestandardowe',
        'description': 'Wyrównuje odczuwaną głośność w trybie Utwór lub Album bez zmiany '
                       'oryginałów.',
        'destination': 'Miejsce docelowe',
        'destination_error': 'BŁĄD — folder docelowy niedostępny: {error}',
        'destination_path_tooltip': 'Kliknij ścieżkę, a następnie użyj strzałek, Home/End lub '
                                    'kółka myszy. Ścieżkę można zaznaczać i kopiować, ale nie '
                                    'zmieniać.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — z podfolderami',
        'drop_title': 'Upuść tutaj foldery lub pliki audio',
        'elapsed_time': 'Czas trwania: {duration}',
        'error_progress': 'Błąd: {file}',
        'estimated_result': 'Wynik szacowany; nie utworzono pliku.',
        'estimated_total_calculating': 'Szacowany czas całkowity: obliczanie…',
        'estimated_total_time': 'Szacowany czas całkowity: {duration}',
        'estimated_total_time_with_finish': 'Szacowany czas całkowity: {duration} — koniec około '
                                            '{time}',
        'estimated_total_unavailable': 'Szacowany czas całkowity: niedostępny',
        'ffmpeg_download_button': 'Otwórz oficjalną stronę FFmpeg',
        'ffmpeg_missing_encoders': 'Ta wersja FFmpeg nie zawiera wszystkich wymaganych koderów '
                                   'audio: {encoders}.',
        'file_exists': 'Plik już istnieje.',
        'files_found': 'Znaleziono {total} plik(ów) audio — {operation} — {parallel} procesów '
                       'równoległych.',
        'guide_help_tooltip': 'Otwiera pełny przewodnik PDF w wybranym języku.',
        'guide_missing_message': 'Nie znaleziono przewodnika PDF: {path}',
        'guide_missing_title': 'Przewodnik niedostępny',
        'guide_open_error': 'System macOS nie mógł otworzyć przewodnika PDF: {path}',
        'help_button': 'Pomoc',
        'help_overview': '• Normalizacja, ReplayGain lub sama analiza.\n'
                         '• Tryby Utwór i Album.\n'
                         '• Zachowanie struktury folderów, metadanych i okładek, gdy FFmpeg może '
                         'je skopiować.\n'
                         '• Oryginały nigdy nie są przenoszone ani modyfikowane.\n'
                         '• Automatyczna równoległość, pamięć analiz i wznawianie.\n'
                         '• Interfejs w dwunastu językach i przewodniki PDF w dziesięciu.',
        'help_title': 'Najważniejsze funkcje',
        'internal_error': 'Błąd wewnętrzny: {error}',
        'interrupted': 'Przetwarzanie przerwane.',
        'language_tooltip': 'Natychmiast zmienia język interfejsu. Wybór jest zapamiętywany; '
                            'nieprzetłumaczone komunikaty techniczne pozostają po angielsku.',
        'level_mode': 'Tryb głośności',
        'log_help_text': 'Każdy wiersz dotyczy pliku lub ogólnego etapu przetwarzania.\n'
                         '\n'
                         '• Początek: stan przetwarzania (OK, OSTRZEŻENIE, BŁĄD, wznowiono lub '
                         'pominięto).\n'
                         '• Dalej: nazwa MP3 i czas poświęcony temu plikowi.\n'
                         '• Pole LUFS: poziom zmierzony przed → poziom uzyskany po przetwarzaniu.\n'
                         '• Koniec: wynik kontroli jakości i ewentualne szczegóły.\n'
                         '\n'
                         'Kolory: zielony = sukces; pomarańczowy = ostrzeżenie; czerwony = plik '
                         'nieukończony; niebieskofioletowy = wznowienie; szary = informacja, '
                         'element pominięty lub anulowanie.\n'
                         '\n'
                         'Czasy skumulowane sumują pracę wszystkich zadań równoległych. Czas '
                         'całkowity to rzeczywisty czas, który upłynął.\n'
                         '\n'
                         'QC OSTRZEŻENIE — szczyt oznacza, że ponownie zmierzony true peak wyjścia '
                         'przekracza wybrany limit o ponad 0,25 dB. Plik mimo to zostaje '
                         'utworzony: nie jest to błąd konwersji. Nie spełnia jednak ściśle '
                         'żądanego pułapu i pozostawia mniej zapasu na kolejne kodowanie lub '
                         'niektóre konwertery. Im bliżej 0 znajduje się wartość dBTP, tym większe '
                         'ryzyko szczytów międzypróbkowych. Aby usunąć powtarzające się '
                         'ostrzeżenie, wybierz niższy cel LUFS lub bezpieczniejszy szczyt '
                         'maksymalny, na przykład −2,0 dBTP, i przetwórz plik ponownie.',
        'log_placeholder': 'Tutaj pojawi się raport z przetwarzania.',
        'log_title': 'Dziennik przetwarzania',
        'loudness_meter_help_text': 'Miernik służy do wizualnej kontroli równomierności '
                                    'normalizacji. Porównuje ostatni plik audio z celem i stale '
                                    'oblicza minimum oraz maksimum z ostatnich 100 plików. Starsze '
                                    'wartości stopniowo opuszczają to okno, dzięki czemu duże '
                                    'serie pozostają dynamiczne. Wynik celu nadal obejmuje całą '
                                    'serię, a wskaźnik nie zmienia ustawień.',
        'loudness_meter_maximum': 'Maks {value}',
        'loudness_meter_minimum': 'Min {value}',
        'loudness_meter_target': 'Cel {value} LUFS',
        'loudness_meter_title': 'Miernik głośności',
        'loudness_meter_tooltip': 'Czerwona linia oznacza cel. Niebieska wartość po lewej pokazuje '
                                  'ostatni plik audio. Szare i ciemnofioletowe linie oraz wartości '
                                  'po prawej pokazują minimum i maksimum z ostatnich 100 plików. '
                                  'Skala powiększa małe różnice, a miernik zeruje się dla każdej '
                                  'nowej serii.',
        'loudness_meter_waiting': 'Oczekiwanie na plik audio',
        'loudness_score_acceptable': 'Akceptowalny',
        'loudness_score_check': 'Do sprawdzenia',
        'loudness_score_excellent': 'Doskonały',
        'loudness_score_good': 'Dobry',
        'loudness_score_needs_qc': 'Wynik celu: włącz kontrolę jakości',
        'loudness_score_not_applicable': 'Wynik celu: nie dotyczy',
        'loudness_score_tooltip': 'Wynik wykorzystuje wyłącznie pliki wyjściowe, które '
                                  'rzeczywiście zmierzono ponownie. Opiera się na błędzie '
                                  'średniokwadratowym między uzyskaną a oczekiwaną głośnością: 100 '
                                  '= wynik dokładny, 50 = łączny błąd 0,5 LU, czyli tolerancja '
                                  'kontroli jakości, a 0 = błąd 1 LU lub większy. W trybie Album '
                                  'oczekiwana wartość każdego utworu uwzględnia wspólne '
                                  'wzmocnienie, aby zachować zamierzone różnice. Błąd RMS '
                                  '(pierwiastek ze średniej kwadratów odchyleń) podsumowuje łączną '
                                  'odległość między uzyskaną głośnością a wartościami docelowymi. '
                                  'Im bliżej 0 LU, tym dokładniejsza jest seria.',
        'loudness_score_value': 'Wynik celu: {score}/100\n{rating}\nBłąd RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Wynik celu: oczekiwanie',
        'measurement_unavailable': 'Pomiar niedostępny.',
        'mode_album': 'Album — zachowuje różnice między utworami',
        'mode_tooltip': 'Tryb Utwór reguluje każdy MP3 osobno. Tryb Album wylicza wspólne '
                        'wzmocnienie dla folderu, zachowując różnice głośności między utworami.',
        'mode_track': 'Utwór — ten sam poziom dla każdego pliku',
        'mp3_filter': 'Obsługiwane audio (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Nie wybrano folderu',
        'no_mp3': 'Nie znaleziono obsługiwanych plików audio.',
        'no_new_source': 'Nie dodano nowego prawidłowego folderu ani obsługiwanego pliku audio.',
        'not_performed': 'Nie wykonano',
        'operation': 'Operacja',
        'operation_analyze': 'Tylko analizuj — symulacja bez tworzenia pliku',
        'operation_analyze_label': 'Tylko analiza',
        'operation_convert': 'Wyrównaj — rzeczywiście normalizuj audio',
        'operation_convert_label': 'Normalizacja audio',
        'operation_replaygain': 'ReplayGain — bez ponownego kodowania',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Wyrównanie rzeczywiście przetwarza dźwięk. MP3, M4A/AAC, OGG i Opus '
                             'wymagają ponownego kodowania; rozmiar zależy od jakości i może '
                             'wzrosnąć. FLAC jest kodowany bezstratnie, ale kompresja może się '
                             'zmienić wraz z próbkami. WAV i AIFF zachowują zgodną częstotliwość, '
                             'kanały i głębię źródła. ReplayGain nie koduje ponownie; Analiza nie '
                             'tworzy pliku.',
        'options_tab': 'Opcje',
        'overwrite': 'Nadpisuj istniejące pliki',
        'overwrite_tooltip': 'Zezwala zastąpić MP3 istniejący w folderze docelowym. Pliki źródłowe '
                             'nigdy nie są nadpisywane.',
        'parallel': 'Procesy równoległe',
        'parallel_adjusted': 'Automatyczna równoległość — procesy: {active}, CPU {cpu:.0f}%.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automatycznie, maksimum {maximum}',
        'parallel_tooltip': 'Określa, ile plików może być przetwarzanych jednocześnie.\n'
                            '\n'
                            '• Auto zaczyna od maksymalnie 4 zadań. Gdy pomiar CPU jest dostępny, '
                            'sprawdza go co sekundę: poniżej 70% obciążenia dodaje jedno zadanie, '
                            'a powyżej 92% usuwa jedno.\n'
                            '• Auto nigdy nie przekracza wykrytej liczby procesorów logicznych, z '
                            'bezwzględnym limitem 16 zadań.\n'
                            '• Gdy pomiar CPU nie jest dostępny, Auto używa bezpośrednio wykrytego '
                            'limitu bez dynamicznego dostosowania.\n'
                            '• Wartość liczbowa ustala maksymalną liczbę równoczesnych zadań; nie '
                            'jest celem obciążenia CPU.\n'
                            '\n'
                            'Więcej zadań może przyspieszyć dużą partię, ale zwiększa obciążenie, '
                            'temperaturę i aktywność dysku. Naciskaj −, aż pojawi się Auto.',
        'paste': 'Wklej',
        'path_left': 'Pokaż lewą część ścieżki',
        'path_right': 'Pokaż prawą część ścieżki',
        'pause': 'Pauza',
        'peak': 'Maksymalny true peak',
        'peak_tooltip': 'Maksymalny true peak jest pułapem, a nie poziomem do osiągnięcia. '
                        'Ogranicza w dBTP najwyższe szczyty odtworzonego przebiegu, także między '
                        'próbkami, aby zmniejszyć ryzyko przesterowania po kodowaniu lub '
                        'transkodowaniu.\n'
                        '\n'
                        '• -1,0 dBTP — typowy pułap dostarczania z najwyższym szczytem '
                        'wyjściowym.\n'
                        '• -1,5 dBTP — wartość domyślna i ostrożny kompromis dla MP3.\n'
                        '• -2,0 dBTP — dodatkowy zapas, przydatny przy ponownym kodowaniu lub '
                        'wysokim celu głośności.\n'
                        '• 0 dBTP — brak zapasu; niezalecane dla MP3.\n'
                        '\n'
                        'Bardziej ujemna wartość jest bezpieczniejsza, ale może uniemożliwić '
                        'bardzo dynamicznym utworom dokładne osiągnięcie celu LUFS.',
        'phase_summary': 'Szacowany podział czasu całkowitego — analiza {analysis}, konwersja '
                         '{conversion}, kontrola jakości {quality}.',
        'pipeline_enabled': 'Potok utworów — każda konwersja rozpoczyna się po zakończeniu jej '
                            'analizy.',
        'pre_measurement': 'Pomiar plików wejściowych…',
        'preset': 'Ustawienie wstępne',
        'preset_dynamic': 'Muzyka dynamiczna',
        'preset_library': 'Biblioteka muzyczna — zalecane',
        'preset_streaming': 'Głośniejszy streaming',
        'preset_tooltip': 'Jednocześnie ustawia spójny cel głośności, maksymalny true peak i '
                          'jakość MP3. Każda ręczna zmiana wybiera tryb Niestandardowy.',
        'processing_cancelled': 'Przetwarzanie anulowane.',
        'processing_paused': 'Przetwarzanie wstrzymane.',
        'processing_resumed': 'Przetwarzanie wznowione.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'OSTRZEŻENIE — kontrola jakości nie powiodła się: {error}',
        'qc_log': ' — KJ {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'OSTRZEŻENIE — {detail}',
        'quality': 'Jakość audio',
        'quality_control': 'Automatyczna kontrola jakości',
        'quality_control_tooltip': 'Ponownie mierzy każdy plik wyjściowy. Dla dynamicznych MP3 '
                                   'pomiar może uruchomić do trzech korygujących ponownych '
                                   'kodowań. Wyłączenie nie zmienia jakości kodera, ale usuwa '
                                   'końcową kontrolę, korekty i działanie miernika.',
        'quality_tooltip': 'Steruje jakością i rozmiarem formatów skompresowanych: mała liczba '
                           'oznacza wyższą jakość i przepływność. Gdy wybrana przepływność '
                           'przewyższa źródło, plik rośnie. Większa liczba zwykle go zmniejsza, '
                           'lecz VBR nie gwarantuje identycznej liczby bajtów. FLAC pozostaje '
                           'bezstratny; WAV i AIFF zachowują właściwości PCM. Zakresy: 0 = '
                           'najwyższa jakość; 1-2 = bardzo wysoka; 3-4 = równowaga; 5-9 = mniejszy '
                           'plik.',
        'ready': 'Gotowe',
        'recursive_scan': 'Rekurencyjne przeszukiwanie folderów…',
        'remove_all': 'Usuń wszystko',
        'remove_selection': 'Usuń zaznaczenie',
        'replaygain_tags_missing': 'Nie znaleziono znaczników ReplayGain.',
        'report_album_dbtp': 'dbtp_wejścia_albumu',
        'report_album_lufs': 'lufs_wejścia_albumu',
        'report_destination': 'cel',
        'report_detail': 'szczegóły',
        'report_error': 'OSTRZEŻENIE — nie można utworzyć raportu CSV: {error}',
        'report_filename_prefix': 'LUFScale_Report',
        'report_gain': 'wzmocnienie_db',
        'report_input_dbtp': 'dbtp_wejścia',
        'report_input_lufs': 'lufs_wejścia',
        'report_log': 'Raport CSV — {path}',
        'report_mode': 'tryb',
        'report_operation': 'operacja',
        'report_output_dbtp': 'dbtp_wyjścia',
        'report_output_lufs': 'lufs_wyjścia',
        'report_path': 'Raport: {path}',
        'report_qc': 'kontrola_jakości',
        'report_seconds': 'czas_sekundy',
        'report_source': 'źródło',
        'report_status': 'status',
        'report_tooltip': 'Tworzy w folderze docelowym szczegółowy raport z pomiarami, czasami i '
                          'ostrzeżeniami.',
        'resume': 'Wznów po przerwaniu',
        'resume_not_saved': ' Nie zapisano punktu wznowienia: {error}',
        'resume_processing': 'Wznów',
        'resume_tooltip': 'Pliki ukończone wcześniej z tymi samymi ustawieniami są rozpoznawane i '
                          'nie są przetwarzane ponownie.',
        'resumed_progress': 'Wznowiono: {file}',
        'scan_error': 'BŁĄD — {error}',
        'settings': 'Ustawienia',
        'show_finder': 'Pokaż w Finderze',
        'show_option_help': 'Pokaż pomoc: {option}',
        'silent_album_copy': 'Skopiowano cichy lub niemierzalny album.',
        'silent_copy': 'Skopiowano cichy lub niemierzalny dźwięk.',
        'silent_copy_no_replaygain': 'Skopiowano cichy dźwięk bez znaczników ReplayGain.',
        'silent_unmeasurable': 'Cichy lub niemierzalny dźwięk.',
        'simulation': 'Symulacja',
        'skip_compliant': 'Nie koduj ponownie plików już zgodnych',
        'skip_compliant_tooltip': 'Opcja domyślnie włączona. Po analizie plik mieszczący się w '
                                  '±0,5 LU od celu i nieprzekraczający limitu true peak jest '
                                  'kopiowany bez zmian i ponownego kodowania. W trybie Album '
                                  'głośność ocenia się dla całego albumu. Jakość i rozmiar '
                                  'pozostają identyczne; dziennik to wskazuje.',
        'skipped_progress': 'Pominięto: {file}',
        'source_audio_count': 'Pliki audio do przetworzenia: {count}',
        'source_list_more': '… zachowano jeszcze {count} źródeł',
        'source_safety': 'Pliki źródłowe nigdy nie są przenoszone ani modyfikowane.',
        'source_selection_tooltip': 'Wybór wielu pozycji: Command-klik dla oddzielnych elementów, '
                                    'Shift-klik dla zakresu.',
        'start': 'Uruchom',
        'status_analyzed': 'PRZEANALIZOWANO',
        'status_cancelled': 'ANULOWANO',
        'status_error': 'BŁĄD',
        'status_ok': 'OK',
        'status_resumed': 'WZNOWIONO',
        'status_skipped': 'POMINIĘTO',
        'switch_to_dark': 'Tryb ciemny',
        'switch_to_light': 'Tryb jasny',
        'tagline': 'Ujednolica odczuwaną głośność dźwięku',
        'target': 'Docelowa głośność',
        'target_tooltip': 'Cel głośności to zamierzona głośność zintegrowana całego utworu, '
                          'wyrażona w LUFS. Mniej ujemna wartość daje głośniejszy plik: -14 LUFS '
                          'jest głośniejsze niż -16 LUFS. Różnica 2 LU odpowiada w przybliżeniu 2 '
                          'dB różnicy poziomu przed ewentualnym ograniczaniem szczytów.\n'
                          '\n'
                          'Wskazówki: -18 LUFS dla spokojniejszego i bardziej dynamicznego wyniku; '
                          '-16 LUFS dla ogólnej równowagi; -14 LUFS dla głośniejszego wyniku w '
                          'stylu streamingu. Platformy mogą następnie stosować własną normalizację '
                          'odtwarzania.\n'
                          '\n'
                          'Sam cel nie spłaszcza dynamiki wewnątrz utworu. Jeśli maksymalny true '
                          'peak uniemożliwia osiągnięcie celu bez przesterowania, wynik może '
                          'pozostać nieco niższy.',
        'theme_accessible': 'Zmień wygląd aplikacji. Wybór zostanie zapamiętany.',
        'total_time': 'Czas całkowity: {duration}',
        'track_mode_log': 'Tryb Utwór — każdy plik audio jest przetwarzany osobno.',
        'track_two_pass': 'Dwuprzebiegowa normalizacja utworu.',
        'true_peak_meter_exceeded': 'Przekroczenie {margin} dB',
        'true_peak_meter_margin': 'Margines {margin} dB',
        'true_peak_meter_title': 'Margines szczytu',
        'true_peak_meter_tooltip': 'Porównuje true peak ostatniego wyniku z wybranym limitem. '
                                   'Znacznik pokazuje ostatnią wartość, a trójkąt zachowuje '
                                   'najwyższy szczyt serii. Zielony: limit spełniony; '
                                   'pomarańczowy: do 0,25 dB ponad limit; czerwony: więcej. '
                                   'Pomarańczowa tolerancja należy do kontroli jakości LUFScale, '
                                   'nie jest normą dostawy. Resetuje się dla każdej serii.',
        'true_peak_meter_waiting': 'Oczekiwanie na pomiar dBTP',
        'version_changes': '• Łączna liczba plików audio aktualizuje się po dodaniu lub usunięciu '
                           'źródeł.\n'
                           '• Miernik odzyskał wymiary i odstęp z wersji 1.21.25 i pozostaje '
                           'nieaktywny bez kontroli jakości.\n'
                           '• Oszacowanie pokazuje też przybliżoną godzinę zakończenia.\n'
                           '• Usunięto dawne wewnętrzne narzędzia testowe.',
        'version_changes_title': 'Nowości w wersji {version}',
        'version_label': 'Wersja {version}',
        'volume': 'Głośność',
        'volume_loud': 'Głośno: -14 LUFS',
        'volume_normal': 'Normalnie: -16 LUFS',
        'volume_soft': 'Cicho: -18 LUFS',
        'volume_tooltip': 'To ustawienie jest skrótem do celu głośności; nie zmienia głośności '
                          'odtwarzania na Macu.\n'
                          '\n'
                          '• Cicho: -18 LUFS — spokojniejszy poziom, większy zapas dynamiki i '
                          'mniejsze ryzyko działania limitera.\n'
                          '• Normalnie: -16 LUFS — zrównoważony kompromis i dobry punkt wyjścia '
                          'dla osobistej biblioteki.\n'
                          '• Głośno: -14 LUFS — bardziej wyraziste odtwarzanie, zbliżone do celu '
                          'Normal w Spotify, lecz częściej wymagające ograniczania.\n'
                          '• Niestandardowo — pozwala bezpośrednio wprowadzić inny cel LUFS.\n'
                          '\n'
                          'Są to praktyczne wybory, a nie uniwersalna norma.',
        'zero_album_gain': 'Zerowe wzmocnienie albumu; dźwięk skopiowano.'},
 'pt': {'activity_cancelled': 'Atividade: processamento cancelado',
        'activity_cancelling': 'Atividade: a cancelar…',
        'activity_completed': 'Atividade: processamento concluído',
        'activity_compliant': 'Conformes: {count}',
        'activity_detected': 'Atividade: {total} ficheiro(s) detetado(s)',
        'activity_errors': 'Erros: {count}',
        'activity_files': 'Ficheiros: {count}',
        'activity_idle': 'Atividade: em espera',
        'activity_preparing': 'Atividade: a preparar ficheiros…',
        'activity_progress': '{total} ficheiros • concluídos {success} • alertas {warnings} • '
                             'erros {failed} • retomados/ignorados {skipped} • conformes '
                             '{compliant}',
        'activity_skipped': 'Retomados/ignorados: {count}',
        'activity_successes': 'Concluídos: {count}',
        'activity_warnings': 'Alertas: {count}',
        'adaptive_disabled_log': 'Análise adaptativa — sondas rápidas paradas após {sample} '
                                 'medições ({successes} sucessos, poupança estimada '
                                 '{percent:+.1f}%).',
        'add_folders': 'Adicionar pastas…',
        'add_mp3': 'Adicionar ficheiros de áudio…',
        'add_replaygain': 'Adicionar ReplayGain',
        'add_source_files': 'Adicionar ficheiros de áudio',
        'add_source_folder': 'Adicionar uma pasta de origem',
        'album_gain_detail': 'Ganho comum do álbum {gain:+.2f} dB.',
        'album_gain_log': 'Álbum «{album}» — ganho comum {gain:+.2f} dB.',
        'album_measurement_error': 'Falha na medição do álbum: {error}',
        'album_mode_log': 'Modo Álbum — cada pasta com ficheiros de áudio forma um álbum.',
        'albums_measurement': 'A medir {count} álbum(ns)…',
        'already_completed': 'Já concluído durante uma execução anterior.',
        'already_compliant_badge': 'CONFORME',
        'already_compliant_copy': 'Já conforme: cópia idêntica sem recodificação de áudio.',
        'already_compliant_log': 'já conforme, sem recodificação',
        'analysis_cache_summary': 'Cache de análise — {hits} medição(ões) reutilizada(s).',
        'analysis_impossible': 'Falha na análise: {error}',
        'analysis_method': 'Método de análise',
        'analysis_method_adaptive': 'Adaptativo — para se não compensar',
        'analysis_method_fast': 'Rápido — experimental',
        'analysis_method_historical': 'Histórico — referência',
        'analysis_method_log': 'Método de análise — {method}.',
        'analysis_method_tooltip': 'Histórico utiliza apenas a medição completa de referência '
                                   'validada na 1.22.13. Rápido testa a sonda linear em cada '
                                   'ficheiro e regressa à medição histórica quando necessário. '
                                   'Adaptativo começa como Rápido; após pelo menos 12 medições e 3 '
                                   'regressos, compara os tempos observados e desativa as sondas '
                                   'se a poupança estimada ficar abaixo de 5%. A qualidade final e '
                                   'o controlo de qualidade não são reduzidos.',
        'analysis_progress': 'Análise {current}/{total}: {file}',
        'analyze': 'Analisar',
        'analyze_operation': 'análise/simulação',
        'analyzed_progress': 'Analisado: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Fluxo de áudio copiado sem recodificação; etiquetas ReplayGain '
                                 'adicionadas.',
        'audio_tab': 'Áudio',
        'auto_start': 'Iniciar automaticamente após arrastar ou colar',
        'auto_start_tooltip': 'Inicia automaticamente o processamento após adicionar origens por '
                              'arrastar e largar ou colar, se já tiver sido escolhido um destino.',
        'cancel': 'Cancelar',
        'cancelled_summary': 'Cancelado — {success} concluído(s), {failed} erro(s), {skipped} '
                             'retomado(s)/ignorado(s), {warnings} aviso(s), {compliant} '
                             'conforme(s) — {duration}.',
        'cancelling': 'A cancelar…',
        'choose': 'Escolher…',
        'choose_output': 'Escolher a pasta de destino',
        'clipboard': 'Área de transferência',
        'clipboard_empty': 'A área de transferência não contém um caminho válido de pasta ou '
                           'ficheiro de áudio compatível.',
        'close_question': 'Cancelar o processamento e fechar a aplicação?',
        'completed_dialog_summary': 'Estado: concluído\n'
                                    'Ficheiros: {files}\n'
                                    'Concluídos: {success}\n'
                                    'Erros: {failed}\n'
                                    'Retomados ou ignorados: {skipped}\n'
                                    'Avisos: {warnings}\n'
                                    'Conformes: {compliant}\n'
                                    'Tempo total: {duration}',
        'completed_summary': 'Concluído — {success} concluído(s), {failed} erro(s), {skipped} '
                             'retomado(s)/ignorado(s), {warnings} aviso(s), {compliant} '
                             'conforme(s) — {duration}.',
        'completed_with_errors': 'Processamento concluído com avisos',
        'convert': 'Normalizar',
        'convert_operation': 'uniformização de áudio',
        'cpu_tooltip': 'Utilização total do processador do Mac, atualizada a cada segundo durante '
                       'o processamento.',
        'cpu_unavailable': 'N/D',
        'cpu_usage': 'CPU',
        'create_report': 'Criar um relatório CSV',
        'custom': 'Personalizado',
        'decrease_value': 'Diminuir o valor',
        'description': 'Uniformiza o volume percebido no modo Faixa ou Álbum sem alterar os '
                       'ficheiros originais.',
        'destination': 'Destino',
        'destination_error': 'ERRO — destino indisponível: {error}',
        'destination_path_tooltip': 'Clique no caminho e use as setas, Início/Fim ou a roda. O '
                                    'caminho pode ser selecionado e copiado, mas não alterado.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — subpastas incluídas',
        'drop_title': 'Largue aqui pastas ou ficheiros de áudio',
        'elapsed_time': 'Tempo decorrido: {duration}',
        'error_progress': 'Erro: {file}',
        'estimated_result': 'Resultado estimado; nenhum ficheiro criado.',
        'estimated_total_calculating': 'Tempo total estimado: a calcular…',
        'estimated_total_time': 'Tempo total estimado: {duration}',
        'estimated_total_time_with_finish': 'Tempo total estimado: {duration} — fim por volta das '
                                            '{time}',
        'estimated_total_unavailable': 'Tempo total estimado: indisponível',
        'ffmpeg_download_button': 'Abrir o site oficial do FFmpeg',
        'ffmpeg_error_no_detail': 'Erro do FFmpeg sem detalhes.',
        'ffmpeg_execution_error': 'Não foi possível executar o FFmpeg: {error}',
        'ffmpeg_incompatible': 'FFmpeg incompatível',
        'ffmpeg_missing': 'FFmpeg não encontrado',
        'ffmpeg_missing_encoders': 'Esta versão do FFmpeg não inclui todos os codificadores de '
                                   'áudio necessários: {encoders}.',
        'ffmpeg_missing_message': 'O FFmpeg deve estar instalado e disponível no PATH ou colocado '
                                  'junto ao programa.',
        'ffmpeg_no_lame': 'Esta versão do FFmpeg não inclui o codificador MP3 libmp3lame.',
        'ffmpeg_no_loudnorm': 'Esta versão do FFmpeg não inclui o filtro loudnorm.',
        'ffmpeg_not_responding': 'O FFmpeg não está a responder corretamente.',
        'file_exists': 'O ficheiro já existe.',
        'files_found': '{total} ficheiro(s) de áudio encontrado(s) — {operation} — {parallel} '
                       'processo(s) paralelo(s).',
        'folder': 'Pasta',
        'folder_unavailable': 'Pasta indisponível',
        'guide_help_tooltip': 'Abre o guia PDF completo no idioma selecionado.',
        'guide_missing_message': 'O guia PDF não foi encontrado: {path}',
        'guide_missing_title': 'Guia indisponível',
        'guide_open_error': 'O macOS não conseguiu abrir o guia PDF: {path}',
        'help_button': 'Ajuda',
        'help_overview': '• Normalização real, ReplayGain ou análise sem criar MP3.\n'
                         '• Modos Faixa e Álbum com preservação das diferenças entre faixas.\n'
                         '• Estrutura de pastas, metadados e capas preservados quando o FFmpeg os '
                         'consegue copiar.\n'
                         '• Os originais nunca são movidos nem modificados.\n'
                         '• Paralelismo Auto, cache de análise e retoma após interrupção.\n'
                         '• Controlo de qualidade, relatório CSV, progresso, CPU, medidor de '
                         'sonoridade e duração total estimada.\n'
                         '• Interface disponível em doze idiomas e guias PDF em doze idiomas.',
        'help_title': 'Principais funcionalidades',
        'increase_value': 'Aumentar o valor',
        'interface_ffmpeg_message': 'A interface está disponível, mas a conversão requer o FFmpeg. '
                                    'Instale o FFmpeg e reinicie a aplicação.',
        'internal_error': 'Erro interno: {error}',
        'interrupted': 'Processamento interrompido.',
        'invalid_location': 'Localização inválida',
        'language': 'Idioma',
        'language_tooltip': 'Altera imediatamente o idioma da interface, das mensagens e dos '
                            'futuros relatórios CSV. A escolha fica memorizada.',
        'level_mode': 'Modo de sonoridade',
        'log_help_text': 'Cada linha corresponde a um ficheiro ou a uma etapa geral.\n'
                         '\n'
                         '• Início: estado do processamento (OK, ALERTA, ERRO, retomado ou '
                         'ignorado).\n'
                         '• Depois: nome do MP3 e tempo dedicado ao ficheiro.\n'
                         '• Cartucho LUFS: nível medido antes → nível obtido após o '
                         'processamento.\n'
                         '• Fim: resultado do controlo de qualidade e eventual detalhe.\n'
                         '\n'
                         'Cores: verde = sucesso; laranja = alerta; vermelho = ficheiro não '
                         'terminado; violeta azulado = retoma; cinzento = informação, item '
                         'ignorado ou cancelamento.\n'
                         '\n'
                         'Os tempos acumulados somam o trabalho de todas as tarefas paralelas. O '
                         'tempo total é a duração real decorrida.\n'
                         '\n'
                         'QC ALERTA — pico significa que o true peak medido novamente na saída '
                         'ultrapassa em mais de 0,25 dB o limite escolhido. O ficheiro é criado na '
                         'mesma: não se trata de um erro de conversão. No entanto, não cumpre '
                         'rigorosamente o teto pedido e deixa menos margem para uma nova '
                         'codificação ou para certos conversores. Quanto mais o valor dBTP se '
                         'aproxima de 0, maior é o risco de picos entre amostras. Para corrigir um '
                         'alerta persistente, escolha um alvo LUFS mais baixo ou um pico máximo '
                         'mais prudente, por exemplo −2,0 dBTP, e processe novamente o ficheiro.',
        'log_placeholder': 'O relatório do processamento será apresentado aqui.',
        'log_title': 'Registo de processamento',
        'loudness_meter_estimated': 'Estimado',
        'loudness_meter_help_text': 'Este medidor verifica visualmente a regularidade da '
                                    'normalização. Compara o último ficheiro de áudio com o alvo e '
                                    'calcula continuamente o mínimo e o máximo dos últimos 100 '
                                    'ficheiros. Os valores antigos saem progressivamente desta '
                                    'janela, mantendo os lotes grandes dinâmicos. A pontuação do '
                                    'alvo continua a abranger todo o lote e o indicador não altera '
                                    'definições.',
        'loudness_meter_maximum': 'Máx {value}',
        'loudness_meter_measured': 'Medido',
        'loudness_meter_minimum': 'Mín {value}',
        'loudness_meter_target': 'Alvo {value} LUFS',
        'loudness_meter_title': 'Medidor de sonoridade',
        'loudness_meter_tooltip': 'A linha vermelha representa o alvo. O valor azul à esquerda '
                                  'acompanha o último ficheiro de áudio. As linhas e os valores '
                                  'cinzento e violeta escuro mostram à direita o mínimo e o máximo '
                                  'dos últimos 100 ficheiros. A escala amplia pequenas diferenças '
                                  'e o medidor é reiniciado em cada novo lote.',
        'loudness_meter_waiting': 'À espera de um ficheiro de áudio',
        'loudness_score_acceptable': 'Aceitável',
        'loudness_score_check': 'Verificar',
        'loudness_score_excellent': 'Excelente',
        'loudness_score_good': 'Boa',
        'loudness_score_needs_qc': 'Pontuação do alvo: ative o controlo de qualidade',
        'loudness_score_not_applicable': 'Pontuação do alvo: não aplicável',
        'loudness_score_tooltip': 'A pontuação utiliza apenas saídas que foram efetivamente '
                                  'medidas de novo. Baseia-se no erro quadrático médio entre a '
                                  'sonoridade obtida e a esperada: 100 = resultado exato, 50 = '
                                  'erro global de 0,5 LU, a tolerância do controlo de qualidade, e '
                                  '0 = erro de 1 LU ou mais. No modo Álbum, o valor esperado de '
                                  'cada faixa inclui o ganho comum para preservar as diferenças '
                                  'pretendidas. O erro RMS (raiz quadrada da média dos desvios ao '
                                  'quadrado) resume a distância global entre as sonoridades '
                                  'obtidas e os respetivos alvos. Quanto mais próximo estiver de 0 '
                                  'LU, mais preciso é o lote.',
        'loudness_score_value': 'Pontuação do alvo: {score}/100\n'
                                '{rating}\n'
                                'Erro RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Pontuação do alvo: em espera',
        'measurement_unavailable': 'Medição indisponível.',
        'mode_album': 'Álbum — preserva as diferenças entre faixas',
        'mode_album_label': 'Álbum',
        'mode_tooltip': 'Faixa ajusta cada MP3 separadamente. Álbum calcula um ganho comum por '
                        'pasta para preservar as diferenças de volume entre as faixas.',
        'mode_track': 'Faixa — mesmo nível para cada ficheiro',
        'mode_track_label': 'Faixa',
        'mp3': 'MP3',
        'mp3_filter': 'Áudio compatível (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Nenhuma pasta selecionada',
        'no_mp3': 'Nenhum ficheiro de áudio compatível encontrado.',
        'no_new_source': 'Não foi adicionada nenhuma pasta ou ficheiro de áudio compatível.',
        'not_performed': 'Não efetuado',
        'open_output_error': 'Não foi possível abrir a pasta de destino: {error}',
        'operation': 'Operação',
        'operation_analyze': 'Apenas analisar — simulação sem criar ficheiros',
        'operation_analyze_label': 'Apenas análise',
        'operation_convert': 'Uniformizar — normalizar realmente o áudio',
        'operation_convert_label': 'Uniformização de áudio',
        'operation_replaygain': 'ReplayGain — sem recodificação de áudio',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Uniformizar processa realmente o áudio. MP3, M4A/AAC, OGG e Opus têm '
                             'de ser recodificados; o tamanho depende da qualidade e pode '
                             'aumentar. FLAC é recodificado sem perdas, mas a compressão pode '
                             'variar porque as amostras mudam. WAV e AIFF conservam frequência, '
                             'canais e profundidade compatíveis com a origem. ReplayGain não '
                             'recodifica; Analisar não cria ficheiros.',
        'options_tab': 'Opções',
        'overwrite': 'Substituir ficheiros existentes',
        'overwrite_tooltip': 'Permite substituir um MP3 já existente no destino. Os ficheiros de '
                             'origem nunca são substituídos.',
        'parallel': 'Processos paralelos',
        'parallel_adjusted': 'Paralelismo automático — {active} processo(s), CPU {cpu:.0f} %.',
        'parallel_auto': 'Auto',
        'parallel_auto_log': 'automático, máximo {maximum}',
        'parallel_tooltip': 'Determina quantos ficheiros podem ser processados simultaneamente.\n'
                            '\n'
                            '• Auto começa com no máximo 4 tarefas. Quando a medição da CPU está '
                            'disponível, verifica-a a cada segundo: adiciona uma tarefa abaixo de '
                            '70% de utilização e retira uma acima de 92%.\n'
                            '• Auto nunca excede o número de processadores lógicos detetados e tem '
                            'um limite absoluto de 16 tarefas.\n'
                            '• Se a medição da CPU não estiver disponível, Auto utiliza '
                            'diretamente esse limite detetado, sem adaptação dinâmica.\n'
                            '• Um valor numérico fixa o número máximo de tarefas simultâneas; não '
                            'é um objetivo de utilização da CPU.\n'
                            '\n'
                            'Mais tarefas podem acelerar um lote grande, mas aumentam a carga, a '
                            'temperatura e a atividade do disco. Prima − até aparecer Auto.',
        'paste': 'Colar',
        'path_left': 'Mostrar a parte esquerda do caminho',
        'path_right': 'Mostrar a parte direita do caminho',
        'pause': 'Pausa',
        'peak': 'Pico real máximo',
        'peak_tooltip': 'O pico verdadeiro máximo é um limite, não um nível a atingir. Limita em '
                        'dBTP os picos mais altos da forma de onda reconstruída, incluindo os que '
                        'surgem entre amostras, para reduzir a saturação após codificação ou '
                        'transcodificação.\n'
                        '\n'
                        '• -1,0 dBTP — limite de entrega comum, com o pico de saída mais alto.\n'
                        '• -1,5 dBTP — valor predefinido e compromisso prudente para MP3.\n'
                        '• -2,0 dBTP — margem adicional, útil se o ficheiro puder ser novamente '
                        'codificado ou com um alvo de sonoridade alto.\n'
                        '• 0 dBTP — sem margem; não recomendado para MP3.\n'
                        '\n'
                        'Um valor mais negativo é mais seguro, mas pode impedir faixas muito '
                        'dinâmicas de atingirem exatamente o alvo LUFS.',
        'phase_summary': 'Distribuição estimada do tempo total — análise {analysis}, conversão '
                         '{conversion}, controlo de qualidade {quality}.',
        'pipeline_enabled': 'Pipeline de Faixa — cada conversão começa assim que a análise '
                            'termina.',
        'pre_measurement': 'A medir os ficheiros de entrada…',
        'preset': 'Predefinição',
        'preset_dynamic': 'Música dinâmica',
        'preset_library': 'Biblioteca musical — recomendado',
        'preset_streaming': 'Streaming mais presente',
        'preset_tooltip': 'Aplica de uma vez um alvo de sonoridade, um pico real máximo e uma '
                          'qualidade MP3 coerentes. Qualquer alteração manual seleciona '
                          'Personalizado.',
        'processing_cancelled': 'Processamento cancelado.',
        'processing_completed': 'Processamento concluído',
        'processing_in_progress': 'Processamento em curso',
        'processing_paused': 'Processamento em pausa.',
        'processing_resumed': 'Processamento retomado.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'AVISO — não foi possível efetuar o controlo de qualidade: {error}',
        'qc_log': ' — CQ {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'AVISO — {detail}',
        'quality': 'Qualidade de áudio',
        'quality_control': 'Controlo de qualidade automático',
        'quality_control_tooltip': 'Volta a medir cada saída. Nos MP3 do caminho dinâmico, a '
                                   'medição pode iniciar até três recodificações corretivas. '
                                   'Desativar não muda a qualidade do codificador, mas remove a '
                                   'verificação final, as correções e a atividade do medidor.',
        'quality_tooltip': 'Controla qualidade e tamanho dos formatos comprimidos: um número baixo '
                           'usa maior qualidade e débito. Se o débito escolhido exceder o '
                           'original, o ficheiro cresce. Um número alto costuma reduzi-lo, mas o '
                           'VBR não garante os mesmos bytes. FLAC permanece sem perdas; WAV e AIFF '
                           'ignoram esta definição e conservam as propriedades PCM. Intervalos: 0 '
                           '= qualidade máxima; 1-2 = muito alta; 3-4 = equilíbrio; 5-9 = tamanho '
                           'menor.',
        'ready': 'Pronto',
        'recursive_scan': 'A analisar pastas recursivamente…',
        'remove_all': 'Remover tudo',
        'remove_selection': 'Remover seleção',
        'replaygain_operation': 'ReplayGain sem recodificação',
        'replaygain_tags_missing': 'As etiquetas ReplayGain não foram encontradas.',
        'report_album_dbtp': 'dbtp_entrada_album',
        'report_album_lufs': 'lufs_entrada_album',
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
        'report_seconds': 'tempo_segundos',
        'report_source': 'origem',
        'report_status': 'estado',
        'report_tooltip': 'Cria no destino um relatório detalhado com medições, durações e avisos.',
        'resume': 'Retomar após uma interrupção',
        'resume_not_saved': ' Ponto de retoma não guardado: {error}',
        'resume_processing': 'Retomar',
        'resume_tooltip': 'Os ficheiros já concluídos com as mesmas definições são reconhecidos e '
                          'não são processados novamente.',
        'resumed_progress': 'Retomado: {file}',
        'scan_error': 'ERRO — {error}',
        'scanning_folders': 'A analisar pastas…',
        'settings': 'Definições',
        'show_finder': 'Mostrar no Finder',
        'show_option_help': 'Mostrar ajuda: {option}',
        'silent_album_copy': 'Álbum silencioso ou não mensurável copiado.',
        'silent_copy': 'Áudio silencioso ou não mensurável copiado.',
        'silent_copy_no_replaygain': 'Áudio silencioso copiado sem etiquetas ReplayGain.',
        'silent_unmeasurable': 'Áudio silencioso ou não mensurável.',
        'simulation': 'Simulação',
        'skip_compliant': 'Não recodificar ficheiros já conformes',
        'skip_compliant_tooltip': 'Ativada por predefinição. Após a análise, um ficheiro a ±0,5 LU '
                                  'do alvo e cujo true peak não ultrapassa o limite é copiado sem '
                                  'alteração nem recodificação. No modo Álbum, a sonoridade é '
                                  'avaliada para o álbum inteiro. A qualidade e o tamanho ficam '
                                  'exatamente preservados; o registo indica-o.',
        'skipped_progress': 'Ignorado: {file}',
        'source_audio_count': 'Ficheiros de áudio a processar: {count}',
        'source_list_more': '… mais {count} fontes mantidas',
        'source_safety': 'Os ficheiros de origem nunca são movidos nem alterados.',
        'source_selection_tooltip': 'Seleção múltipla: ⌘ clique para itens separados e Shift '
                                    'clique para um intervalo.',
        'sources_added': '{count} origem(ns) adicionada(s).',
        'start': 'Iniciar',
        'status_analyzed': 'ANALISADO',
        'status_cancelled': 'CANCELADO',
        'status_error': 'ERRO',
        'status_ok': 'OK',
        'status_resumed': 'RETOMADO',
        'status_skipped': 'IGNORADO',
        'switch_to_dark': 'Modo escuro',
        'switch_to_light': 'Modo claro',
        'tagline': 'Uniformiza o volume de áudio percecionado',
        'target': 'Alvo de sonoridade',
        'target_tooltip': 'O alvo de sonoridade é a sonoridade integrada pretendida para toda a '
                          'faixa, expressa em LUFS. Um valor menos negativo produz um ficheiro '
                          'mais alto: -14 LUFS é mais alto do que -16 LUFS. Uma diferença de 2 LU '
                          'corresponde aproximadamente a 2 dB de nível antes de eventual limitação '
                          'de pico.\n'
                          '\n'
                          'Referências: -18 LUFS para um resultado mais calmo e dinâmico; -16 LUFS '
                          'para equilíbrio geral; -14 LUFS para um resultado mais alto de tipo '
                          'streaming. As plataformas podem depois aplicar a sua própria '
                          'normalização de reprodução.\n'
                          '\n'
                          'Este alvo não achata por si só a dinâmica interna da faixa. Se o pico '
                          'verdadeiro máximo impedir que o alvo seja atingido sem saturação, o '
                          'resultado pode ficar ligeiramente mais baixo.',
        'theme_accessible': 'Alterar o aspeto da aplicação. A escolha fica memorizada.',
        'total_time': 'Tempo total: {duration}',
        'track_mode_log': 'Modo Faixa — cada ficheiro de áudio é tratado separadamente.',
        'track_two_pass': 'Normalização de faixa em duas passagens.',
        'true_peak_meter_exceeded': 'Excesso {margin} dB',
        'true_peak_meter_margin': 'Margem {margin} dB',
        'true_peak_meter_title': 'Margem de pico',
        'true_peak_meter_tooltip': 'Compara o true peak da última saída com o limite escolhido. O '
                                   'marcador mostra o último valor e o triângulo conserva o pico '
                                   'mais alto do lote. Verde: limite respeitado; laranja: excesso '
                                   'até 0,25 dB; vermelho: excesso maior. A tolerância laranja '
                                   'pertence ao controlo de qualidade LUFScale e não é uma norma '
                                   'de entrega. Reinicia em cada lote.',
        'true_peak_meter_waiting': 'A aguardar uma medição dBTP',
        'version_changes': '• O total de ficheiros de áudio atualiza-se ao adicionar ou retirar '
                           'fontes.\n'
                           '• O medidor recupera as dimensões e a separação da versão 1.21.25 e '
                           'fica inativo sem controlo de qualidade.\n'
                           '• A estimativa mostra também a hora aproximada de conclusão.\n'
                           '• As antigas ferramentas internas de teste foram removidas.',
        'version_changes_title': 'Novidades da versão {version}',
        'version_label': 'Versão {version}',
        'volume': 'Volume',
        'volume_loud': 'Forte: -14 LUFS',
        'volume_normal': 'Normal: -16 LUFS',
        'volume_soft': 'Suave: -18 LUFS',
        'volume_tooltip': 'Esta definição é um atalho para o alvo de sonoridade; não altera o '
                          'volume de audição do Mac.\n'
                          '\n'
                          '• Suave: -18 LUFS — nível mais calmo, maior margem dinâmica e menor '
                          'probabilidade de acionar o limitador.\n'
                          '• Normal: -16 LUFS — compromisso equilibrado e bom ponto de partida '
                          'para uma biblioteca pessoal.\n'
                          '• Forte: -14 LUFS — reprodução mais presente, próxima do alvo Normal do '
                          'Spotify, mas com maior probabilidade de exigir limitação.\n'
                          '• Personalizado — permite introduzir diretamente outro alvo LUFS.\n'
                          '\n'
                          'São escolhas práticas, não uma norma universal.',
        'zero_album_gain': 'Ganho do álbum nulo; áudio copiado.'},
 'ru': {'activity_cancelled': 'Активность: обработка отменена',
        'activity_cancelling': 'Активность: отмена…',
        'activity_completed': 'Активность: обработка завершена',
        'activity_compliant': 'Соответствует: {count}',
        'activity_detected': 'Активность: обнаружено файлов: {total}',
        'activity_errors': 'Ошибки: {count}',
        'activity_files': 'Файлы: {count}',
        'activity_idle': 'Активность: ожидание',
        'activity_preparing': 'Активность: подготовка файлов…',
        'activity_progress': '{total} файлов • успешно {success} • предупреждения {warnings} • '
                             'ошибки {failed} • возобновлено/пропущено {skipped} • соответствует '
                             '{compliant}',
        'activity_skipped': 'Возобн./пропущ.: {count}',
        'activity_successes': 'Успешно: {count}',
        'activity_warnings': 'Предупреждения: {count}',
        'adaptive_disabled_log': 'Адаптивный анализ — быстрые пробы остановлены после {sample} '
                                 'замеров ({successes} успешных, расчётная экономия '
                                 '{percent:+.1f}%).',
        'add_folders': 'Добавить папки…',
        'add_mp3': 'Добавить аудиофайлы…',
        'add_replaygain': 'Добавить ReplayGain',
        'add_source_files': 'Добавить аудиофайлы',
        'album_gain_detail': 'Общее усиление альбома {gain:+.2f} дБ.',
        'album_gain_log': 'Альбом «{album}» — общее усиление {gain:+.2f} дБ.',
        'album_measurement_error': 'Не удалось измерить альбом: {error}',
        'album_mode_log': 'Режим «Альбом» — каждая папка с аудиофайлами образует альбом.',
        'albums_measurement': 'Измерение альбомов: {count}…',
        'already_completed': 'Уже завершено во время предыдущего запуска.',
        'already_compliant_badge': 'СООТВЕТСТВУЕТ',
        'already_compliant_copy': 'Уже соответствует: скопирован без изменений и перекодирования '
                                  'аудио.',
        'already_compliant_log': 'уже соответствует, без перекодирования',
        'analysis_cache_summary': 'Кэш анализа — повторно использовано измерений: {hits}.',
        'analysis_impossible': 'Ошибка анализа: {error}',
        'analysis_method': 'Метод анализа',
        'analysis_method_adaptive': 'Адаптивный — остановка без выгоды',
        'analysis_method_fast': 'Быстрый — экспериментальный',
        'analysis_method_historical': 'Исторический — эталон',
        'analysis_method_log': 'Метод анализа — {method}.',
        'analysis_method_tooltip': 'Исторический использует только полный эталонный замер, '
                                   'проверенный в 1.22.13. Быстрый проверяет линейную пробу для '
                                   'каждого файла и при необходимости возвращается к историческому '
                                   'замеру. Адаптивный начинает как Быстрый; после как минимум 12 '
                                   'замеров и 3 возвратов он сравнивает фактическое время и '
                                   'отключает пробы, если расчётная экономия остаётся ниже 5%. '
                                   'Итоговое качество и контроль качества не упрощаются.',
        'analysis_progress': 'Анализ {current}/{total}: {file}',
        'analyze': 'Анализировать',
        'analyzed_progress': 'Проанализировано: {file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': 'Аудиопоток скопирован без перекодирования; добавлены теги '
                                 'ReplayGain.',
        'audio_tab': 'Аудио',
        'auto_start': 'Запускать после перетаскивания или вставки',
        'auto_start_tooltip': 'Автоматически запускает обработку после перетаскивания или вставки, '
                              'если папка назначения уже выбрана.',
        'cancel': 'Отмена',
        'cancelled_summary': 'Отменено — успешно {success}, ошибок {failed}, '
                             'возобновлено/пропущено {skipped}, предупреждений {warnings}, '
                             'соответствует {compliant} — {duration}.',
        'choose': 'Выбрать…',
        'clipboard_empty': 'Буфер обмена не содержит допустимого пути к папке или поддерживаемому '
                           'аудиофайлу.',
        'completed_dialog_summary': 'Состояние: завершено\n'
                                    'Файлы: {files}\n'
                                    'Успешно: {success}\n'
                                    'Ошибки: {failed}\n'
                                    'Возобновлено или пропущено: {skipped}\n'
                                    'Предупреждения: {warnings}\n'
                                    'Соответствует: {compliant}\n'
                                    'Общее время: {duration}',
        'completed_summary': 'Завершено — успешно {success}, ошибок {failed}, '
                             'возобновлено/пропущено {skipped}, предупреждений {warnings}, '
                             'соответствует {compliant} — {duration}.',
        'convert': 'Нормализовать',
        'convert_operation': 'нормализация аудио',
        'cpu_tooltip': 'Общая загрузка CPU компьютера Mac, обновляемая каждую секунду во время '
                       'обработки.',
        'cpu_usage': 'ЦП',
        'create_report': 'Создать отчёт CSV',
        'custom': 'Пользовательский',
        'description': 'Выравнивает воспринимаемую громкость в режиме «Трек» или «Альбом», не '
                       'изменяя оригиналы.',
        'destination': 'Папка назначения',
        'destination_error': 'ОШИБКА — папка назначения недоступна: {error}',
        'destination_path_tooltip': 'Щёлкните путь и используйте стрелки, Home/End или колесо '
                                    'мыши. Путь можно выделить и скопировать, но нельзя изменить.',
        'drop_subtitle': 'MP3, FLAC, WAV, AIFF, M4A, OGG, Opus — включая вложенные папки',
        'drop_title': 'Перетащите сюда папки или аудиофайлы',
        'elapsed_time': 'Прошло: {duration}',
        'error_progress': 'Ошибка: {file}',
        'estimated_result': 'Расчётный результат; файл не создан.',
        'estimated_total_calculating': 'Общее расчётное время: вычисление…',
        'estimated_total_time': 'Общее расчётное время: {duration}',
        'estimated_total_time_with_finish': 'Общее расчётное время: {duration} — завершение около '
                                            '{time}',
        'estimated_total_unavailable': 'Общее расчётное время: недоступно',
        'ffmpeg_download_button': 'Открыть официальный сайт FFmpeg',
        'ffmpeg_missing_encoders': 'Эта версия FFmpeg не содержит все необходимые аудиокодеры: '
                                   '{encoders}.',
        'file_exists': 'Файл уже существует.',
        'files_found': 'Найдено аудиофайлов: {total} — {operation} — параллельных процессов: '
                       '{parallel}.',
        'guide_help_tooltip': 'Открывает полное PDF-руководство на выбранном языке.',
        'guide_missing_message': 'PDF-руководство не найдено: {path}',
        'guide_missing_title': 'Руководство недоступно',
        'guide_open_error': 'macOS не удалось открыть PDF-руководство: {path}',
        'help_button': 'Справка',
        'help_overview': '• Нормализация, ReplayGain или только анализ.\n'
                         '• Режимы «Трек» и «Альбом».\n'
                         '• Сохранение структуры папок, метаданных и обложек, когда FFmpeg может '
                         'их скопировать.\n'
                         '• Оригиналы никогда не перемещаются и не изменяются.\n'
                         '• Автоматическая параллельность, кэш анализа и возобновление.\n'
                         '• Интерфейс на двенадцати языках и PDF-руководства на десяти.',
        'help_title': 'Основные возможности',
        'internal_error': 'Внутренняя ошибка: {error}',
        'interrupted': 'Обработка прервана.',
        'language_tooltip': 'Сразу меняет язык интерфейса. Выбор сохраняется; непереведённые '
                            'технические сообщения остаются на английском.',
        'level_mode': 'Режим громкости',
        'log_help_text': 'Каждая строка относится к файлу или общему этапу обработки.\n'
                         '\n'
                         '• Начало: состояние обработки (OK, ПРЕДУПРЕЖДЕНИЕ, ОШИБКА, возобновлено '
                         'или пропущено).\n'
                         '• Далее: имя MP3 и время, затраченное на этот файл.\n'
                         '• Поле LUFS: уровень до обработки → уровень после обработки.\n'
                         '• Конец: результат контроля качества и дополнительные сведения.\n'
                         '\n'
                         'Цвета: зелёный = успех; оранжевый = предупреждение; красный = файл не '
                         'завершён; сине-фиолетовый = возобновление; серый = информация, пропуск '
                         'или отмена.\n'
                         '\n'
                         'Накопленные времена суммируют работу всех параллельных задач. Общее '
                         'время — это фактически прошедшая продолжительность.\n'
                         '\n'
                         'QC ПРЕДУПРЕЖДЕНИЕ — пик означает, что повторно измеренный истинный пик '
                         'выходного файла превышает выбранный предел более чем на 0,25 дБ. Файл '
                         'всё равно создаётся: это не ошибка преобразования. Однако он не '
                         'полностью соответствует заданному потолку и оставляет меньше запаса для '
                         'повторного кодирования или некоторых конвертеров. Чем ближе значение '
                         'dBTP к 0, тем выше риск межсемпловых пиков. Чтобы устранить '
                         'повторяющееся предупреждение, выберите более тихую цель LUFS или более '
                         'осторожный максимальный пик, например −2,0 dBTP, и обработайте файл '
                         'снова.',
        'log_placeholder': 'Здесь появится отчёт обработки.',
        'log_title': 'Журнал обработки',
        'loudness_meter_help_text': 'Измеритель позволяет визуально контролировать равномерность '
                                    'нормализации. Он сравнивает последний аудиофайл с целью и '
                                    'постоянно вычисляет минимум и максимум последних 100 файлов. '
                                    'Старые значения постепенно покидают это окно, поэтому большие '
                                    'серии остаются динамичными. Итоговая оценка цели по-прежнему '
                                    'охватывает всю серию, а индикатор не меняет настройки.',
        'loudness_meter_maximum': 'Макс {value}',
        'loudness_meter_minimum': 'Мин {value}',
        'loudness_meter_target': 'Цель {value} LUFS',
        'loudness_meter_title': 'Измеритель громкости',
        'loudness_meter_tooltip': 'Красная линия показывает цель. Синее значение слева относится к '
                                  'последнему аудиофайлу. Серые и тёмно-фиолетовые линии и '
                                  'значения справа показывают минимум и максимум последних 100 '
                                  'файлов. Шкала увеличивает небольшие различия; при каждой новой '
                                  'серии измеритель сбрасывается.',
        'loudness_meter_waiting': 'Ожидание аудиофайла',
        'loudness_score_acceptable': 'Приемлемо',
        'loudness_score_check': 'Проверить',
        'loudness_score_excellent': 'Отлично',
        'loudness_score_good': 'Хорошо',
        'loudness_score_needs_qc': 'Оценка цели: включите контроль качества',
        'loudness_score_not_applicable': 'Оценка цели: неприменимо',
        'loudness_score_tooltip': 'Оценка использует только выходные файлы, которые действительно '
                                  'были измерены повторно. Она основана на среднеквадратичной '
                                  'ошибке между полученной и ожидаемой громкостью: 100 = точный '
                                  'результат, 50 = общая ошибка 0,5 LU, то есть допуск контроля '
                                  'качества, а 0 = ошибка 1 LU или больше. В режиме «Альбом» '
                                  'ожидаемое значение каждой дорожки учитывает общее усиление, '
                                  'чтобы сохранить задуманные различия. Ошибка RMS (квадратный '
                                  'корень из среднего квадратов отклонений) показывает общее '
                                  'расстояние между полученной громкостью и целевыми значениями. '
                                  'Чем она ближе к 0 LU, тем точнее серия.',
        'loudness_score_value': 'Оценка цели: {score}/100\n{rating}\nОшибка RMS: {deviation}\xa0LU',
        'loudness_score_waiting': 'Оценка цели: ожидание',
        'measurement_unavailable': 'Измерение недоступно.',
        'mode_album': 'Альбом — сохраняет различия между треками',
        'mode_tooltip': 'Режим «Трек» регулирует каждый MP3 отдельно. Режим «Альбом» вычисляет '
                        'общее усиление для папки, сохраняя различия громкости между треками.',
        'mode_track': 'Трек — единая громкость файлов',
        'mp3_filter': 'Поддерживаемое аудио (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': 'Папка не выбрана',
        'no_mp3': 'Поддерживаемые аудиофайлы не найдены.',
        'no_new_source': 'Не добавлено ни одной новой папки или поддерживаемого аудиофайла.',
        'not_performed': 'Не выполнено',
        'operation': 'Операция',
        'operation_analyze': 'Только анализ — без создания файла',
        'operation_analyze_label': 'Только анализ',
        'operation_convert': 'Выровнять — нормализовать аудио',
        'operation_convert_label': 'Нормализация аудио',
        'operation_replaygain': 'ReplayGain — без перекодирования',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': 'Выравнивание действительно обрабатывает звук. MP3, M4A/AAC, OGG и '
                             'Opus нужно перекодировать; размер зависит от качества и может '
                             'увеличиться. FLAC перекодируется без потерь, но степень сжатия может '
                             'измениться вместе с отсчётами. WAV и AIFF сохраняют совместимые '
                             'частоту, каналы и разрядность источника. ReplayGain не перекодирует; '
                             'Анализ не создаёт файл.',
        'options_tab': 'Параметры',
        'overwrite': 'Перезаписывать существующие файлы',
        'overwrite_tooltip': 'Разрешает заменить MP3, уже существующий в папке назначения. '
                             'Исходные файлы никогда не перезаписываются.',
        'parallel': 'Параллельные процессы',
        'parallel_adjusted': 'Автоматическая параллельность — процессов: {active}, CPU {cpu:.0f}%.',
        'parallel_auto': 'Авто',
        'parallel_auto_log': 'автоматически, максимум {maximum}',
        'parallel_tooltip': 'Определяет, сколько файлов можно обрабатывать одновременно.\n'
                            '\n'
                            '• «Авто» начинает максимум с 4 задач. Если измерение CPU доступно, '
                            'оно проверяется каждую секунду: ниже 70% добавляется одна задача, '
                            'выше 92% одна задача убирается.\n'
                            '• «Авто» никогда не превышает обнаруженное число логических '
                            'процессоров и имеет абсолютный предел 16 задач.\n'
                            '• Если измерение CPU недоступно, «Авто» сразу использует обнаруженный '
                            'предел без динамической регулировки.\n'
                            '• Числовое значение задаёт максимальное число одновременных задач; '
                            'это не целевая загрузка CPU.\n'
                            '\n'
                            'Большее число задач может ускорить крупную партию, но увеличивает '
                            'нагрузку, нагрев и активность диска. Нажимайте − до появления «Авто».',
        'paste': 'Вставить',
        'path_left': 'Показать левую часть пути',
        'path_right': 'Показать правую часть пути',
        'pause': 'Пауза',
        'peak': 'Максимальный true peak',
        'peak_tooltip': 'Максимальный true peak — это предел, а не уровень, которого нужно '
                        'достичь. Он ограничивает в dBTP самые высокие пики восстановленной формы '
                        'сигнала, включая межсемпловые, чтобы снизить риск перегрузки после '
                        'кодирования или транскодирования.\n'
                        '\n'
                        '• -1,0 dBTP — распространённый предел поставки с самым высоким выходным '
                        'пиком.\n'
                        '• -1,5 dBTP — значение по умолчанию и осторожный компромисс для MP3.\n'
                        '• -2,0 dBTP — дополнительный запас, полезный при повторном кодировании '
                        'или высокой целевой громкости.\n'
                        '• 0 dBTP — запас отсутствует; для MP3 не рекомендуется.\n'
                        '\n'
                        'Более отрицательное значение безопаснее, но может не позволить очень '
                        'динамичным трекам точно достичь цели LUFS.',
        'phase_summary': 'Расчётное распределение общего времени — анализ {analysis}, '
                         'преобразование {conversion}, контроль качества {quality}.',
        'pipeline_enabled': 'Конвейер треков — преобразование начинается сразу после завершения '
                            'анализа.',
        'pre_measurement': 'Измерение входных файлов…',
        'preset': 'Предустановка',
        'preset_dynamic': 'Динамичная музыка',
        'preset_library': 'Музыкальная библиотека — рекомендуется',
        'preset_streaming': 'Более громкий стриминг',
        'preset_tooltip': 'Одновременно задаёт согласованные целевую громкость, максимальный true '
                          'peak и качество MP3. Любое ручное изменение выбирает режим '
                          '«Пользовательский».',
        'processing_cancelled': 'Обработка отменена.',
        'processing_paused': 'Обработка приостановлена.',
        'processing_resumed': 'Обработка продолжена.',
        'progress_status': '{status}: {file}',
        'qc_impossible': 'ПРЕДУПРЕЖДЕНИЕ — контроль качества не выполнен: {error}',
        'qc_log': ' — КК {quality}',
        'qc_ok': 'OK',
        'qc_warning': 'ПРЕДУПРЕЖДЕНИЕ — {detail}',
        'quality': 'Качество аудио',
        'quality_control': 'Автоматический контроль качества',
        'quality_control_tooltip': 'Повторно измеряет каждый выходной файл. Для динамических MP3 '
                                   'измерение может запустить до трёх корректирующих '
                                   'перекодирований. Отключение не меняет качество кодера, но '
                                   'убирает итоговую проверку, коррекции и работу индикатора.',
        'quality_tooltip': 'Управляет качеством и размером сжатых форматов: малое число означает '
                           'более высокие качество и битрейт. Если выбранный битрейт выше '
                           'исходного, файл увеличится. Большее число обычно уменьшает размер, но '
                           'VBR не гарантирует одинаковое число байтов. FLAC остаётся без потерь; '
                           'WAV и AIFF сохраняют свойства PCM. Диапазоны: 0 = максимальное '
                           'качество; 1-2 = очень высокое; 3-4 = баланс; 5-9 = меньший размер.',
        'ready': 'Готово',
        'recursive_scan': 'Рекурсивное сканирование папок…',
        'remove_all': 'Удалить всё',
        'remove_selection': 'Удалить выбранное',
        'replaygain_tags_missing': 'Теги ReplayGain не найдены.',
        'report_album_dbtp': 'вход_альбом_dbtp',
        'report_album_lufs': 'вход_альбом_lufs',
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
        'report_seconds': 'время_секунды',
        'report_source': 'источник',
        'report_status': 'статус',
        'report_tooltip': 'Создаёт в папке назначения подробный отчёт с измерениями, временем и '
                          'предупреждениями.',
        'resume': 'Возобновить после прерывания',
        'resume_not_saved': ' Точка возобновления не сохранена: {error}',
        'resume_processing': 'Продолжить',
        'resume_tooltip': 'Ранее завершённые с теми же настройками файлы распознаются и не '
                          'обрабатываются повторно.',
        'resumed_progress': 'Возобновлено: {file}',
        'scan_error': 'ОШИБКА — {error}',
        'settings': 'Настройки',
        'show_finder': 'Показать в Finder',
        'show_option_help': 'Показать справку: {option}',
        'silent_album_copy': 'Тихий или неизмеримый альбом скопирован.',
        'silent_copy': 'Тихий или неизмеримый звук скопирован.',
        'silent_copy_no_replaygain': 'Тихий звук скопирован без тегов ReplayGain.',
        'silent_unmeasurable': 'Тихий или неизмеримый звук.',
        'simulation': 'Моделирование',
        'skip_compliant': 'Не перекодировать уже соответствующие файлы',
        'skip_compliant_tooltip': 'По умолчанию включено. После анализа файл копируется без '
                                  'изменений и перекодирования, если громкость отличается от цели '
                                  'не более чем на ±0,5 LU, а истинный пик не превышает предел. В '
                                  'режиме «Альбом» громкость оценивается для всего альбома. '
                                  'Качество и размер сохраняются точно; это указано в журнале.',
        'skipped_progress': 'Пропущено: {file}',
        'source_audio_count': 'Аудиофайлов к обработке: {count}',
        'source_list_more': '… сохранено ещё источников: {count}',
        'source_safety': 'Исходные файлы никогда не перемещаются и не изменяются.',
        'source_selection_tooltip': 'Множественный выбор: Command-щелчок для отдельных элементов, '
                                    'Shift-щелчок для диапазона.',
        'start': 'Запустить',
        'status_analyzed': 'ПРОАНАЛИЗИРОВАНО',
        'status_cancelled': 'ОТМЕНЕНО',
        'status_error': 'ОШИБКА',
        'status_ok': 'OK',
        'status_resumed': 'ВОЗОБНОВЛЕНО',
        'status_skipped': 'ПРОПУЩЕНО',
        'switch_to_dark': 'Тёмная тема',
        'switch_to_light': 'Светлая тема',
        'tagline': 'Выравнивает воспринимаемую громкость звука',
        'target': 'Целевая громкость',
        'target_tooltip': 'Целевая громкость — это требуемая интегральная громкость всего трека в '
                          'LUFS. Менее отрицательное значение даёт более громкий файл: -14 LUFS '
                          'громче, чем -16 LUFS. Разница 2 LU примерно соответствует разнице '
                          'уровня 2 дБ до возможного ограничения пиков.\n'
                          '\n'
                          'Ориентиры: -18 LUFS для более спокойного и динамичного результата; -16 '
                          'LUFS для общего баланса; -14 LUFS для более громкого результата в стиле '
                          'стриминга. Платформы могут затем применять собственную нормализацию '
                          'воспроизведения.\n'
                          '\n'
                          'Сама цель не выравнивает внутреннюю динамику трека. Если максимальный '
                          'true peak не позволяет достичь цели без перегрузки, результат может '
                          'остаться немного ниже.',
        'theme_accessible': 'Изменить оформление приложения. Выбор сохраняется.',
        'total_time': 'Общее время: {duration}',
        'track_mode_log': 'Режим «Трек» — каждый аудиофайл обрабатывается отдельно.',
        'track_two_pass': 'Двухпроходная нормализация трека.',
        'true_peak_meter_exceeded': 'Превышение {margin} дБ',
        'true_peak_meter_margin': 'Запас {margin} дБ',
        'true_peak_meter_title': 'Запас пика',
        'true_peak_meter_tooltip': 'Сравнивает истинный пик последнего результата с выбранным '
                                   'пределом. Метка показывает последнее значение, треугольник '
                                   'сохраняет наивысший пик серии. Зелёный: предел соблюдён; '
                                   'оранжевый: превышение до 0,25 дБ; красный: больше. Оранжевый '
                                   'допуск относится к контролю качества LUFScale и не является '
                                   'стандартом передачи. Сбрасывается для каждой серии.',
        'true_peak_meter_waiting': 'Ожидание измерения dBTP',
        'version_changes': '• Общее число аудиофайлов обновляется при добавлении и удалении '
                           'источников.\n'
                           '• Индикатор снова имеет размеры и отступ версии 1.21.25 и не работает '
                           'без контроля качества.\n'
                           '• Оценка показывает также примерное время завершения.\n'
                           '• Удалены прежние внутренние инструменты тестирования.',
        'version_changes_title': 'Новое в версии {version}',
        'version_label': 'Версия {version}',
        'volume': 'Громкость',
        'volume_loud': 'Громко: -14 LUFS',
        'volume_normal': 'Обычно: -16 LUFS',
        'volume_soft': 'Тихо: -18 LUFS',
        'volume_tooltip': 'Эта настройка служит быстрым выбором целевой громкости; она не меняет '
                          'громкость воспроизведения на Mac.\n'
                          '\n'
                          '• Тихо: -18 LUFS — более спокойный уровень, больший динамический запас '
                          'и меньшая вероятность работы лимитера.\n'
                          '• Нормально: -16 LUFS — сбалансированный компромисс и удобная отправная '
                          'точка для личной библиотеки.\n'
                          '• Громко: -14 LUFS — более выразительное звучание, близкое к цели '
                          'Spotify «Нормально», но чаще требующее ограничения.\n'
                          '• Пользовательский — позволяет напрямую ввести другую цель LUFS.\n'
                          '\n'
                          'Это практические варианты, а не универсальный стандарт.',
        'zero_album_gain': 'Нулевое усиление альбома; звук скопирован.'},
 'zh': {'activity_cancelled': '活动：处理已取消',
        'activity_cancelling': '活动：正在取消…',
        'activity_completed': '活动：处理完成',
        'activity_compliant': '合规：{count}',
        'activity_detected': '活动：检测到 {total} 个文件',
        'activity_errors': '错误：{count}',
        'activity_files': '文件：{count}',
        'activity_idle': '活动：等待中',
        'activity_preparing': '活动：正在准备文件…',
        'activity_progress': '{total} 个文件 • 成功 {success} • 警告 {warnings} • 错误 {failed} • 已续传/跳过 '
                             '{skipped} • 合规 {compliant}',
        'activity_skipped': '已续传/跳过：{count}',
        'activity_successes': '成功：{count}',
        'activity_warnings': '警告：{count}',
        'adaptive_disabled_log': '自适应分析 — 在{sample}次测量后停止快速探测（成功{successes}次，估算节省{percent:+.1f}%）。',
        'add_folders': '添加文件夹…',
        'add_mp3': '添加音频文件…',
        'add_replaygain': '添加 ReplayGain',
        'add_source_files': '添加音频文件',
        'add_source_folder': '添加来源文件夹',
        'album_gain_detail': '专辑共同增益 {gain:+.2f} dB。',
        'album_gain_log': '专辑“{album}” — 共同增益 {gain:+.2f} dB。',
        'album_measurement_error': '专辑测量失败：{error}',
        'album_mode_log': '专辑模式 — 每个包含音频文件的文件夹视为一个专辑。',
        'albums_measurement': '正在测量 {count} 个专辑…',
        'already_completed': '已在上一次运行中完成。',
        'already_compliant_badge': '已符合',
        'already_compliant_copy': '已符合要求：原样复制，不重新编码音频。',
        'already_compliant_log': '已符合要求，未重新编码',
        'analysis_cache_summary': '分析缓存 — 重用了 {hits} 个测量结果。',
        'analysis_impossible': '分析失败：{error}',
        'analysis_method': '分析方法',
        'analysis_method_adaptive': '自适应 — 无收益时停止',
        'analysis_method_fast': '快速方式 — 实验',
        'analysis_method_historical': '历史方式 — 基准',
        'analysis_method_log': '分析方法 — {method}。',
        'analysis_method_tooltip': '历史方式仅使用在1.22.13中验证的完整参考测量。快速方式会对每个文件尝试线性探测，必要时回退到历史测量。自适应方式先按快速方式运行；完成至少12次测量和3次回退后比较实测时间，如果估算节省仍低于5%，就停用探测。最终质量和质量控制不会降低。',
        'analysis_progress': '分析 {current}/{total}：{file}',
        'analyze': '分析',
        'analyze_operation': '分析/模拟',
        'analyzed_progress': '已分析：{file}',
        'app_name': 'LUFScale',
        'audio_copy_replaygain': '音频流未经重新编码已复制；已添加 ReplayGain 标签。',
        'audio_tab': '音频',
        'auto_start': '拖放或粘贴后自动开始',
        'auto_start_tooltip': '已选择目标位置时，通过拖放或粘贴添加来源后自动开始处理。',
        'cancel': '取消',
        'cancelled_summary': '已取消 — 成功 {success}，错误 {failed}，续传/跳过 {skipped}，警告 {warnings}，合规 '
                             '{compliant} — {duration}。',
        'cancelling': '正在取消…',
        'choose': '选择…',
        'choose_output': '选择目标文件夹',
        'clipboard': '剪贴板',
        'clipboard_empty': '剪贴板中没有有效的文件夹或受支持音频文件路径。',
        'close_question': '取消处理并关闭应用？',
        'completed_dialog_summary': '状态：已完成\n'
                                    '文件数：{files}\n'
                                    '成功：{success}\n'
                                    '错误：{failed}\n'
                                    '续传或跳过：{skipped}\n'
                                    '警告：{warnings}\n'
                                    '合规：{compliant}\n'
                                    '总时间：{duration}',
        'completed_summary': '已完成 — 成功 {success}，错误 {failed}，续传/跳过 {skipped}，警告 {warnings}，合规 '
                             '{compliant} — {duration}。',
        'completed_with_errors': '处理完成，但有警告',
        'convert': '统一响度',
        'convert_operation': '音频标准化',
        'cpu_tooltip': '处理期间每秒更新一次的 Mac 总 CPU 使用率。',
        'cpu_unavailable': '不可用',
        'cpu_usage': 'CPU',
        'create_report': '创建 CSV 报告',
        'custom': '自定义',
        'decrease_value': '减小数值',
        'description': '在不修改原文件的情况下，以单曲或专辑模式统一感知响度。',
        'destination': '目标位置',
        'destination_error': '错误 — 目标位置不可用：{error}',
        'destination_path_tooltip': '单击路径，然后使用方向键、Home/End 或鼠标滚轮浏览。路径可以选择和复制，但不能修改。',
        'drop_subtitle': 'MP3、FLAC、WAV、AIFF、M4A、OGG、Opus — 支持子文件夹',
        'drop_title': '将文件夹或音频文件拖放到这里',
        'elapsed_time': '已用时间：{duration}',
        'error_progress': '错误：{file}',
        'estimated_result': '估算结果；未创建文件。',
        'estimated_total_calculating': '预计总时间：正在计算…',
        'estimated_total_time': '预计总时间：{duration}',
        'estimated_total_time_with_finish': '预计总时间：{duration} — 约 {time} 完成',
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
        'folder': '文件夹',
        'folder_unavailable': '文件夹不可用',
        'guide_help_tooltip': '打开所选语言的完整 PDF 指南。',
        'guide_missing_message': '找不到 PDF 指南：{path}',
        'guide_missing_title': '指南不可用',
        'guide_open_error': 'macOS 无法打开 PDF 指南：{path}',
        'help_button': '帮助',
        'help_overview': '• 实际音频标准化、ReplayGain，或仅分析而不创建 MP3。\n'
                         '• 单曲和专辑模式，可保留曲目之间的响度差异。\n'
                         '• 当 FFmpeg 可以复制时，保留文件夹结构、元数据和封面。\n'
                         '• 原文件绝不会被移动或修改。\n'
                         '• 自动并行、分析缓存以及中断后续传。\n'
                         '• 质量控制、CSV 报告、进度、CPU、响度表和预计总时长。\n'
                         '• 界面和 PDF 指南提供十二种语言。',
        'help_title': '主要功能',
        'increase_value': '增大数值',
        'interface_ffmpeg_message': '界面可用，但转换需要 FFmpeg。请安装 FFmpeg 并重新启动应用。',
        'internal_error': '内部错误：{error}',
        'interrupted': '处理已中断。',
        'invalid_location': '位置无效',
        'language': '语言',
        'language_tooltip': '立即更改界面、消息和后续 CSV 报告的语言，并记住所选语言。',
        'level_mode': '响度模式',
        'log_help_text': '每一行描述一个文件或常规处理步骤。\n'
                         '\n'
                         '• 开头：处理状态（OK、警告、错误、已续传或已跳过）。\n'
                         '• 然后：MP3 名称和该文件的处理时间。\n'
                         '• LUFS 标记：处理前测得的电平 → 处理后的电平。\n'
                         '• 末尾：质量控制结果和其他详情。\n'
                         '\n'
                         '颜色：绿色 = 成功；橙色 = 警告；红色 = 文件未完成；蓝紫色 = 续传；灰色 = 信息、跳过或取消。\n'
                         '\n'
                         '累计时间会相加所有并行任务的工作时间。总时间是实际经过的时间。\n'
                         '\n'
                         'QC 警告—峰值表示输出重新测得的真实峰值比所选上限高出 0.25 dB '
                         '以上。文件仍会创建，因此这不是转换错误。不过，它没有严格满足所要求的上限，并为再次编码或某些转换器留下较少余量。dBTP 越接近 '
                         '0，出现采样间峰值的风险越高。若警告持续出现，请选择更低的 LUFS 目标或更安全的最大峰值（例如 −2.0 dBTP），然后重新处理文件。',
        'log_placeholder': '处理日志将显示在此处。',
        'log_title': '处理日志',
        'loudness_meter_estimated': '估算',
        'loudness_meter_help_text': '此响度表用于直观检查标准化的一致性。它把最新音频文件与目标比较，并持续计算最近100个文件的最小值和最大值。较早的数值会逐步移出此窗口，因此大批量处理时显示仍会动态变化。目标评分仍涵盖整个批次，此指标不会更改任何设置。',
        'loudness_meter_maximum': '最大 {value}',
        'loudness_meter_measured': '实测',
        'loudness_meter_minimum': '最小 {value}',
        'loudness_meter_target': '目标 {value} LUFS',
        'loudness_meter_title': '响度表',
        'loudness_meter_tooltip': '红线表示目标值。左侧蓝色数值显示最新音频文件。右侧灰色和深紫色线条及数值显示最近100个文件的最小值和最大值。刻度会放大细微差异，并在每个新批次开始时重置。',
        'loudness_meter_waiting': '等待音频文件',
        'loudness_score_acceptable': '可接受',
        'loudness_score_check': '请检查',
        'loudness_score_excellent': '优秀',
        'loudness_score_good': '良好',
        'loudness_score_needs_qc': '目标评分：请启用质量控制',
        'loudness_score_not_applicable': '目标评分：不适用',
        'loudness_score_tooltip': '评分只使用实际重新测量的输出。RMS 误差（平方差平均值的平方根）概括所得响度与目标之间的整体距离。越接近 0 '
                                  'LU，批次越准确：100 = 精确，50 = 0.5 LU RMS 误差，0 = 1 LU '
                                  '或更大。专辑模式中，每个曲目的期望值包含共同增益，以保留原有差异。',
        'loudness_score_value': '目标评分：{score}/100\n{rating}\nRMS 误差：{deviation}\xa0LU',
        'loudness_score_waiting': '目标评分：等待',
        'measurement_unavailable': '测量不可用。',
        'mode_album': '专辑 — 保留曲目之间的差异',
        'mode_album_label': '专辑',
        'mode_tooltip': '单曲模式分别调整每个 MP3。专辑模式为每个文件夹计算一个共同增益，以保留曲目之间的响度差异。',
        'mode_track': '单曲 — 每个文件使用相同响度',
        'mode_track_label': '单曲',
        'mp3': 'MP3',
        'mp3_filter': '支持的音频 (*.mp3 *.flac *.wav *.aif *.aiff *.m4a *.ogg *.opus)',
        'no_folder': '未选择文件夹',
        'no_mp3': '未找到受支持的音频文件。',
        'no_new_source': '未添加新的有效文件夹或受支持的音频文件。',
        'not_performed': '未执行',
        'open_output_error': '无法打开目标文件夹：{error}',
        'operation': '操作',
        'operation_analyze': '仅分析 — 不创建文件的模拟',
        'operation_analyze_label': '仅分析',
        'operation_convert': '均衡 — 实际标准化音频',
        'operation_convert_label': '音频标准化',
        'operation_replaygain': 'ReplayGain — 不重新编码音频',
        'operation_replaygain_label': 'ReplayGain',
        'operation_tooltip': '均衡会实际处理音频。MP3、M4A/AAC、OGG 和 Opus 必须重新编码，文件大小取决于质量设置并可能增加。FLAC '
                             '以无损方式重编码，但样本变化会改变压缩率。WAV 和 AIFF 保留与源兼容的采样率、声道和位深。ReplayGain '
                             '不重编码；仅分析不会创建文件。',
        'options_tab': '选项',
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
        'qc_log': ' — 质控 {quality}',
        'qc_ok': 'OK',
        'qc_warning': '警告 — {detail}',
        'quality': '音频质量',
        'quality_control': '自动质量控制',
        'quality_control_tooltip': '重新测量每个输出。对于动态路径MP3，测量结果可能触发最多三次纠正性重新编码。关闭此功能不会改变编码器质量，但会取消最终验证、纠正和响度表活动。',
        'quality_tooltip': '控制压缩格式的质量和大小。数字越小，质量和码率越高；若所选码率高于源文件，输出会变大。较大数字通常可减小文件，但 VBR '
                           '不能保证字节数相同。FLAC 始终无损；WAV 和 AIFF 保留 PCM 属性。 范围：0 = 最高质量；1-2 = 很高；3-4 = '
                           '均衡；5-9 = 较小文件。',
        'ready': '就绪',
        'recursive_scan': '正在递归扫描文件夹…',
        'remove_all': '全部移除',
        'remove_selection': '移除所选项',
        'replaygain_operation': '无需重新编码的 ReplayGain',
        'replaygain_tags_missing': '未找到 ReplayGain 标签。',
        'report_album_dbtp': '专辑输入_dbtp',
        'report_album_lufs': '专辑输入_lufs',
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
        'report_seconds': '已用秒数',
        'report_source': '来源',
        'report_status': '状态',
        'report_tooltip': '在目标位置创建包含测量、耗时和警告的详细报告。',
        'resume': '中断后继续',
        'resume_not_saved': ' 未保存续传检查点：{error}',
        'resume_processing': '继续',
        'resume_tooltip': '识别使用相同设置已经完成的文件，不再重复处理。',
        'resumed_progress': '已续传：{file}',
        'scan_error': '错误 — {error}',
        'scanning_folders': '正在扫描文件夹…',
        'settings': '设置',
        'show_finder': '在 Finder 中显示',
        'show_option_help': '显示帮助：{option}',
        'silent_album_copy': '静音或无法测量的专辑已复制。',
        'silent_copy': '静音或无法测量的音频已复制。',
        'silent_copy_no_replaygain': '静音音频已复制，但未添加 ReplayGain 标签。',
        'silent_unmeasurable': '音频静音或无法测量。',
        'simulation': '模拟',
        'skip_compliant': '不重新编码已符合要求的文件',
        'skip_compliant_tooltip': '默认启用。分析后，响度与目标相差不超过 ±0.5 LU '
                                  '且真峰值不超过上限的文件会原样复制，不重新编码。专辑模式按整张专辑的响度判断。这样可完全保留质量和大小，日志会明确说明。',
        'skipped_progress': '已跳过：{file}',
        'source_audio_count': '待处理音频文件：{count}',
        'source_list_more': '… 另保留 {count} 个来源',
        'source_safety': '源文件绝不会被移动或修改。',
        'source_selection_tooltip': '多选：按住 Command 单击选择分散项目，按住 Shift 单击选择连续范围。',
        'sources_added': '已添加 {count} 个来源。',
        'start': '开始',
        'status_analyzed': '已分析',
        'status_cancelled': '已取消',
        'status_error': '错误',
        'status_ok': 'OK',
        'status_resumed': '已续传',
        'status_skipped': '已跳过',
        'switch_to_dark': '深色模式',
        'switch_to_light': '浅色模式',
        'tagline': '统一感知音量',
        'target': '响度目标',
        'target_tooltip': '响度目标是整首曲目的目标综合响度，以 LUFS 表示。数值越不负，文件听起来越响：-14 LUFS 比 -16 LUFS 响。2 LU '
                          '的差值在峰值限制前约等于 2 dB 的电平差。\n'
                          '\n'
                          '参考：-18 LUFS 更平静、更有动态；-16 LUFS 适合一般均衡；-14 LUFS '
                          '适合较响亮的流媒体风格。平台之后可能应用自己的播放标准化。\n'
                          '\n'
                          '目标本身不会压平曲目内部的动态。如果最大真峰值不允许在不削波的情况下达到目标，结果可能略低。',
        'theme_accessible': '更改应用程序外观。选择会被记住。',
        'total_time': '总时间：{duration}',
        'track_mode_log': '单曲模式 — 分别处理每个音频文件。',
        'track_two_pass': '两遍单曲标准化。',
        'true_peak_meter_exceeded': '超出 {margin} dB',
        'true_peak_meter_margin': '余量 {margin} dB',
        'true_peak_meter_title': '峰值余量',
        'true_peak_meter_tooltip': '将上一输出的真峰值与所选上限比较。标记显示最新值，三角形保留本批次最高峰值。绿色表示符合上限；橙色表示超出不超过 0.25 '
                                   'dB；红色表示超出更多。橙色容差仅用于 LUFScale 质量控制，并非交付标准。每批任务都会重置。',
        'true_peak_meter_waiting': '等待 dBTP 测量',
        'version_changes': '• 添加或移除来源时会实时更新音频文件总数。\n'
                           '• 响度表恢复1.21.25的尺寸和间距；关闭质量控制时保持不活动。\n'
                           '• 预计时间现在也显示大致完成时刻。\n'
                           '• 已移除旧的内部测试工具。',
        'version_changes_title': '版本 {version} 的新增内容',
        'version_label': '版本 {version}',
        'volume': '音量',
        'volume_loud': '响亮: -14 LUFS',
        'volume_normal': '标准: -16 LUFS',
        'volume_soft': '柔和: -18 LUFS',
        'volume_tooltip': '此设置是响度目标的快捷方式，不会改变 Mac 的播放音量。\n'
                          '\n'
                          '• 柔和：-18 LUFS — 更平静，动态余量更大，较少触发限制器。\n'
                          '• 标准：-16 LUFS — 均衡折中，适合作为个人音乐库的起点。\n'
                          '• 响亮：-14 LUFS — 播放更突出，但更可能需要限制。\n'
                          '• 自定义 — 直接输入其他 LUFS 目标。\n'
                          '\n'
                          '这些是实用选择，并非通用标准。',
        'zero_album_gain': '专辑增益为零；音频已复制。'}}

EXTRA_CORE_TEXTS: dict[str, dict[str, str]] = {'de': {'album_unmeasurable': 'Die Lautheit des Albums kann nicht gemessen werden.',
        'empty_album': 'Ein Album muss mindestens eine unterstützte Audiodatei enthalten.',
        'incomplete_measurements': 'Unvollständige FFmpeg-Messwerte: {fields}',
        'loudness_changed': 'Lautheit um {value:+.2f} LU verändert',
        'loudness_unmeasurable': 'Die Lautheit kann nicht gemessen werden.',
        'measurements_ok': 'Messwerte entsprechen den Vorgaben.',
        'no_inputs': 'Fügen Sie mindestens einen Ordner oder eine unterstützte Audiodatei hinzu.',
        'no_measurements': 'FFmpeg hat keine verwertbaren Lautheitsmesswerte geliefert.',
        'output_contains_source': 'Der ausgewählte Zielordner enthält bereits die Quelldatei. '
                                  'Wählen Sie einen anderen Speicherort.',
        'output_inside_source': 'Der Zielordner darf nicht innerhalb eines Quellordners liegen. '
                                'Wählen Sie einen Speicherort außerhalb der hinzugefügten Ordner.',
        'output_not_silent': 'Die Ausgabe ist nicht mehr still.',
        'output_recreates_source': 'Dieser Zielordner würde Dateien direkt in der Quelle neu '
                                   'erstellen. Wählen Sie einen anderen Speicherort.',
        'output_unmeasurable': 'Die Ausgabe hat keine messbare Lautheit.',
        'peak_above_limit': 'Spitzenpegel {value:.2f} dBTP über dem Grenzwert',
        'peak_changed': 'Spitzenpegel um {value:+.2f} dB verändert',
        'silent_preserved': 'Stilles Audio beibehalten.',
        'unexpected_loudness': '{actual:.2f} LUFS statt {expected:.2f}'},
 'es': {'album_unmeasurable': 'No se puede medir la sonoridad del álbum.',
        'empty_album': 'Un álbum debe contener al menos un archivo de audio compatible.',
        'incomplete_measurements': 'Mediciones de FFmpeg incompletas: {fields}',
        'loudness_changed': 'sonoridad modificada en {value:+.2f} LU',
        'loudness_unmeasurable': 'No se puede medir la sonoridad.',
        'measurements_ok': 'Mediciones correctas.',
        'no_inputs': 'Añade al menos una carpeta o un archivo de audio compatible.',
        'no_measurements': 'FFmpeg no devolvió mediciones de sonoridad utilizables.',
        'output_contains_source': 'La carpeta de destino seleccionada ya contiene el archivo de '
                                  'origen. Elige otra ubicación.',
        'output_inside_source': 'La carpeta de destino no puede estar dentro de una carpeta de '
                                'origen. Elige una ubicación fuera de las carpetas añadidas.',
        'output_not_silent': 'La salida ya no es silenciosa.',
        'output_recreates_source': 'Esta carpeta de destino volvería a crear los archivos '
                                   'directamente en el origen. Elige otra ubicación.',
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
        'output_contains_source': 'चुने गए आउटपुट फ़ोल्डर में स्रोत फ़ाइल पहले से है। कोई दूसरा '
                                  'स्थान चुनें।',
        'output_inside_source': 'आउटपुट फ़ोल्डर स्रोत फ़ोल्डर के अंदर नहीं हो सकता। जोड़े गए '
                                'फ़ोल्डरों के बाहर कोई स्थान चुनें।',
        'output_not_silent': 'आउटपुट अब मौन नहीं है।',
        'output_recreates_source': 'यह आउटपुट फ़ोल्डर फ़ाइलों को सीधे स्रोत में फिर बनाएगा। कोई '
                                   'दूसरा स्थान चुनें।',
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
        'output_contains_source': 'La cartella di destinazione selezionata contiene già il file '
                                  'sorgente. Scegli un’altra posizione.',
        'output_inside_source': 'La cartella di destinazione non può trovarsi dentro una cartella '
                                'sorgente. Scegli una posizione esterna alle cartelle aggiunte.',
        'output_not_silent': 'L’uscita non è più silenziosa.',
        'output_recreates_source': 'Questa cartella di destinazione ricreerebbe i file '
                                   'direttamente nella sorgente. Scegli un’altra posizione.',
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
 'nl': {'album_unmeasurable': 'De luidheid van het album kan niet worden gemeten.',
        'empty_album': 'Een album moet ten minste één ondersteund audiobestand bevatten.',
        'incomplete_measurements': 'Onvolledige FFmpeg-metingen: {fields}',
        'loudness_changed': 'luidheid gewijzigd met {value:+.2f} LU',
        'loudness_unmeasurable': 'De luidheid kan niet worden gemeten.',
        'measurements_ok': 'Metingen voldoen.',
        'no_inputs': 'Voeg ten minste één map of ondersteund audiobestand toe.',
        'no_measurements': 'FFmpeg heeft geen bruikbare luidheidsmetingen teruggegeven.',
        'output_contains_source': 'De gekozen doelmap bevat het bronbestand al. Kies een andere '
                                  'locatie.',
        'output_inside_source': 'De doelmap mag niet in een bronmap staan. Kies een locatie buiten '
                                'de toegevoegde mappen.',
        'output_not_silent': 'De uitvoer is niet meer stil.',
        'output_recreates_source': 'Met deze doelmap zouden bestanden direct in de bron worden '
                                   'gemaakt. Kies een andere locatie.',
        'output_unmeasurable': 'De uitvoer heeft geen meetbare luidheid.',
        'peak_above_limit': 'piek {value:.2f} dBTP boven de limiet',
        'peak_changed': 'piek gewijzigd met {value:+.2f} dB',
        'silent_preserved': 'Stille audio behouden.',
        'unexpected_loudness': '{actual:.2f} LUFS in plaats van {expected:.2f}'},
 'pl': {'album_unmeasurable': 'Nie można zmierzyć głośności albumu.',
        'empty_album': 'Album musi zawierać co najmniej jeden obsługiwany plik audio.',
        'incomplete_measurements': 'Niepełne pomiary FFmpeg: {fields}',
        'loudness_changed': 'głośność zmieniona o {value:+.2f} LU',
        'loudness_unmeasurable': 'Nie można zmierzyć głośności.',
        'measurements_ok': 'Pomiary są zgodne.',
        'no_inputs': 'Dodaj co najmniej jeden folder lub obsługiwany plik audio.',
        'no_measurements': 'FFmpeg nie zwrócił użytecznych pomiarów głośności.',
        'output_contains_source': 'Wybrany folder docelowy już zawiera plik źródłowy. Wybierz inne '
                                  'miejsce.',
        'output_inside_source': 'Folder docelowy nie może znajdować się wewnątrz folderu '
                                'źródłowego. Wybierz miejsce poza dodanymi folderami.',
        'output_not_silent': 'Wyjście nie jest już ciche.',
        'output_recreates_source': 'Ten folder docelowy tworzyłby pliki bezpośrednio w źródle. '
                                   'Wybierz inne miejsce.',
        'output_unmeasurable': 'Wyjście nie ma mierzalnej głośności.',
        'peak_above_limit': 'szczyt {value:.2f} dBTP powyżej limitu',
        'peak_changed': 'szczyt zmieniony o {value:+.2f} dB',
        'silent_preserved': 'Zachowano cichy dźwięk.',
        'unexpected_loudness': '{actual:.2f} LUFS zamiast {expected:.2f}'},
 'pt': {'album_unmeasurable': 'Não é possível medir a sonoridade do álbum.',
        'empty_album': 'Um álbum deve conter pelo menos um ficheiro de áudio compatível.',
        'incomplete_measurements': 'Medições FFmpeg incompletas: {fields}',
        'loudness_changed': 'sonoridade alterada em {value:+.2f} LU',
        'loudness_unmeasurable': 'Não é possível medir a sonoridade.',
        'measurements_ok': 'Medições conformes.',
        'no_inputs': 'Adicione pelo menos uma pasta ou um ficheiro de áudio compatível.',
        'no_measurements': 'O FFmpeg não devolveu medições de sonoridade utilizáveis.',
        'output_contains_source': 'A pasta de destino selecionada já contém o ficheiro de origem. '
                                  'Escolha outra localização.',
        'output_inside_source': 'A pasta de destino não pode estar dentro de uma pasta de origem. '
                                'Escolha uma localização fora das pastas adicionadas.',
        'output_not_silent': 'A saída deixou de ser silenciosa.',
        'output_recreates_source': 'Esta pasta de destino voltaria a criar os ficheiros '
                                   'diretamente na origem. Escolha outra localização.',
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
        'output_contains_source': 'Выбранная папка назначения уже содержит исходный файл. Выберите '
                                  'другое место.',
        'output_inside_source': 'Папка назначения не может находиться внутри исходной папки. '
                                'Выберите место вне добавленных папок.',
        'output_not_silent': 'Выходной сигнал больше не является тихим.',
        'output_recreates_source': 'Эта папка назначения привела бы к созданию файлов прямо в '
                                   'источнике. Выберите другое место.',
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

# Stable 1.22.21 interface updates.  Keeping these overrides together makes
# the new log, meter and release wording identical across all ten secondary
# catalogues without regenerating unrelated historical entries.
TRANSLATION_UPDATES_12221: dict[str, dict[str, str]] = {
    'de': {
        'analysis_method_tooltip': 'Die stabile Version verwendet automatisch die vollständige historische Referenzmessung, die einzige am Referenzkorpus validierte Methode. Schnell und Adaptiv werden nicht mehr angeboten.',
        'finalization_completed': 'Abschluss in {duration} beendet.',
        'finalizing': 'Abschluss — Bericht, Analyse-Cache und Fortsetzungsdaten…',
        'input_lufs_log': 'Eingang {value} LUFS',
        'loudness_meter_help_text': 'Die rote Linie ist das Ziel. Blau zeigt die letzte nachgemessene Ausgabe. Min ist die niedrigste und Max die höchste Lautheit der letzten 20 Ausgaben; dieses Fenster gleitet mit jeder Datei. Ohne Qualitätskontrolle bleibt die Anzeige inaktiv.',
        'loudness_meter_tooltip': 'Die rote Linie ist das Ziel. Blau folgt der letzten nachgemessenen Ausgabe. Rechts sind Min und Max die niedrigste und höchste Lautheit der letzten 20 Ausgaben. Das Fenster gleitet mit jeder Datei und wird für einen neuen Stapel zurückgesetzt.',
        'version_changes': '• Tabellenüberschriften der Voreinstellungen und Markierung 4 im Schnellstart wurden korrigiert.\n• Die Abschlussübersicht passt ihre Breite dem Text an.\n• Das Protokoll kennzeichnet Eingangs-LUFS ohne Qualitätskontrolle und misst die Abschlusszeit.\n• Min/Max folgen den letzten 20 Ausgaben; die historische Analyse wird automatisch verwendet.',
    },
    'es': {
        'analysis_method_tooltip': 'La versión estable usa automáticamente la medición histórica completa, única validada en el corpus de referencia. Rápido y Adaptativo ya no se ofrecen.',
        'finalization_completed': 'Finalización terminada en {duration}.',
        'finalizing': 'Finalización — informe, caché de análisis y datos de reanudación…',
        'input_lufs_log': 'entrada {value} LUFS',
        'loudness_meter_help_text': 'La línea roja es el objetivo. El valor azul es la última salida medida de nuevo. Min es la sonoridad más baja y Max la más alta de las últimas 20 salidas; la ventana se desplaza con cada archivo. Sin control de calidad, el medidor queda inactivo.',
        'loudness_meter_tooltip': 'La línea roja es el objetivo. El valor azul sigue la última salida medida de nuevo. A la derecha, Min y Max son la sonoridad más baja y más alta de las últimas 20 salidas. La ventana se desplaza con cada archivo y se reinicia en cada lote.',
        'version_changes': '• Se corrigen los encabezados de la tabla de preajustes y el marcador 4 del inicio rápido.\n• El resumen final adapta su ancho al texto.\n• El registro identifica los LUFS de entrada sin control de calidad y cronometra la finalización.\n• Min/Max siguen las últimas 20 salidas y se usa automáticamente el análisis Histórico.',
    },
    'hi': {
        'analysis_method_tooltip': 'स्थिर संस्करण अपने-आप पूर्ण ऐतिहासिक संदर्भ माप का उपयोग करता है; संदर्भ संग्रह पर सत्यापित यही एक विधि है। तेज़ और अनुकूली विकल्प अब उपलब्ध नहीं हैं।',
        'finalization_completed': 'अंतिम चरण {duration} में पूरा हुआ।',
        'finalizing': 'अंतिम चरण — रिपोर्ट, विश्लेषण कैश और पुनःआरंभ डेटा…',
        'input_lufs_log': 'इनपुट {value} LUFS',
        'loudness_meter_help_text': 'लाल रेखा लक्ष्य है। नीला मान अंतिम दोबारा मापा आउटपुट है। Min पिछली 20 आउटपुट का सबसे कम और Max सबसे अधिक लाउडनेस है; यह विंडो हर फ़ाइल के साथ आगे बढ़ती है। गुणवत्ता जाँच बंद होने पर मीटर निष्क्रिय रहता है।',
        'loudness_meter_tooltip': 'लाल रेखा लक्ष्य है और नीला मान अंतिम दोबारा मापा आउटपुट। दाईं ओर Min और Max पिछली 20 आउटपुट के न्यूनतम और अधिकतम लाउडनेस हैं। विंडो हर फ़ाइल के साथ खिसकती है और नए बैच पर रीसेट होती है।',
        'version_changes': '• प्रीसेट तालिका के शीर्षक और त्वरित शुरुआत का चिह्न 4 ठीक किए गए।\n• अंतिम सारांश की चौड़ाई पाठ के अनुसार बदलती है।\n• गुणवत्ता जाँच बंद होने पर लॉग इनपुट LUFS बताता है और अंतिम चरण का समय दिखाता है।\n• Min/Max पिछली 20 आउटपुट का अनुसरण करते हैं और ऐतिहासिक विश्लेषण अपने-आप उपयोग होता है।',
    },
    'it': {
        'analysis_method_tooltip': 'La versione stabile usa automaticamente la misura storica completa, l’unico metodo convalidato sul corpus di riferimento. Rapido e Adattivo non sono più proposti.',
        'finalization_completed': 'Finalizzazione completata in {duration}.',
        'finalizing': 'Finalizzazione — rapporto, cache di analisi e dati di ripresa…',
        'input_lufs_log': 'ingresso {value} LUFS',
        'loudness_meter_help_text': 'La linea rossa è l’obiettivo. Il valore blu è l’ultima uscita rimisurata. Min è la sonorità più bassa e Max la più alta delle ultime 20 uscite; la finestra scorre a ogni file. Senza controllo qualità il misuratore resta inattivo.',
        'loudness_meter_tooltip': 'La linea rossa è l’obiettivo e il valore blu segue l’ultima uscita rimisurata. A destra, Min e Max sono la sonorità più bassa e più alta delle ultime 20 uscite. La finestra scorre a ogni file e si azzera per un nuovo lotto.',
        'version_changes': '• Corrette le intestazioni della tabella dei preimpostati e il riferimento 4 dell’avvio rapido.\n• Il riepilogo finale adatta la larghezza al testo.\n• Il registro identifica i LUFS in ingresso senza controllo qualità e misura la finalizzazione.\n• Min/Max seguono le ultime 20 uscite e l’analisi Storica viene usata automaticamente.',
    },
    'ja': {
        'analysis_method_tooltip': '安定版では、基準コーパスで検証済みの完全な履歴方式を自動的に使用します。高速方式と適応方式は選択肢から削除されました。',
        'finalization_completed': '最終処理は {duration} で完了しました。',
        'finalizing': '最終処理 — レポート、解析キャッシュ、再開データ…',
        'input_lufs_log': '入力 {value} LUFS',
        'loudness_meter_help_text': '赤線は目標、青値は最後に再測定した出力です。Min は直近20出力の最小ラウドネス、Max は最大ラウドネスで、ファイルごとに範囲が移動します。品質管理が無効な場合、メーターは動作しません。',
        'loudness_meter_tooltip': '赤線は目標、青値は最後に再測定した出力です。右側の Min と Max は直近20出力の最小・最大ラウドネスです。範囲はファイルごとに移動し、新しいバッチでリセットされます。',
        'version_changes': '• プリセット表の見出しとクイックスタートの番号4を修正しました。\n• 完了画面の幅をテキストに合わせます。\n• 品質管理なしの入力LUFSを明記し、最終処理時間を記録します。\n• Min/Max は直近20出力を追跡し、履歴方式を自動使用します。',
    },
    'nl': {
        'analysis_method_tooltip': 'De stabiele versie gebruikt automatisch de volledige historische referentiemeting, de enige methode die op de referentiecollectie is gevalideerd. Snel en Adaptief worden niet meer aangeboden.',
        'finalization_completed': 'Afronding voltooid in {duration}.',
        'finalizing': 'Afronding — rapport, analysecache en hervattingsgegevens…',
        'input_lufs_log': 'invoer {value} LUFS',
        'loudness_meter_help_text': 'De rode lijn is het doel. De blauwe waarde is de laatst opnieuw gemeten uitvoer. Min is de laagste en Max de hoogste luidheid van de laatste 20 uitvoerbestanden; dit venster schuift bij elk bestand. Zonder kwaliteitscontrole blijft de meter inactief.',
        'loudness_meter_tooltip': 'De rode lijn is het doel en blauw volgt de laatst opnieuw gemeten uitvoer. Rechts zijn Min en Max de laagste en hoogste luidheid van de laatste 20 uitvoerbestanden. Het venster schuift bij elk bestand en wordt bij een nieuwe reeks gewist.',
        'version_changes': '• De koppen van de voorinstellingentabel en markering 4 van Snel beginnen zijn gecorrigeerd.\n• De eindsamenvatting past haar breedte aan de tekst aan.\n• Het logboek benoemt invoer-LUFS zonder kwaliteitscontrole en meet de afronding.\n• Min/Max volgen de laatste 20 uitvoerbestanden en Historische analyse wordt automatisch gebruikt.',
    },
    'pl': {
        'analysis_method_tooltip': 'Wersja stabilna automatycznie używa pełnego historycznego pomiaru odniesienia, jedynej metody zweryfikowanej na korpusie referencyjnym. Tryby Szybki i Adaptacyjny nie są już oferowane.',
        'finalization_completed': 'Finalizacja zakończona w {duration}.',
        'finalizing': 'Finalizacja — raport, pamięć analiz i dane wznowienia…',
        'input_lufs_log': 'wejście {value} LUFS',
        'loudness_meter_help_text': 'Czerwona linia oznacza cel. Niebieska wartość to ostatni ponownie zmierzony wynik. Min jest najniższą, a Max najwyższą głośnością z ostatnich 20 wyników; okno przesuwa się z każdym plikiem. Bez kontroli jakości miernik jest nieaktywny.',
        'loudness_meter_tooltip': 'Czerwona linia oznacza cel, a niebieska wartość ostatni ponownie zmierzony wynik. Po prawej Min i Max pokazują najniższą i najwyższą głośność z ostatnich 20 wyników. Okno przesuwa się z każdym plikiem i zeruje dla nowej serii.',
        'version_changes': '• Poprawiono nagłówki tabeli ustawień oraz znacznik 4 szybkiego startu.\n• Podsumowanie końcowe dopasowuje szerokość do tekstu.\n• Dziennik oznacza wejściowe LUFS bez kontroli jakości i mierzy finalizację.\n• Min/Max śledzą ostatnie 20 wyników, a analiza Historyczna jest używana automatycznie.',
    },
    'pt': {
        'analysis_method_tooltip': 'A versão estável usa automaticamente a medição histórica completa, o único método validado no corpus de referência. Rápido e Adaptativo deixaram de ser propostos.',
        'finalization_completed': 'Finalização concluída em {duration}.',
        'finalizing': 'Finalização — relatório, cache de análise e dados de retoma…',
        'input_lufs_log': 'entrada {value} LUFS',
        'loudness_meter_help_text': 'A linha vermelha é o alvo. O valor azul é a última saída novamente medida. Min é a sonoridade mais baixa e Max a mais alta das últimas 20 saídas; a janela desliza a cada ficheiro. Sem controlo de qualidade, o medidor fica inativo.',
        'loudness_meter_tooltip': 'A linha vermelha é o alvo e o valor azul segue a última saída novamente medida. À direita, Min e Max são a sonoridade mais baixa e mais alta das últimas 20 saídas. A janela desliza a cada ficheiro e reinicia num novo lote.',
        'version_changes': '• Corrigidos os cabeçalhos da tabela de predefinições e o marcador 4 do início rápido.\n• O resumo final adapta a largura ao texto.\n• O registo identifica LUFS de entrada sem controlo de qualidade e mede a finalização.\n• Min/Max seguem as últimas 20 saídas e a análise Histórica é usada automaticamente.',
    },
    'ru': {
        'analysis_method_tooltip': 'Стабильная версия автоматически использует полный исторический эталонный замер — единственный метод, проверенный на эталонном наборе. Быстрый и адаптивный варианты больше не предлагаются.',
        'finalization_completed': 'Завершение выполнено за {duration}.',
        'finalizing': 'Завершение — отчёт, кэш анализа и данные возобновления…',
        'input_lufs_log': 'вход {value} LUFS',
        'loudness_meter_help_text': 'Красная линия — цель. Синее значение — последний повторно измеренный результат. Min — минимальная, Max — максимальная громкость среди последних 20 результатов; окно сдвигается с каждым файлом. Без контроля качества индикатор неактивен.',
        'loudness_meter_tooltip': 'Красная линия — цель, синее значение — последний повторно измеренный результат. Справа Min и Max показывают минимальную и максимальную громкость последних 20 результатов. Окно сдвигается с каждым файлом и сбрасывается для новой серии.',
        'version_changes': '• Исправлены заголовки таблицы предустановок и метка 4 быстрого запуска.\n• Итоговое окно подбирает ширину по тексту.\n• Журнал помечает входные LUFS без контроля качества и измеряет время завершения.\n• Min/Max отслеживают последние 20 результатов; исторический анализ используется автоматически.',
    },
    'zh': {
        'analysis_method_tooltip': '稳定版自动使用完整的历史参考测量，这是唯一经过参考语料验证的方法。快速和自适应方式不再提供。',
        'finalization_completed': '最终处理在 {duration} 内完成。',
        'finalizing': '最终处理 — 报告、分析缓存和恢复数据…',
        'input_lufs_log': '输入 {value} LUFS',
        'loudness_meter_help_text': '红线是目标，蓝色数值是最后一个重新测量的输出。Min 是最近20个输出中的最低响度，Max 是最高响度；窗口随每个文件滑动。关闭质量控制时，电平表保持不活动。',
        'loudness_meter_tooltip': '红线是目标，蓝色数值跟随最后一个重新测量的输出。右侧 Min 和 Max 分别表示最近20个输出的最低和最高响度。窗口随每个文件滑动，并在新批次开始时重置。',
        'version_changes': '• 修正预设表标题和快速开始中的标记4。\n• 完成摘要会根据文字调整宽度。\n• 关闭质量控制时，日志会标明输入LUFS并记录最终处理时间。\n• Min/Max 跟踪最近20个输出，并自动使用历史分析。',
    },
}

for _language, _updates in TRANSLATION_UPDATES_12221.items():
    EXTRA_TEXTS.setdefault(_language, {}).update(_updates)


# The requested locale names are selectable in 1.22.22.  Until a reviewed
# native catalogue exists for a locale, the unified loader deliberately uses
# its English source text instead of presenting an unrelated French UI.
REQUESTED_LANGUAGE_CODES_12222 = (
    "ar",
    "bg",
    "cs",
    "da",
    "el",
    "fa",
    "fi",
    "he",
    "hr",
    "hu",
    "id",
    "ko",
    "lt",
    "lv",
    "ms",
    "no",
    "pt_BR",
    "ro",
    "sk",
    "sl",
    "sr",
    "sv",
    "th",
    "tr",
    "uk",
    "vi",
    "zh_TW",
)
for _language in REQUESTED_LANGUAGE_CODES_12222:
    EXTRA_TEXTS.setdefault(_language, {})


TRANSLATION_UPDATES_12222: dict[str, dict[str, str]] = {
    "de": {
        "output_lufs_log": "Ausgabe {value} LUFS",
        "loudness_meter_help_text": "Die rote Linie ist das Ziel. Blau zeigt die letzte nachgemessene Ausgabe. Min ist die niedrigste und Max die höchste Lautheit der letzten 30 Ausgaben; dieses Fenster gleitet mit jeder Datei. Ohne Qualitätskontrolle bleibt die Anzeige inaktiv.",
        "loudness_meter_tooltip": "Die rote Linie ist das Ziel. Blau folgt der letzten nachgemessenen Ausgabe. Rechts sind Min und Max die niedrigste und höchste Lautheit der letzten 30 Ausgaben. Das Fenster gleitet mit jeder Datei und wird für einen neuen Stapel zurückgesetzt.",
    },
    "es": {
        "output_lufs_log": "salida {value} LUFS",
        "loudness_meter_help_text": "La línea roja es el objetivo. El valor azul es la última salida medida de nuevo. Min es la sonoridad más baja y Max la más alta de las últimas 30 salidas; la ventana se desplaza con cada archivo. Sin control de calidad, el medidor queda inactivo.",
        "loudness_meter_tooltip": "La línea roja es el objetivo. El valor azul sigue la última salida medida de nuevo. A la derecha, Min y Max son la sonoridad más baja y más alta de las últimas 30 salidas. La ventana se desplaza con cada archivo y se reinicia en cada lote.",
    },
    "hi": {
        "output_lufs_log": "आउटपुट {value} LUFS",
        "loudness_meter_help_text": "लाल रेखा लक्ष्य है। नीला मान अंतिम दोबारा मापा आउटपुट है। Min पिछली 30 आउटपुट का सबसे कम और Max सबसे अधिक लाउडनेस है; यह विंडो हर फ़ाइल के साथ आगे बढ़ती है। गुणवत्ता जाँच बंद होने पर मीटर निष्क्रिय रहता है।",
        "loudness_meter_tooltip": "लाल रेखा लक्ष्य है और नीला मान अंतिम दोबारा मापा आउटपुट। दाईं ओर Min और Max पिछली 30 आउटपुट के न्यूनतम और अधिकतम लाउडनेस हैं। विंडो हर फ़ाइल के साथ खिसकती है और नए बैच पर रीसेट होती है।",
    },
    "it": {
        "output_lufs_log": "uscita {value} LUFS",
        "loudness_meter_help_text": "La linea rossa è l’obiettivo. Il valore blu è l’ultima uscita rimisurata. Min è la sonorità più bassa e Max la più alta delle ultime 30 uscite; la finestra scorre a ogni file. Senza controllo qualità il misuratore resta inattivo.",
        "loudness_meter_tooltip": "La linea rossa è l’obiettivo e il valore blu segue l’ultima uscita rimisurata. A destra, Min e Max sono la sonorità più bassa e più alta delle ultime 30 uscite. La finestra scorre a ogni file e si azzera per un nuovo lotto.",
    },
    "ja": {
        "output_lufs_log": "出力 {value} LUFS",
        "loudness_meter_help_text": "赤線は目標、青値は最後に再測定した出力です。Min は直近30出力の最小ラウドネス、Max は最大ラウドネスで、ファイルごとに範囲が移動します。品質管理が無効な場合、メーターは動作しません。",
        "loudness_meter_tooltip": "赤線は目標、青値は最後に再測定した出力です。右側の Min と Max は直近30出力の最小・最大ラウドネスです。範囲はファイルごとに移動し、新しいバッチでリセットされます。",
    },
    "nl": {
        "output_lufs_log": "uitvoer {value} LUFS",
        "loudness_meter_help_text": "De rode lijn is het doel. De blauwe waarde is de laatst opnieuw gemeten uitvoer. Min is de laagste en Max de hoogste luidheid van de laatste 30 uitvoerbestanden; dit venster schuift bij elk bestand. Zonder kwaliteitscontrole blijft de meter inactief.",
        "loudness_meter_tooltip": "De rode lijn is het doel en blauw volgt de laatst opnieuw gemeten uitvoer. Rechts zijn Min en Max de laagste en hoogste luidheid van de laatste 30 uitvoerbestanden. Het venster schuift bij elk bestand en wordt bij een nieuwe reeks gewist.",
    },
    "pl": {
        "output_lufs_log": "wyjście {value} LUFS",
        "loudness_meter_help_text": "Czerwona linia oznacza cel. Niebieska wartość to ostatni ponownie zmierzony wynik. Min jest najniższą, a Max najwyższą głośnością z ostatnich 30 wyników; okno przesuwa się z każdym plikiem. Bez kontroli jakości miernik jest nieaktywny.",
        "loudness_meter_tooltip": "Czerwona linia oznacza cel, a niebieska wartość ostatni ponownie zmierzony wynik. Po prawej Min i Max pokazują najniższą i najwyższą głośność z ostatnich 30 wyników. Okno przesuwa się z każdym plikiem i zeruje dla nowej serii.",
    },
    "pt": {
        "output_lufs_log": "saída {value} LUFS",
        "loudness_meter_help_text": "A linha vermelha é o alvo. O valor azul é a última saída novamente medida. Min é a sonoridade mais baixa e Max a mais alta das últimas 30 saídas; a janela desliza a cada ficheiro. Sem controlo de qualidade, o medidor fica inativo.",
        "loudness_meter_tooltip": "A linha vermelha é o alvo e o valor azul segue a última saída novamente medida. À direita, Min e Max são a sonoridade mais baixa e mais alta das últimas 30 saídas. A janela desliza a cada ficheiro e reinicia num novo lote.",
    },
    "ru": {
        "output_lufs_log": "выход {value} LUFS",
        "loudness_meter_help_text": "Красная линия — цель. Синее значение — последний повторно измеренный результат. Min — минимальная, Max — максимальная громкость среди последних 30 результатов; окно сдвигается с каждым файлом. Без контроля качества индикатор неактивен.",
        "loudness_meter_tooltip": "Красная линия — цель, синее значение — последний повторно измеренный результат. Справа Min и Max показывают минимальную и максимальную громкость последних 30 результатов. Окно сдвигается с каждым файлом и сбрасывается для новой серии.",
    },
    "zh": {
        "output_lufs_log": "输出 {value} LUFS",
        "loudness_meter_help_text": "红线是目标，蓝色数值是最后一个重新测量的输出。Min 是最近30个输出中的最低响度，Max 是最高响度；窗口随每个文件滑动。关闭质量控制时，电平表保持不活动。",
        "loudness_meter_tooltip": "红线是目标，蓝色数值跟随最后一个重新测量的输出。右侧 Min 和 Max 分别表示最近30个输出的最低和最高响度。窗口随每个文件滑动，并在新批次开始时重置。",
    },
}
for _language, _updates in TRANSLATION_UPDATES_12222.items():
    EXTRA_TEXTS.setdefault(_language, {}).update(_updates)
for _language in TRANSLATION_UPDATES_12221:
    # Avoid showing the previous release notes under the new version number.
    EXTRA_TEXTS[_language].pop("version_changes", None)


TRANSLATION_UPDATES_12224: dict[str, str] = {
    "de": "• Pause → Abbrechen endet jetzt auch dann normal, wenn der Koordinator der parallelen Aufgaben noch auf Fortsetzen wartet.\n• Das Abschlusssignal entsperrt die Bedienelemente und führt nach der Bereinigung ein bereits bestätigtes Schließen aus.\n• Die FFmpeg-Prozessbeendigung aus Version 1.22.23 bleibt erhalten.\n• Audio-Engine und Normalisierungsberechnungen bleiben unverändert.",
    "es": "• Pausa → Cancelar termina ahora normalmente incluso si el coordinador de tareas paralelas aún espera la reanudación.\n• La señal de finalización desbloquea los controles y ejecuta, tras la limpieza, un cierre ya confirmado.\n• Se conserva la lógica de detención de procesos FFmpeg de la versión 1.22.23.\n• El motor de audio y los cálculos de normalización no cambian.",
    "hi": "• रोकें → रद्द करें अब सामान्य रूप से पूरा होता है, भले ही समानांतर कार्य समन्वयक अभी भी फिर से शुरू होने की प्रतीक्षा कर रहा हो।\n• समापन संकेत नियंत्रणों को खोलता है और सफाई के बाद पहले से पुष्टि की गई बंद करने की क्रिया पूरी करता है।\n• संस्करण 1.22.23 की FFmpeg प्रक्रिया-रोक तर्क सुरक्षित रखी गई है।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    "it": "• Pausa → Annulla ora termina normalmente anche se il coordinatore delle attività parallele attende ancora la ripresa.\n• Il segnale di completamento sblocca i comandi ed esegue, dopo la pulizia, una chiusura già confermata.\n• La logica di arresto dei processi FFmpeg della versione 1.22.23 viene mantenuta.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    "ja": "• 一時停止 → キャンセルは、並列タスクのコーディネーターが再開を待っている場合でも正常に終了するようになりました。\n• 完了信号で操作を再有効化し、後処理の後に確認済みの終了を実行します。\n• バージョン 1.22.23 の FFmpeg プロセス停止処理は維持されます。\n• 音声エンジンと正規化計算は変更されていません。",
    "nl": "• Pauze → Annuleren eindigt nu normaal, ook als de coördinator van parallelle taken nog op Hervatten wacht.\n• Het eindsignaal ontgrendelt de bediening en voert na het opruimen een al bevestigde afsluiting uit.\n• De FFmpeg-processtop van versie 1.22.23 blijft behouden.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    "pl": "• Pauza → Anuluj kończy się teraz prawidłowo, nawet gdy koordynator zadań równoległych nadal czeka na wznowienie.\n• Sygnał zakończenia odblokowuje elementy sterujące i po sprzątaniu wykonuje wcześniej potwierdzone zamknięcie.\n• Zachowano logikę zatrzymywania procesów FFmpeg z wersji 1.22.23.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    "pt": "• Pausa → Cancelar termina agora normalmente, mesmo quando o coordenador de tarefas paralelas ainda aguarda a retoma.\n• O sinal de conclusão desbloqueia os controlos e executa, após a limpeza, um fecho já confirmado.\n• Mantém-se a lógica de paragem dos processos FFmpeg da versão 1.22.23.\n• O motor de áudio e os cálculos de normalização não mudam.",
    "ru": "• Пауза → Отмена теперь завершается нормально, даже если координатор параллельных задач ещё ожидает возобновления.\n• Сигнал завершения разблокирует элементы управления и после очистки выполняет уже подтверждённое закрытие.\n• Логика остановки процессов FFmpeg из версии 1.22.23 сохранена.\n• Аудиодвижок и расчёты нормализации не изменены.",
    "zh": "• 暂停 → 取消现在可以正常结束，即使并行任务协调器仍在等待恢复。\n• 完成信号会解锁控件，并在清理后执行已确认的关闭操作。\n• 保留版本 1.22.23 的 FFmpeg 进程停止逻辑。\n• 音频引擎和标准化计算保持不变。",
}
for _language, _changes in TRANSLATION_UPDATES_12224.items():
    EXTRA_TEXTS.setdefault(_language, {})["version_changes"] = _changes


# Version 1.22.25 narrows the selector to the 16 choices retained by the
# product.  Keep the existing translated feature list, but replace its final
# language-summary bullet so every selectable native catalogue reports the
# same current contract.
LANGUAGE_SELECTOR_SUMMARIES_12225: dict[str, str] = {
    "de": "• Sprachauswahl mit 16 Einträgen: 11 Auswahlmöglichkeiten haben einen eigenen Oberflächenkatalog und eine eigene Anleitung; die übrigen verwenden Referenzenglisch.",
    "es": "• Selector de 16 idiomas: 11 opciones tienen un catálogo de interfaz y una guía propios; las demás usan el inglés de referencia.",
    "hi": "• 16 भाषाओं का चयनकर्ता: 11 विकल्पों में अपना इंटरफ़ेस कैटलॉग और मार्गदर्शक है; शेष विकल्प संदर्भ अंग्रेज़ी का उपयोग करते हैं।",
    "it": "• Selettore con 16 lingue: 11 opzioni hanno un catalogo dell’interfaccia e una guida dedicati; le altre usano l’inglese di riferimento.",
    "ja": "• 16言語の選択リスト：11項目には専用のインターフェースカタログとガイドがあり、その他は参照用の英語を使用します。",
    "nl": "• Taalkiezer met 16 opties: 11 opties hebben een eigen interfacecatalogus en handleiding; de overige gebruiken het Engelse referentietekst.",
    "pl": "• Selektor 16 języków: 11 opcji ma własny katalog interfejsu i przewodnik; pozostałe używają referencyjnego tekstu angielskiego.",
    "pt": "• Seletor com 16 idiomas: 11 opções têm um catálogo de interface e um guia próprios; as restantes usam o inglês de referência.",
    "ru": "• В списке 16 языков: для 11 вариантов есть собственный каталог интерфейса и руководство; остальные используют эталонный английский текст.",
}

VERSION_CHANGES_12225: dict[str, str] = {
    "de": "• Die Sprachauswahl enthält jetzt 16 Einträge.\n• Die 23 entfernten Sprachen werden in der Oberfläche nicht mehr angeboten.\n• Eine zuvor gespeicherte entfernte Auswahl fällt beim Start automatisch auf Französisch zurück.\n• Audio-Engine und Normalisierungsberechnungen bleiben unverändert.",
    "es": "• El selector de idioma contiene ahora 16 opciones.\n• Los 23 idiomas retirados ya no se ofrecen en la interfaz.\n• Una opción retirada que se hubiera guardado vuelve automáticamente al francés al iniciar.\n• El motor de audio y los cálculos de normalización no cambian.",
    "hi": "• भाषा चयनकर्ता में अब 16 विकल्प हैं।\n• हटाई गई 23 भाषाएँ अब इंटरफ़ेस में उपलब्ध नहीं हैं।\n• पहले सहेजा गया हटाया हुआ विकल्प शुरू होने पर अपने-आप फ़्रेंच पर लौटता है।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    "it": "• Il selettore della lingua contiene ora 16 opzioni.\n• Le 23 lingue rimosse non sono più proposte nell’interfaccia.\n• Una scelta rimossa salvata in precedenza torna automaticamente al francese all’avvio.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    "ja": "• 言語選択リストは16項目になりました。\n• 削除された23言語はインターフェースに表示されません。\n• 以前に保存された削除済みの選択は、起動時に自動的にフランス語へ戻ります。\n• 音声エンジンとノーマライズ計算は変更されていません。",
    "nl": "• De taalkiezer bevat nu 16 opties.\n• De 23 verwijderde talen worden niet meer in de interface aangeboden.\n• Een eerder opgeslagen verwijderde keuze valt bij het starten automatisch terug op Frans.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    "pl": "• Selektor języka zawiera teraz 16 opcji.\n• Usunięte 23 języki nie są już oferowane w interfejsie.\n• Wcześniej zapisany usunięty wybór po uruchomieniu automatycznie wraca do języka francuskiego.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    "pt": "• O seletor de idioma contém agora 16 opções.\n• Os 23 idiomas retirados já não são apresentados na interface.\n• Uma opção retirada que tenha sido guardada volta automaticamente ao francês no arranque.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    "ru": "• В списке выбора языка теперь 16 вариантов.\n• Удалённые 23 языка больше не предлагаются в интерфейсе.\n• Ранее сохранённый удалённый вариант при запуске автоматически заменяется французским.\n• Аудиодвижок и расчёты нормализации не изменены.",
}

for _language, _summary in LANGUAGE_SELECTOR_SUMMARIES_12225.items():
    _overview = EXTRA_TEXTS[_language]["help_overview"]
    EXTRA_TEXTS[_language]["help_overview"] = (
        _overview.rsplit("\n", 1)[0] + "\n" + _summary
    )
    EXTRA_TEXTS[_language]["version_changes"] = VERSION_CHANGES_12225[_language]


# Version 1.22.26 restores the original twelve native catalogues and their
# matching PDF guides.  These updates also keep the shortened source counter,
# multi-day completion estimate and release notes native in every catalogue.
TRANSLATION_UPDATES_12226: dict[str, dict[str, str]] = {
    "de": {
        "source_audio_count": "Dateien: {count}",
        "estimated_total_time_with_day_finish": "Geschätzte Gesamtzeit: {duration} — Ende am {date} gegen {time} (Wartezeit: {days} T {hours} Std.)",
        "help_overview": "• Sprachauswahl mit 12 Einträgen; jede Sprache besitzt einen eigenen Oberflächenkatalog und eine eigene PDF-Anleitung.",
        "version_changes": "• Die ursprünglichen 12 Sprachen und ihre 12 PDF-Anleitungen sind wiederhergestellt; Englisch ist beim ersten Start die Standardsprache.\n• Abstände der Einstellungen, −/+-Tasten und Ausrichtung des Lautheitsmessers wurden korrigiert.\n• Mehrtägige Schätzungen zeigen Datum und Wartezeit in Tagen/Stunden.\n• Das Protokoll ist vereinfacht und zeigt stets den tatsächlichen LUFS-Übergang; Abschlusszusammenfassungen werden nicht mehr abgeschnitten.\n• Audio-Engine und Normalisierungsberechnungen bleiben unverändert.",
    },
    "es": {
        "source_audio_count": "Archivos: {count}",
        "estimated_total_time_with_day_finish": "Tiempo total estimado: {duration} — finalización el {date} hacia las {time} (espera: {days} d {hours} h)",
        "help_overview": "• Selector de 12 idiomas; cada uno tiene su propio catálogo de interfaz y su guía PDF.",
        "version_changes": "• Se restauran los 12 idiomas originales y sus 12 guías PDF; el inglés es el idioma predeterminado en el primer inicio.\n• Se corrigen el espaciado de los ajustes, los botones −/+ y la alineación del medidor de sonoridad.\n• Las estimaciones de varios días muestran la fecha y la espera en días/horas.\n• El registro se simplifica y muestra siempre la transición LUFS real; los resúmenes finales ya no se truncan.\n• El motor de audio y los cálculos de normalización no cambian.",
    },
    "hi": {
        "source_audio_count": "फ़ाइलें: {count}",
        "estimated_total_time_with_day_finish": "अनुमानित कुल समय: {duration} — {date} को लगभग {time} पर समाप्ति (प्रतीक्षा: {days} दिन {hours} घंटे)",
        "help_overview": "• 12 भाषाओं का चयनकर्ता; हर भाषा का अपना इंटरफ़ेस कैटलॉग और PDF मार्गदर्शक है।",
        "version_changes": "• मूल 12 भाषाएँ और उनके 12 PDF मार्गदर्शक बहाल किए गए; पहली बार शुरू होने पर अंग्रेज़ी डिफ़ॉल्ट भाषा है।\n• सेटिंग पंक्तियों का अंतर, −/+ बटन और लाउडनेस मीटर का संरेखण सुधारा गया।\n• कई दिनों के अनुमान में तारीख और दिनों/घंटों की प्रतीक्षा दिखाई जाती है।\n• लॉग सरल किया गया है और वास्तविक LUFS परिवर्तन हमेशा दिखता है; समापन सारांश अब कटता नहीं है।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    },
    "it": {
        "source_audio_count": "File: {count}",
        "estimated_total_time_with_day_finish": "Tempo totale stimato: {duration} — fine il {date} verso le {time} (attesa: {days} g {hours} h)",
        "help_overview": "• Selettore con 12 lingue; ciascuna dispone del proprio catalogo dell’interfaccia e della propria guida PDF.",
        "version_changes": "• Sono ripristinate le 12 lingue originali e le relative 12 guide PDF; al primo avvio la lingua predefinita è l’inglese.\n• Sono corretti la spaziatura delle impostazioni, i pulsanti −/+ e l’allineamento del misuratore di sonorità.\n• Le stime su più giorni mostrano la data e l’attesa in giorni/ore.\n• Il registro è semplificato e mostra sempre la transizione LUFS effettiva; i riepiloghi finali non vengono più troncati.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    },
    "ja": {
        "source_audio_count": "ファイル：{count}",
        "estimated_total_time_with_day_finish": "推定合計時間：{duration} — {date} {time}頃に完了（待ち時間：{days}日 {hours}時間）",
        "help_overview": "• 12言語の選択リスト。各言語に専用のインターフェースカタログとPDFガイドがあります。",
        "version_changes": "• 元の12言語と12冊のPDFガイドを復元し、初回起動時の既定言語を英語にしました。\n• 設定行の間隔、−/+ボタン、ラウドネスメーターの配置を修正しました。\n• 複数日にわたる推定では、日付と待ち時間（日/時間）を表示します。\n• ログを簡素化し、実際のLUFS変化を常に表示します。完了概要が途中で切れなくなりました。\n• 音声エンジンとノーマライズ計算は変更されていません。",
    },
    "nl": {
        "source_audio_count": "Bestanden: {count}",
        "estimated_total_time_with_day_finish": "Geschatte totale tijd: {duration} — klaar rond {time} op {date} (wachttijd: {days} d {hours} u)",
        "help_overview": "• Taalkiezer met 12 opties; elke taal heeft een eigen interfacecatalogus en PDF-handleiding.",
        "version_changes": "• De oorspronkelijke 12 talen en hun 12 PDF-handleidingen zijn hersteld; bij de eerste start is Engels de standaardtaal.\n• De afstand tussen instellingen, de −/+-knoppen en de uitlijning van de luidheidsmeter zijn gecorrigeerd.\n• Schattingen over meerdere dagen tonen de datum en wachttijd in dagen/uren.\n• Het logboek is vereenvoudigd en toont altijd de werkelijke LUFS-overgang; eindsamenvattingen worden niet meer afgekapt.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    },
    "pl": {
        "source_audio_count": "Pliki: {count}",
        "estimated_total_time_with_day_finish": "Szacowany czas całkowity: {duration} — koniec {date} około {time} (oczekiwanie: {days} d {hours} godz.)",
        "help_overview": "• Selektor 12 języków; każdy ma własny katalog interfejsu i przewodnik PDF.",
        "version_changes": "• Przywrócono 12 pierwotnych języków i 12 odpowiadających im przewodników PDF; przy pierwszym uruchomieniu domyślny jest angielski.\n• Poprawiono odstępy ustawień, przyciski −/+ i wyrównanie miernika głośności.\n• Estymacje obejmujące kilka dni pokazują datę oraz czas oczekiwania w dniach/godzinach.\n• Dziennik uproszczono i zawsze pokazuje rzeczywistą zmianę LUFS; podsumowania końcowe nie są już obcinane.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    },
    "pt": {
        "source_audio_count": "Ficheiros: {count}",
        "estimated_total_time_with_day_finish": "Tempo total estimado: {duration} — fim em {date} por volta das {time} (espera: {days} d {hours} h)",
        "help_overview": "• Seletor com 12 idiomas; cada um tem o seu catálogo de interface e guia PDF.",
        "version_changes": "• Foram repostos os 12 idiomas originais e os respetivos 12 guias PDF; no primeiro arranque, o inglês é o idioma predefinido.\n• Foram corrigidos o espaçamento das definições, os botões −/+ e o alinhamento do medidor de sonoridade.\n• As estimativas de vários dias mostram a data e a espera em dias/horas.\n• O registo foi simplificado e mostra sempre a transição LUFS real; os resumos finais deixam de ficar truncados.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    },
    "ru": {
        "source_audio_count": "Файлы: {count}",
        "estimated_total_time_with_day_finish": "Общее расчётное время: {duration} — завершение {date} около {time} (ожидание: {days} д {hours} ч)",
        "help_overview": "• В списке 12 языков; для каждого есть собственный каталог интерфейса и руководство PDF.",
        "version_changes": "• Восстановлены исходные 12 языков и соответствующие 12 руководств PDF; при первом запуске по умолчанию используется английский.\n• Исправлены интервалы между настройками, кнопки −/+ и выравнивание индикатора громкости.\n• Для многодневных оценок отображаются дата и время ожидания в днях/часах.\n• Журнал упрощён и всегда показывает фактический переход LUFS; итоговые сводки больше не обрезаются.\n• Аудиодвижок и расчёты нормализации не изменены.",
    },
    "zh": {
        "source_audio_count": "文件：{count}",
        "estimated_total_time_with_day_finish": "预计总时间：{duration} — 将于 {date} {time} 左右完成（等待：{days} 天 {hours} 小时）",
        "help_overview": "• 语言选择器包含12种语言；每种语言都有专用的界面目录和PDF指南。",
        "version_changes": "• 恢复原有12种语言及其12份PDF指南；首次启动时默认使用英语。\n• 修正设置行间距、−/+按钮和响度表的对齐。\n• 跨多日的预计时间会显示日期以及需要等待的天数/小时数。\n• 简化日志并始终显示实际LUFS变化；完成摘要不再被截断。\n• 音频引擎和标准化计算保持不变。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12226.items():
    _overview_summary = _updates.pop("help_overview")
    _overview = EXTRA_TEXTS[_language]["help_overview"]
    EXTRA_TEXTS[_language]["help_overview"] = (
        _overview.rsplit("\n", 1)[0] + "\n" + _overview_summary
    )
    EXTRA_TEXTS[_language].update(_updates)


# Version 1.22.27 keeps the twelve-language contract while making the meter
# extrema periodic, shortening the estimate wording and documenting the
# compact results layout in every native catalogue.
TRANSLATION_UPDATES_12227: dict[str, dict[str, str]] = {
    "de": {
        "estimated_total_time_with_finish": "Geschätzte Gesamtzeit: {duration} — {time}",
        "estimated_total_time_with_day_finish": "Geschätzte Gesamtzeit: {duration} — {days} T, {time}",
        "loudness_meter_help_text": "Die rote Linie ist das Ziel. Blau zeigt die letzte nachgemessene Ausgabe. Min ist die niedrigste und Max die höchste Lautheit der aktuellen Gruppe; beide Werte beginnen nach jeweils 20 Ausgaben von vorn. Ohne Qualitätskontrolle bleibt die Anzeige inaktiv.",
        "loudness_meter_tooltip": "Die rote Linie ist das Ziel, Blau die letzte nachgemessene Ausgabe. Rechts gelten Min und Max für die aktuelle Gruppe und werden nach jeweils 20 Ausgaben sowie bei einem neuen Stapel zurückgesetzt.",
        "version_changes": "• Min und Max der Lautheitsanzeige werden nach jeder Gruppe von 20 Ausgaben zurückgesetzt.\n• Anzeige und Protokoll sind gleich hoch; die Wertung bleibt dicht an der Anzeige und die Hauptseite läuft nicht mehr über.\n• Die Schätzung zeigt nur noch die Anzahl der Tage und danach die erwartete Uhrzeit.\n• Abschlusssummaries haben keinen schwarzen Hintergrund mehr; die Schnellstart-Titel der Anleitungen wurden nach unten versetzt.\n• Audio-Engine und Normalisierungsberechnungen bleiben unverändert.",
    },
    "es": {
        "estimated_total_time_with_finish": "Tiempo total estimado: {duration} — {time}",
        "estimated_total_time_with_day_finish": "Tiempo total estimado: {duration} — {days} d, {time}",
        "loudness_meter_help_text": "La línea roja es el objetivo y el valor azul es la última salida medida de nuevo. Min es la sonoridad más baja y Max la más alta del grupo actual; ambos valores se reinician después de cada 20 salidas. Sin control de calidad, el medidor queda inactivo.",
        "loudness_meter_tooltip": "La línea roja es el objetivo y el valor azul sigue la última salida medida de nuevo. A la derecha, Min y Max corresponden al grupo actual y se reinician cada 20 salidas y al comenzar un lote nuevo.",
        "version_changes": "• Min y Max del medidor se reinician después de cada grupo de 20 salidas.\n• El medidor y el registro tienen la misma altura; la puntuación queda junto al medidor y la página principal ya no desborda.\n• La estimación muestra simplemente el número de días seguido de la hora prevista.\n• Los resúmenes finales ya no tienen fondo negro y los títulos de inicio rápido de las guías se han bajado.\n• El motor de audio y los cálculos de normalización no cambian.",
    },
    "hi": {
        "estimated_total_time_with_finish": "अनुमानित कुल समय: {duration} — {time}",
        "estimated_total_time_with_day_finish": "अनुमानित कुल समय: {duration} — {days} दिन, {time}",
        "loudness_meter_help_text": "लाल रेखा लक्ष्य है और नीला मान अंतिम दोबारा मापा गया आउटपुट है। Min वर्तमान समूह की सबसे कम और Max सबसे अधिक लाउडनेस है; हर 20 आउटपुट के बाद दोनों मान फिर से शुरू होते हैं। गुणवत्ता जाँच बंद होने पर मीटर निष्क्रिय रहता है।",
        "loudness_meter_tooltip": "लाल रेखा लक्ष्य है और नीला मान अंतिम दोबारा मापा गया आउटपुट है। दाईं ओर Min और Max वर्तमान समूह के लिए हैं और हर 20 आउटपुट तथा नए बैच की शुरुआत पर रीसेट होते हैं।",
        "version_changes": "• मीटर के Min और Max हर 20 आउटपुट के समूह के बाद रीसेट होते हैं।\n• मीटर और लॉग की ऊँचाई समान है; स्कोर मीटर के पास रहता है और मुख्य पृष्ठ अब बाहर नहीं निकलता।\n• अनुमान केवल दिनों की संख्या और उसके बाद अपेक्षित समय दिखाता है।\n• अंतिम सारांश में अब काला पृष्ठभूमि नहीं है और मार्गदर्शकों के त्वरित शुरुआत शीर्षक नीचे किए गए हैं।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    },
    "it": {
        "estimated_total_time_with_finish": "Tempo totale stimato: {duration} — {time}",
        "estimated_total_time_with_day_finish": "Tempo totale stimato: {duration} — {days} g, {time}",
        "loudness_meter_help_text": "La linea rossa è l’obiettivo e il valore blu è l’ultima uscita rimisurata. Min è la sonorità più bassa e Max la più alta del gruppo corrente; entrambi i valori ripartono dopo ogni 20 uscite. Senza controllo qualità il misuratore resta inattivo.",
        "loudness_meter_tooltip": "La linea rossa è l’obiettivo e il valore blu segue l’ultima uscita rimisurata. A destra, Min e Max riguardano il gruppo corrente e si azzerano ogni 20 uscite e all’inizio di un nuovo lotto.",
        "version_changes": "• Min e Max del misuratore si azzerano dopo ogni gruppo di 20 uscite.\n• Misuratore e registro hanno la stessa altezza; il punteggio resta vicino al misuratore e la pagina principale non deborda più.\n• La stima mostra semplicemente il numero di giorni seguito dall’ora prevista.\n• I riepiloghi finali non hanno più uno sfondo nero e i titoli di avvio rapido delle guide sono stati abbassati.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    },
    "ja": {
        "estimated_total_time_with_finish": "推定合計時間：{duration} — {time}",
        "estimated_total_time_with_day_finish": "推定合計時間：{duration} — {days}日、{time}",
        "loudness_meter_help_text": "赤線は目標、青値は最後に再測定した出力です。Min は現在のグループの最小ラウドネス、Max は最大ラウドネスで、20出力ごとに両方の値がリセットされます。品質管理が無効な場合、メーターは動作しません。",
        "loudness_meter_tooltip": "赤線は目標、青値は最後に再測定した出力です。右側の Min と Max は現在のグループを対象とし、20出力ごと、および新しいバッチの開始時にリセットされます。",
        "version_changes": "• メーターの Min と Max は20出力ごとにリセットされます。\n• メーターとログの高さをそろえ、スコアをメーターの近くに配置し、メイン画面のはみ出しを解消しました。\n• 推定表示は日数と、その後に予定時刻だけを示します。\n• 完了概要の黒い背景をなくし、ガイドのクイックスタート見出しを下げました。\n• 音声エンジンとノーマライズ計算は変更されていません。",
    },
    "nl": {
        "estimated_total_time_with_finish": "Geschatte totale tijd: {duration} — {time}",
        "estimated_total_time_with_day_finish": "Geschatte totale tijd: {duration} — {days} d, {time}",
        "loudness_meter_help_text": "De rode lijn is het doel en de blauwe waarde is de laatst opnieuw gemeten uitvoer. Min is de laagste en Max de hoogste luidheid van de huidige groep; beide waarden beginnen na elke 20 uitvoerbestanden opnieuw. Zonder kwaliteitscontrole blijft de meter inactief.",
        "loudness_meter_tooltip": "De rode lijn is het doel en blauw volgt de laatst opnieuw gemeten uitvoer. Rechts gelden Min en Max voor de huidige groep; ze worden na elke 20 uitvoerbestanden en bij een nieuwe reeks gewist.",
        "version_changes": "• Min en Max van de meter worden na elke groep van 20 uitvoerbestanden gewist.\n• Meter en logboek hebben dezelfde hoogte; de score blijft dicht bij de meter en de hoofdpagina loopt niet meer over.\n• De schatting toont alleen het aantal dagen, gevolgd door het verwachte tijdstip.\n• Eindsamenvattingen hebben geen zwarte achtergrond meer en de titels voor snel starten in de handleidingen zijn verlaagd.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    },
    "pl": {
        "estimated_total_time_with_finish": "Szacowany czas całkowity: {duration} — {time}",
        "estimated_total_time_with_day_finish": "Szacowany czas całkowity: {duration} — {days} d, {time}",
        "loudness_meter_help_text": "Czerwona linia oznacza cel, a niebieska wartość ostatni ponownie zmierzony wynik. Min to najniższa, a Max najwyższa głośność bieżącej grupy; obie wartości są zerowane po każdych 20 wynikach. Bez kontroli jakości miernik jest nieaktywny.",
        "loudness_meter_tooltip": "Czerwona linia oznacza cel, a niebieska wartość ostatni ponownie zmierzony wynik. Po prawej Min i Max dotyczą bieżącej grupy i są zerowane co 20 wyników oraz przy rozpoczęciu nowej serii.",
        "version_changes": "• Min i Max miernika są zerowane po każdej grupie 20 wyników.\n• Miernik i dziennik mają tę samą wysokość; wynik pozostaje blisko miernika, a strona główna już nie wychodzi poza okno.\n• Estymacja pokazuje tylko liczbę dni, a następnie przewidywaną godzinę.\n• Podsumowania końcowe nie mają już czarnego tła, a tytuły szybkiego startu w przewodnikach przesunięto niżej.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    },
    "pt": {
        "estimated_total_time_with_finish": "Tempo total estimado: {duration} — {time}",
        "estimated_total_time_with_day_finish": "Tempo total estimado: {duration} — {days} d, {time}",
        "loudness_meter_help_text": "A linha vermelha é o alvo e o valor azul é a última saída novamente medida. Min é a sonoridade mais baixa e Max a mais alta do grupo atual; ambos os valores recomeçam após cada 20 saídas. Sem controlo de qualidade, o medidor fica inativo.",
        "loudness_meter_tooltip": "A linha vermelha é o alvo e o valor azul segue a última saída novamente medida. À direita, Min e Max referem-se ao grupo atual e reiniciam a cada 20 saídas e no início de um novo lote.",
        "version_changes": "• Min e Max do medidor reiniciam após cada grupo de 20 saídas.\n• O medidor e o registo têm a mesma altura; a pontuação fica junto ao medidor e a página principal deixa de transbordar.\n• A estimativa mostra apenas o número de dias seguido da hora prevista.\n• Os resumos finais deixam de ter fundo preto e os títulos de início rápido dos guias foram deslocados para baixo.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    },
    "ru": {
        "estimated_total_time_with_finish": "Общее расчётное время: {duration} — {time}",
        "estimated_total_time_with_day_finish": "Общее расчётное время: {duration} — {days} д, {time}",
        "loudness_meter_help_text": "Красная линия — цель, синее значение — последний повторно измеренный результат. Min — минимальная, Max — максимальная громкость текущей группы; оба значения сбрасываются после каждых 20 результатов. Без контроля качества индикатор неактивен.",
        "loudness_meter_tooltip": "Красная линия — цель, синее значение — последний повторно измеренный результат. Справа Min и Max относятся к текущей группе и сбрасываются каждые 20 результатов, а также в начале новой серии.",
        "version_changes": "• Min и Max индикатора сбрасываются после каждой группы из 20 результатов.\n• Индикатор и журнал имеют одинаковую высоту; оценка расположена рядом с индикатором, а главная страница больше не выходит за границы окна.\n• Расчёт показывает только число дней, а затем ожидаемое время.\n• У итоговых сводок больше нет чёрного фона, а заголовки быстрого старта в руководствах опущены ниже.\n• Аудиодвижок и расчёты нормализации не изменены.",
    },
    "zh": {
        "estimated_total_time_with_finish": "预计总时间：{duration} — {time}",
        "estimated_total_time_with_day_finish": "预计总时间：{duration} — {days} 天，{time}",
        "loudness_meter_help_text": "红线是目标，蓝色数值是最后一个重新测量的输出。Min 是当前组的最低响度，Max 是最高响度；每20个输出后这两个值都会重新开始。关闭质量控制时，电平表保持不活动。",
        "loudness_meter_tooltip": "红线是目标，蓝色数值跟随最后一个重新测量的输出。右侧 Min 和 Max 对应当前组，每20个输出以及新批次开始时都会重置。",
        "version_changes": "• 电平表的 Min 和 Max 每20个输出重置一次。\n• 电平表与日志高度一致，评分紧邻电平表，主页面不再溢出。\n• 预计时间只显示天数，后面接预计时刻。\n• 完成摘要不再有黑色背景，指南的快速开始标题已下移。\n• 音频引擎和标准化计算保持不变。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12227.items():
    EXTRA_TEXTS[_language].update(_updates)


# Version 1.22.28 adds compact status lights for the six workflow options and
# makes the meter panel fixed-height while leaving the processing log elastic.
VERSION_CHANGES_12228: dict[str, str] = {
    "de": "• Sechs kompakte Statusleuchten zeigen ständig den Zustand der Optionen OVR, SKP, RES, QC, CSV und AUT.\n• Der Rahmen der Lautheitsanzeige behält beim Vergrößern des Hauptfensters eine feste Höhe; nur das Verarbeitungsprotokoll wächst.\n• Der Ergebnisbereich bleibt innerhalb des Fensters und erzwingt bei der normalen Startgröße keinen vertikalen Bildlauf mehr.\n• Audio-Engine und Normalisierungsberechnungen bleiben unverändert.",
    "es": "• Seis luces compactas reflejan continuamente el estado de las opciones OVR, SKP, RES, QC, CSV y AUT.\n• El marco del medidor de sonoridad conserva una altura fija al ampliar la ventana principal; solo se expande el registro de procesamiento.\n• La zona de resultados permanece dentro de la ventana y ya no obliga a mostrar una barra de desplazamiento vertical con el tamaño inicial normal.\n• El motor de audio y los cálculos de normalización no cambian.",
    "hi": "• छह छोटे संकेतक OVR, SKP, RES, QC, CSV और AUT विकल्पों की स्थिति लगातार दिखाते हैं।\n• मुख्य विंडो बड़ी करने पर लाउडनेस मीटर का फ़्रेम निश्चित ऊँचाई पर रहता है; केवल प्रोसेसिंग लॉग फैलता है।\n• परिणाम क्षेत्र विंडो के भीतर रहता है और सामान्य शुरुआती आकार पर अब ऊर्ध्व स्क्रॉलबार आवश्यक नहीं होता।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    "it": "• Sei spie compatte mostrano continuamente lo stato delle opzioni OVR, SKP, RES, QC, CSV e AUT.\n• Il riquadro del misuratore di sonorità mantiene un’altezza fissa quando la finestra principale viene ingrandita; si espande solo il registro di elaborazione.\n• L’area dei risultati resta dentro la finestra e non impone più una barra di scorrimento verticale alle normali dimensioni iniziali.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    "ja": "• 6個の小さなランプが OVR、SKP、RES、QC、CSV、AUT の各オプションの状態を常に示します。\n• メインウィンドウを広げてもラウドネスメーター枠の高さは固定され、処理ログだけが拡張されます。\n• 結果領域はウィンドウ内に収まり、通常の起動サイズでは縦スクロールバーが不要になりました。\n• 音声エンジンとノーマライズ計算は変更されていません。",
    "nl": "• Zes compacte lampjes tonen voortdurend de status van de opties OVR, SKP, RES, QC, CSV en AUT.\n• Het kader van de luidheidsmeter houdt een vaste hoogte wanneer het hoofdvenster wordt vergroot; alleen het verwerkingslogboek groeit mee.\n• Het resultatengedeelte blijft binnen het venster en veroorzaakt bij de normale startgrootte geen verticale schuifbalk meer.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    "pl": "• Sześć małych kontrolek stale pokazuje stan opcji OVR, SKP, RES, QC, CSV i AUT.\n• Ramka miernika głośności zachowuje stałą wysokość po powiększeniu głównego okna; rozszerza się tylko dziennik przetwarzania.\n• Obszar wyników pozostaje w granicach okna i przy zwykłym rozmiarze początkowym nie wymusza już pionowego paska przewijania.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    "pt": "• Seis luzes compactas refletem continuamente o estado das opções OVR, SKP, RES, QC, CSV e AUT.\n• O quadro do medidor de sonoridade mantém uma altura fixa ao ampliar a janela principal; apenas o registo de processamento se expande.\n• A área de resultados permanece dentro da janela e deixa de impor uma barra de deslocamento vertical no tamanho inicial normal.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    "ru": "• Шесть компактных индикаторов постоянно показывают состояние параметров OVR, SKP, RES, QC, CSV и AUT.\n• Рамка индикатора громкости сохраняет фиксированную высоту при увеличении главного окна; расширяется только журнал обработки.\n• Область результатов остаётся в пределах окна и при обычном начальном размере больше не требует вертикальной полосы прокрутки.\n• Аудиодвижок и расчёты нормализации не изменены.",
    "zh": "• 六个紧凑指示灯持续显示 OVR、SKP、RES、QC、CSV 和 AUT 选项的状态。\n• 放大主窗口时，响度表框架保持固定高度；只有处理日志会扩展。\n• 结果区域保持在窗口内，正常启动尺寸下不再需要垂直滚动条。\n• 音频引擎和标准化计算保持不变。",
}

for _language, _changes in VERSION_CHANGES_12228.items():
    EXTRA_TEXTS[_language]["version_changes"] = _changes


# Version 1.22.29 keeps extrema exact over a short rolling window, localizes
# the six compact indicators and uses locale-appropriate full stops in the
# multi-day estimate.
TRANSLATION_UPDATES_12229: dict[str, dict[str, str]] = {
    "de": {
        "estimated_total_time_with_day_finish": "Geschätzte Gesamtzeit: {duration} — {days} T. {time}",
        "loudness_meter_help_text": "Die rote Linie ist das Ziel. Blau zeigt die letzte nachgemessene Ausgabe. Min und Max beziehen sich fortlaufend auf die letzten 8 nachgemessenen Ausgaben; mit jeder neuen Messung entfällt die älteste. Ohne Qualitätskontrolle bleibt die Anzeige inaktiv.",
        "loudness_meter_tooltip": "Die rote Linie ist das Ziel, Blau die letzte nachgemessene Ausgabe. Rechts werden Min und Max über ein gleitendes Fenster der letzten 8 Ausgaben sowie bei einem neuen Stapel neu berechnet.",
        "option_status_overwrite": "ÜBS",
        "option_status_skip_compliant": "NNC",
        "option_status_resume": "FOR",
        "option_status_quality_control": "QK",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUT",
        "version_changes": "• Mehrtägige Schätzungen verwenden nach der Tageszahl einen Punkt.\n• Min und Max werden über die letzten 8 Ausgaben neu berechnet und bleiben dadurch beweglich.\n• Die sechs Leuchten sind etwas größer, plastischer und in der gewählten Sprache beschriftet.\n• Das Startfenster passt sich dem Inhalt an; danach wächst nur das Protokoll, die Anzeige bleibt fest.\n• In allen zwölf Anleitungen steht die Versionsnummer in Schrift und Grundlinie des Untertitels.\n• Audio-Engine und Normalisierungsberechnungen bleiben unverändert.",
    },
    "es": {
        "estimated_total_time_with_day_finish": "Tiempo total estimado: {duration} — {days} d. {time}",
        "loudness_meter_help_text": "La línea roja es el objetivo y el valor azul es la última salida medida de nuevo. Min y Max abarcan continuamente las 8 últimas salidas medidas; cada nueva medición elimina la más antigua. Sin control de calidad, el medidor queda inactivo.",
        "loudness_meter_tooltip": "La línea roja es el objetivo y el valor azul sigue la última salida medida de nuevo. A la derecha, Min y Max se recalculan sobre una ventana móvil de las 8 últimas salidas y al comenzar un lote nuevo.",
        "option_status_overwrite": "SOB",
        "option_status_skip_compliant": "NRC",
        "option_status_resume": "REA",
        "option_status_quality_control": "CC",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUT",
        "version_changes": "• Las estimaciones de varios días usan un punto después del número de días.\n• Min y Max se recalculan sobre las 8 últimas salidas para mantenerse dinámicos.\n• Las seis luces son algo mayores, tienen relieve y usan abreviaturas del idioma elegido.\n• La ventana inicial se ajusta al contenido; después solo crece el registro y el medidor queda fijo.\n• Las doce guías alinean la versión con la tipografía del subtítulo.\n• El motor de audio y los cálculos de normalización no cambian.",
    },
    "hi": {
        "estimated_total_time_with_day_finish": "अनुमानित कुल समय: {duration} — {days} दिन। {time}",
        "loudness_meter_help_text": "लाल रेखा लक्ष्य है और नीला मान अंतिम दोबारा मापा गया आउटपुट है। Min और Max लगातार अंतिम 8 दोबारा मापे गए आउटपुट पर आधारित हैं; हर नई माप के साथ सबसे पुरानी माप हट जाती है। गुणवत्ता जाँच बंद होने पर मीटर निष्क्रिय रहता है।",
        "loudness_meter_tooltip": "लाल रेखा लक्ष्य है और नीला मान अंतिम दोबारा मापा गया आउटपुट है। दाईं ओर Min और Max की गणना अंतिम 8 आउटपुट की चलती विंडो पर और नए बैच की शुरुआत में फिर से होती है।",
        "option_status_overwrite": "अधि",
        "option_status_skip_compliant": "अनु",
        "option_status_resume": "जारी",
        "option_status_quality_control": "गुण",
        "option_status_report": "CSV",
        "option_status_auto_start": "स्व",
        "version_changes": "• कई दिनों के अनुमान में दिनों की संख्या के बाद पूर्ण विराम है।\n• Min और Max अंतिम 8 आउटपुट पर फिर से गिने जाते हैं ताकि वे गतिशील रहें।\n• छह लाइटें थोड़ी बड़ी, उभरी हुई और चुनी गई भाषा के संक्षेपों वाली हैं।\n• आरंभ में विंडो सामग्री के अनुसार बैठती है; बाद में केवल लॉग बढ़ता है और मीटर स्थिर रहता है।\n• सभी बारह गाइडों में संस्करण संख्या उपशीर्षक की फ़ॉन्ट और आधार रेखा पर है।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    },
    "it": {
        "estimated_total_time_with_day_finish": "Tempo totale stimato: {duration} — {days} g. {time}",
        "loudness_meter_help_text": "La linea rossa è l’obiettivo e il valore blu è l’ultima uscita rimisurata. Min e Max coprono sempre le 8 uscite rimisurate più recenti; ogni nuova misura elimina la più vecchia. Senza controllo qualità il misuratore resta inattivo.",
        "loudness_meter_tooltip": "La linea rossa è l’obiettivo e il valore blu segue l’ultima uscita rimisurata. A destra, Min e Max vengono ricalcolati su una finestra mobile delle ultime 8 uscite e all’inizio di un nuovo lotto.",
        "option_status_overwrite": "SOV",
        "option_status_skip_compliant": "NRC",
        "option_status_resume": "RIP",
        "option_status_quality_control": "CQ",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUT",
        "version_changes": "• Le stime su più giorni usano un punto dopo il numero di giorni.\n• Min e Max vengono ricalcolati sulle ultime 8 uscite e restano dinamici.\n• Le sei spie sono leggermente più grandi, in rilievo e abbreviate nella lingua scelta.\n• La finestra iniziale si adatta al contenuto; poi cresce solo il registro e il misuratore resta fisso.\n• Le dodici guide allineano la versione alla tipografia del sottotitolo.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    },
    "ja": {
        "estimated_total_time_with_day_finish": "推定合計時間：{duration} — {days}日。{time}",
        "loudness_meter_help_text": "赤線は目標、青値は最後に再測定した出力です。Min と Max は常に直近8件の再測定出力を対象とし、新しい測定が入るたびに最も古い値が外れます。品質管理が無効な場合、メーターは動作しません。",
        "loudness_meter_tooltip": "赤線は目標、青値は最後に再測定した出力です。右側の Min と Max は直近8出力の移動窓と、新しいバッチの開始時に再計算されます。",
        "option_status_overwrite": "上書",
        "option_status_skip_compliant": "適合",
        "option_status_resume": "再開",
        "option_status_quality_control": "品質",
        "option_status_report": "CSV",
        "option_status_auto_start": "自動",
        "version_changes": "• 複数日にわたる推定では日数の後に句点を表示します。\n• Min と Max を直近8出力で再計算し、動きが止まりにくくしました。\n• 6個のランプを少し大きく立体的にし、選択言語の略記を表示します。\n• 起動時に内容へ合わせ、以後はログだけが伸びてメーターは固定されます。\n• 12冊すべてでバージョン番号を副題と同じ書体・基準線に揃えました。\n• 音声エンジンとノーマライズ計算は変更されていません。",
    },
    "nl": {
        "estimated_total_time_with_day_finish": "Geschatte totale tijd: {duration} — {days} d. {time}",
        "loudness_meter_help_text": "De rode lijn is het doel en de blauwe waarde is de laatst opnieuw gemeten uitvoer. Min en Max omvatten steeds de 8 recentste opnieuw gemeten uitvoerbestanden; bij elke nieuwe meting valt de oudste weg. Zonder kwaliteitscontrole blijft de meter inactief.",
        "loudness_meter_tooltip": "De rode lijn is het doel en blauw volgt de laatst opnieuw gemeten uitvoer. Rechts worden Min en Max opnieuw berekend over een voortschrijdend venster van de laatste 8 uitvoerbestanden en bij een nieuwe reeks.",
        "option_status_overwrite": "OVS",
        "option_status_skip_compliant": "NOC",
        "option_status_resume": "HER",
        "option_status_quality_control": "KC",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUT",
        "version_changes": "• Meerdaagse schattingen gebruiken een punt na het aantal dagen.\n• Min en Max worden over de laatste 8 uitvoerbestanden herberekend en blijven zo dynamisch.\n• De zes lampjes zijn iets groter, plastischer en afgekort in de gekozen taal.\n• Het startvenster past bij de inhoud; daarna groeit alleen het logboek en blijft de meter vast.\n• In alle twaalf handleidingen staat de versie op dezelfde basislijn en in hetzelfde lettertype als de ondertitel.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    },
    "pl": {
        "estimated_total_time_with_day_finish": "Szacowany czas całkowity: {duration} — {days} d. {time}",
        "loudness_meter_help_text": "Czerwona linia oznacza cel, a niebieska wartość ostatni ponownie zmierzony wynik. Min i Max stale obejmują 8 ostatnich ponownie zmierzonych wyników; każda nowa miara usuwa najstarszą. Bez kontroli jakości miernik jest nieaktywny.",
        "loudness_meter_tooltip": "Czerwona linia oznacza cel, a niebieska wartość ostatni ponownie zmierzony wynik. Po prawej Min i Max są przeliczane w ruchomym oknie 8 ostatnich wyników oraz przy rozpoczęciu nowej serii.",
        "option_status_overwrite": "NAD",
        "option_status_skip_compliant": "NKP",
        "option_status_resume": "WZN",
        "option_status_quality_control": "KJ",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUT",
        "version_changes": "• Estymacje wielodniowe używają kropki po liczbie dni.\n• Min i Max są przeliczane dla 8 ostatnich wyników, dzięki czemu pozostają dynamiczne.\n• Sześć kontrolek jest nieco większych, przestrzennych i opisanych skrótami w wybranym języku.\n• Okno startowe dopasowuje się do treści; potem rośnie tylko dziennik, a miernik pozostaje stały.\n• We wszystkich dwunastu przewodnikach wersja ma krój i linię bazową podtytułu.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    },
    "pt": {
        "estimated_total_time_with_day_finish": "Tempo total estimado: {duration} — {days} d. {time}",
        "loudness_meter_help_text": "A linha vermelha é o alvo e o valor azul é a última saída novamente medida. Min e Max abrangem sempre as 8 saídas novamente medidas mais recentes; cada nova medição retira a mais antiga. Sem controlo de qualidade, o medidor fica inativo.",
        "loudness_meter_tooltip": "A linha vermelha é o alvo e o valor azul segue a última saída novamente medida. À direita, Min e Max são recalculados numa janela móvel das últimas 8 saídas e no início de um novo lote.",
        "option_status_overwrite": "SUB",
        "option_status_skip_compliant": "NRC",
        "option_status_resume": "RET",
        "option_status_quality_control": "CQ",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUT",
        "version_changes": "• As estimativas de vários dias usam um ponto após o número de dias.\n• Min e Max são recalculados nas últimas 8 saídas para permanecerem dinâmicos.\n• As seis luzes são ligeiramente maiores, em relevo e abreviadas no idioma escolhido.\n• A janela inicial ajusta-se ao conteúdo; depois apenas o registo cresce e o medidor fica fixo.\n• Os doze guias alinham a versão com a tipografia do subtítulo.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    },
    "ru": {
        "estimated_total_time_with_day_finish": "Общее расчётное время: {duration} — {days} д. {time}",
        "loudness_meter_help_text": "Красная линия — цель, синее значение — последний повторно измеренный результат. Min и Max постоянно охватывают 8 последних повторно измеренных результатов; при каждом новом измерении самое старое исключается. Без контроля качества индикатор неактивен.",
        "loudness_meter_tooltip": "Красная линия — цель, синее значение — последний повторно измеренный результат. Справа Min и Max пересчитываются в скользящем окне 8 последних результатов и в начале новой серии.",
        "option_status_overwrite": "ПЕР",
        "option_status_skip_compliant": "НПК",
        "option_status_resume": "ВОЗ",
        "option_status_quality_control": "КК",
        "option_status_report": "CSV",
        "option_status_auto_start": "АВТ",
        "version_changes": "• В многодневном расчёте после числа дней ставится точка.\n• Min и Max пересчитываются по 8 последним результатам и остаются динамичными.\n• Шесть индикаторов стали немного крупнее и объёмнее, а подписи переведены.\n• Начальное окно подстраивается под содержимое; затем растёт только журнал, индикатор остаётся фиксированным.\n• Во всех двенадцати руководствах номер версии выровнен и набран шрифтом подзаголовка.\n• Аудиодвижок и расчёты нормализации не изменены.",
    },
    "zh": {
        "estimated_total_time_with_day_finish": "预计总时间：{duration} — {days} 天。{time}",
        "loudness_meter_help_text": "红线是目标，蓝色数值是最后一个重新测量的输出。Min 和 Max 始终对应最近8个重新测量的输出；每加入一个新测量值，最旧的值就会移出。关闭质量控制时，电平表保持不活动。",
        "loudness_meter_tooltip": "红线是目标，蓝色数值跟随最后一个重新测量的输出。右侧 Min 和 Max 会按最近8个输出的滑动窗口以及新批次开始时重新计算。",
        "option_status_overwrite": "覆盖",
        "option_status_skip_compliant": "合规",
        "option_status_resume": "继续",
        "option_status_quality_control": "质控",
        "option_status_report": "CSV",
        "option_status_auto_start": "自动",
        "version_changes": "• 多日预计在天数后使用句号。\n• Min 和 Max 按最近8个输出重新计算，保持动态。\n• 六个指示灯略微增大并呈立体效果，缩写随所选语言变化。\n• 启动窗口按内容调整；之后只有日志增高，响度表保持固定。\n• 十二份指南中的版本号均与副标题使用同一字体和基线。\n• 音频引擎和标准化计算保持不变。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12229.items():
    EXTRA_TEXTS[_language].update(_updates)


# Version 1.23.0 adopts semantic minor releases for visible compatible
# functionality and renders every processing status from a language-neutral
# code.  The same localized abbreviations are used above the tabs and inside
# the six rows of the Options tab.
TRANSLATION_UPDATES_12300: dict[str, dict[str, str]] = {
    "de": {
        "status_ok": "ERFOLG",
        "qc_ok": "ERFOLG",
        "status_warning": "WARNUNG",
        "version_changes": (
            "• Die Abkürzungen der sechs Optionen stehen jetzt auch in jeder Zeile des Registers Optionen.\n"
            "• Gesamtdauer und Endzeit werden im 24-Stunden-Format angezeigt.\n"
            "• Alle Protokollzustände, einschließlich Erfolg und Warnung, werden sprachgerecht angezeigt.\n"
            "• Die runden Leuchten haben mehr Abstand und bleiben im hellen Modus lesbar.\n"
            "• Protokoll und Anzeige sind beim Start gleich hoch; danach wächst nur das Protokoll.\n"
            "• Die Einstellungsidentität verwendet nur noch LUFScale; der letzte Anhang trägt einen allgemeinen Titel."
        ),
    },
    "es": {
        "status_ok": "CORRECTO",
        "qc_ok": "CORRECTO",
        "status_warning": "AVISO",
        "version_changes": (
            "• Las abreviaturas de las seis opciones aparecen también en cada fila de la pestaña Opciones.\n"
            "• La duración total y la hora de fin usan el formato de 24 horas.\n"
            "• Todos los estados del registro, incluidos éxito y aviso, se muestran en el idioma elegido.\n"
            "• Las luces redondas tienen más espacio y siguen siendo legibles en modo claro.\n"
            "• El registro y el medidor tienen la misma altura al inicio; después solo crece el registro.\n"
            "• La identidad de preferencias usa solo LUFScale y el último anexo tiene un título general."
        ),
    },
    "hi": {
        "status_ok": "सफल",
        "qc_ok": "सफल",
        "status_warning": "चेतावनी",
        "version_changes": (
            "• छह विकल्पों के संक्षेप अब विकल्प टैब की हर पंक्ति में भी दिखते हैं।\n"
            "• कुल अवधि और समाप्ति समय 24-घंटे के प्रारूप में दिखते हैं।\n"
            "• सफलता और चेतावनी सहित सभी लॉग स्थितियाँ चुनी गई भाषा में दिखती हैं।\n"
            "• गोल संकेतकों के नीचे अधिक जगह है और वे हल्के मोड में भी स्पष्ट हैं।\n"
            "• आरंभ में लॉग और मीटर की ऊँचाई समान है; बाद में केवल लॉग बढ़ता है।\n"
            "• प्राथमिकता पहचान में अब केवल LUFScale है और अंतिम परिशिष्ट का शीर्षक सामान्य है।"
        ),
    },
    "it": {
        "status_ok": "RIUSCITO",
        "qc_ok": "RIUSCITO",
        "status_warning": "AVVISO",
        "version_changes": (
            "• Le abbreviazioni delle sei opzioni compaiono anche in ogni riga della scheda Opzioni.\n"
            "• Durata totale e ora di fine usano il formato 24 ore.\n"
            "• Tutti gli stati del registro, inclusi riuscito e avviso, seguono la lingua scelta.\n"
            "• Le spie rotonde sono più distanziate e leggibili in modalità chiara.\n"
            "• Registro e misuratore hanno la stessa altezza all’avvio; poi cresce solo il registro.\n"
            "• L’identità delle preferenze usa solo LUFScale e l’ultima appendice ha un titolo generale."
        ),
    },
    "ja": {
        "status_ok": "成功",
        "qc_ok": "成功",
        "status_warning": "警告",
        "version_changes": (
            "• 6項目の略記をオプションタブの各行にも表示します。\n"
            "• 合計時間と終了時刻を24時間形式で表示します。\n"
            "• 成功、警告を含むすべてのログ状態を選択言語で表示します。\n"
            "• 丸いランプの下に余白を設け、ライトモードでも読みやすくしました。\n"
            "• 起動時はログとメーターを同じ高さにし、その後はログだけが伸びます。\n"
            "• 設定の識別名は LUFScale のみとなり、最後の付録名を一般化しました。"
        ),
    },
    "nl": {
        "status_ok": "GESLAAGD",
        "qc_ok": "GESLAAGD",
        "status_warning": "WAARSCHUWING",
        "version_changes": (
            "• De afkortingen van de zes opties staan nu ook in elke rij van het tabblad Opties.\n"
            "• Totale duur en eindtijd worden in 24-uursnotatie getoond.\n"
            "• Alle logstatussen, waaronder geslaagd en waarschuwing, volgen de gekozen taal.\n"
            "• De ronde lampjes hebben meer tussenruimte en blijven leesbaar in lichte modus.\n"
            "• Logboek en meter zijn bij het starten even hoog; daarna groeit alleen het logboek.\n"
            "• De voorkeursidentiteit gebruikt alleen LUFScale en de laatste bijlage heeft een algemene titel."
        ),
    },
    "pl": {
        "status_ok": "SUKCES",
        "qc_ok": "SUKCES",
        "status_warning": "OSTRZEŻENIE",
        "version_changes": (
            "• Skróty sześciu opcji są widoczne także w każdym wierszu karty Opcje.\n"
            "• Łączny czas i godzina zakończenia są wyświetlane w formacie 24-godzinnym.\n"
            "• Wszystkie stany dziennika, w tym sukces i ostrzeżenie, są wyświetlane w wybranym języku.\n"
            "• Okrągłe kontrolki mają większy odstęp i są czytelne w trybie jasnym.\n"
            "• Przy starcie dziennik i miernik mają tę samą wysokość; później rośnie tylko dziennik.\n"
            "• Identyfikator preferencji używa tylko nazwy LUFScale, a ostatni dodatek ma ogólny tytuł."
        ),
    },
    "pt": {
        "status_ok": "SUCESSO",
        "qc_ok": "SUCESSO",
        "status_warning": "AVISO",
        "version_changes": (
            "• As abreviaturas das seis opções aparecem também em cada linha do separador Opções.\n"
            "• A duração total e a hora de fim usam o formato de 24 horas.\n"
            "• Todos os estados do registo, incluindo sucesso e aviso, seguem o idioma escolhido.\n"
            "• As luzes redondas têm mais espaço e continuam legíveis no modo claro.\n"
            "• O registo e o medidor têm a mesma altura ao iniciar; depois só o registo cresce.\n"
            "• A identidade das preferências usa apenas LUFScale e o último anexo tem um título geral."
        ),
    },
    "ru": {
        "status_ok": "УСПЕШНО",
        "qc_ok": "УСПЕШНО",
        "status_warning": "ПРЕДУПРЕЖДЕНИЕ",
        "version_changes": (
            "• Сокращения шести параметров отображаются также в каждой строке вкладки параметров.\n"
            "• Общая длительность и время завершения показаны в 24-часовом формате.\n"
            "• Все состояния журнала, включая успех и предупреждение, выводятся на выбранном языке.\n"
            "• Круглые индикаторы лучше разделены и читаются в светлом режиме.\n"
            "• При запуске журнал и индикатор имеют одинаковую высоту; затем растёт только журнал.\n"
            "• Идентификатор настроек использует только LUFScale, а последний раздел получил общее название."
        ),
    },
    "zh": {
        "status_ok": "成功",
        "qc_ok": "成功",
        "status_warning": "警告",
        "version_changes": (
            "• 六个选项的缩写也显示在“选项”标签页的每一行中。\n"
            "• 总时长和结束时刻采用24小时制。\n"
            "• 包括成功和警告在内的所有日志状态均按所选语言显示。\n"
            "• 圆形指示灯下方留有更大间距，并在浅色模式下保持清晰。\n"
            "• 启动时日志与响度表等高；之后只有日志会增高。\n"
            "• 偏好设置标识仅使用 LUFScale，最后一节附录改为通用标题。"
        ),
    },
}

for _language, _updates in TRANSLATION_UPDATES_12300.items():
    EXTRA_TEXTS[_language].update(_updates)
    _log_help = EXTRA_TEXTS[_language].get("log_help_text")
    if _log_help:
        EXTRA_TEXTS[_language]["log_help_text"] = _log_help.replace(
            "OK", _updates["status_ok"]
        )


# Version 1.23.1 completes the dialog chrome catalogues and makes the target
# score follow the same rolling eight-output horizon as the visible extrema.
WINDOW_TITLE_UPDATES_12301: dict[str, dict[str, str]] = {
    "nl": {
        "add_source_folder": "Bronmap toevoegen",
        "choose_output": "Doelmap kiezen",
        "clipboard": "Klembord",
        "completed_with_errors": "Verwerking voltooid met waarschuwingen",
        "ffmpeg_incompatible": "FFmpeg is niet compatibel",
        "ffmpeg_missing": "FFmpeg niet gevonden",
        "folder_unavailable": "Map niet beschikbaar",
        "invalid_location": "Ongeldige locatie",
        "processing_completed": "Verwerking voltooid",
        "processing_in_progress": "Verwerking bezig",
    },
    "pl": {
        "add_source_folder": "Dodaj folder źródłowy",
        "choose_output": "Wybierz folder docelowy",
        "clipboard": "Schowek",
        "completed_with_errors": "Przetwarzanie zakończone z ostrzeżeniami",
        "ffmpeg_incompatible": "Niezgodna wersja FFmpeg",
        "ffmpeg_missing": "Nie znaleziono FFmpeg",
        "folder_unavailable": "Folder niedostępny",
        "invalid_location": "Nieprawidłowa lokalizacja",
        "processing_completed": "Przetwarzanie zakończone",
        "processing_in_progress": "Przetwarzanie w toku",
    },
    "ru": {
        "add_source_folder": "Добавить исходную папку",
        "choose_output": "Выбрать папку назначения",
        "clipboard": "Буфер обмена",
        "completed_with_errors": "Обработка завершена с предупреждениями",
        "ffmpeg_incompatible": "Несовместимая версия FFmpeg",
        "ffmpeg_missing": "FFmpeg не найден",
        "folder_unavailable": "Папка недоступна",
        "invalid_location": "Недопустимое расположение",
        "processing_completed": "Обработка завершена",
        "processing_in_progress": "Выполняется обработка",
    },
    "ja": {
        "add_source_folder": "ソースフォルダーを追加",
        "choose_output": "保存先フォルダーを選択",
        "clipboard": "クリップボード",
        "completed_with_errors": "警告付きで処理完了",
        "ffmpeg_incompatible": "FFmpegに互換性がありません",
        "ffmpeg_missing": "FFmpegが見つかりません",
        "folder_unavailable": "フォルダーを利用できません",
        "invalid_location": "保存先が無効です",
        "processing_completed": "処理完了",
        "processing_in_progress": "処理中",
    },
}

for _language, _updates in WINDOW_TITLE_UPDATES_12301.items():
    EXTRA_TEXTS[_language].update(_updates)


DIALOG_OK_12301 = {
    "de": "OK",
    "es": "Aceptar",
    "hi": "ठीक है",
    "it": "OK",
    "ja": "確認",
    "nl": "OK",
    "pl": "OK",
    "pt": "OK",
    "ru": "ОК",
    "zh": "确定",
}

SCORE_WINDOW_INTRO_12301 = {
    "de": "Der Zielwert wird wie Min und Max aus den letzten 8 tatsächlich nachgemessenen Ausgaben neu berechnet; jede neue Messung entfernt die älteste.",
    "es": "La puntuación objetivo se recalcula, igual que Min y Max, con las 8 últimas salidas realmente medidas; cada medición nueva elimina la más antigua.",
    "hi": "लक्ष्य स्कोर भी Min और Max की तरह वास्तव में दोबारा मापे गए अंतिम 8 आउटपुट से फिर गिना जाता है; हर नई माप सबसे पुरानी माप को हटा देती है।",
    "it": "Il punteggio obiettivo viene ricalcolato, come Min e Max, sulle ultime 8 uscite realmente rimisurate; ogni nuova misura elimina la più vecchia.",
    "ja": "目標スコアも Min／Max と同じく、実際に再測定した直近8件で再計算し、新しい測定ごとに最も古い値を外します。",
    "nl": "De doelscore wordt net als Min en Max opnieuw berekend over de 8 recentste werkelijk opnieuw gemeten uitvoerbestanden; elke nieuwe meting verwijdert de oudste.",
    "pl": "Wynik celu, tak jak Min i Max, jest przeliczany dla 8 ostatnich faktycznie ponownie zmierzonych wyników; każdy nowy pomiar usuwa najstarszy.",
    "pt": "A pontuação do alvo é recalculada, tal como Min e Max, nas 8 saídas realmente medidas de novo mais recentes; cada nova medição retira a mais antiga.",
    "ru": "Оценка цели, как Min и Max, пересчитывается по 8 последним фактически повторно измеренным результатам; каждое новое измерение исключает самое старое.",
    "zh": "目标评分与 Min 和 Max 一样，按最近8个实际重新测量的输出重新计算；每加入一个新测量值，就移除最旧的值。",
}

VERSION_CHANGES_12301 = {
    "de": "• Der Zielwert folgt jetzt demselben gleitenden Fenster aus 8 Ausgaben wie Min und Max.\n• Dialogtitel und Bestätigungsschaltflächen verwenden die gewählte Sprache; asiatische Schriften erhalten zusätzliche Höhe.\n• Die Statusleuchten werden als echte Kreise gezeichnet und vom Rahmen abgerückt.\n• In Optionen steht jedes Kürzel links direkt vor seinem Kontrollkästchen; Hilfe bleibt rechts.\n• Normalisieren ist nach dem Hinzufügen einer Quelle verfügbar; Pause und Abbrechen folgen dem tatsächlichen Verarbeitungszustand.\n• Audio-Engine und Normalisierungsberechnungen sind unverändert.",
    "es": "• La puntuación objetivo usa ahora la misma ventana móvil de 8 salidas que Min y Max.\n• Los títulos y botones de confirmación de los diálogos usan el idioma elegido; las escrituras asiáticas reciben altura adicional.\n• Las luces de estado se dibujan como círculos reales y se separan del marco.\n• En Opciones, cada sigla queda a la izquierda, justo antes de su casilla; Ayuda permanece a la derecha.\n• Normalizar está disponible al añadir una fuente; Pausa y Cancelar siguen el estado real del proceso.\n• El motor de audio y los cálculos de normalización no cambian.",
    "hi": "• लक्ष्य स्कोर अब Min और Max की तरह अंतिम 8 आउटपुट की चलती विंडो का उपयोग करता है।\n• संवाद के शीर्षक और पुष्टि बटन चुनी गई भाषा में हैं; एशियाई लिपियों को अतिरिक्त ऊँचाई मिलती है।\n• स्थिति संकेतक वास्तविक गोल वृत्त के रूप में बनाए गए हैं और फ्रेम से ऊपर रखे गए हैं।\n• विकल्प में हर संक्षेप बाईं ओर, उसकी चेकबॉक्स से ठीक पहले है; सहायता बटन दाईं ओर रहता है।\n• स्रोत जोड़ते ही सामान्यीकरण उपलब्ध है; रोकें और रद्द करें वास्तविक प्रक्रिया स्थिति का पालन करते हैं।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    "it": "• Il punteggio obiettivo usa ora la stessa finestra mobile di 8 uscite di Min e Max.\n• Titoli e pulsanti di conferma dei dialoghi usano la lingua scelta; le scritture asiatiche ricevono altezza aggiuntiva.\n• Le spie di stato sono disegnate come cerchi reali e sollevate dal bordo.\n• In Opzioni ogni sigla è a sinistra, subito prima della casella; Aiuto resta a destra.\n• Normalizza è disponibile dopo l’aggiunta di una sorgente; Pausa e Annulla seguono lo stato reale del processo.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    "ja": "• 目標スコアを Min／Max と同じ直近8出力の移動窓で再計算します。\n• ダイアログのタイトルと確認ボタンを選択言語で表示し、日本語・中国語・ヒンディー語には高さの余裕を追加しました。\n• 状態ランプを実際の円として描画し、枠線から少し上へ離しました。\n• オプションでは略記を左揃えでチェック欄の直前に置き、ヘルプは右側に残します。\n• ソース追加後すぐにノーマライズを選べ、処理開始後は一時停止とキャンセルが実際の状態に従います。\n• 音声エンジンとノーマライズ計算は変更していません。",
    "nl": "• De doelscore gebruikt nu hetzelfde voortschrijdende venster van 8 uitvoerbestanden als Min en Max.\n• Dialoogtitels en bevestigingsknoppen volgen de gekozen taal; Aziatische schriften krijgen extra hoogte.\n• Statuslampjes worden als echte cirkels getekend en van de rand opgetild.\n• In Opties staat elke afkorting links, direct voor het selectievakje; Help blijft rechts.\n• Normaliseren is beschikbaar zodra een bron is toegevoegd; Pauze en Annuleren volgen de werkelijke verwerkingsstatus.\n• Audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    "pl": "• Wynik celu używa teraz tego samego ruchomego okna 8 wyników co Min i Max.\n• Tytuły okien dialogowych i przyciski potwierdzenia używają wybranego języka; pisma azjatyckie otrzymują dodatkową wysokość.\n• Kontrolki stanu są rysowane jako prawdziwe koła i odsunięte od ramki.\n• W Opcjach każdy skrót jest po lewej, tuż przed polem wyboru; Pomoc pozostaje po prawej.\n• Normalizacja jest dostępna po dodaniu źródła; Pauza i Anuluj śledzą rzeczywisty stan przetwarzania.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    "pt": "• A pontuação do alvo usa agora a mesma janela móvel de 8 saídas que Min e Max.\n• Os títulos e botões de confirmação dos diálogos usam o idioma escolhido; as escritas asiáticas recebem altura adicional.\n• As luzes de estado são desenhadas como círculos reais e afastadas da moldura.\n• Em Opções, cada sigla fica à esquerda, imediatamente antes da caixa; Ajuda permanece à direita.\n• Uniformizar fica disponível depois de adicionar uma origem; Pausa e Cancelar seguem o estado real do processamento.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    "ru": "• Оценка цели теперь использует то же скользящее окно из 8 результатов, что Min и Max.\n• Заголовки и кнопки подтверждения диалогов выводятся на выбранном языке; для азиатских письменностей добавлен запас высоты.\n• Индикаторы состояния рисуются как настоящие круги и подняты над рамкой.\n• На вкладке параметров каждое сокращение выровнено слева перед флажком; кнопка справки остаётся справа.\n• Нормализация доступна после добавления источника; Пауза и Отмена следуют фактическому состоянию обработки.\n• Аудиодвижок и расчёты нормализации не изменены.",
    "zh": "• 目标评分现在与 Min 和 Max 一样，使用最近8个输出的滑动窗口。\n• 对话框标题和确认按钮采用所选语言；日文、中文和印地文增加了高度余量。\n• 状态指示灯按真正的圆形绘制，并与边框拉开距离。\n• 在“选项”中，每个缩写左对齐并置于复选框之前；帮助按钮仍在右侧。\n• 添加来源后即可执行响度统一；处理开始后，暂停和取消会跟随真实状态。\n• 音频引擎和标准化计算保持不变。",
}

for _language in DIALOG_OK_12301:
    EXTRA_TEXTS[_language]["dialog_ok"] = DIALOG_OK_12301[_language]
    EXTRA_TEXTS[_language]["loudness_score_tooltip"] = (
        SCORE_WINDOW_INTRO_12301[_language]
        + "\n\n"
        + EXTRA_TEXTS[_language]["loudness_score_tooltip"]
    )
    EXTRA_TEXTS[_language]["version_changes"] = (
        VERSION_CHANGES_12301[_language]
    )


# Version 1.23.2 restores an explicit destination-first workflow and gives
# every localized option acronym the same centred geometry.
VERSION_CHANGES_12302 = {
    "de": "• In Optionen steht jede Hilfe-Schaltfläche direkt hinter dem zugehörigen Text.\n• Die Kürzel verwenden in allen zwölf Sprachen breitere, einheitlich zentrierte Felder.\n• Japanisch, Chinesisch und Hindi behalten die kompakte Fenstergröße, ohne bei normaler Bildschirmhöhe eine Bildlaufleiste zu erzeugen.\n• Normalisieren erfordert wieder eine vorher über die eigene Schaltfläche gewählte Zielmappe und öffnet beim Start keinen Auswahldialog mehr.\n• Audio-Engine und Normalisierungsberechnungen sind unverändert.",
    "es": "• En Opciones, cada botón de Ayuda aparece justo después del texto asociado.\n• Las siglas usan celdas más anchas y el mismo centrado en los doce idiomas.\n• Japonés, chino e hindi conservan el tamaño compacto de la ventana sin crear una barra de desplazamiento con la altura normal de pantalla.\n• Normalizar vuelve a exigir que se elija antes el destino con su botón y ya no abre un selector al iniciar el proceso.\n• El motor de audio y los cálculos de normalización no cambian.",
    "hi": "• विकल्प में हर सहायता बटन उससे जुड़े पाठ के तुरंत बाद रखा गया है।\n• सभी बारह भाषाओं में संक्षेप अधिक चौड़ी कोशिकाओं में समान रूप से केंद्रित हैं।\n• जापानी, चीनी और हिन्दी सामान्य स्क्रीन ऊँचाई पर स्क्रॉलबार बनाए बिना विंडो का संक्षिप्त आकार बनाए रखते हैं।\n• सामान्यीकरण से पहले समर्पित बटन से लक्ष्य फ़ोल्डर चुनना आवश्यक है; प्रक्रिया शुरू करते समय चयन विंडो अब नहीं खुलती।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    "it": "• In Opzioni, ogni pulsante Aiuto segue immediatamente il testo associato.\n• Le sigle usano celle più larghe e lo stesso centraggio in tutte le dodici lingue.\n• Giapponese, cinese e hindi mantengono la finestra compatta senza creare una barra di scorrimento alla normale altezza dello schermo.\n• Normalizza richiede di nuovo la scelta preventiva della destinazione con il pulsante dedicato e non apre più un selettore all’avvio.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    "ja": "• オプションでは各ヘルプボタンを対応する説明文の直後に配置しました。\n• 12言語すべてで略記欄を広げ、同じ位置に中央揃えします。\n• 日本語・中国語・ヒンディー語でも、通常の画面高さではスクロールバーを出さずにコンパクトなウィンドウサイズを保ちます。\n• ノーマライズの前に専用ボタンで保存先を選ぶ方式に戻し、処理開始時には選択画面を開きません。\n• 音声エンジンとノーマライズ計算は変更していません。",
    "nl": "• In Opties staat elke Help-knop direct achter de bijbehorende tekst.\n• De afkortingen gebruiken in alle twaalf talen bredere, gelijkmatig gecentreerde vakken.\n• Japans, Chinees en Hindi behouden het compacte venster zonder bij normale schermhoogte een schuifbalk te veroorzaken.\n• Normaliseren vereist opnieuw dat de doelmap vooraf met de aparte knop wordt gekozen en opent bij de start geen keuzevenster meer.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    "pl": "• W Opcjach każdy przycisk Pomocy znajduje się bezpośrednio za powiązanym tekstem.\n• Skróty mają szersze i jednakowo wyśrodkowane pola we wszystkich dwunastu językach.\n• Japoński, chiński i hindi zachowują kompaktowy rozmiar okna bez paska przewijania przy normalnej wysokości ekranu.\n• Normalizacja ponownie wymaga wcześniejszego wybrania miejsca docelowego osobnym przyciskiem i nie otwiera okna wyboru przy uruchamianiu.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    "pt": "• Em Opções, cada botão de Ajuda surge imediatamente após o texto associado.\n• As siglas usam células mais largas e o mesmo alinhamento centrado nos doze idiomas.\n• Japonês, chinês e hindi mantêm a janela compacta sem criar uma barra de deslocamento na altura normal do ecrã.\n• Uniformizar volta a exigir a escolha prévia do destino pelo botão dedicado e deixa de abrir um seletor ao iniciar.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    "ru": "• На вкладке параметров каждая кнопка справки расположена сразу после связанного текста.\n• Сокращения помещены в более широкие и одинаково центрированные поля во всех двенадцати языках.\n• Для японского, китайского и хинди сохраняется компактный размер окна без полосы прокрутки при обычной высоте экрана.\n• Перед нормализацией снова требуется выбрать папку назначения отдельной кнопкой; при запуске обработки окно выбора больше не открывается.\n• Аудиодвижок и расчёты нормализации не изменены.",
    "zh": "• 在“选项”中，每个帮助按钮都紧跟在对应文字之后。\n• 十二种语言的缩写均使用更宽且统一居中的单元格。\n• 日文、中文和印地文在正常屏幕高度下保持紧凑窗口尺寸，不再触发滚动条。\n• 统一响度前必须先用专用按钮选择目标文件夹；开始处理时不再弹出选择窗口。\n• 音频引擎和标准化计算保持不变。",
}

for _language, _changes in VERSION_CHANGES_12302.items():
    EXTRA_TEXTS[_language]["version_changes"] = _changes


# Version 1.23.3 keeps the main-window geometry independent from the selected
# script and explains a missing destination without opening a chooser.
TRANSLATION_UPDATES_12303 = {
    "de": {
        "destination_required_start": "Wählen Sie zuerst den Zielordner mit der Schaltfläche „Auswählen…“.",
        "version_changes": "• Die Erfolgszelle im Handbuch enthält kein weißes Quadrat mehr; die vier Schritte verwenden runde Marken.\n• Quellen und Einstellungen bleiben in allen zwölf Sprachen gleich hoch, ohne zusätzliche Bildlaufleiste für Japanisch, Chinesisch oder Hindi.\n• Beim Start enden Protokoll und Anzeige auf gleicher Höhe; danach wächst nur das Protokoll mit dem Fenster.\n• Die Hilfe-Schaltflächen der Optionen erhalten mehr Abstand zum Text.\n• Normalisieren ist nach dem Hinzufügen einer Quelle verfügbar. Fehlt das Ziel, erscheint eine Meldung ohne Auswahldialog; Pause und Abbrechen werden während der Verarbeitung aktiv.\n• Audio-Engine und Normalisierungsberechnungen sind unverändert.",
    },
    "es": {
        "destination_required_start": "Primero elija la carpeta de destino con el botón «Elegir…».",
        "version_changes": "• La celda de éxito del manual ya no contiene un cuadrado blanco y los cuatro pasos usan marcadores circulares.\n• Fuentes y Ajustes conservan la misma altura en los doce idiomas, sin una barra adicional en japonés, chino o hindi.\n• Al iniciar, el registro y el medidor terminan al mismo nivel; después solo crece el registro con la ventana.\n• Los botones de Ayuda de las opciones tienen más espacio tras el texto.\n• Normalizar queda disponible al añadir una fuente. Si falta el destino, aparece un mensaje sin abrir un selector; Pausa y Cancelar se activan durante el proceso.\n• El motor de audio y los cálculos de normalización no cambian.",
    },
    "hi": {
        "destination_required_start": "पहले “चुनें…” बटन से गंतव्य फ़ोल्डर चुनें।",
        "version_changes": "• मार्गदर्शिका की सफलता वाली कोशिका में अब सफेद चौकोर नहीं है और चारों चरण गोल चिह्नों में हैं।\n• स्रोत और सेटिंग पैनल सभी बारह भाषाओं में समान ऊँचाई रखते हैं; जापानी, चीनी या हिन्दी अतिरिक्त स्क्रॉलबार नहीं जोड़ते।\n• आरंभ में लॉग और लाउडनेस मीटर का निचला किनारा समान रहता है; बाद में विंडो के साथ केवल लॉग बढ़ता है।\n• विकल्पों के सहायता बटन और पाठ के बीच अधिक दूरी है।\n• स्रोत जोड़ते ही सामान्यीकरण उपलब्ध हो जाता है। गंतव्य न होने पर चयन विंडो खोले बिना संदेश दिखता है; प्रक्रिया के दौरान रोकें और रद्द करें सक्रिय होते हैं।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    },
    "it": {
        "destination_required_start": "Scegli prima la cartella di destinazione con il pulsante «Scegli…».",
        "version_changes": "• La cella di riuscita del manuale non contiene più il quadrato bianco e i quattro passaggi usano indicatori circolari.\n• Sorgenti e Impostazioni mantengono la stessa altezza nelle dodici lingue, senza una barra aggiunta da giapponese, cinese o hindi.\n• All’avvio, registro e misuratore terminano allo stesso livello; in seguito solo il registro cresce con la finestra.\n• I pulsanti Aiuto delle opzioni hanno più spazio dopo il testo.\n• Normalizza è disponibile appena si aggiunge una sorgente. Se manca la destinazione, un messaggio lo indica senza aprire un selettore; Pausa e Annulla si attivano durante il processo.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    },
    "ja": {
        "destination_required_start": "先に「選択…」ボタンで保存先フォルダーを選んでください。",
        "version_changes": "• ガイドの成功セルから白い四角を除去し、4つの手順番号を丸いマーカーにしました。\n• ソースと設定の高さを12言語で共通にし、日本語・中国語・ヒンディー語でも余分なスクロールバーを出しません。\n• 起動時はログとラウドネスメーターの下端が揃い、その後ウィンドウを広げてもログだけが伸びます。\n• オプションのヘルプボタンと説明文の間隔を広げました。\n• ソース追加後はノーマライズを選べます。保存先がない場合は選択画面を開かずに案内を表示し、処理中は一時停止とキャンセルが有効になります。\n• 音声エンジンとノーマライズ計算は変更していません。",
    },
    "nl": {
        "destination_required_start": "Kies eerst de doelmap met de knop ‘Kiezen…’.",
        "version_changes": "• De succescel in de handleiding bevat geen wit vierkant meer en de vier stappen gebruiken ronde markeringen.\n• Bronnen en Instellingen blijven in alle twaalf talen even hoog, zonder extra schuifbalk voor Japans, Chinees of Hindi.\n• Bij het starten eindigen logboek en meter op dezelfde hoogte; daarna groeit alleen het logboek met het venster mee.\n• De Help-knoppen bij opties hebben meer ruimte na de tekst.\n• Normaliseren is beschikbaar zodra een bron is toegevoegd. Ontbreekt de bestemming, dan verschijnt een melding zonder keuzevenster; Pauze en Annuleren worden actief tijdens de verwerking.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    },
    "pl": {
        "destination_required_start": "Najpierw wybierz folder docelowy przyciskiem „Wybierz…”.",
        "version_changes": "• Komórka powodzenia w przewodniku nie zawiera już białego kwadratu, a cztery kroki mają okrągłe znaczniki.\n• Źródła i Ustawienia zachowują tę samą wysokość we wszystkich dwunastu językach, bez dodatkowego paska dla japońskiego, chińskiego lub hindi.\n• Po uruchomieniu dziennik i miernik kończą się na tej samej wysokości; później wraz z oknem rośnie tylko dziennik.\n• Przyciski Pomocy w opcjach mają większy odstęp od tekstu.\n• Normalizacja jest dostępna po dodaniu źródła. Jeśli brak miejsca docelowego, pojawia się komunikat bez okna wyboru; Pauza i Anuluj stają się aktywne podczas przetwarzania.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    },
    "pt": {
        "destination_required_start": "Escolha primeiro a pasta de destino com o botão «Escolher…».",
        "version_changes": "• A célula de sucesso do guia deixou de ter um quadrado branco e os quatro passos usam marcadores circulares.\n• Origens e Definições mantêm a mesma altura nos doze idiomas, sem barra adicional em japonês, chinês ou hindi.\n• Ao iniciar, o registo e o medidor terminam ao mesmo nível; depois apenas o registo cresce com a janela.\n• Os botões de Ajuda das opções têm mais espaço após o texto.\n• Uniformizar fica disponível após adicionar uma origem. Se faltar o destino, surge uma mensagem sem abrir um seletor; Pausa e Cancelar ficam ativos durante o processamento.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    },
    "ru": {
        "destination_required_start": "Сначала выберите папку назначения кнопкой «Выбрать…».",
        "version_changes": "• В ячейке успешного результата руководства больше нет белого квадрата, а четыре шага отмечены круглыми значками.\n• Панели источников и настроек сохраняют одинаковую высоту на всех двенадцати языках; японский, китайский и хинди не добавляют полосу прокрутки.\n• При запуске журнал и индикатор заканчиваются на одном уровне; затем вместе с окном увеличивается только журнал.\n• Между текстом параметра и кнопкой справки увеличен интервал.\n• Нормализация доступна после добавления источника. Если папка назначения не выбрана, появляется сообщение без окна выбора; во время обработки активируются Пауза и Отмена.\n• Аудиодвижок и расчёты нормализации не изменены.",
    },
    "zh": {
        "destination_required_start": "请先用“选择…”按钮选择目标文件夹。",
        "version_changes": "• 指南的成功状态单元格不再出现白色方块，四个步骤均改用圆形标记。\n• 来源与设置面板在十二种语言中保持相同高度，日文、中文和印地文不会再增加滚动条。\n• 启动时，日志与响度表底部对齐；之后调整窗口高度时只扩展日志。\n• 选项文字与帮助按钮之间增加了间距。\n• 添加来源后即可使用响度统一。若尚未选择目标位置，会显示提示而不打开选择器；处理期间暂停和取消按钮会启用。\n• 音频引擎和标准化计算保持不变。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12303.items():
    EXTRA_TEXTS[_language].update(_updates)


# Version 1.23.4 sizes translated help-dialog confirmation buttons from the
# active font metrics and keeps an explicit vertical safety margin.
VERSION_CHANGES_12304 = {
    "de": "• Hilfetexte erhalten zwei zusätzliche Zeilen typografischen Sicherheitsabstand und bei Bedarf eine vertikale Bildlaufleiste; die letzte Zeile wird nicht mehr abgeschnitten. Auch die Bestätigungsschaltflächen passen ihre Höhe an die aktive Schrift an.\n• Die Zeile Normalisieren–Pause–Abbrechen hat eine feste kompakte Höhe; Japanisch, Chinesisch und Hindi verschieben den Inhalt nicht mehr und lösen bei normaler Fensterhöhe keine Bildlaufleiste aus.\n• Audio-Engine und Normalisierungsberechnungen sind unverändert.",
    "es": "• Los textos de ayuda conservan dos líneas adicionales de margen tipográfico y, si hace falta, una barra de desplazamiento vertical; la última línea ya no se recorta. Los botones de confirmación también adaptan su altura a la fuente activa.\n• La fila Normalizar–Pausa–Cancelar tiene una altura compacta fija; el japonés, el chino y el hindi ya no desplazan el contenido ni activan la barra a la altura normal de la ventana.\n• El motor de audio y los cálculos de normalización no cambian.",
    "hi": "• सहायता पाठ में दो अतिरिक्त पंक्तियों की टाइपोग्राफ़िक जगह और आवश्यकता पर लंबवत स्क्रॉल उपलब्ध है; अंतिम पंक्ति अब नहीं कटती। पुष्टि बटन भी सक्रिय फ़ॉन्ट के अनुसार अपनी ऊँचाई बदलते हैं।\n• सामान्यीकरण–विराम–रद्द पंक्ति की ऊँचाई निश्चित और संक्षिप्त है; जापानी, चीनी और हिन्दी अब सामग्री को नहीं खिसकाते और सामान्य विंडो ऊँचाई पर स्क्रॉलबार नहीं दिखाते।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    "it": "• I testi di aiuto mantengono due righe aggiuntive di margine tipografico e, se necessario, uno scorrimento verticale; l’ultima riga non viene più tagliata. Anche i pulsanti di conferma adattano l’altezza al carattere attivo.\n• La riga Normalizza–Pausa–Annulla ha un’altezza compatta fissa; giapponese, cinese e hindi non spostano più il contenuto e non attivano la barra alla normale altezza della finestra.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    "ja": "• ヘルプ本文に2行分の余白を追加し、必要な場合は縦スクロールを使用します。最後の行が切れず、確認ボタンの高さも使用中のフォントに合わせて調整されます。\n• ノーマライズ・一時停止・キャンセルの行を固定のコンパクトな高さにしました。日本語・中国語・ヒンディー語でも内容がずれず、通常のウィンドウ高さでスクロールバーが表示されません。\n• 音声エンジンとノーマライズ計算は変更していません。",
    "nl": "• Helpteksten krijgen twee extra regels typografische veiligheidsruimte en zo nodig verticale scrolling; de laatste regel wordt niet meer afgesneden. Ook bevestigingsknoppen passen hun hoogte aan het actieve lettertype aan.\n• De rij Normaliseren–Pauze–Annuleren heeft een vaste compacte hoogte; Japans, Chinees en Hindi verschuiven de inhoud niet meer en activeren bij normale vensterhoogte geen schuifbalk.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    "pl": "• Teksty pomocy mają dwie dodatkowe linie zapasu typograficznego i w razie potrzeby przewijanie pionowe; ostatnia linia nie jest już obcinana. Przyciski potwierdzenia również dopasowują wysokość do aktywnej czcionki.\n• Wiersz Normalizuj–Pauza–Anuluj ma stałą kompaktową wysokość; język japoński, chiński i hindi nie przesuwają już zawartości ani nie uruchamiają paska przy normalnej wysokości okna.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    "pt": "• Os textos de ajuda mantêm duas linhas adicionais de margem tipográfica e, quando necessário, deslocamento vertical; a última linha deixa de ficar cortada. Os botões de confirmação também ajustam a altura à fonte ativa.\n• A linha Uniformizar–Pausa–Cancelar tem uma altura compacta fixa; japonês, chinês e hindi deixam de deslocar o conteúdo e de ativar a barra à altura normal da janela.\n• O motor de áudio e os cálculos de normalização permanecem inalterados.",
    "ru": "• Для текста справки добавлен типографский запас в две строки и, при необходимости, вертикальная прокрутка; последняя строка больше не обрезается. Кнопки подтверждения также подстраивают высоту под активный шрифт.\n• Строка «Нормализация–Пауза–Отмена» имеет фиксированную компактную высоту; японский, китайский и хинди больше не смещают содержимое и не вызывают полосу прокрутки при обычной высоте окна.\n• Аудиодвижок и расчёты нормализации не изменены.",
    "zh": "• 帮助正文保留两行额外的排版余量，并在需要时提供垂直滚动；最后一行不再被裁切。确认按钮的高度也会适配当前字体。\n• 统一响度–暂停–取消一行采用固定的紧凑高度；日文、中文和印地文不再使内容偏移，也不会在正常窗口高度下触发滚动条。\n• 音频引擎和标准化计算保持不变。",
}

for _language, _changes in VERSION_CHANGES_12304.items():
    EXTRA_TEXTS[_language]["version_changes"] = _changes


# Version 1.23.5 completes the close-confirmation catalogue and fixes the
# remaining language-dependent geometry in the main window.
CLOSE_QUESTION_UPDATES_12305 = {
    "ja": "処理をキャンセルしてアプリケーションを終了しますか？",
    "nl": "Verwerking annuleren en de toepassing sluiten?",
    "pl": "Anulować przetwarzanie i zamknąć aplikację?",
    "ru": "Отменить обработку и закрыть приложение?",
}

VERSION_CHANGES_12305 = {
    "de": "• Die Bestätigung zum Schließen während der Verarbeitung ist in allen zwölf Sprachen übersetzt.\n• Ein fester Abstand trennt Protokoll und Lautheitsmesser von der unteren Statusleiste; nur das Protokoll wächst mit dem Fenster.\n• Titel und Registerleiste der Einstellungen haben eine gemeinsame feste Höhe, sodass Japanisch, Chinesisch und Hindi den Inhalt nicht mehr verschieben.\n• Audio-Engine und Normalisierungsberechnungen sind unverändert.",
    "es": "• La confirmación de cierre durante el procesamiento está traducida en los doce idiomas.\n• Un espacio fijo separa el registro y el medidor de sonoridad de la barra de estado inferior; solo el registro crece con la ventana.\n• El título y la barra de pestañas de Ajustes tienen una altura fija común, de modo que el japonés, el chino y el hindi ya no desplazan el contenido.\n• El motor de audio y los cálculos de normalización no cambian.",
    "hi": "• प्रसंस्करण के दौरान बंद करने की पुष्टि सभी बारह भाषाओं में अनूदित है।\n• एक निश्चित अंतर लॉग और लाउडनेस मीटर को नीचे की स्थिति पट्टी से अलग रखता है; विंडो के साथ केवल लॉग बढ़ता है।\n• सेटिंग्स शीर्षक और टैब पट्टी की ऊँचाई समान और निश्चित है, इसलिए जापानी, चीनी और हिन्दी अब सामग्री को नीचे नहीं खिसकाते।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    "it": "• La conferma di chiusura durante l’elaborazione è tradotta in tutte le dodici lingue.\n• Uno spazio fisso separa il registro e il misuratore di sonorità dalla barra di stato inferiore; solo il registro cresce con la finestra.\n• Il titolo e la barra delle schede delle Impostazioni hanno un’altezza fissa comune, quindi giapponese, cinese e hindi non spostano più il contenuto.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    "ja": "• 処理中に閉じる際の確認メッセージを12言語すべてで翻訳しました。\n• 処理ログとラウドネスメーターの下に固定の余白を設け、下部ステータスバーから離しました。ウィンドウを広げた場合はログだけが伸びます。\n• 設定タイトルとタブバーの高さを共通の固定値にし、日本語・中国語・ヒンディー語でも内容が下へずれないようにしました。\n• 音声エンジンとノーマライズ計算は変更していません。",
    "nl": "• De sluitbevestiging tijdens de verwerking is in alle twaalf talen vertaald.\n• Een vaste tussenruimte scheidt het logboek en de luidheidsmeter van de onderste statusbalk; alleen het logboek groeit met het venster mee.\n• De titel en tabbladen van Instellingen hebben dezelfde vaste hoogte, zodat Japans, Chinees en Hindi de inhoud niet meer verschuiven.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    "pl": "• Potwierdzenie zamknięcia podczas przetwarzania jest przetłumaczone na wszystkie dwanaście języków.\n• Stały odstęp oddziela dziennik i miernik głośności od dolnego paska stanu; wraz z oknem rośnie tylko dziennik.\n• Tytuł i pasek kart Ustawień mają wspólną stałą wysokość, dzięki czemu język japoński, chiński i hindi nie przesuwają już zawartości.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    "pt": "• A confirmação de fecho durante o processamento está traduzida nos doze idiomas.\n• Um espaço fixo separa o registo e o medidor de sonoridade da barra de estado inferior; apenas o registo cresce com a janela.\n• O título e a barra de separadores das Definições têm uma altura fixa comum, pelo que japonês, chinês e hindi deixam de deslocar o conteúdo.\n• O motor áudio e os cálculos de normalização permanecem inalterados.",
    "ru": "• Подтверждение закрытия во время обработки переведено на все двенадцать языков.\n• Фиксированный отступ отделяет журнал и индикатор громкости от нижней строки состояния; вместе с окном увеличивается только журнал.\n• Заголовок и панель вкладок настроек имеют общую фиксированную высоту, поэтому японский, китайский и хинди больше не смещают содержимое вниз.\n• Аудиодвижок и расчёты нормализации не изменены.",
    "zh": "• 处理期间的关闭确认消息已翻译为全部十二种语言。\n• 处理日志和响度表与底部状态栏之间保留固定间距；调整窗口高度时只有日志会增高。\n• “设置”标题与标签栏采用统一的固定高度，日文、中文和印地文不再使内容下移。\n• 音频引擎和标准化计算保持不变。",
}

for _language, _question in CLOSE_QUESTION_UPDATES_12305.items():
    EXTRA_TEXTS[_language]["close_question"] = _question

for _language, _changes in VERSION_CHANGES_12305.items():
    EXTRA_TEXTS[_language]["version_changes"] = _changes


# Version 1.23.6 keeps structured per-file issue lists and replaces the
# unreliable QLabel-based help body with a scrollable text document.
TRANSLATION_UPDATES_12306 = {
    "de": {
        "close_button": "Schließen",
        "errors_button": "Fehler ({count})",
        "errors_button_tooltip": "Öffnet die Fehlerliste mit Dateiname, Pfad und Details. Verfügbar während einer Pause oder nach der Verarbeitung.",
        "errors_dialog_title": "Verarbeitungsfehler",
        "issue_detail_column": "Details",
        "issue_file_column": "Datei",
        "issue_path_column": "Pfad",
        "save_issue_list": "Als CSV speichern…",
        "save_issue_list_error": "Die Liste konnte nicht gespeichert werden: {error}",
        "save_issue_list_error_title": "Speichern fehlgeschlagen",
        "save_issue_list_title": "CSV-Liste speichern",
        "csv_file_filter": "CSV-Dateien (*.csv)",
        "warnings_button": "Warnungen ({count})",
        "warnings_button_tooltip": "Öffnet die Warnungsliste mit Dateiname, Pfad und Details. Verfügbar während einer Pause oder nach der Verarbeitung.",
        "warnings_dialog_title": "Verarbeitungswarnungen",
        "log_help_text": "Jede Zeile beschreibt eine Datei oder einen allgemeinen Verarbeitungsschritt.\n\n• Eine erfolgreiche Zeile beginnt direkt mit dem Dateinamen; ERFOLG wird nicht mehr wiederholt.\n• KONFORM, FORTGESETZT, ÜBERSPRUNGEN, ABGEBROCHEN und FEHLER bleiben sichtbar, wenn sie zusätzliche Information liefern.\n• Pegel zeigen Eingang → erneut gemessenen Ausgang und danach gegebenenfalls das Ergebnis der Qualitätskontrolle.\n• Die Schaltflächen Warnungen und Fehler öffnen getrennte Listen mit Dateiname, Pfad und Details. Sie sind während einer Pause oder nach der Verarbeitung verfügbar; jede Liste kann gespeichert werden.\n\nFarben: Grün = Erfolg; Orange = Warnung; Rot = nicht fertiggestellte Datei; Blauviolett = Fortsetzung; Grau = Information, Überspringen oder Abbruch.\n\nQC-WARNUNG — Peak bedeutet, dass der erneut gemessene True Peak der Ausgabe den gewählten Grenzwert um mehr als 0,25 dB überschreitet. Die Datei wird trotzdem erstellt. Wählen Sie bei einer wiederkehrenden Warnung ein leiseres LUFS-Ziel oder einen vorsichtigeren maximalen Peak, etwa −2,0 dBTP.\n\nDie kumulierten Zeiten addieren die Arbeit aller parallelen Aufgaben. Die Gesamtzeit ist die tatsächlich verstrichene Dauer.",
        "version_changes": "• Erfolgreiche Protokollzeilen beginnen mit dem Dateinamen, ohne wiederholtes ERFOLG.\n• Alle sechs Anzeigen zeigen beim Überfahren von Kreis oder Kürzel ihre vollständige Beschreibung.\n• Warnungen und Fehler werden getrennt mit Dateiname, Pfad und Details gespeichert; die Listen sind während einer Pause oder danach sichtbar und als UTF-8-Text exportierbar.\n• Hilfefenster verwenden ein zuverlässig scrollbares Dokument, damit die letzte Zeile in allen zwölf Sprachen lesbar bleibt.\n• Audio-Engine und Normalisierungsberechnungen sind unverändert.",
    },
    "es": {
        "close_button": "Cerrar",
        "errors_button": "Errores ({count})",
        "errors_button_tooltip": "Abre la lista de errores con nombre de archivo, ruta y detalle. Disponible durante una pausa o después del proceso.",
        "errors_dialog_title": "Errores del proceso",
        "issue_detail_column": "Detalle",
        "issue_file_column": "Archivo",
        "issue_path_column": "Ruta",
        "save_issue_list": "Guardar como CSV…",
        "save_issue_list_error": "No se pudo guardar la lista: {error}",
        "save_issue_list_error_title": "No se pudo guardar",
        "save_issue_list_title": "Guardar la lista CSV",
        "csv_file_filter": "Archivos CSV (*.csv)",
        "warnings_button": "Alertas ({count})",
        "warnings_button_tooltip": "Abre la lista de alertas con nombre de archivo, ruta y detalle. Disponible durante una pausa o después del proceso.",
        "warnings_dialog_title": "Alertas del proceso",
        "log_help_text": "Cada línea corresponde a un archivo o a una etapa general.\n\n• Una línea correcta empieza directamente por el nombre del archivo; CORRECTO ya no se repite.\n• CONFORME, REANUDADO, OMITIDO, CANCELADO y ERROR permanecen cuando aportan información útil.\n• Los niveles muestran entrada → salida vuelta a medir y, después, el posible resultado del control de calidad.\n• Los botones Alertas y Errores abren listas independientes con nombre, ruta y detalle. Están disponibles durante una pausa o después del proceso y cada lista puede guardarse.\n\nColores: verde = éxito; naranja = alerta; rojo = archivo no terminado; violeta azulado = reanudación; gris = información, omisión o cancelación.\n\nQC ALERTA — pico indica que el pico verdadero vuelto a medir supera en más de 0,25 dB el límite elegido. El archivo se crea igualmente. Para corregir una alerta persistente, elija un objetivo LUFS más bajo o un pico máximo más prudente, por ejemplo −2,0 dBTP.\n\nLos tiempos acumulados suman el trabajo de todas las tareas paralelas. El tiempo total es la duración real transcurrida.",
        "version_changes": "• Las líneas correctas del registro empiezan por el nombre del archivo, sin repetir CORRECTO.\n• Las seis luces muestran su descripción completa al pasar por el círculo o la sigla.\n• Alertas y errores se conservan por separado con nombre, ruta y detalle; sus listas se consultan en pausa o al terminar y se exportan como texto UTF-8.\n• Las ayudas usan un documento desplazable fiable para que la última línea sea legible en los doce idiomas.\n• El motor de audio y los cálculos de normalización no cambian.",
    },
    "hi": {
        "close_button": "बंद करें",
        "errors_button": "त्रुटियाँ ({count})",
        "errors_button_tooltip": "फ़ाइल नाम, पथ और विवरण सहित त्रुटि सूची खोलता है। विराम के दौरान या प्रसंस्करण के बाद उपलब्ध।",
        "errors_dialog_title": "प्रसंस्करण त्रुटियाँ",
        "issue_detail_column": "विवरण",
        "issue_file_column": "फ़ाइल",
        "issue_path_column": "पथ",
        "save_issue_list": "CSV के रूप में सहेजें…",
        "save_issue_list_error": "सूची सहेजी नहीं जा सकी: {error}",
        "save_issue_list_error_title": "सहेजना संभव नहीं",
        "save_issue_list_title": "CSV सूची सहेजें",
        "csv_file_filter": "CSV फ़ाइलें (*.csv)",
        "warnings_button": "चेतावनियाँ ({count})",
        "warnings_button_tooltip": "फ़ाइल नाम, पथ और विवरण सहित चेतावनी सूची खोलता है। विराम के दौरान या प्रसंस्करण के बाद उपलब्ध।",
        "warnings_dialog_title": "प्रसंस्करण चेतावनियाँ",
        "log_help_text": "हर पंक्ति किसी फ़ाइल या सामान्य प्रसंस्करण चरण का वर्णन करती है।\n\n• सफल पंक्ति सीधे फ़ाइल नाम से शुरू होती है; सफल स्थिति दोहराई नहीं जाती।\n• अनुरूप, जारी, छोड़ा गया, रद्द और त्रुटि तभी दिखते हैं जब वे उपयोगी जानकारी देते हैं।\n• स्तर इनपुट → दोबारा मापा आउटपुट और उसके बाद गुणवत्ता-नियंत्रण परिणाम दिखाते हैं।\n• चेतावनियाँ और त्रुटियाँ बटन नाम, पथ और विवरण वाली अलग सूचियाँ खोलते हैं। वे विराम के दौरान या प्रसंस्करण के बाद उपलब्ध हैं और हर सूची सहेजी जा सकती है।\n\nरंग: हरा = सफलता; नारंगी = चेतावनी; लाल = अधूरी फ़ाइल; नीला-बैंगनी = जारी; धूसर = सूचना, छोड़ा गया या रद्द।\n\nQC चेतावनी — पीक का अर्थ है कि दोबारा मापी गई ट्रू पीक चुनी सीमा से 0.25 dB से अधिक ऊपर है। फ़ाइल फिर भी बनती है। लगातार चेतावनी के लिए कम LUFS लक्ष्य या −2.0 dBTP जैसी सुरक्षित अधिकतम पीक चुनें।\n\nसंचयी समय सभी समानांतर कार्यों का योग है। कुल समय वास्तविक बीता समय है।",
        "version_changes": "• सफल लॉग पंक्तियाँ अब दोहराई गई स्थिति के बिना फ़ाइल नाम से शुरू होती हैं।\n• छहों लाइटों के वृत्त या संक्षेप पर माउस रखने से पूरा विवरण दिखता है।\n• चेतावनियाँ और त्रुटियाँ नाम, पथ और विवरण के साथ अलग रखी जाती हैं; सूचियाँ विराम या समाप्ति के बाद देखी और UTF-8 टेक्स्ट में सहेजी जा सकती हैं।\n• सहायता विंडो विश्वसनीय स्क्रॉल दस्तावेज़ इस्तेमाल करती हैं, इसलिए अंतिम पंक्ति सभी बारह भाषाओं में पढ़ी जा सकती है।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    },
    "it": {
        "close_button": "Chiudi",
        "errors_button": "Errori ({count})",
        "errors_button_tooltip": "Apre l’elenco degli errori con nome file, percorso e dettagli. Disponibile durante una pausa o dopo l’elaborazione.",
        "errors_dialog_title": "Errori di elaborazione",
        "issue_detail_column": "Dettagli",
        "issue_file_column": "File",
        "issue_path_column": "Percorso",
        "save_issue_list": "Salva come CSV…",
        "save_issue_list_error": "Impossibile salvare l’elenco: {error}",
        "save_issue_list_error_title": "Salvataggio impossibile",
        "save_issue_list_title": "Salva elenco CSV",
        "csv_file_filter": "File CSV (*.csv)",
        "warnings_button": "Avvisi ({count})",
        "warnings_button_tooltip": "Apre l’elenco degli avvisi con nome file, percorso e dettagli. Disponibile durante una pausa o dopo l’elaborazione.",
        "warnings_dialog_title": "Avvisi di elaborazione",
        "log_help_text": "Ogni riga riguarda un file o una fase generale.\n\n• Una riga riuscita inizia direttamente con il nome del file; RIUSCITO non viene più ripetuto.\n• CONFORME, RIPRESO, IGNORATO, ANNULLATO ed ERRORE restano visibili quando aggiungono informazioni utili.\n• I livelli mostrano ingresso → uscita rimisurata e poi l’eventuale risultato del controllo qualità.\n• I pulsanti Avvisi ed Errori aprono elenchi separati con nome, percorso e dettagli. Sono disponibili durante una pausa o dopo l’elaborazione e ogni elenco può essere salvato.\n\nColori: verde = riuscito; arancione = avviso; rosso = file non completato; viola bluastro = ripresa; grigio = informazione, elemento ignorato o annullamento.\n\nQC AVVISO — picco indica che il true peak rimisurato supera di oltre 0,25 dB il limite scelto. Il file viene comunque creato. Per un avviso persistente, scegliere un obiettivo LUFS più basso o un picco massimo più prudente, per esempio −2,0 dBTP.\n\nI tempi cumulativi sommano il lavoro di tutte le attività parallele. Il tempo totale è la durata effettivamente trascorsa.",
        "version_changes": "• Le righe riuscite del registro iniziano dal nome del file, senza ripetere RIUSCITO.\n• Le sei spie mostrano la descrizione completa passando sul cerchio o sulla sigla.\n• Avvisi ed errori sono conservati separatamente con nome, percorso e dettagli; gli elenchi sono consultabili in pausa o al termine ed esportabili come testo UTF-8.\n• Le finestre di aiuto usano un documento scorrevole affidabile, così l’ultima riga resta leggibile nelle dodici lingue.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    },
    "ja": {
        "close_button": "閉じる",
        "errors_button": "エラー ({count})",
        "errors_button_tooltip": "ファイル名、パス、詳細を含むエラー一覧を開きます。一時停止中または処理後に利用できます。",
        "errors_dialog_title": "処理エラー",
        "issue_detail_column": "詳細",
        "issue_file_column": "ファイル",
        "issue_path_column": "パス",
        "save_issue_list": "CSVで保存…",
        "save_issue_list_error": "一覧を保存できませんでした：{error}",
        "save_issue_list_error_title": "保存できません",
        "save_issue_list_title": "CSV一覧を保存",
        "csv_file_filter": "CSVファイル (*.csv)",
        "warnings_button": "警告 ({count})",
        "warnings_button_tooltip": "ファイル名、パス、詳細を含む警告一覧を開きます。一時停止中または処理後に利用できます。",
        "warnings_dialog_title": "処理の警告",
        "log_help_text": "各行はファイルまたは処理全体の段階を示します。\n\n• 成功した行はファイル名から始まり、「成功」を繰り返しません。\n• 適合、再開、スキップ、キャンセル、エラーは、追加情報になる場合だけ表示します。\n• レベルは入力 → 再測定した出力、その後に品質チェック結果を示します。\n• 「警告」と「エラー」ボタンは、ファイル名、パス、詳細を含む別々の一覧を開きます。一時停止中または処理後に利用でき、各一覧を保存できます。\n\n色：緑 = 成功、オレンジ = 警告、赤 = 未完了、青紫 = 再開、灰色 = 情報、スキップ、キャンセル。\n\nQC警告 — ピークは、再測定したトゥルーピークが選択上限を0.25 dB以上超えたことを示します。ファイルは作成されます。警告が続く場合は、より低いLUFS目標または−2.0 dBTPなどの安全な最大ピークを選んでください。\n\n累積時間は並列タスクすべての作業時間の合計です。合計時間は実際の経過時間です。",
        "version_changes": "• 成功したログ行は、重複する「成功」を付けずファイル名から始まります。\n• 6個のランプは、円または略記にポインターを置くと完全な説明を表示します。\n• 警告とエラーはファイル名、パス、詳細とともに別々に保持され、一時停止中または処理後に確認し、UTF-8テキストへ保存できます。\n• ヘルプは信頼性の高いスクロール文書を使用し、12言語すべてで最終行を読めます。\n• 音声エンジンとノーマライズ計算は変更していません。",
    },
    "nl": {
        "close_button": "Sluiten",
        "errors_button": "Fouten ({count})",
        "errors_button_tooltip": "Opent de foutenlijst met bestandsnaam, pad en details. Beschikbaar tijdens een pauze of na de verwerking.",
        "errors_dialog_title": "Verwerkingsfouten",
        "issue_detail_column": "Details",
        "issue_file_column": "Bestand",
        "issue_path_column": "Pad",
        "save_issue_list": "Opslaan als CSV…",
        "save_issue_list_error": "De lijst kon niet worden opgeslagen: {error}",
        "save_issue_list_error_title": "Opslaan mislukt",
        "save_issue_list_title": "CSV-lijst opslaan",
        "csv_file_filter": "CSV-bestanden (*.csv)",
        "warnings_button": "Waarschuwingen ({count})",
        "warnings_button_tooltip": "Opent de waarschuwingen met bestandsnaam, pad en details. Beschikbaar tijdens een pauze of na de verwerking.",
        "warnings_dialog_title": "Verwerkingswaarschuwingen",
        "log_help_text": "Elke regel beschrijft een bestand of een algemene verwerkingsstap.\n\n• Een geslaagde regel begint direct met de bestandsnaam; GESLAAGD wordt niet meer herhaald.\n• CONFORM, HERVAT, OVERGESLAGEN, GEANNULEERD en FOUT blijven zichtbaar wanneer ze nuttige informatie toevoegen.\n• Niveaus tonen invoer → opnieuw gemeten uitvoer, gevolgd door het resultaat van de kwaliteitscontrole.\n• De knoppen Waarschuwingen en Fouten openen aparte lijsten met naam, pad en details. Ze zijn beschikbaar tijdens een pauze of na de verwerking en elke lijst kan worden opgeslagen.\n\nKleuren: groen = geslaagd; oranje = waarschuwing; rood = niet voltooid bestand; blauwviolet = hervatting; grijs = informatie, overslaan of annulering.\n\nQC-WAARSCHUWING — piek betekent dat de opnieuw gemeten true peak meer dan 0,25 dB boven de gekozen grens ligt. Het bestand wordt toch aangemaakt. Kies bij een aanhoudende waarschuwing een lager LUFS-doel of een voorzichtiger maximale piek, bijvoorbeeld −2,0 dBTP.\n\nDe cumulatieve tijden tellen het werk van alle parallelle taken op. De totale tijd is de werkelijk verstreken duur.",
        "version_changes": "• Geslaagde logregels beginnen met de bestandsnaam, zonder herhaald GESLAAGD.\n• De zes lampjes tonen hun volledige beschrijving boven de cirkel of afkorting.\n• Waarschuwingen en fouten blijven apart bewaard met naam, pad en details; de lijsten zijn in pauze of na afloop zichtbaar en als UTF-8-tekst op te slaan.\n• Helpvensters gebruiken een betrouwbaar scrollbaar document, zodat de laatste regel in alle twaalf talen leesbaar blijft.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    },
    "pl": {
        "close_button": "Zamknij",
        "errors_button": "Błędy ({count})",
        "errors_button_tooltip": "Otwiera listę błędów z nazwą pliku, ścieżką i szczegółami. Dostępna podczas pauzy lub po przetwarzaniu.",
        "errors_dialog_title": "Błędy przetwarzania",
        "issue_detail_column": "Szczegóły",
        "issue_file_column": "Plik",
        "issue_path_column": "Ścieżka",
        "save_issue_list": "Zapisz jako CSV…",
        "save_issue_list_error": "Nie można zapisać listy: {error}",
        "save_issue_list_error_title": "Nie można zapisać",
        "save_issue_list_title": "Zapisz listę CSV",
        "csv_file_filter": "Pliki CSV (*.csv)",
        "warnings_button": "Ostrzeżenia ({count})",
        "warnings_button_tooltip": "Otwiera listę ostrzeżeń z nazwą pliku, ścieżką i szczegółami. Dostępna podczas pauzy lub po przetwarzaniu.",
        "warnings_dialog_title": "Ostrzeżenia przetwarzania",
        "log_help_text": "Każdy wiersz dotyczy pliku lub ogólnego etapu przetwarzania.\n\n• Wiersz zakończony powodzeniem zaczyna się od nazwy pliku; SUKCES nie jest już powtarzany.\n• ZGODNY, WZNOWIONO, POMINIĘTO, ANULOWANO i BŁĄD pozostają, gdy przekazują użyteczną informację.\n• Poziomy pokazują wejście → ponownie zmierzone wyjście, a następnie wynik kontroli jakości.\n• Przyciski Ostrzeżenia i Błędy otwierają osobne listy z nazwą, ścieżką i szczegółami. Są dostępne podczas pauzy lub po przetwarzaniu; każdą listę można zapisać.\n\nKolory: zielony = sukces; pomarańczowy = ostrzeżenie; czerwony = plik nieukończony; niebieskofioletowy = wznowienie; szary = informacja, pominięcie lub anulowanie.\n\nQC OSTRZEŻENIE — szczyt oznacza, że ponownie zmierzony true peak przekracza wybrany limit o ponad 0,25 dB. Plik mimo to zostaje utworzony. Przy powtarzającym się ostrzeżeniu wybierz niższy cel LUFS lub bezpieczniejszy szczyt, na przykład −2,0 dBTP.\n\nCzasy skumulowane sumują pracę wszystkich zadań równoległych. Czas całkowity to rzeczywisty czas, który upłynął.",
        "version_changes": "• Udane wiersze dziennika zaczynają się nazwą pliku, bez powtarzania SUKCES.\n• Sześć kontrolek pokazuje pełny opis po wskazaniu koła lub skrótu.\n• Ostrzeżenia i błędy są przechowywane osobno z nazwą, ścieżką i szczegółami; listy są dostępne podczas pauzy lub po zakończeniu i można je zapisać jako tekst UTF-8.\n• Pomoc korzysta z niezawodnego przewijanego dokumentu, dzięki czemu ostatni wiersz jest czytelny we wszystkich dwunastu językach.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    },
    "pt": {
        "close_button": "Fechar",
        "errors_button": "Erros ({count})",
        "errors_button_tooltip": "Abre a lista de erros com nome do ficheiro, caminho e detalhe. Disponível durante uma pausa ou após o processamento.",
        "errors_dialog_title": "Erros do processamento",
        "issue_detail_column": "Detalhe",
        "issue_file_column": "Ficheiro",
        "issue_path_column": "Caminho",
        "save_issue_list": "Guardar como CSV…",
        "save_issue_list_error": "Não foi possível guardar a lista: {error}",
        "save_issue_list_error_title": "Não foi possível guardar",
        "save_issue_list_title": "Guardar a lista CSV",
        "csv_file_filter": "Ficheiros CSV (*.csv)",
        "warnings_button": "Alertas ({count})",
        "warnings_button_tooltip": "Abre a lista de alertas com nome do ficheiro, caminho e detalhe. Disponível durante uma pausa ou após o processamento.",
        "warnings_dialog_title": "Alertas do processamento",
        "log_help_text": "Cada linha corresponde a um ficheiro ou a uma etapa geral.\n\n• Uma linha bem-sucedida começa diretamente pelo nome do ficheiro; SUCESSO deixa de ser repetido.\n• CONFORME, RETOMADO, IGNORADO, CANCELADO e ERRO permanecem quando acrescentam informação útil.\n• Os níveis mostram entrada → saída medida novamente e depois o eventual resultado do controlo de qualidade.\n• Os botões Alertas e Erros abrem listas separadas com nome, caminho e detalhe. Estão disponíveis durante uma pausa ou após o processamento e cada lista pode ser guardada.\n\nCores: verde = sucesso; laranja = alerta; vermelho = ficheiro não terminado; violeta azulado = retoma; cinzento = informação, item ignorado ou cancelamento.\n\nQC ALERTA — pico significa que o true peak medido novamente ultrapassa em mais de 0,25 dB o limite escolhido. O ficheiro é criado na mesma. Para um alerta persistente, escolha um alvo LUFS mais baixo ou um pico máximo mais prudente, por exemplo −2,0 dBTP.\n\nOs tempos acumulados somam o trabalho de todas as tarefas paralelas. O tempo total é a duração real decorrida.",
        "version_changes": "• As linhas bem-sucedidas do registo começam pelo nome do ficheiro, sem repetir SUCESSO.\n• As seis luzes mostram a descrição completa ao passar pelo círculo ou sigla.\n• Alertas e erros ficam separados com nome, caminho e detalhe; as listas estão disponíveis em pausa ou no fim e podem ser guardadas como texto UTF-8.\n• As ajudas usam um documento deslocável fiável, mantendo a última linha legível nos doze idiomas.\n• O motor áudio e os cálculos de normalização permanecem inalterados.",
    },
    "ru": {
        "close_button": "Закрыть",
        "errors_button": "Ошибки ({count})",
        "errors_button_tooltip": "Открывает список ошибок с именем файла, путём и подробностями. Доступен во время паузы или после обработки.",
        "errors_dialog_title": "Ошибки обработки",
        "issue_detail_column": "Подробности",
        "issue_file_column": "Файл",
        "issue_path_column": "Путь",
        "save_issue_list": "Сохранить как CSV…",
        "save_issue_list_error": "Не удалось сохранить список: {error}",
        "save_issue_list_error_title": "Сохранение невозможно",
        "save_issue_list_title": "Сохранить список CSV",
        "csv_file_filter": "Файлы CSV (*.csv)",
        "warnings_button": "Предупреждения ({count})",
        "warnings_button_tooltip": "Открывает список предупреждений с именем файла, путём и подробностями. Доступен во время паузы или после обработки.",
        "warnings_dialog_title": "Предупреждения обработки",
        "log_help_text": "Каждая строка относится к файлу или общему этапу обработки.\n\n• Успешная строка начинается сразу с имени файла; УСПЕШНО больше не повторяется.\n• СООТВЕТСТВУЕТ, ВОЗОБНОВЛЕНО, ПРОПУЩЕНО, ОТМЕНЕНО и ОШИБКА остаются, когда несут полезную информацию.\n• Уровни показывают вход → повторно измеренный выход, затем результат контроля качества.\n• Кнопки «Предупреждения» и «Ошибки» открывают отдельные списки с именем, путём и подробностями. Они доступны во время паузы или после обработки; каждый список можно сохранить.\n\nЦвета: зелёный = успех; оранжевый = предупреждение; красный = файл не завершён; сине-фиолетовый = возобновление; серый = информация, пропуск или отмена.\n\nQC ПРЕДУПРЕЖДЕНИЕ — пик означает, что повторно измеренный истинный пик превышает выбранный предел более чем на 0,25 дБ. Файл всё равно создаётся. При повторяющемся предупреждении выберите более тихую цель LUFS или более осторожный максимальный пик, например −2,0 dBTP.\n\nНакопленные времена суммируют работу всех параллельных задач. Общее время — фактически прошедшая продолжительность.",
        "version_changes": "• Успешные строки журнала начинаются с имени файла, без повторения УСПЕШНО.\n• Все шесть индикаторов показывают полное описание при наведении на круг или сокращение.\n• Предупреждения и ошибки хранятся отдельно с именем, путём и подробностями; списки доступны во время паузы или после обработки и сохраняются как текст UTF-8.\n• Окна справки используют надёжно прокручиваемый документ, поэтому последняя строка читается на всех двенадцати языках.\n• Аудиодвижок и расчёты нормализации не изменены.",
    },
    "zh": {
        "close_button": "关闭",
        "errors_button": "错误 ({count})",
        "errors_button_tooltip": "打开错误列表，其中包含文件名、路径和详情。暂停期间或处理结束后可用。",
        "errors_dialog_title": "处理错误",
        "issue_detail_column": "详情",
        "issue_file_column": "文件",
        "issue_path_column": "路径",
        "save_issue_list": "另存为 CSV…",
        "save_issue_list_error": "无法保存列表：{error}",
        "save_issue_list_error_title": "无法保存",
        "save_issue_list_title": "保存 CSV 列表",
        "csv_file_filter": "CSV 文件 (*.csv)",
        "warnings_button": "警告 ({count})",
        "warnings_button_tooltip": "打开警告列表，其中包含文件名、路径和详情。暂停期间或处理结束后可用。",
        "warnings_dialog_title": "处理警告",
        "log_help_text": "每一行描述一个文件或常规处理步骤。\n\n• 成功的行直接以文件名开头，不再重复“成功”。\n• 合规、已续传、已跳过、已取消和错误只在提供额外信息时保留。\n• 电平显示输入 → 重新测量的输出，之后是可能的质量控制结果。\n• “警告”和“错误”按钮分别打开包含文件名、路径和详情的列表。暂停期间或处理结束后可用，每个列表都能保存。\n\n颜色：绿色 = 成功；橙色 = 警告；红色 = 文件未完成；蓝紫色 = 续传；灰色 = 信息、跳过或取消。\n\nQC 警告—峰值表示重新测得的真实峰值比所选上限高出 0.25 dB 以上。文件仍会创建。若警告持续出现，请选择更低的 LUFS 目标或更安全的最大峰值，例如 −2.0 dBTP。\n\n累计时间会相加所有并行任务的工作时间。总时间是实际经过的时间。",
        "version_changes": "• 成功的日志行现在以文件名开头，不再重复“成功”。\n• 六个指示灯在悬停圆点或缩写时显示完整说明。\n• 警告与错误分别保留文件名、路径和详情；列表可在暂停期间或处理结束后查看，并可保存为 UTF-8 文本。\n• 帮助窗口使用可靠的可滚动文档，确保十二种语言的最后一行均可阅读。\n• 音频引擎和标准化计算保持不变。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12306.items():
    EXTRA_TEXTS[_language].update(_updates)


# Version 1.23.7 clarifies that quality control measures every output format,
# removes hover descriptions from the compact status lights, localizes the
# full QC log phrase, and stabilizes the results-header geometry and score
# palette.  Audio processing remains unchanged.
TRANSLATION_UPDATES_12307 = {
    "de": {
        "qc_log": " — Qualitätskontrolle: {quality}",
        "quality_control_tooltip": "Misst jede Ausgabe unabhängig vom Format erneut. Nur MP3-Dateien, die über den Dynamikpfad verarbeitet werden, können anschließend bis zu dreimal neu kodiert werden, um eine Abweichung zu korrigieren. Das Deaktivieren dieser Option ändert die Encoderqualität nicht, entfernt aber die Abschlussprüfung, diese Korrekturen und die Anzeigeaktivität.",
        "version_changes": "• Die Hilfe zur Qualitätskontrolle stellt klar, dass jedes Ausgabeformat erneut gemessen wird; nur MP3-Dateien des Dynamikpfads können bis zu drei korrigierende Neukodierungen erhalten.\n• Die sechs Optionsleuchten zeigen beim Darüberfahren keine Beschreibung mehr.\n• Das Ergebnis der Qualitätskontrolle ist im Protokoll vollständig übersetzt, ohne englische Abkürzung.\n• Protokoll und Anzeige verwenden gleich hohe Kopfzeilen; der Anzeigetitel bleibt in seinem Bereich und die Anzeige behält ihre feste Größe.\n• Das Bewertungsfeld verwendet eine ruhigere, zum aktiven Design passende Farbpalette.\n• Audio-Engine und Normalisierungsberechnungen sind unverändert.",
    },
    "es": {
        "qc_log": " — control de calidad: {quality}",
        "quality_control_tooltip": "Vuelve a medir cada salida, sea cual sea su formato. Solo los MP3 procesados por la ruta dinámica pueden recodificarse después hasta tres veces para corregir una desviación. Desactivar esta opción no cambia la calidad del codificador, pero elimina la verificación final, esas correcciones y la actividad del medidor.",
        "version_changes": "• La ayuda del control de calidad aclara que se vuelve a medir cada formato de salida; solo los MP3 de la ruta dinámica pueden recibir hasta tres recodificaciones correctivas.\n• Las seis luces de opciones ya no muestran descripciones al pasar el puntero.\n• El resultado del control de calidad aparece totalmente traducido en el registro, sin siglas inglesas.\n• El registro y el medidor usan cabeceras de la misma altura; el título del medidor permanece en su zona y el medidor conserva su tamaño fijo.\n• El panel de puntuación usa una paleta más suave y coherente con el tema activo.\n• El motor de audio y los cálculos de normalización no cambian.",
    },
    "hi": {
        "qc_log": " — गुणवत्ता नियंत्रण: {quality}",
        "quality_control_tooltip": "हर आउटपुट को उसके प्रारूप की परवाह किए बिना दोबारा मापता है। केवल डायनेमिक पथ से संसाधित MP3 को किसी विचलन को सुधारने के लिए बाद में अधिकतम तीन बार फिर से एन्कोड किया जा सकता है। इस विकल्प को बंद करने से एन्कोडर गुणवत्ता नहीं बदलती, लेकिन अंतिम जाँच, ये सुधार और मीटर की गतिविधि हट जाती है।",
        "version_changes": "• गुणवत्ता नियंत्रण की सहायता स्पष्ट करती है कि हर आउटपुट प्रारूप को दोबारा मापा जाता है; केवल डायनेमिक पथ वाले MP3 को अधिकतम तीन सुधारात्मक री-एन्कोड मिल सकते हैं।\n• छह विकल्प संकेतक अब माउस ले जाने पर विवरण नहीं दिखाते।\n• गुणवत्ता नियंत्रण का परिणाम लॉग में पूरी तरह अनूदित है और अंग्रेज़ी संक्षेप नहीं रखता।\n• लॉग और लाउडनेस मीटर के शीर्षक समान ऊँचाई के हैं; मीटर का शीर्षक अपने क्षेत्र में रहता है और मीटर का आकार स्थिर रहता है।\n• स्कोर पैनल सक्रिय थीम के अनुरूप अधिक संतुलित रंगों का उपयोग करता है।\n• ऑडियो इंजन और सामान्यीकरण गणनाएँ अपरिवर्तित हैं।",
    },
    "it": {
        "qc_log": " — controllo qualità: {quality}",
        "quality_control_tooltip": "Rimisura ogni uscita, indipendentemente dal formato. Solo gli MP3 elaborati dal percorso dinamico possono poi essere ricodificati fino a tre volte per correggere uno scostamento. Disattivare questa opzione non cambia la qualità dell’encoder, ma elimina la verifica finale, queste correzioni e l’attività del misuratore.",
        "version_changes": "• L’aiuto del controllo qualità chiarisce che ogni formato di uscita viene rimisurato; solo gli MP3 del percorso dinamico possono ricevere fino a tre ricodifiche correttive.\n• Le sei spie delle opzioni non mostrano più descrizioni al passaggio del puntatore.\n• Il risultato del controllo qualità è interamente tradotto nel registro, senza sigle inglesi.\n• Registro e misuratore usano intestazioni della stessa altezza; il titolo resta nella propria area e il misuratore conserva la dimensione fissa.\n• Il pannello del punteggio usa una tavolozza più discreta e coerente con il tema attivo.\n• Il motore audio e i calcoli di normalizzazione restano invariati.",
    },
    "ja": {
        "qc_log": " — 品質チェック：{quality}",
        "quality_control_tooltip": "形式にかかわらず、すべての出力を再測定します。その後、ずれを補正するために最大3回再エンコードされる可能性があるのは、ダイナミック経路で処理したMP3だけです。このオプションを無効にしてもエンコーダー品質は変わりませんが、最終確認、これらの補正、メーター表示は行われません。",
        "version_changes": "• 品質チェックのヘルプで、すべての出力形式を再測定し、最大3回の補正再エンコードの対象はダイナミック経路のMP3だけであることを明記しました。\n• 6個のオプションランプは、ポインターを置いても説明を表示しません。\n• ログの品質チェック結果を、英語の略記を残さず完全に翻訳しました。\n• ログとメーターの見出しを同じ高さにし、タイトルを領域内に保ったままメーターの固定サイズを維持します。\n• スコア欄は、選択中のテーマに合う落ち着いた配色を使用します。\n• 音声エンジンとノーマライズ計算は変更していません。",
    },
    "nl": {
        "qc_log": " — kwaliteitscontrole: {quality}",
        "quality_control_tooltip": "Meet elke uitvoer opnieuw, ongeacht de bestandsindeling. Alleen MP3-bestanden die via het dynamische pad worden verwerkt, kunnen daarna maximaal drie keer opnieuw worden gecodeerd om een afwijking te corrigeren. Uitschakelen verandert de encoderkwaliteit niet, maar verwijdert de eindcontrole, deze correcties en de meteractiviteit.",
        "version_changes": "• De hulp bij kwaliteitscontrole maakt duidelijk dat elk uitvoerformaat opnieuw wordt gemeten; alleen MP3-bestanden van het dynamische pad kunnen maximaal drie corrigerende hercoderingen krijgen.\n• De zes optielampjes tonen geen beschrijving meer bij aanwijzen.\n• Het resultaat van de kwaliteitscontrole is volledig vertaald in het logboek, zonder Engelse afkorting.\n• Logboek en meter gebruiken koppen met dezelfde hoogte; de metertitel blijft in zijn gebied en de meter behoudt zijn vaste formaat.\n• Het scorevlak gebruikt een rustigere kleurstelling die bij het actieve thema past.\n• De audio-engine en normalisatieberekeningen zijn ongewijzigd.",
    },
    "pl": {
        "qc_log": " — kontrola jakości: {quality}",
        "quality_control_tooltip": "Ponownie mierzy każdy plik wyjściowy niezależnie od formatu. Tylko pliki MP3 przetwarzane ścieżką dynamiczną mogą być następnie ponownie kodowane do trzech razy, aby skorygować odchylenie. Wyłączenie tej opcji nie zmienia jakości kodera, ale usuwa końcową kontrolę, te korekty i działanie miernika.",
        "version_changes": "• Pomoc kontroli jakości wyjaśnia, że każdy format wyjściowy jest ponownie mierzony; tylko MP3 ze ścieżki dynamicznej mogą otrzymać do trzech korekcyjnych ponownych kodowań.\n• Sześć kontrolek opcji nie wyświetla już opisu po wskazaniu.\n• Wynik kontroli jakości jest w dzienniku w pełni przetłumaczony, bez angielskiego skrótu.\n• Dziennik i miernik mają nagłówki tej samej wysokości; tytuł miernika pozostaje w swoim obszarze, a miernik zachowuje stały rozmiar.\n• Panel wyniku używa spokojniejszej palety zgodnej z aktywnym motywem.\n• Silnik audio i obliczenia normalizacji pozostają bez zmian.",
    },
    "pt": {
        "qc_log": " — controlo de qualidade: {quality}",
        "quality_control_tooltip": "Volta a medir cada saída, independentemente do formato. Só os MP3 processados pelo caminho dinâmico podem depois ser recodificados até três vezes para corrigir um desvio. Desativar esta opção não altera a qualidade do codificador, mas remove a verificação final, essas correções e a atividade do medidor.",
        "version_changes": "• A ajuda do controlo de qualidade esclarece que todos os formatos de saída são medidos novamente; só os MP3 do caminho dinâmico podem receber até três recodificações corretivas.\n• As seis luzes das opções deixam de mostrar descrições ao passar o ponteiro.\n• O resultado do controlo de qualidade fica totalmente traduzido no registo, sem sigla inglesa.\n• O registo e o medidor usam cabeçalhos da mesma altura; o título permanece na sua área e o medidor conserva o tamanho fixo.\n• O painel da pontuação usa uma paleta mais discreta e coerente com o tema ativo.\n• O motor áudio e os cálculos de normalização permanecem inalterados.",
    },
    "ru": {
        "qc_log": " — контроль качества: {quality}",
        "quality_control_tooltip": "Повторно измеряет каждый выходной файл независимо от формата. Только MP3, обработанные по динамическому пути, затем могут быть повторно закодированы до трёх раз для исправления отклонения. Отключение этой опции не меняет качество кодера, но убирает итоговую проверку, эти исправления и работу индикатора.",
        "version_changes": "• В справке по контролю качества указано, что повторно измеряется каждый формат вывода; только MP3 динамического пути могут получить до трёх корректирующих перекодирований.\n• Шесть индикаторов параметров больше не показывают описание при наведении.\n• Результат контроля качества в журнале полностью переведён и не содержит английского сокращения.\n• Заголовки журнала и индикатора имеют одинаковую высоту; название остаётся в своей области, а размер индикатора фиксирован.\n• Панель оценки использует более спокойную палитру, соответствующую активной теме.\n• Аудиодвижок и расчёты нормализации не изменены.",
    },
    "zh": {
        "qc_log": " — 质量控制：{quality}",
        "quality_control_tooltip": "无论格式如何，都会重新测量每个输出。只有通过动态路径处理的MP3才可能随后重新编码最多三次，以纠正偏差。关闭此选项不会改变编码器质量，但会取消最终验证、这些纠正和响度表活动。",
        "version_changes": "• 质量控制帮助明确说明所有输出格式都会重新测量；只有动态路径的MP3可能进行最多三次纠正性重新编码。\n• 六个选项指示灯在悬停时不再显示说明。\n• 日志中的质量控制结果已完整翻译，不再保留英文缩写。\n• 日志和响度表使用相同高度的标题栏；响度表标题保持在其区域内，响度表维持固定尺寸。\n• 评分面板使用更柔和、与当前主题一致的配色。\n• 音频引擎和标准化计算保持不变。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12307.items():
    EXTRA_TEXTS[_language].update(_updates)


# Experimental 1.24.0 hybrid-engine notice shown by the version button.
TRANSLATION_UPDATES_12400_TEST = {
    "fr": {
        "version_changes": "• Version expérimentale : FFmpeg reste chargé du décodage, des encodeurs, des métadonnées et du muxage.\n• Le filtre ebur128 tente les mesures initiales et le contrôle qualité ; les trois premières mesures sont comparées à la référence loudnorm.\n• Le chemin rapide n’est autorisé que si les écarts I/TP/LRA/seuil restent dans 0,15/0,15/0,20/0,20 et si la conversion linéaire garde ses marges de sécurité.\n• Les MP3 dynamiques, les résultats proches d’une limite et toute calibration incertaine ou refusée utilisent loudnorm intégralement.\n• Un diagnostic JSON accompagne le rapport CSV pour mesurer les usages rapides, les replis, les écarts et les temps.",
    },
    "en": {
        "version_changes": "• Experimental build: FFmpeg still handles decoding, encoders, metadata and muxing.\n• The ebur128 filter attempts initial and quality-control measurements; the first three measurements are compared with the loudnorm reference.\n• The fast path is enabled only when I/TP/LRA/threshold differences stay within 0.15/0.15/0.20/0.20 and linear conversion retains its safety margins.\n• Dynamic MP3 files, near-limit results and any uncertain or rejected calibration use loudnorm in full.\n• A JSON diagnostic accompanies the CSV report with fast uses, fallbacks, differences and timings.",
    },
    "de": {
        "version_changes": "• Experimentelle Version: FFmpeg übernimmt weiterhin Decodierung, Encoder, Metadaten und Muxing.\n• Der Filter ebur128 versucht Erst- und Qualitätsmessungen; die ersten drei Messungen werden mit der loudnorm-Referenz verglichen.\n• Der schnelle Pfad wird nur freigegeben, wenn die Abweichungen I/TP/LRA/Schwelle innerhalb 0,15/0,15/0,20/0,20 bleiben und die lineare Umwandlung Sicherheitsabstände wahrt.\n• Dynamische MP3-Dateien, grenznahe Ergebnisse sowie unsichere oder abgelehnte Kalibrierungen verwenden vollständig loudnorm.\n• Eine JSON-Diagnose ergänzt den CSV-Bericht um schnelle Nutzungen, Rückfälle, Abweichungen und Zeiten.",
    },
    "es": {
        "version_changes": "• Versión experimental: FFmpeg sigue gestionando la decodificación, los codificadores, los metadatos y el multiplexado.\n• El filtro ebur128 intenta las mediciones iniciales y de control de calidad; las tres primeras se comparan con la referencia loudnorm.\n• La vía rápida solo se habilita si las diferencias I/TP/LRA/umbral permanecen dentro de 0,15/0,15/0,20/0,20 y la conversión lineal conserva sus márgenes de seguridad.\n• Los MP3 dinámicos, los resultados próximos a un límite y toda calibración incierta o rechazada usan loudnorm completo.\n• Un diagnóstico JSON acompaña al informe CSV con usos rápidos, repliegues, diferencias y tiempos.",
    },
    "it": {
        "version_changes": "• Versione sperimentale: FFmpeg continua a gestire decodifica, codificatori, metadati e muxing.\n• Il filtro ebur128 tenta le misure iniziali e di controllo qualità; le prime tre vengono confrontate con il riferimento loudnorm.\n• Il percorso rapido è abilitato solo se gli scarti I/TP/LRA/soglia restano entro 0,15/0,15/0,20/0,20 e la conversione lineare conserva i margini di sicurezza.\n• Gli MP3 dinamici, i risultati vicini a un limite e ogni calibrazione incerta o rifiutata usano loudnorm completo.\n• Una diagnostica JSON accompagna il rapporto CSV con usi rapidi, ripieghi, scarti e tempi.",
    },
    "pt": {
        "version_changes": "• Versão experimental: o FFmpeg continua responsável pela descodificação, codificadores, metadados e multiplexagem.\n• O filtro ebur128 tenta as medições iniciais e de controlo de qualidade; as três primeiras são comparadas com a referência loudnorm.\n• O caminho rápido só é ativado se as diferenças I/TP/LRA/limiar ficarem dentro de 0,15/0,15/0,20/0,20 e a conversão linear mantiver margens de segurança.\n• MP3 dinâmicos, resultados próximos de um limite e qualquer calibração incerta ou recusada usam loudnorm integralmente.\n• Um diagnóstico JSON acompanha o relatório CSV com utilizações rápidas, recuos, diferenças e tempos.",
    },
    "nl": {
        "version_changes": "• Experimentele versie: FFmpeg blijft decodering, encoders, metadata en muxing verzorgen.\n• Het filter ebur128 probeert de eerste metingen en kwaliteitsmetingen; de eerste drie worden met de loudnorm-referentie vergeleken.\n• Het snelle pad wordt alleen vrijgegeven als de verschillen I/TP/LRA/drempel binnen 0,15/0,15/0,20/0,20 blijven en lineaire conversie haar veiligheidsmarges behoudt.\n• Dynamische MP3-bestanden, resultaten dicht bij een grens en onzekere of afgewezen kalibraties gebruiken volledig loudnorm.\n• Een JSON-diagnose vult het CSV-rapport aan met snel gebruik, terugvallen, verschillen en tijden.",
    },
    "pl": {
        "version_changes": "• Wersja eksperymentalna: FFmpeg nadal obsługuje dekodowanie, kodery, metadane i multipleksowanie.\n• Filtr ebur128 próbuje pomiarów początkowych i kontroli jakości; pierwsze trzy pomiary są porównywane z odniesieniem loudnorm.\n• Szybka ścieżka jest włączana tylko wtedy, gdy różnice I/TP/LRA/próg mieszczą się w 0,15/0,15/0,20/0,20, a konwersja liniowa zachowuje marginesy bezpieczeństwa.\n• Dynamiczne MP3, wyniki bliskie granicy oraz niepewna lub odrzucona kalibracja w pełni używają loudnorm.\n• Diagnostyka JSON uzupełnia raport CSV o szybkie użycia, przejścia awaryjne, różnice i czasy.",
    },
    "ru": {
        "version_changes": "• Экспериментальная версия: FFmpeg по-прежнему выполняет декодирование, кодирование, обработку метаданных и мультиплексирование.\n• Фильтр ebur128 пробует начальные и контрольные измерения; первые три сравниваются с эталоном loudnorm.\n• Быстрый путь включается только при отклонениях I/TP/LRA/порога не более 0,15/0,15/0,20/0,20 и достаточных запасах для линейного преобразования.\n• Динамические MP3, результаты у границы и любая неопределённая или отклонённая калибровка полностью используют loudnorm.\n• Диагностика JSON дополняет отчёт CSV данными о быстрых проходах, возвратах, отклонениях и времени.",
    },
    "ja": {
        "version_changes": "• 実験版：デコード、エンコード、メタデータ、マルチプレックスは引き続きFFmpegが担当します。\n• ebur128フィルターが初回測定と品質チェック測定を試し、最初の3測定を基準のloudnormと比較します。\n• I/TP/LRA/しきい値の差が0.15/0.15/0.20/0.20以内で、線形変換の安全余裕が保たれる場合だけ高速経路を有効にします。\n• ダイナミック経路のMP3、限界に近い結果、不確実または不合格の校正ではloudnormを完全に使用します。\n• 高速使用、フォールバック、差、時間を記録したJSON診断がCSVレポートに添付されます。",
    },
    "hi": {
        "version_changes": "• प्रायोगिक संस्करण: डिकोडिंग, एन्कोडर, मेटाडेटा और मक्सिंग अब भी FFmpeg संभालता है।\n• ebur128 फ़िल्टर प्रारंभिक और गुणवत्ता-जाँच माप आज़माता है; पहले तीन मापों की loudnorm संदर्भ से तुलना होती है।\n• तेज़ पथ तभी चालू होता है जब I/TP/LRA/थ्रेशोल्ड अंतर 0.15/0.15/0.20/0.20 के भीतर हों और रैखिक रूपांतरण में सुरक्षा मार्जिन बना रहे।\n• डायनामिक MP3, सीमा के पास परिणाम और अनिश्चित या अस्वीकृत कैलिब्रेशन पूरी तरह loudnorm का उपयोग करते हैं।\n• तेज़ उपयोग, फ़ॉलबैक, अंतर और समय वाला JSON निदान CSV रिपोर्ट के साथ बनता है।",
    },
    "zh": {
        "version_changes": "• 实验版本：FFmpeg仍负责解码、编码器、元数据和封装。\n• ebur128滤镜尝试初始测量和质量控制测量；前三次测量会与loudnorm基准比较。\n• 仅当I/TP/LRA/阈值差异保持在0.15/0.15/0.20/0.20以内且线性转换保留安全余量时，才启用快速路径。\n• 动态MP3、接近限值的结果以及任何不确定或被拒绝的校准都会完整使用loudnorm。\n• JSON诊断文件会随CSV报告生成，记录快速路径、回退、差异和耗时。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12400_TEST.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language].update(_updates)


# Previous diagnostic notice retained as translation history.
TRANSLATION_UPDATES_12403_TEST = {
    "fr": {
        "version_changes": "• Version diagnostique : ebur128 observe la première tentative de QC de chaque MP3 et chacune des trois reprises possibles, avant la décision suivante de loudnorm.\n• loudnorm reste seul responsable du verdict, du calcul des reprises, du choix de la meilleure tentative et du fichier livré ; ebur128 ne peut modifier aucun résultat audio.\n• Le JSON indique le numéro de tentative, la cible interne, les valeurs et écarts I/TP, l’accord des décisions de qualité et de reprise, ainsi que la tentative finalement retenue.\n• L’exclusion globale des MP3 dynamiques est retirée uniquement du classement hypothétique ; les tolérances et marges restent sans autorité.\n• Les sorties non MP3 ne sont pas sondées ; le surcoût de chaque mesure MP3 supplémentaire est volontaire.",
    },
    "en": {
        "version_changes": "• Diagnostic build: ebur128 observes each MP3’s first QC attempt and every one of up to three retries before loudnorm makes the next decision.\n• loudnorm alone controls the verdict, retry calculation, best-attempt selection and delivered file; ebur128 cannot change any audio result.\n• The JSON records the attempt number, internal target, I/TP values and differences, quality and retry decision agreement, and the attempt ultimately selected.\n• The blanket dynamic-MP3 exclusion is removed only from hypothetical classification; tolerances and margins remain non-authoritative.\n• Non-MP3 outputs are not probed; the extra time for every MP3 shadow measurement is intentional.",
    },
    "de": {
        "version_changes": "• Diagnoseversion: ebur128 beobachtet den ersten QC-Versuch jeder MP3-Datei und bis zu drei Wiederholungen, bevor loudnorm die nächste Entscheidung trifft.\n• Nur loudnorm bestimmt Urteil, Wiederholungsberechnung, Auswahl des besten Versuchs und Ausgabedatei; ebur128 kann kein Audioergebnis ändern.\n• Die JSON-Datei enthält Versuchsnummer, internes Ziel, I/TP-Werte und Abweichungen, Übereinstimmung der Qualitäts- und Wiederholungsentscheidungen sowie den ausgewählten Versuch.\n• Der pauschale Ausschluss dynamischer MP3-Dateien entfällt nur in der hypothetischen Einstufung; Toleranzen und Abstände bleiben ohne Einfluss.\n• Nicht-MP3-Ausgaben werden nicht geprüft; die zusätzliche Messzeit pro MP3-Versuch ist beabsichtigt.",
    },
    "es": {
        "version_changes": "• Versión de diagnóstico: ebur128 observa el primer intento de control de cada MP3 y hasta tres reintentos antes de que loudnorm tome la siguiente decisión.\n• Solo loudnorm determina el veredicto, el cálculo de reintentos, la selección del mejor intento y el archivo entregado; ebur128 no puede cambiar el audio.\n• El JSON registra el número de intento, el objetivo interno, valores y diferencias I/TP, la coincidencia de las decisiones de calidad y reintento y el intento seleccionado.\n• La exclusión general de MP3 dinámicos se elimina únicamente de la clasificación hipotética; tolerancias y márgenes no tienen autoridad.\n• No se sondean salidas que no sean MP3; el tiempo adicional de cada medición es intencionado.",
    },
    "it": {
        "version_changes": "• Versione diagnostica: ebur128 osserva il primo controllo di ogni MP3 e fino a tre nuovi tentativi prima della decisione successiva di loudnorm.\n• Solo loudnorm determina esito, calcolo dei nuovi tentativi, scelta del tentativo migliore e file consegnato; ebur128 non modifica l’audio.\n• Il JSON registra numero del tentativo, obiettivo interno, valori e scarti I/TP, accordo delle decisioni di qualità e ripetizione e tentativo selezionato.\n• L’esclusione generale degli MP3 dinamici viene rimossa solo dalla classificazione ipotetica; tolleranze e margini restano senza autorità.\n• Le uscite non MP3 non vengono sondate; il tempo aggiuntivo di ogni misura è intenzionale.",
    },
    "pt": {
        "version_changes": "• Versão de diagnóstico: o ebur128 observa a primeira tentativa de controlo de cada MP3 e até três repetições antes da decisão seguinte do loudnorm.\n• Só o loudnorm determina o resultado, o cálculo das repetições, a escolha da melhor tentativa e o ficheiro entregue; o ebur128 não altera o áudio.\n• O JSON regista o número da tentativa, o alvo interno, valores e diferenças I/TP, concordância das decisões de qualidade e repetição e a tentativa escolhida.\n• A exclusão geral dos MP3 dinâmicos é removida apenas da classificação hipotética; tolerâncias e margens continuam sem autoridade.\n• As saídas não MP3 não são sondadas; o tempo adicional de cada medição é intencional.",
    },
    "nl": {
        "version_changes": "• Diagnoseversie: ebur128 observeert de eerste QC-poging van elke MP3 en maximaal drie nieuwe pogingen voordat loudnorm de volgende beslissing neemt.\n• Alleen loudnorm bepaalt oordeel, berekening van nieuwe pogingen, keuze van de beste poging en geleverd bestand; ebur128 wijzigt geen audio.\n• De JSON vermeldt pogingnummer, intern doel, I/TP-waarden en verschillen, overeenstemming van kwaliteits- en herhalingsbeslissingen en de gekozen poging.\n• De algemene uitsluiting van dynamische MP3-bestanden vervalt alleen in de hypothetische indeling; toleranties en marges blijven zonder invloed.\n• Niet-MP3-uitvoer wordt niet onderzocht; de extra meettijd per poging is opzettelijk.",
    },
    "pl": {
        "version_changes": "• Wersja diagnostyczna: ebur128 obserwuje pierwszą próbę QC każdego MP3 i maksymalnie trzy ponowienia przed kolejną decyzją loudnorm.\n• Tylko loudnorm określa werdykt, oblicza ponowienia, wybiera najlepszą próbę i plik wynikowy; ebur128 nie zmienia dźwięku.\n• JSON zapisuje numer próby, cel wewnętrzny, wartości i różnice I/TP, zgodność decyzji jakości i ponowienia oraz wybraną próbę.\n• Ogólne wykluczenie dynamicznych MP3 usunięto wyłącznie z klasyfikacji hipotetycznej; tolerancje i marginesy nie mają wpływu.\n• Wyjścia inne niż MP3 nie są badane; dodatkowy czas każdego pomiaru jest zamierzony.",
    },
    "ru": {
        "version_changes": "• Диагностическая версия: ebur128 наблюдает первую QC-попытку каждого MP3 и до трёх повторов до следующего решения loudnorm.\n• Только loudnorm определяет результат, рассчитывает повторы, выбирает лучшую попытку и итоговый файл; ebur128 не изменяет звук.\n• JSON записывает номер попытки, внутреннюю цель, значения и отклонения I/TP, совпадение решений качества и повтора, а также выбранную попытку.\n• Общий запрет для динамических MP3 снят только в гипотетической классификации; допуски и запасы не влияют на обработку.\n• Выходы не в MP3 не проверяются; дополнительное время каждого измерения предусмотрено намеренно.",
    },
    "ja": {
        "version_changes": "• 診断版：各MP3の最初のQCと最大3回の再試行を、loudnormが次の判断を行う前にebur128が観察します。\n• 判定、再試行の計算、最良試行の選択、納品ファイルはloudnormだけが決定し、ebur128は音声を変更できません。\n• JSONには試行番号、内部目標、I/TP値と差、品質・再試行判断の一致、最終選択された試行を記録します。\n• ダイナミックMP3の一律除外を外すのは仮想分類のみで、許容値と安全余裕に処理権限はありません。\n• MP3以外は測定せず、各追加測定の時間増加は意図したものです。",
    },
    "hi": {
        "version_changes": "• नैदानिक संस्करण: loudnorm के अगले निर्णय से पहले ebur128 हर MP3 की पहली QC कोशिश और अधिकतम तीन पुनःप्रयासों को देखता है।\n• परिणाम, पुनःप्रयास गणना, सर्वोत्तम कोशिश और दी गई फ़ाइल केवल loudnorm तय करता है; ebur128 ऑडियो नहीं बदल सकता।\n• JSON में कोशिश संख्या, आंतरिक लक्ष्य, I/TP मान व अंतर, गुणवत्ता और पुनःप्रयास निर्णयों की सहमति तथा चुनी गई कोशिश दर्ज होती है।\n• डायनामिक MP3 का सामान्य बहिष्कार केवल काल्पनिक वर्गीकरण से हटाया गया है; सहनशीलता और मार्जिन का कोई अधिकार नहीं है।\n• गैर-MP3 आउटपुट नहीं मापे जाते; हर अतिरिक्त माप का समय जानबूझकर जोड़ा गया है।",
    },
    "zh": {
        "version_changes": "• 诊断版本：在loudnorm作出下一步决定前，ebur128观察每个MP3的首次QC及最多三次重试。\n• 判定、重试计算、最佳尝试选择和最终文件均只由loudnorm决定；ebur128不能改变音频。\n• JSON记录尝试编号、内部目标、I/TP数值与差异、质量和重试决定是否一致，以及最终选中的尝试。\n• 仅在假设分类中取消对动态MP3的一律排除；容差和安全余量不参与实际处理。\n• 不探测非MP3输出；每次附加测量带来的时间开销是有意的。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12403_TEST.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language].update(_updates)


# Experimental 1.24.4 notice: ebur128 certifies only the strict inner QC
# region.  The first boundary/error fallback permanently locks that file and
# every later retry to loudnorm.
TRANSLATION_UPDATES_12404_TEST = {
    "fr": {
        "version_changes": "• Version expérimentale : l’analyse initiale, la conversion et les reprises MP3 restent fondées sur loudnorm.\n• Le QC MP3 essaie ebur128 en premier ; il ne peut valider qu’une sortie nettement à l’intérieur des limites de sonie et de crête.\n• Au premier résultat proche d’une limite ou à la première erreur, le fichier bascule définitivement sur loudnorm pour cet essai et toutes ses reprises.\n• Les sorties non MP3 utilisent loudnorm ; le JSON indique le moteur réellement utilisé, les replis, le verrou permanent et les temps.",
    },
    "en": {
        "version_changes": "• Experimental build: initial analysis, conversion and MP3 retries remain based on loudnorm.\n• MP3 QC tries ebur128 first; it may certify only an output clearly inside the loudness and peak limits.\n• At the first near-boundary result or error, that file permanently switches to loudnorm for the current attempt and every retry.\n• Non-MP3 outputs use loudnorm; the JSON records the engine actually used, fallbacks, permanent lock and timings.",
    },
    "de": {
        "version_changes": "• Experimentelle Version: Erstanalyse, Konvertierung und MP3-Wiederholungen beruhen weiterhin auf loudnorm.\n• Die MP3-Qualitätskontrolle versucht zuerst ebur128; bestätigt werden dürfen nur Ergebnisse deutlich innerhalb der Lautheits- und Spitzenwertgrenzen.\n• Beim ersten grenznahen Ergebnis oder Fehler wechselt die Datei für diesen Versuch und alle Wiederholungen dauerhaft zu loudnorm.\n• Nicht-MP3-Ausgaben verwenden loudnorm; die JSON-Datei protokolliert Motor, Rückfälle, dauerhafte Sperre und Zeiten.",
    },
    "es": {
        "version_changes": "• Versión experimental: el análisis inicial, la conversión y los reintentos MP3 siguen basados en loudnorm.\n• El control MP3 prueba primero ebur128; solo puede validar una salida claramente dentro de los límites de sonoridad y pico.\n• Ante el primer resultado cercano a un límite o error, ese archivo cambia definitivamente a loudnorm para el intento actual y todos los reintentos.\n• Las salidas no MP3 usan loudnorm; el JSON registra el motor usado, los repliegues, el bloqueo permanente y los tiempos.",
    },
    "it": {
        "version_changes": "• Versione sperimentale: analisi iniziale, conversione e nuovi tentativi MP3 restano basati su loudnorm.\n• Il QC MP3 prova prima ebur128; può convalidare solo un’uscita nettamente entro i limiti di sonorità e picco.\n• Al primo risultato vicino a un limite o errore, il file passa definitivamente a loudnorm per il tentativo corrente e tutti i successivi.\n• Le uscite non MP3 usano loudnorm; il JSON registra motore usato, ripieghi, blocco permanente e tempi.",
    },
    "pt": {
        "version_changes": "• Versão experimental: a análise inicial, a conversão e as repetições MP3 continuam baseadas no loudnorm.\n• O QC de MP3 tenta primeiro o ebur128; só pode validar uma saída claramente dentro dos limites de sonoridade e pico.\n• No primeiro resultado próximo de um limite ou erro, o ficheiro muda definitivamente para loudnorm nessa tentativa e em todas as repetições.\n• As saídas não MP3 usam loudnorm; o JSON regista o motor usado, recuos, bloqueio permanente e tempos.",
    },
    "nl": {
        "version_changes": "• Experimentele versie: eerste analyse, conversie en MP3-herpogingen blijven op loudnorm gebaseerd.\n• De MP3-kwaliteitscontrole probeert eerst ebur128; alleen een resultaat ruim binnen de luidheids- en piekgrenzen mag worden goedgekeurd.\n• Bij het eerste grensgeval of de eerste fout schakelt dat bestand voor deze poging en alle herpogingen permanent over op loudnorm.\n• Niet-MP3-uitvoer gebruikt loudnorm; de JSON vermeldt motor, terugval, permanente vergrendeling en tijden.",
    },
    "pl": {
        "version_changes": "• Wersja eksperymentalna: analiza początkowa, konwersja i ponowienia MP3 nadal opierają się na loudnorm.\n• Kontrola MP3 najpierw próbuje ebur128; może zatwierdzić tylko wynik wyraźnie mieszczący się w granicach głośności i szczytu.\n• Pierwszy wynik blisko granicy lub błąd trwale przełącza plik na loudnorm dla tej próby i wszystkich ponowień.\n• Wyjścia inne niż MP3 używają loudnorm; JSON zapisuje silnik, powroty, trwałą blokadę i czasy.",
    },
    "ru": {
        "version_changes": "• Экспериментальная версия: начальный анализ, преобразование и повторы MP3 по-прежнему основаны на loudnorm.\n• QC для MP3 сначала запускает ebur128; он подтверждает только результат с явным запасом по громкости и пику.\n• Первый пограничный результат или ошибка навсегда переключает файл на loudnorm для этой попытки и всех повторов.\n• Для выходов не MP3 используется loudnorm; JSON записывает движок, откаты, постоянную блокировку и время.",
    },
    "ja": {
        "version_changes": "• 実験版：初期解析、変換、MP3再試行は引き続きloudnormに基づきます。\n• MP3のQCは最初にebur128を試し、ラウドネスとピークの限界から十分内側の出力だけを合格にできます。\n• 境界に近い結果またはエラーが一度でも出ると、そのファイルは現在の試行と以後の再試行で常にloudnormを使用します。\n• MP3以外はloudnormを使用し、JSONに使用エンジン、フォールバック、恒久ロック、時間を記録します。",
    },
    "hi": {
        "version_changes": "• प्रायोगिक संस्करण: प्रारंभिक विश्लेषण, रूपांतरण और MP3 पुनःप्रयास loudnorm पर ही आधारित रहते हैं।\n• MP3 QC पहले ebur128 आज़माता है; वह केवल उस आउटपुट को स्वीकार कर सकता है जो लाउडनेस और पीक सीमाओं के स्पष्ट रूप से भीतर हो।\n• सीमा के पास पहला परिणाम या त्रुटि आते ही वह फ़ाइल वर्तमान और सभी अगली कोशिशों के लिए स्थायी रूप से loudnorm पर चली जाती है।\n• गैर-MP3 आउटपुट loudnorm का उपयोग करते हैं; JSON वास्तविक इंजन, फ़ॉलबैक, स्थायी लॉक और समय दर्ज करता है।",
    },
    "zh": {
        "version_changes": "• 实验版本：初始分析、转换和MP3重试仍以loudnorm为基础。\n• MP3质量控制先尝试ebur128；它只能确认明显处于响度和峰值限制以内的输出。\n• 一旦出现接近边界的结果或错误，该文件在当前尝试及所有后续重试中永久改用loudnorm。\n• 非MP3输出使用loudnorm；JSON记录实际引擎、回退、永久锁定和耗时。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12404_TEST.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language].update(_updates)


# Stable 1.24.5 documentation refresh. The audio route is unchanged; these
# strings describe the full behavior shipped in the validated stable build.
TRANSLATION_UPDATES_12405_RC = {
    "fr": {
        "report_qc_engine": "moteur_qc",
        "version_changes": "• Version stable 1.24.5 : MP3, FLAC, WAV, AIFF, M4A, OGG et Opus ; modes Piste et Album.\n• Convertir vise une cible LUFS sous un plafond True Peak ; les fichiers déjà conformes sont copiés octet pour octet. ReplayGain préserve le flux audio et Analyser ne crée pas de fichier audio.\n• Chaque sortie est remesurée. Le QC MP3 utilise ebur128 uniquement dans une zone sûre, puis verrouille loudnorm dès la première limite ou erreur ; les autres formats utilisent loudnorm.\n• Les MP3 dynamiques peuvent recevoir jusqu’à trois tentatives correctives.\n• Le CSV indique le moteur QC : une décimale pour ebur128 et deux pour loudnorm ; le diagnostic JSON conserve les décisions et les temps.\n• Face à une approche de gain MP3 quantifié ou par balises, LUFScale privilégie une cible LUFS configurable, un plafond True Peak, sept formats, une vérification de sortie et une traçabilité détaillée. Le compromis est le réencodage des formats avec perte non conformes en mode Convertir.",
    },
    "en": {
        "report_qc_engine": "qc_engine",
        "version_changes": "• Stable 1.24.5: MP3, FLAC, WAV, AIFF, M4A, OGG and Opus; Track and Album modes.\n• Convert targets configurable LUFS under a True Peak ceiling; already-compliant files are copied byte for byte. ReplayGain preserves the audio stream and Analyze creates no audio file.\n• Every output is remeasured. MP3 QC uses ebur128 only in a safe region, then locks to loudnorm at the first boundary or error; other formats use loudnorm.\n• Dynamic MP3 processing may receive up to three corrective attempts.\n• CSV reports the QC engine: one decimal for ebur128 and two for loudnorm; diagnostic JSON retains decisions and timing.\n• Compared with quantized MP3 gain or tag-based methods, LUFScale prioritizes a configurable LUFS target, True Peak ceiling, seven formats, output verification and a detailed audit trail. The trade-off is re-encoding non-compliant lossy files in Convert mode.",
    },
    "de": {
        "report_qc_engine": "qc_messverfahren",
        "help_overview": "• Normalisierung, ReplayGain oder Analyse für MP3, FLAC, WAV, AIFF, M4A, OGG und Opus.\n• Track- und Album-Modus; Unterschiede zwischen Titeln bleiben im Album erhalten.\n• Ordnerstruktur, kompatible Metadaten und Cover bleiben erhalten. Originale werden nie geändert.\n• Bereits konforme Quellen werden bytegenau kopiert.\n• Auto-Parallelität, Analyse-Cache und Fortsetzung nach Unterbrechung.\n• Qualitätskontrolle, CSV-Bericht, Diagnose-JSON, Fortschritt, CPU, Lautheitsmesser und Zeitschätzung.\n• Zwölf Sprachen mit jeweils eigener PDF-Anleitung.",
        "version_changes": "• Stabile Version 1.24.5: sieben Audioformate sowie Track- und Album-Modus.\n• Konvertieren zielt auf LUFS unter einem True-Peak-Limit; bereits konforme Dateien werden bytegenau kopiert. ReplayGain bewahrt den Audiostream, Analysieren erzeugt keine Audiodatei.\n• Jede Ausgabe wird erneut gemessen. MP3-QC nutzt ebur128 nur im sicheren Bereich und sperrt an der ersten Grenze oder beim ersten Fehler auf loudnorm; andere Formate nutzen loudnorm.\n• Dynamische MP3-Verarbeitung erlaubt bis zu drei Korrekturversuche.\n• CSV nennt die QC-Methode mit einer Dezimale für ebur128 und zwei für loudnorm; JSON bewahrt Entscheidungen und Zeiten.\n• Gegenüber quantisiertem MP3-Gain oder Tags priorisiert LUFScale ein konfigurierbares LUFS-Ziel, True Peak, sieben Formate, Ausgabekontrolle und Nachweis. Dafür werden nicht konforme verlustbehaftete Dateien beim Konvertieren neu codiert.",
    },
    "es": {
        "report_qc_engine": "motor_control_calidad",
        "help_overview": "• Normalización, ReplayGain o análisis de MP3, FLAC, WAV, AIFF, M4A, OGG y Opus.\n• Modos Pista y Álbum, conservando las diferencias entre pistas del álbum.\n• Se conservan árbol de carpetas, metadatos y carátulas compatibles. Los originales nunca cambian.\n• Las fuentes ya conformes se copian byte a byte.\n• Paralelismo Auto, caché de análisis y reanudación tras una interrupción.\n• Control de calidad, CSV, JSON diagnóstico, progreso, CPU, medidor y tiempo estimado.\n• Doce idiomas, cada uno con su guía PDF.",
        "version_changes": "• Versión estable 1.24.5: siete formatos de audio y modos Pista y Álbum.\n• Convertir busca LUFS bajo un límite True Peak; los archivos ya conformes se copian byte a byte. ReplayGain conserva el flujo y Analizar no crea audio.\n• Cada salida se vuelve a medir. El QC MP3 usa ebur128 solo en la zona segura y bloquea loudnorm al primer límite o error; los demás formatos usan loudnorm.\n• El MP3 dinámico admite hasta tres intentos correctivos.\n• El CSV indica el motor QC con un decimal para ebur128 y dos para loudnorm; el JSON guarda decisiones y tiempos.\n• Frente a ganancia MP3 cuantizada o etiquetas, LUFScale prioriza objetivo LUFS configurable, True Peak, siete formatos, verificación y trazabilidad. El coste es recodificar archivos con pérdida no conformes al Convertir.",
    },
    "it": {
        "report_qc_engine": "motore_controllo_qualità",
        "help_overview": "• Normalizzazione, ReplayGain o analisi di MP3, FLAC, WAV, AIFF, M4A, OGG e Opus.\n• Modalità Traccia e Album, con differenze tra i brani dell’album preservate.\n• Albero cartelle, metadati e copertine compatibili sono conservati. Gli originali non cambiano mai.\n• Le sorgenti già conformi sono copiate byte per byte.\n• Parallelismo Auto, cache di analisi e ripresa dopo interruzione.\n• Controllo qualità, CSV, JSON diagnostico, avanzamento, CPU, misuratore e stima del tempo.\n• Dodici lingue, ciascuna con la propria guida PDF.",
        "version_changes": "• Versione stabile 1.24.5: sette formati audio e modalità Traccia e Album.\n• Converti punta a LUFS sotto un limite True Peak; i file già conformi sono copiati byte per byte. ReplayGain conserva il flusso e Analizza non crea audio.\n• Ogni uscita è rimisurata. Il QC MP3 usa ebur128 solo nella zona sicura e blocca loudnorm al primo limite o errore; gli altri formati usano loudnorm.\n• L’elaborazione MP3 dinamica consente fino a tre tentativi correttivi.\n• Il CSV indica il motore QC con un decimale per ebur128 e due per loudnorm; il JSON conserva decisioni e tempi.\n• Rispetto a gain MP3 quantizzato o tag, LUFScale privilegia obiettivo LUFS configurabile, True Peak, sette formati, verifica e tracciabilità. Il compromesso è ricodificare i file con perdita non conformi in Converti.",
    },
    "pt": {
        "report_qc_engine": "motor_controlo_qualidade",
        "help_overview": "• Normalização, ReplayGain ou análise de MP3, FLAC, WAV, AIFF, M4A, OGG e Opus.\n• Modos Pista e Álbum, preservando diferenças entre faixas do álbum.\n• Árvore de pastas, metadados e capas compatíveis são preservados. Os originais nunca mudam.\n• Origens já conformes são copiadas byte a byte.\n• Paralelismo Auto, cache de análise e retoma após interrupção.\n• Controlo de qualidade, CSV, JSON diagnóstico, progresso, CPU, medidor e tempo estimado.\n• Doze idiomas, cada um com o seu guia PDF.",
        "version_changes": "• Versão estável 1.24.5: sete formatos de áudio e modos Pista e Álbum.\n• Converter visa LUFS sob um teto True Peak; ficheiros já conformes são copiados byte a byte. ReplayGain preserva o fluxo e Analisar não cria áudio.\n• Cada saída é novamente medida. O QC MP3 usa ebur128 só na zona segura e bloqueia loudnorm no primeiro limite ou erro; outros formatos usam loudnorm.\n• O MP3 dinâmico permite até três tentativas corretivas.\n• O CSV indica o motor QC com uma decimal para ebur128 e duas para loudnorm; o JSON guarda decisões e tempos.\n• Face a ganho MP3 quantizado ou etiquetas, LUFScale privilegia alvo LUFS configurável, True Peak, sete formatos, verificação e rastreabilidade. O compromisso é recodificar formatos com perdas não conformes ao Converter.",
    },
    "nl": {
        "report_qc_engine": "qc_meetmethode",
        "help_overview": "• Normalisatie, ReplayGain of analyse van MP3, FLAC, WAV, AIFF, M4A, OGG en Opus.\n• Track- en Albummodus; verschillen tussen albumtracks blijven behouden.\n• Mapstructuur, compatibele metadata en artwork blijven behouden. Originelen veranderen nooit.\n• Reeds conforme bronnen worden byte voor byte gekopieerd.\n• Automatische paralleliteit, analysecache en hervatten na onderbreking.\n• Kwaliteitscontrole, CSV, diagnose-JSON, voortgang, CPU, meter en tijdschatting.\n• Twaalf talen, elk met een eigen PDF-handleiding.",
        "version_changes": "• Stabiele versie 1.24.5: zeven audioformaten en Track- en Albummodus.\n• Converteren richt op LUFS onder een True Peak-plafond; reeds conforme bestanden worden byte voor byte gekopieerd. ReplayGain behoudt de stream en Analyseren maakt geen audio.\n• Elke uitvoer wordt opnieuw gemeten. MP3-QC gebruikt ebur128 alleen in het veilige gebied en zet loudnorm vast bij de eerste grens of fout; andere formaten gebruiken loudnorm.\n• Dynamische MP3-verwerking biedt maximaal drie correctiepogingen.\n• CSV vermeldt de QC-engine met één decimaal voor ebur128 en twee voor loudnorm; JSON bewaart beslissingen en tijden.\n• Tegenover gekwantiseerde MP3-gain of tags kiest LUFScale voor instelbaar LUFS, True Peak, zeven formaten, uitvoercontrole en traceerbaarheid. De afweging is hercodering van niet-conforme verliesformaten bij Converteren.",
    },
    "pl": {
        "report_qc_engine": "silnik_kontroli_jakości",
        "help_overview": "• Normalizacja, ReplayGain lub analiza MP3, FLAC, WAV, AIFF, M4A, OGG i Opus.\n• Tryby Ścieżka i Album z zachowaniem różnic między utworami albumu.\n• Zachowana struktura folderów, zgodne metadane i okładki. Oryginały nigdy się nie zmieniają.\n• Źródła już zgodne są kopiowane bajt w bajt.\n• Automatyczna równoległość, pamięć analizy i wznawianie po przerwaniu.\n• Kontrola jakości, CSV, JSON diagnostyczny, postęp, CPU, miernik i szacowany czas.\n• Dwanaście języków, każdy z własnym przewodnikiem PDF.",
        "version_changes": "• Stabilna wersja 1.24.5: siedem formatów oraz tryby Ścieżka i Album.\n• Konwersja celuje w LUFS pod limitem True Peak; pliki już zgodne są kopiowane bajt w bajt. ReplayGain zachowuje strumień, Analiza nie tworzy audio.\n• Każde wyjście jest mierzone ponownie. QC MP3 używa ebur128 tylko w bezpiecznym obszarze i blokuje loudnorm przy pierwszej granicy lub błędzie; inne formaty używają loudnorm.\n• Dynamiczne MP3 dopuszcza trzy próby korekcyjne.\n• CSV wskazuje silnik QC: jedno miejsce dla ebur128, dwa dla loudnorm; JSON przechowuje decyzje i czasy.\n• Wobec kwantowanego gainu MP3 lub tagów LUFScale stawia na ustawiany LUFS, True Peak, siedem formatów, weryfikację i audyt. Ceną jest ponowne kodowanie niezgodnych formatów stratnych w Konwersji.",
    },
    "ru": {
        "report_qc_engine": "движок_контроля_качества",
        "help_overview": "• Нормализация, ReplayGain или анализ MP3, FLAC, WAV, AIFF, M4A, OGG и Opus.\n• Режимы Трек и Альбом с сохранением различий между треками альбома.\n• Сохраняются структура папок, совместимые метаданные и обложки. Оригиналы не меняются.\n• Уже соответствующие источники копируются байт в байт.\n• Автопараллельность, кэш анализа и продолжение после прерывания.\n• Контроль качества, CSV, диагностический JSON, ход работы, CPU, измеритель и оценка времени.\n• Двенадцать языков, для каждого отдельное руководство PDF.",
        "version_changes": "• Стабильная версия 1.24.5: семь аудиоформатов, режимы Трек и Альбом.\n• Конвертация нацелена на LUFS под пределом True Peak; уже соответствующие файлы копируются байт в байт. ReplayGain сохраняет поток, Анализ не создаёт аудио.\n• Каждый выход измеряется повторно. QC MP3 использует ebur128 только в безопасной зоне и фиксирует loudnorm при первой границе или ошибке; другие форматы используют loudnorm.\n• Динамический MP3 допускает до трёх корректирующих попыток.\n• CSV указывает движок QC: один знак для ebur128 и два для loudnorm; JSON хранит решения и время.\n• В сравнении с квантованным gain MP3 или тегами LUFScale даёт настраиваемые LUFS, True Peak, семь форматов, проверку и аудит. Компромисс — повторное кодирование несоответствующих форматов с потерями при Конвертации.",
    },
    "ja": {
        "report_qc_engine": "品質チェック_測定方式",
        "help_overview": "• MP3、FLAC、WAV、AIFF、M4A、OGG、Opusの変換、ReplayGain、解析。\n• トラック／アルバムモード。アルバム内の曲間差を保持します。\n• フォルダー構造、対応メタデータ、アートワークを保持。元ファイルは変更しません。\n• 適合済みソースはバイト単位で同一コピーします。\n• 自動並列処理、解析キャッシュ、中断後の再開。\n• 品質管理、CSV、診断JSON、進捗、CPU、メーター、時間予測。\n• 12言語それぞれに専用PDFガイドがあります。",
        "version_changes": "• 安定版1.24.5：7音声形式、トラック／アルバムモード。\n• 変換はTrue Peak上限内でLUFSを目指し、適合済みファイルは同一コピーします。ReplayGainは音声ストリームを保持し、解析は音声ファイルを作りません。\n• 全出力を再測定します。MP3 QCは安全領域だけebur128を使い、最初の境界またはエラーでloudnormに固定します。他形式はloudnormです。\n• 動的MP3は最大3回の補正試行が可能です。\n• CSVはQCエンジンを示し、ebur128は小数1桁、loudnormは2桁。JSONは判断と時間を保存します。\n• 量子化MP3ゲインやタグ方式に比べ、LUFScaleは設定可能なLUFS、True Peak、7形式、出力検証、監査を重視します。変換時に不適合な非可逆形式を再エンコードする点がトレードオフです。",
    },
    "hi": {
        "report_qc_engine": "गुणवत्ता_जाँच_इंजन",
        "help_overview": "• MP3, FLAC, WAV, AIFF, M4A, OGG और Opus का normalisation, ReplayGain या analysis।\n• Track और Album modes; album tracks के आपसी अंतर सुरक्षित।\n• Folder tree, समर्थित metadata और artwork सुरक्षित; originals कभी नहीं बदलते।\n• पहले से अनुरूप स्रोत byte-for-byte कॉपी होते हैं।\n• Auto parallelism, analysis cache और interruption के बाद resume।\n• Quality control, CSV, diagnostic JSON, progress, CPU, meter और time estimate।\n• बारह भाषाएँ, हर एक का अपना PDF guide।",
        "version_changes": "• स्थिर 1.24.5: सात audio formats और Track/Album modes।\n• Convert True Peak सीमा में LUFS लक्ष्य पाता है; अनुरूप files byte-for-byte copy होती हैं। ReplayGain stream बचाता है और Analyze audio file नहीं बनाता।\n• हर output फिर मापा जाता है। MP3 QC ebur128 केवल सुरक्षित क्षेत्र में उपयोग करता है और पहली सीमा या error पर loudnorm lock करता है; अन्य formats loudnorm उपयोग करते हैं।\n• Dynamic MP3 में अधिकतम तीन corrective attempts हैं।\n• CSV QC engine बताता है: ebur128 के लिए एक और loudnorm के लिए दो दशमलव; JSON निर्णय और समय रखता है।\n• Quantized MP3 gain या tags की तुलना में LUFScale configurable LUFS, True Peak, सात formats, output verification और audit देता है। Convert में non-compliant lossy formats का re-encode इसका trade-off है।",
    },
    "zh": {
        "report_qc_engine": "质量控制_测量引擎",
        "help_overview": "• 支持 MP3、FLAC、WAV、AIFF、M4A、OGG 和 Opus 的标准化、ReplayGain 或分析。\n• 单曲与专辑模式，保留专辑曲目之间的差异。\n• 保留目录结构、兼容的元数据和封面；绝不修改原文件。\n• 已合规的源文件逐字节复制。\n• 自动并行、分析缓存及中断后续作。\n• 质量控制、CSV、诊断 JSON、进度、CPU、响度表和时间估计。\n• 十二种语言，每种都有独立 PDF 指南。",
        "version_changes": "• 稳定版 1.24.5：七种音频格式，以及单曲/专辑模式。\n• 转换在 True Peak 上限内达到 LUFS 目标；已合规文件逐字节复制。ReplayGain 保留音频流，分析不创建音频文件。\n• 每个输出都会复测。MP3 QC 只在安全区使用 ebur128，遇到首个边界或错误后锁定 loudnorm；其他格式使用 loudnorm。\n• 动态 MP3 最多可进行三次纠正尝试。\n• CSV 标明 QC 引擎：ebur128 一位小数，loudnorm 两位；JSON 保留决策与耗时。\n• 相比量化 MP3 增益或标签方法，LUFScale 强调可配置 LUFS、True Peak、七种格式、输出验证和审计。代价是在转换模式下重新编码不合规的有损格式。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12405_RC.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language].update(_updates)


# LUFScale 1.24.6 keeps the public version label plain and makes the meter's
# five-analysis refresh cadence and file attribution explicit in every catalogue.
TRANSLATION_UPDATES_12406 = {
    "fr": {
        "loudness_meter_current_file": "Dernier : {file}",
        "loudness_meter_no_file": "En attente d’une analyse",
        "loudness_meter_worst_file": "Plus grand écart : {file}",
        "loudness_meter_worst_file_detail": "Plus grand écart des 8 dernières analyses : {file} — {measured} LUFS pour {expected} LUFS, écart {deviation} LU.",
        "loudness_meter_help_text": "Le trait rouge est la cible et la valeur bleue suit chaque sortie remesurée. Min et Max de la fenêtre glissante de 8 résultats sont publiés toutes les 5 analyses ; le dernier groupe incomplet est publié à la fin du traitement. La ligne sous le vumètre nomme le fichier présentant le plus grand écart parmi les 8 dernières analyses. Le vumètre reste inactif sans contrôle qualité.",
        "loudness_meter_tooltip": "Cible rouge, dernière sortie en bleu. Min et Max sont mis à jour par groupes de 5 analyses. Le fichier du plus grand écart récent est indiqué sous le vumètre.",
        "loudness_score_tooltip": "Le score utilise les 8 dernières sorties réellement remesurées. L’écart RMS résume leur distance à la cible : 100 = résultat exact, 50 = 0,5 LU et 0 = 1 LU ou plus. La ligne sous le vumètre identifie le fichier dont l’écart absolu est le plus élevé dans cette fenêtre.",
        "version_changes": "• Les boutons −/+ désactivés suivent désormais correctement le thème clair.\n• Les onglets Audio et Options utilisent une seule bordure continue, indépendante du dessin natif macOS.\n• Min et Max sont publiés par groupes de cinq analyses ; le fichier du plus grand écart récent est indiqué sous le vumètre.\n• Les listes d’alertes et d’erreurs restent exportées en CSV.\n• L’identité affichée est simplement 1.24.6.",
    },
    "en": {
        "loudness_meter_current_file": "Latest: {file}",
        "loudness_meter_no_file": "Waiting for an analysis",
        "loudness_meter_worst_file": "Largest error: {file}",
        "loudness_meter_worst_file_detail": "Largest error in the latest 8 analyses: {file} — {measured} LUFS for {expected} LUFS, {deviation} LU error.",
        "loudness_meter_help_text": "The rolling-window Min and Max for the latest 8 results are published every 5 analyses; an incomplete final group is published when processing ends. The line below the meter names the file with the largest error among the latest 8 analyses. The meter stays inactive without quality control.",
        "loudness_meter_tooltip": "Red target, latest output in blue. Min and Max update in groups of 5 analyses. The file with the largest recent error appears below the meter.",
        "loudness_score_tooltip": "The score uses the latest 8 genuinely remeasured outputs. RMS error summarizes their distance from target: 100 is exact, 50 is 0.5 LU, and 0 is 1 LU or more. The line below the meter identifies the file with the largest absolute error in this window.",
        "version_changes": "• Disabled −/+ buttons now follow the light theme correctly.\n• Audio and Options use one continuous page border independent of native macOS drawing.\n• Min and Max are published in groups of five analyses, and the file with the largest recent error appears below the meter.\n• Warning and error lists remain exportable as CSV.\n• The displayed identity is simply 1.24.6.",
    },
    "de": {
        "loudness_meter_current_file": "Zuletzt: {file}",
        "loudness_meter_no_file": "Warten auf eine Analyse",
        "loudness_meter_worst_file": "Größte Abweichung: {file}",
        "loudness_meter_worst_file_detail": "Größte Abweichung der letzten 8 Analysen: {file} — {measured} LUFS statt {expected} LUFS, Abweichung {deviation} LU.",
        "loudness_meter_help_text": "Min und Max des gleitenden Fensters der letzten 8 Ergebnisse werden alle 5 Analysen veröffentlicht; eine unvollständige Schlussgruppe erscheint am Verarbeitungsende. Unter dem Messgerät steht die Datei mit der größten Abweichung der letzten 8 Analysen.",
        "loudness_meter_tooltip": "Rotes Ziel, letzte Ausgabe in Blau. Min und Max werden in Gruppen von 5 Analysen aktualisiert; darunter steht die Datei mit der größten jüngsten Abweichung.",
        "loudness_score_tooltip": "Der Zielwert verwendet die letzten 8 erneut gemessenen Ausgaben. 100 ist exakt, 50 entspricht 0,5 LU RMS-Abweichung und 0 entspricht 1 LU oder mehr. Unter dem Messgerät steht die Datei mit der größten absoluten Abweichung.",
        "version_changes": "• Deaktivierte −/+-Tasten passen nun zum hellen Thema.\n• Audio und Optionen besitzen eine einzige durchgehende Seitenumrandung.\n• Min und Max erscheinen in Fünfergruppen; die Datei mit der größten jüngsten Abweichung steht unter dem Messgerät.\n• Warnungs- und Fehlerlisten bleiben als CSV exportierbar.\n• Angezeigt wird nur 1.24.6.",
    },
    "es": {
        "loudness_meter_current_file": "Último: {file}",
        "loudness_meter_no_file": "Esperando un análisis",
        "loudness_meter_worst_file": "Mayor desviación: {file}",
        "loudness_meter_worst_file_detail": "Mayor desviación de los últimos 8 análisis: {file} — {measured} LUFS para {expected} LUFS, desviación {deviation} LU.",
        "loudness_meter_help_text": "Min y Max de la ventana móvil de los últimos 8 resultados se publican cada 5 análisis; el grupo final incompleto se publica al terminar. Debajo del medidor aparece el archivo con mayor desviación entre los últimos 8 análisis.",
        "loudness_meter_tooltip": "Objetivo rojo y última salida en azul. Min y Max se actualizan por grupos de 5 análisis; debajo aparece el archivo con mayor desviación reciente.",
        "loudness_score_tooltip": "La puntuación usa las últimas 8 salidas medidas de nuevo. 100 es exacto, 50 equivale a 0,5 LU de error RMS y 0 a 1 LU o más. Debajo del medidor se identifica el archivo con mayor error absoluto.",
        "version_changes": "• Los botones −/+ desactivados respetan el tema claro.\n• Audio y Opciones usan un único borde continuo.\n• Min y Max se publican en grupos de cinco y se muestra el archivo con mayor desviación reciente.\n• Las listas de avisos y errores siguen exportándose en CSV.\n• La identidad mostrada es solo 1.24.6.",
    },
    "it": {
        "loudness_meter_current_file": "Ultimo: {file}",
        "loudness_meter_no_file": "In attesa di un’analisi",
        "loudness_meter_worst_file": "Scarto maggiore: {file}",
        "loudness_meter_worst_file_detail": "Scarto maggiore nelle ultime 8 analisi: {file} — {measured} LUFS rispetto a {expected} LUFS, scarto {deviation} LU.",
        "loudness_meter_help_text": "Min e Max della finestra mobile degli ultimi 8 risultati sono pubblicati ogni 5 analisi; il gruppo finale incompleto appare al termine. Sotto il misuratore compare il file con lo scarto maggiore delle ultime 8 analisi.",
        "loudness_meter_tooltip": "Obiettivo rosso e ultima uscita in blu. Min e Max si aggiornano per gruppi di 5 analisi; sotto compare il file con lo scarto recente maggiore.",
        "loudness_score_tooltip": "Il punteggio usa le ultime 8 uscite rimisurate. 100 è esatto, 50 equivale a 0,5 LU di errore RMS e 0 a 1 LU o più. Sotto il misuratore è indicato il file con l’errore assoluto maggiore.",
        "version_changes": "• I pulsanti −/+ disabilitati ora rispettano il tema chiaro.\n• Audio e Opzioni usano un solo bordo continuo.\n• Min e Max sono pubblicati in gruppi di cinque e viene indicato il file con lo scarto recente maggiore.\n• Gli elenchi di avvisi ed errori restano esportabili in CSV.\n• L’identità visualizzata è semplicemente 1.24.6.",
    },
    "pt": {
        "loudness_meter_current_file": "Último: {file}",
        "loudness_meter_no_file": "A aguardar uma análise",
        "loudness_meter_worst_file": "Maior desvio: {file}",
        "loudness_meter_worst_file_detail": "Maior desvio das últimas 8 análises: {file} — {measured} LUFS para {expected} LUFS, desvio {deviation} LU.",
        "loudness_meter_help_text": "Min e Max da janela móvel dos últimos 8 resultados são publicados a cada 5 análises; o grupo final incompleto aparece no fim. Sob o medidor surge o ficheiro com o maior desvio das últimas 8 análises.",
        "loudness_meter_tooltip": "Alvo vermelho e última saída em azul. Min e Max atualizam-se por grupos de 5 análises; abaixo aparece o ficheiro com o maior desvio recente.",
        "loudness_score_tooltip": "A pontuação usa as últimas 8 saídas novamente medidas. 100 é exato, 50 equivale a 0,5 LU de erro RMS e 0 a 1 LU ou mais. Sob o medidor é identificado o ficheiro com o maior erro absoluto.",
        "version_changes": "• Os botões −/+ desativados respeitam agora o tema claro.\n• Áudio e Opções usam uma única borda contínua.\n• Min e Max são publicados em grupos de cinco e o ficheiro com maior desvio recente é indicado.\n• As listas de alertas e erros continuam exportáveis em CSV.\n• A identidade apresentada é apenas 1.24.6.",
    },
    "nl": {
        "loudness_meter_current_file": "Laatste: {file}",
        "loudness_meter_no_file": "Wachten op een analyse",
        "loudness_meter_worst_file": "Grootste afwijking: {file}",
        "loudness_meter_worst_file_detail": "Grootste afwijking van de laatste 8 analyses: {file} — {measured} LUFS voor {expected} LUFS, afwijking {deviation} LU.",
        "loudness_meter_help_text": "Min en Max van het schuivende venster met de laatste 8 resultaten verschijnen elke 5 analyses; een onvolledige laatste groep verschijnt aan het einde. Onder de meter staat het bestand met de grootste afwijking van de laatste 8 analyses.",
        "loudness_meter_tooltip": "Rood doel en laatste uitvoer in blauw. Min en Max worden per 5 analyses bijgewerkt; daaronder staat het bestand met de grootste recente afwijking.",
        "loudness_score_tooltip": "De score gebruikt de laatste 8 opnieuw gemeten uitvoerbestanden. 100 is exact, 50 is 0,5 LU RMS-fout en 0 is 1 LU of meer. Onder de meter staat het bestand met de grootste absolute fout.",
        "version_changes": "• Uitgeschakelde −/+-knoppen volgen nu het lichte thema.\n• Audio en Opties gebruiken één ononderbroken rand.\n• Min en Max verschijnen in groepen van vijf en het bestand met de grootste recente afwijking wordt getoond.\n• Waarschuwings- en foutenlijsten blijven als CSV exporteerbaar.\n• Alleen 1.24.6 wordt als identiteit getoond.",
    },
    "pl": {
        "loudness_meter_current_file": "Ostatni: {file}",
        "loudness_meter_no_file": "Oczekiwanie na analizę",
        "loudness_meter_worst_file": "Największe odchylenie: {file}",
        "loudness_meter_worst_file_detail": "Największe odchylenie z ostatnich 8 analiz: {file} — {measured} LUFS przy celu {expected} LUFS, odchylenie {deviation} LU.",
        "loudness_meter_help_text": "Min i Max ruchomego okna ostatnich 8 wyników są publikowane co 5 analiz; niepełna grupa końcowa pojawia się po zakończeniu. Pod miernikiem widnieje plik o największym odchyleniu z ostatnich 8 analiz.",
        "loudness_meter_tooltip": "Czerwony cel i ostatni wynik na niebiesko. Min i Max aktualizują się grupami po 5 analiz; poniżej widnieje plik o największym ostatnim odchyleniu.",
        "loudness_score_tooltip": "Wynik obejmuje 8 ostatnich ponownie zmierzonych plików. 100 oznacza dokładny cel, 50 błąd RMS 0,5 LU, a 0 błąd 1 LU lub większy. Pod miernikiem wskazany jest plik o największym błędzie bezwzględnym.",
        "version_changes": "• Wyłączone przyciski −/+ są teraz zgodne z jasnym motywem.\n• Audio i Opcje używają jednej ciągłej ramki.\n• Min i Max są publikowane grupami po pięć, a plik o największym ostatnim odchyleniu jest wskazany.\n• Listy ostrzeżeń i błędów nadal można eksportować do CSV.\n• Wyświetlana identyfikacja to wyłącznie 1.24.6.",
    },
    "ru": {
        "loudness_meter_current_file": "Последний: {file}",
        "loudness_meter_no_file": "Ожидание анализа",
        "loudness_meter_worst_file": "Наибольшее отклонение: {file}",
        "loudness_meter_worst_file_detail": "Наибольшее отклонение за последние 8 анализов: {file} — {measured} LUFS при цели {expected} LUFS, отклонение {deviation} LU.",
        "loudness_meter_help_text": "Min и Max скользящего окна последних 8 результатов публикуются каждые 5 анализов; неполная последняя группа появляется по завершении. Под измерителем указан файл с наибольшим отклонением за последние 8 анализов.",
        "loudness_meter_tooltip": "Красная цель и последний выход синим. Min и Max обновляются группами по 5 анализов; ниже указан файл с наибольшим недавним отклонением.",
        "loudness_score_tooltip": "Оценка использует последние 8 повторно измеренных выходов. 100 — точное совпадение, 50 — ошибка RMS 0,5 LU, 0 — 1 LU или больше. Под измерителем указан файл с наибольшей абсолютной ошибкой.",
        "version_changes": "• Отключённые кнопки −/+ теперь соответствуют светлой теме.\n• Вкладки Аудио и Параметры используют одну непрерывную рамку.\n• Min и Max публикуются группами по пять; указан файл с наибольшим недавним отклонением.\n• Списки предупреждений и ошибок по-прежнему экспортируются в CSV.\n• Отображается только номер 1.24.6.",
    },
    "ja": {
        "loudness_meter_current_file": "最新：{file}",
        "loudness_meter_no_file": "解析待ち",
        "loudness_meter_worst_file": "最大偏差：{file}",
        "loudness_meter_worst_file_detail": "直近8件の最大偏差：{file} — 目標 {expected} LUFS に対して {measured} LUFS、偏差 {deviation} LU。",
        "loudness_meter_help_text": "直近8件の移動ウィンドウの Min／Max は5件の解析ごとに更新し、最後の不足分は処理終了時に表示します。メーター下には直近8件で偏差が最大のファイルを表示します。品質管理を無効にするとメーターは動作しません。",
        "loudness_meter_tooltip": "赤が目標、青が最新出力です。Min／Max は5件ごとに更新し、下に最近の最大偏差ファイルを表示します。",
        "loudness_score_tooltip": "スコアは再測定した直近8件を使用します。100は一致、50はRMS偏差0.5 LU、0は1 LU以上です。メーター下に絶対偏差が最大のファイルを表示します。",
        "version_changes": "• 無効な−／＋ボタンがライトテーマに正しく従います。\n• Audio／Options は途切れない単一枠を使用します。\n• Min／Max を5件ごとに更新し、最近の最大偏差ファイルを表示します。\n• 警告／エラー一覧はCSVで保存できます。\n• 表示名は1.24.6のみです。",
    },
    "hi": {
        "loudness_meter_current_file": "नवीनतम: {file}",
        "loudness_meter_no_file": "विश्लेषण की प्रतीक्षा",
        "loudness_meter_worst_file": "सबसे बड़ा अंतर: {file}",
        "loudness_meter_worst_file_detail": "पिछले 8 विश्लेषणों में सबसे बड़ा अंतर: {file} — {expected} LUFS लक्ष्य के लिए {measured} LUFS, अंतर {deviation} LU।",
        "loudness_meter_help_text": "पिछले 8 results की moving window के Min और Max हर 5 analyses के बाद प्रकाशित होते हैं; अधूरा अंतिम समूह processing के अंत में दिखता है। मीटर के नीचे पिछले 8 analyses में सबसे बड़े अंतर वाली file दिखाई जाती है।",
        "loudness_meter_tooltip": "लाल लक्ष्य, नीले रंग में नवीनतम output। Min और Max हर 5 analyses में update होते हैं; नीचे सबसे बड़े हालिया अंतर वाली file दिखती है।",
        "loudness_score_tooltip": "Score पिछले 8 दोबारा मापे गए outputs का उपयोग करता है। 100 सटीक, 50 का अर्थ 0.5 LU RMS अंतर और 0 का अर्थ 1 LU या अधिक है। मीटर के नीचे सबसे बड़े absolute अंतर वाली file दिखती है।",
        "version_changes": "• Disabled −/+ buttons अब light theme से मेल खाते हैं।\n• Audio और Options में एक लगातार border है।\n• Min और Max पाँच analyses के समूह में प्रकाशित होते हैं और सबसे बड़े हालिया अंतर वाली file दिखाई जाती है।\n• Warning और error lists CSV में export होती रहती हैं।\n• Display identity केवल 1.24.6 है।",
    },
    "zh": {
        "loudness_meter_current_file": "最新：{file}",
        "loudness_meter_no_file": "等待分析",
        "loudness_meter_worst_file": "最大偏差：{file}",
        "loudness_meter_worst_file_detail": "最近 8 次分析中的最大偏差：{file} — 目标 {expected} LUFS，实测 {measured} LUFS，偏差 {deviation} LU。",
        "loudness_meter_help_text": "最近 8 个结果的滑动窗口 Min 和 Max 每完成 5 次分析后发布；处理结束时会发布不足 5 次的最后一组。表头下方显示最近 8 次分析中偏差最大的文件。关闭质量控制时，响度表不工作。",
        "loudness_meter_tooltip": "红色为目标，蓝色为最新输出。Min 和 Max 每 5 次分析更新一次；下方显示最近偏差最大的文件。",
        "loudness_score_tooltip": "评分使用最近 8 个实际复测输出。100 表示完全一致，50 表示 RMS 偏差 0.5 LU，0 表示偏差达到或超过 1 LU。响度表下方标出绝对偏差最大的文件。",
        "version_changes": "• 禁用的 −/+ 按钮现在正确匹配浅色主题。\n• 音频与选项页使用一条连续边框。\n• Min 和 Max 每五次分析发布，并显示最近偏差最大的文件。\n• 警告和错误列表仍可导出为 CSV。\n• 显示标识仅为 1.24.6。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12406.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language].update(_updates)


# LUFScale 1.24.7 simplifies the meter, refreshes the duration estimate,
# clarifies the compact option labels and uses a 0.60 LU final QC boundary.
TRANSLATION_UPDATES_12407 = {
    "fr": {
        "loudness_meter_help_text": "Le trait rouge est la cible et la valeur bleue est la sonie réellement remesurée de la dernière sortie. Elle monte ou descend à chaque fichier. Les valeurs Min/Max et la ligne d’attribution sous le vumètre ont été retirées. Le vumètre reste inactif sans contrôle qualité.",
        "loudness_meter_tooltip": "Cible en rouge ; sonie réellement remesurée de la dernière sortie en bleu.",
        "loudness_score_tooltip": "Le score utilise les 8 dernières sorties réellement remesurées. L’écart RMS résume leur distance à la cible : 100 = résultat exact, 50 = 0,5 LU et 0 = 1 LU ou plus.",
        "quality_control_tooltip": "Remesure chaque sortie. Les corrections continuent de viser ±0,50 LU ; une alerte de sonie n’apparaît qu’au-delà de ±0,60 LU. Les MP3 dynamiques gardent jusqu’à trois essais correctifs ; WAV, AIFF et FLAC peuvent recevoir jusqu’à deux reprises depuis la source si la marge True Peak le permet. Désactiver cette option supprime la vérification, les reprises et l’activité du vumètre.",
        "option_status_overwrite": "ÉCRAS",
        "option_status_skip_compliant": "SAUT",
        "option_status_resume": "REPR",
        "option_status_quality_control": "QUAL",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• Le vumètre affiche uniquement la cible et la dernière valeur réellement remesurée ; Min/Max et le nom de fichier inférieur sont retirés.\n• La tolérance finale du contrôle de sonie est de ±0,60 LU ; les valeurs exactes restent affichées.\n• Le temps total estimé est recalculé périodiquement pendant le traitement.\n• Les aides évitent les barres de défilement inutiles, les listes d’incidents suivent le thème clair et la bordure des Réglages est continue.\n• Les six voyants utilisent des libellés locaux plus explicites.",
    },
    "en": {
        "loudness_meter_help_text": "The red line is the target and the blue value is the latest output’s genuinely remeasured loudness. It moves up or down for every file. Min/Max and the attribution line below the meter have been removed. The meter stays inactive without quality control.",
        "loudness_meter_tooltip": "Red target; latest output’s genuinely remeasured loudness in blue.",
        "loudness_score_tooltip": "The score uses the latest 8 genuinely remeasured outputs. RMS error summarizes their distance from target: 100 is exact, 50 is 0.5 LU, and 0 is 1 LU or more.",
        "quality_control_tooltip": "Remeasures every output. Corrections still target ±0.50 LU; a loudness warning appears only beyond ±0.60 LU. Dynamic MP3 keeps up to three corrective attempts; WAV, AIFF, and FLAC may receive up to two fresh-source retries when True Peak headroom allows. Disabling this option removes verification, retries, and meter activity.",
        "option_status_overwrite": "OVER",
        "option_status_skip_compliant": "SKIP",
        "option_status_resume": "RES",
        "option_status_quality_control": "QUAL",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• The meter now shows only the target and latest genuinely remeasured value; Min/Max and the lower filename are removed.\n• The final loudness-QC tolerance is ±0.60 LU while exact values remain visible.\n• Estimated total time is recalculated periodically during processing.\n• Help avoids unnecessary scrollbars, issue lists follow the light theme, and Settings uses one continuous border.\n• The six option lights use clearer localized labels.",
    },
    "de": {
        "loudness_meter_help_text": "Die rote Linie ist das Ziel, der blaue Wert die tatsächlich nachgemessene Lautheit der letzten Ausgabe. Er bewegt sich bei jeder Datei. Min/Max und die Dateizeile unter dem Messgerät wurden entfernt.",
        "loudness_meter_tooltip": "Rotes Ziel; tatsächlich nachgemessene letzte Ausgabe in Blau.",
        "loudness_score_tooltip": "Der Wert verwendet die letzten 8 nachgemessenen Ausgaben. 100 ist exakt, 50 entspricht 0,5 LU RMS-Abweichung und 0 entspricht 1 LU oder mehr.",
        "quality_control_tooltip": "Misst jede Ausgabe erneut. Korrekturen zielen weiter auf ±0,50 LU; eine Lautheitswarnung erscheint erst außerhalb von ±0,60 LU. Dynamische MP3 behalten bis zu drei Versuche; WAV, AIFF und FLAC können bei ausreichendem True-Peak-Spielraum bis zu zweimal aus der Quelle neu erstellt werden. Abschalten entfernt Prüfung, Wiederholungen und Messgerätaktivität.",
        "option_status_overwrite": "ÜBR",
        "option_status_skip_compliant": "ÜSP",
        "option_status_resume": "FORT",
        "option_status_quality_control": "QUAL",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• Das Messgerät zeigt nur Ziel und letzten nachgemessenen Wert; Min/Max und Dateizeile entfallen.\n• Die abschließende Lautheitstoleranz beträgt ±0,60 LU; exakte Werte bleiben sichtbar.\n• Die geschätzte Gesamtzeit wird regelmäßig neu berechnet.\n• Hilfe, helle Problemlisten und die durchgehende Einstellungsumrandung wurden korrigiert.\n• Die sechs Leuchten tragen klarere lokale Kürzel.",
    },
    "es": {
        "loudness_meter_help_text": "La línea roja es el objetivo y el valor azul es la sonoridad realmente medida de la última salida. Sube o baja con cada archivo. Se han retirado Min/Max y la línea de archivo inferior.",
        "loudness_meter_tooltip": "Objetivo rojo; última salida realmente medida en azul.",
        "loudness_score_tooltip": "La puntuación usa las últimas 8 salidas medidas de nuevo. 100 es exacto, 50 equivale a 0,5 LU de error RMS y 0 a 1 LU o más.",
        "quality_control_tooltip": "Vuelve a medir cada salida. Las correcciones siguen buscando ±0,50 LU; la alerta de sonoridad solo aparece fuera de ±0,60 LU. Los MP3 dinámicos conservan hasta tres intentos; WAV, AIFF y FLAC pueden repetirse desde la fuente hasta dos veces si hay margen True Peak. Desactivar elimina verificación, repeticiones y actividad del medidor.",
        "option_status_overwrite": "SOB",
        "option_status_skip_compliant": "OMIT",
        "option_status_resume": "REA",
        "option_status_quality_control": "CAL",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• El medidor muestra solo el objetivo y el último valor medido; se retiran Min/Max y el nombre inferior.\n• La tolerancia final de sonoridad es ±0,60 LU y se conservan los valores exactos.\n• El tiempo total estimado se recalcula periódicamente.\n• Se corrigen la ayuda, las listas claras y el borde continuo de Ajustes.\n• Las seis luces usan etiquetas locales más claras.",
    },
    "it": {
        "loudness_meter_help_text": "La linea rossa è l’obiettivo e il valore blu è la sonorità realmente rimisurata dell’ultima uscita. Sale o scende per ogni file. Min/Max e la riga del file sotto il misuratore sono stati rimossi.",
        "loudness_meter_tooltip": "Obiettivo rosso; ultima uscita realmente rimisurata in blu.",
        "loudness_score_tooltip": "Il punteggio usa le ultime 8 uscite rimisurate. 100 è esatto, 50 equivale a 0,5 LU di errore RMS e 0 a 1 LU o più.",
        "quality_control_tooltip": "Rimisura ogni uscita. Le correzioni continuano a mirare a ±0,50 LU; l’avviso di sonorità appare solo oltre ±0,60 LU. Gli MP3 dinamici mantengono fino a tre tentativi; WAV, AIFF e FLAC possono essere rifatti dalla sorgente fino a due volte se resta margine True Peak. Disattivare elimina verifica, tentativi e attività del misuratore.",
        "option_status_overwrite": "SOV",
        "option_status_skip_compliant": "SALT",
        "option_status_resume": "RIP",
        "option_status_quality_control": "QUAL",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• Il misuratore mostra solo obiettivo e ultimo valore rimisurato; Min/Max e il nome inferiore sono rimossi.\n• La tolleranza finale è ±0,60 LU, con valori esatti sempre visibili.\n• Il tempo totale stimato viene ricalcolato periodicamente.\n• Sono corretti aiuti, elenchi chiari e bordo continuo delle Impostazioni.\n• Le sei spie usano etichette locali più chiare.",
    },
    "pt": {
        "loudness_meter_help_text": "A linha vermelha é o alvo e o valor azul é a sonoridade realmente medida da última saída. Sobe ou desce em cada ficheiro. Min/Max e a linha do ficheiro sob o medidor foram removidos.",
        "loudness_meter_tooltip": "Alvo vermelho; última saída realmente medida em azul.",
        "loudness_score_tooltip": "A pontuação usa as últimas 8 saídas novamente medidas. 100 é exato, 50 equivale a 0,5 LU de erro RMS e 0 a 1 LU ou mais.",
        "quality_control_tooltip": "Volta a medir cada saída. As correções continuam a visar ±0,50 LU; o alerta de sonoridade só aparece fora de ±0,60 LU. Os MP3 dinâmicos mantêm até três tentativas; WAV, AIFF e FLAC podem ser refeitos da origem até duas vezes se houver margem True Peak. Desativar remove verificação, tentativas e atividade do medidor.",
        "option_status_overwrite": "SUB",
        "option_status_skip_compliant": "IGN",
        "option_status_resume": "RET",
        "option_status_quality_control": "QUAL",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• O medidor mostra apenas o alvo e o último valor medido; Min/Max e o nome inferior foram removidos.\n• A tolerância final é ±0,60 LU e os valores exatos continuam visíveis.\n• O tempo total estimado é recalculado periodicamente.\n• Foram corrigidos a ajuda, as listas claras e o contorno contínuo das Definições.\n• As seis luzes usam etiquetas locais mais claras.",
    },
    "nl": {
        "loudness_meter_help_text": "De rode lijn is het doel en de blauwe waarde de werkelijk opnieuw gemeten luidheid van de laatste uitvoer. De waarde beweegt bij elk bestand. Min/Max en de bestandsregel onder de meter zijn verwijderd.",
        "loudness_meter_tooltip": "Rood doel; werkelijk opnieuw gemeten laatste uitvoer in blauw.",
        "loudness_score_tooltip": "De score gebruikt de laatste 8 opnieuw gemeten uitvoerbestanden. 100 is exact, 50 is 0,5 LU RMS-fout en 0 is 1 LU of meer.",
        "quality_control_tooltip": "Meet elke uitvoer opnieuw. Correcties blijven op ±0,50 LU mikken; een luidheidswaarschuwing verschijnt pas buiten ±0,60 LU. Dynamische MP3 behoudt maximaal drie pogingen; WAV, AIFF en FLAC kunnen bij voldoende True-Peak-ruimte maximaal tweemaal vanaf de bron worden herhaald. Uitschakelen verwijdert controle, pogingen en meteractiviteit.",
        "option_status_overwrite": "OVS",
        "option_status_skip_compliant": "SLA",
        "option_status_resume": "HER",
        "option_status_quality_control": "KWAL",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• De meter toont alleen doel en laatste opnieuw gemeten waarde; Min/Max en de onderste bestandsnaam vervallen.\n• De uiteindelijke tolerantie is ±0,60 LU; exacte waarden blijven zichtbaar.\n• De geschatte totale tijd wordt regelmatig herberekend.\n• Help, lichte probleemlijsten en de doorlopende rand van Instellingen zijn gecorrigeerd.\n• De zes lampjes gebruiken duidelijkere lokale labels.",
    },
    "pl": {
        "loudness_meter_help_text": "Czerwona linia oznacza cel, a niebieska wartość rzeczywiście zmierzoną głośność ostatniego wyniku. Zmienia się przy każdym pliku. Usunięto Min/Max i wiersz pliku pod miernikiem.",
        "loudness_meter_tooltip": "Czerwony cel; ostatni rzeczywiście zmierzony wynik na niebiesko.",
        "loudness_score_tooltip": "Wynik obejmuje 8 ostatnich ponownie zmierzonych plików. 100 oznacza dokładny cel, 50 błąd RMS 0,5 LU, a 0 błąd 1 LU lub większy.",
        "quality_control_tooltip": "Ponownie mierzy każde wyjście. Korekty nadal celują w ±0,50 LU; ostrzeżenie pojawia się dopiero poza ±0,60 LU. Dynamiczne MP3 zachowują do trzech prób; WAV, AIFF i FLAC mogą być ponowione ze źródła do dwóch razy, jeśli pozwala zapas True Peak. Wyłączenie usuwa kontrolę, próby i działanie miernika.",
        "option_status_overwrite": "NAD",
        "option_status_skip_compliant": "POM",
        "option_status_resume": "WZN",
        "option_status_quality_control": "JAK",
        "option_status_report": "CSV",
        "option_status_auto_start": "AUTO",
        "version_changes": "• Miernik pokazuje tylko cel i ostatni zmierzony wynik; usunięto Min/Max i dolną nazwę pliku.\n• Końcowa tolerancja wynosi ±0,60 LU, a dokładne wartości pozostają widoczne.\n• Szacowany czas całkowity jest okresowo przeliczany.\n• Poprawiono pomoc, jasne listy problemów i ciągłą ramkę Ustawień.\n• Sześć kontrolek ma czytelniejsze lokalne etykiety.",
    },
    "ru": {
        "loudness_meter_help_text": "Красная линия — цель, синее значение — реально измеренная громкость последнего результата. Оно меняется для каждого файла. Min/Max и строка с именем файла под индикатором удалены.",
        "loudness_meter_tooltip": "Красная цель; последний реально измеренный результат показан синим.",
        "loudness_score_tooltip": "Оценка использует 8 последних повторно измеренных выходов. 100 — точное совпадение, 50 — ошибка RMS 0,5 LU, 0 — 1 LU или больше.",
        "quality_control_tooltip": "Повторно измеряет каждый выход. Коррекция по-прежнему стремится к ±0,50 LU; предупреждение появляется только за пределами ±0,60 LU. Для динамических MP3 сохраняется до трёх попыток; WAV, AIFF и FLAC могут быть повторены из источника до двух раз при наличии запаса True Peak. Отключение убирает проверку, повторы и работу индикатора.",
        "option_status_overwrite": "ПЕР",
        "option_status_skip_compliant": "ПРО",
        "option_status_resume": "ВОЗ",
        "option_status_quality_control": "КАЧ",
        "option_status_report": "CSV",
        "option_status_auto_start": "АВТО",
        "version_changes": "• Индикатор показывает только цель и последнее измеренное значение; Min/Max и нижнее имя файла удалены.\n• Итоговый допуск составляет ±0,60 LU, точные значения остаются видимыми.\n• Расчёт общего времени периодически обновляется.\n• Исправлены справка, светлые списки проблем и непрерывная рамка настроек.\n• Шесть индикаторов получили более понятные подписи.",
    },
    "ja": {
        "loudness_meter_help_text": "赤線は目標、青値は直前の出力を実際に再測定したラウドネスです。ファイルごとに上下します。Min／Maxとメーター下のファイル表示は削除しました。",
        "loudness_meter_tooltip": "赤が目標、青が直前の出力を実際に再測定した値です。",
        "loudness_score_tooltip": "スコアは再測定した直近8件を使用します。100は一致、50はRMS偏差0.5 LU、0は1 LU以上です。",
        "quality_control_tooltip": "各出力を再測定します。補正は±0.50 LUを目指し、ラウドネス警告は±0.60 LUを超えた場合だけ表示します。動的MP3は最大3回、WAV／AIFF／FLACはTrue Peakの余裕があれば元ファイルから最大2回再試行します。無効にすると確認、再試行、メーター表示を行いません。",
        "option_status_overwrite": "上書き",
        "option_status_skip_compliant": "適合済",
        "option_status_resume": "再開",
        "option_status_quality_control": "品質",
        "option_status_report": "CSV",
        "option_status_auto_start": "自動",
        "version_changes": "• メーターは目標と直前の再測定値だけを表示し、Min／Maxと下部のファイル名を削除しました。\n• 最終許容差は±0.60 LUで、正確な値は表示されます。\n• 推定合計時間を処理中に定期的に再計算します。\n• ヘルプ、ライトテーマの問題一覧、設定枠を修正しました。\n• 6個のランプを分かりやすい表示にしました。",
    },
    "hi": {
        "loudness_meter_help_text": "लाल रेखा लक्ष्य है और नीला मान अंतिम output की वास्तव में दोबारा मापी गई loudness है। यह हर file पर ऊपर या नीचे जाता है। Min/Max और meter के नीचे की file पंक्ति हटा दी गई है।",
        "loudness_meter_tooltip": "लाल लक्ष्य; अंतिम output का वास्तविक दोबारा मापा मान नीले रंग में।",
        "loudness_score_tooltip": "Score पिछले 8 दोबारा मापे गए outputs का उपयोग करता है। 100 सटीक, 50 का अर्थ 0.5 LU RMS अंतर और 0 का अर्थ 1 LU या अधिक है।",
        "quality_control_tooltip": "हर output फिर मापता है। Corrections ±0.50 LU को लक्ष्य बनाते हैं; loudness warning केवल ±0.60 LU से बाहर आती है। Dynamic MP3 में अधिकतम तीन attempts रहते हैं; True Peak headroom मिलने पर WAV, AIFF और FLAC source से दो बार तक दोहराए जा सकते हैं। बंद करने पर verification, retries और meter activity हटते हैं।",
        "option_status_overwrite": "अधि",
        "option_status_skip_compliant": "छोड़",
        "option_status_resume": "जारी",
        "option_status_quality_control": "गुण",
        "option_status_report": "CSV",
        "option_status_auto_start": "स्वतः",
        "version_changes": "• Meter केवल लक्ष्य और अंतिम दोबारा मापा मान दिखाता है; Min/Max और नीचे का file नाम हटा दिया गया है।\n• अंतिम tolerance ±0.60 LU है और exact values दिखती रहती हैं।\n• Estimated total time processing के दौरान समय-समय पर फिर गिना जाता है।\n• Help, light-theme issue lists और Settings border ठीक किए गए हैं।\n• छह lights में अधिक स्पष्ट local labels हैं।",
    },
    "zh": {
        "loudness_meter_help_text": "红线是目标，蓝色数值是最后一个输出实际复测的响度，并会随每个文件上下移动。Min/Max 和表下方的文件行已移除。",
        "loudness_meter_tooltip": "红色为目标，蓝色为最后一个输出的实际复测值。",
        "loudness_score_tooltip": "评分使用最近8个实际复测输出。100表示完全一致，50表示RMS偏差0.5 LU，0表示偏差达到或超过1 LU。",
        "quality_control_tooltip": "重新测量每个输出。校正仍以±0.50 LU为目标；只有超出±0.60 LU才显示响度警告。动态MP3保留最多三次尝试；True Peak余量允许时，WAV、AIFF和FLAC可从源文件最多重试两次。关闭后将取消验证、重试和响度表活动。",
        "option_status_overwrite": "覆盖",
        "option_status_skip_compliant": "合规",
        "option_status_resume": "继续",
        "option_status_quality_control": "质控",
        "option_status_report": "CSV",
        "option_status_auto_start": "自动",
        "version_changes": "• 响度表只显示目标和最新复测值；已移除Min/Max和下方文件名。\n• 最终响度容差为±0.60 LU，精确数值仍会显示。\n• 处理期间会定期重新计算预计总时间。\n• 已修正帮助窗口、浅色问题列表和连续的设置边框。\n• 六个指示灯使用更清晰的本地标签。",
    },
}

for _language, _updates in TRANSLATION_UPDATES_12407.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language].update(_updates)


# LUFScale 1.24.8 localizes the CSV save browser independently from macOS,
# makes the low score actionable, and retires three selectable catalogues.
TRANSLATION_UPDATES_12408 = {
    "fr": {
        "help_overview": "• Normalisation réelle, ReplayGain ou analyse des formats MP3, FLAC, WAV, AIFF, M4A, OGG et Opus.\n• Modes Piste et Album avec conservation des écarts entre les titres.\n• Arborescence, métadonnées et pochettes conservées lorsque FFmpeg peut les recopier.\n• Originaux jamais déplacés ni modifiés.\n• Parallélisme Auto, cache d’analyse et reprise après interruption.\n• Contrôle qualité, rapport CSV, progression, CPU, vumètre de sonie et durée totale estimée.\n• Sélecteur de 9 langues, chacune avec son catalogue d’interface et son guide PDF dédiés.",
        "loudness_meter_help_text": "Le trait rouge est la cible et la valeur bleue est la sonie réellement remesurée de la dernière sortie. Elle monte ou descend à chaque fichier. Le score résume les 8 dernières sorties remesurées. Si le panneau rouge indique « Voir les alertes », mettez le traitement en pause ou attendez sa fin, puis ouvrez Alertes pour identifier les fichiers concernés. Le vumètre reste inactif sans contrôle qualité.",
        "loudness_score_check": "Voir les alertes",
        "loudness_score_tooltip": "Le score utilise les 8 dernières sorties réellement remesurées. 100 = résultat exact, 50 = écart RMS de 0,60 LU et 0 = 1,20 LU ou plus. Le panneau rouge implique qu’au moins une alerte de sonie peut être consultée avec le bouton Alertes.",
        "save_dialog_location": "Dossier",
        "save_dialog_filename": "Nom du fichier",
        "save_dialog_filetype": "Format",
        "save_dialog_save": "Enregistrer",
        "save_dialog_cancel": "Annuler",
        "version_changes": "• Le sélecteur d’enregistrement CSV utilise la langue choisie dans LUFScale, indépendamment de la langue de macOS.\n• Le score rouge est aligné sur la tolérance QC de ±0,60 LU et indique « Voir les alertes ».\n• Deutsch, Nederlands et Polski sont retirés du sélecteur ; neuf langues et neuf guides restent fournis.\n• Le vumètre conserve uniquement la cible et la dernière valeur remesurée.\n• Le moteur audio et les seuils du contrôle qualité sont inchangés.",
    },
    "en": {
        "help_overview": "• Normalization, ReplayGain or analysis of MP3, FLAC, WAV, AIFF, M4A, OGG and Opus audio.\n• Track and Album modes with preserved differences between tracks.\n• Folder tree, metadata and artwork preserved when FFmpeg can copy them.\n• Originals are never moved or modified.\n• Auto parallelism, analysis cache and resume after interruption.\n• Quality control, CSV report, progress, CPU, loudness meter and estimated total duration.\n• 9-language selector, each with its own interface catalogue and PDF guide.",
        "loudness_meter_help_text": "The red line is the target and the blue value is the latest output’s genuinely remeasured loudness. It moves up or down for every file. The score summarizes the latest 8 remeasured outputs. If the red panel says “View warnings”, pause processing or wait for it to finish, then open Warnings to identify the affected files. The meter stays inactive without quality control.",
        "loudness_score_check": "View warnings",
        "loudness_score_tooltip": "The score uses the latest 8 genuinely remeasured outputs. 100 is exact, 50 is 0.60 LU RMS error, and 0 is 1.20 LU or more. A red panel means at least one loudness warning can be reviewed with the Warnings button.",
        "save_dialog_location": "Location",
        "save_dialog_filename": "File name",
        "save_dialog_filetype": "Format",
        "save_dialog_save": "Save",
        "save_dialog_cancel": "Cancel",
        "version_changes": "• The CSV save browser follows the language selected in LUFScale, independently of the macOS language.\n• The red score is aligned with the ±0.60 LU QC tolerance and says “View warnings”.\n• Deutsch, Nederlands and Polski are removed from the selector; nine languages and nine guides remain.\n• The meter keeps only the target and latest remeasured value.\n• The audio engine and quality-control thresholds are unchanged.",
    },
    "es": {
        "loudness_meter_help_text": "La línea roja es el objetivo y el valor azul es la sonoridad realmente medida de la última salida. Sube o baja con cada archivo. La puntuación resume las últimas 8 salidas medidas. Si el panel rojo indica «Ver alertas», pause el proceso o espere a que termine y abra Alertas para identificar los archivos afectados.",
        "loudness_score_check": "Ver alertas",
        "loudness_score_tooltip": "La puntuación usa las últimas 8 salidas medidas. 100 es exacto, 50 equivale a un error RMS de 0,60 LU y 0 a 1,20 LU o más. Un panel rojo implica que se puede consultar al menos una alerta de sonoridad con el botón Alertas.",
        "save_dialog_location": "Ubicación",
        "save_dialog_filename": "Nombre del archivo",
        "save_dialog_filetype": "Formato",
        "save_dialog_save": "Guardar",
        "save_dialog_cancel": "Cancelar",
        "version_changes": "• El selector para guardar CSV usa el idioma elegido en LUFScale, independientemente del idioma de macOS.\n• La puntuación roja se alinea con la tolerancia QC de ±0,60 LU e indica «Ver alertas».\n• Deutsch, Nederlands y Polski se retiran del selector; quedan nueve idiomas y nueve guías.\n• El medidor conserva solo el objetivo y el último valor medido.\n• El motor de audio y los umbrales de control no cambian.",
    },
    "it": {
        "loudness_meter_help_text": "La linea rossa è l’obiettivo e il valore blu è la sonorità realmente rimisurata dell’ultima uscita. Sale o scende per ogni file. Il punteggio riassume le ultime 8 uscite rimisurate. Se il pannello rosso indica «Vedi avvisi», metti in pausa l’elaborazione o attendi la fine, quindi apri Avvisi per identificare i file interessati.",
        "loudness_score_check": "Vedi avvisi",
        "loudness_score_tooltip": "Il punteggio usa le ultime 8 uscite rimisurate. 100 è esatto, 50 equivale a un errore RMS di 0,60 LU e 0 a 1,20 LU o più. Un pannello rosso indica che almeno un avviso di sonorità è consultabile con il pulsante Avvisi.",
        "save_dialog_location": "Posizione",
        "save_dialog_filename": "Nome file",
        "save_dialog_filetype": "Formato",
        "save_dialog_save": "Salva",
        "save_dialog_cancel": "Annulla",
        "version_changes": "• Il selettore di salvataggio CSV usa la lingua scelta in LUFScale, indipendentemente dalla lingua di macOS.\n• Il punteggio rosso è allineato alla tolleranza QC di ±0,60 LU e indica «Vedi avvisi».\n• Deutsch, Nederlands e Polski sono rimossi dal selettore; restano nove lingue e nove guide.\n• Il misuratore conserva solo l’obiettivo e l’ultimo valore rimisurato.\n• Il motore audio e le soglie QC non cambiano.",
    },
    "pt": {
        "loudness_meter_help_text": "A linha vermelha é o alvo e o valor azul é a sonoridade realmente medida da última saída. Sobe ou desce em cada ficheiro. A pontuação resume as últimas 8 saídas medidas. Se o painel vermelho indicar «Ver alertas», pause o processamento ou aguarde o fim e abra Alertas para identificar os ficheiros afetados.",
        "loudness_score_check": "Ver alertas",
        "loudness_score_tooltip": "A pontuação usa as últimas 8 saídas medidas. 100 é exato, 50 equivale a um erro RMS de 0,60 LU e 0 a 1,20 LU ou mais. Um painel vermelho significa que pelo menos um alerta de sonoridade pode ser consultado no botão Alertas.",
        "save_dialog_location": "Localização",
        "save_dialog_filename": "Nome do ficheiro",
        "save_dialog_filetype": "Formato",
        "save_dialog_save": "Guardar",
        "save_dialog_cancel": "Cancelar",
        "version_changes": "• O seletor para guardar CSV usa o idioma escolhido no LUFScale, independentemente do idioma do macOS.\n• A pontuação vermelha segue a tolerância QC de ±0,60 LU e indica «Ver alertas».\n• Deutsch, Nederlands e Polski saem do seletor; ficam nove idiomas e nove guias.\n• O medidor conserva apenas o alvo e o último valor medido.\n• O motor de áudio e os limites QC não mudam.",
    },
    "ru": {
        "loudness_meter_help_text": "Красная линия — цель, синее значение — реально измеренная громкость последнего результата. Оно меняется для каждого файла. Оценка обобщает 8 последних повторно измеренных выходов. Если на красной панели указано «Открыть предупреждения», приостановите обработку или дождитесь её окончания, затем откройте Предупреждения и найдите затронутые файлы.",
        "loudness_score_check": "Открыть предупреждения",
        "loudness_score_tooltip": "Оценка использует 8 последних повторно измеренных выходов. 100 — точное совпадение, 50 — ошибка RMS 0,60 LU, 0 — 1,20 LU или больше. Красная панель означает, что кнопка Предупреждения содержит хотя бы одно предупреждение по громкости.",
        "save_dialog_location": "Папка",
        "save_dialog_filename": "Имя файла",
        "save_dialog_filetype": "Формат",
        "save_dialog_save": "Сохранить",
        "save_dialog_cancel": "Отмена",
        "version_changes": "• Окно сохранения CSV использует язык, выбранный в LUFScale, независимо от языка macOS.\n• Красная оценка согласована с допуском QC ±0,60 LU и предлагает открыть предупреждения.\n• Deutsch, Nederlands и Polski удалены из списка; остаются девять языков и девять руководств.\n• Индикатор сохраняет только цель и последнее измеренное значение.\n• Аудиодвижок и пороги QC не изменены.",
    },
    "ja": {
        "loudness_meter_help_text": "赤線は目標、青値は直前の出力を実際に再測定したラウドネスです。ファイルごとに上下します。スコアは直近8件の再測定結果を要約します。赤いパネルに「警告を確認」と表示されたら、処理を一時停止するか完了を待ち、［警告］を開いて対象ファイルを確認してください。",
        "loudness_score_check": "警告を確認",
        "loudness_score_tooltip": "スコアは再測定した直近8件を使用します。100は一致、50はRMS偏差0.60 LU、0は1.20 LU以上です。赤いパネルは、［警告］ボタンで確認できるラウドネス警告が少なくとも1件あることを示します。",
        "save_dialog_location": "保存先",
        "save_dialog_filename": "ファイル名",
        "save_dialog_filetype": "形式",
        "save_dialog_save": "保存",
        "save_dialog_cancel": "キャンセル",
        "version_changes": "• CSV保存画面はmacOSの言語とは独立して、LUFScaleで選んだ言語を使用します。\n• 赤いスコアをQC許容差±0.60 LUに合わせ、「警告を確認」と表示します。\n• Deutsch、Nederlands、Polskiを一覧から削除し、9言語と9冊のガイドを収録します。\n• メーターは目標と直前の再測定値だけを表示します。\n• 音声エンジンとQCしきい値は変更していません。",
    },
    "hi": {
        "loudness_meter_help_text": "लाल रेखा लक्ष्य है और नीला मान अंतिम output की वास्तव में दोबारा मापी गई loudness है। यह हर file पर ऊपर या नीचे जाता है। Score अंतिम 8 दोबारा मापे गए outputs का सार देता है। लाल panel में «चेतावनियाँ देखें» आए तो processing रोकें या पूरी होने दें, फिर प्रभावित files पहचानने के लिए चेतावनियाँ खोलें।",
        "loudness_score_check": "चेतावनियाँ देखें",
        "loudness_score_tooltip": "Score अंतिम 8 दोबारा मापे गए outputs का उपयोग करता है। 100 सटीक, 50 का अर्थ 0.60 LU RMS अंतर और 0 का अर्थ 1.20 LU या अधिक है। लाल panel का अर्थ है कि चेतावनियाँ button में कम से कम एक loudness warning उपलब्ध है।",
        "save_dialog_location": "स्थान",
        "save_dialog_filename": "फ़ाइल नाम",
        "save_dialog_filetype": "प्रारूप",
        "save_dialog_save": "सहेजें",
        "save_dialog_cancel": "रद्द करें",
        "version_changes": "• CSV save window macOS की भाषा से अलग, LUFScale में चुनी गई भाषा उपयोग करती है।\n• लाल score QC की ±0.60 LU tolerance से मेल खाता है और «चेतावनियाँ देखें» कहता है।\n• Deutsch, Nederlands और Polski सूची से हटाए गए हैं; नौ भाषाएँ और नौ guides रहते हैं।\n• Meter केवल लक्ष्य और अंतिम दोबारा मापा मान रखता है।\n• Audio engine और QC thresholds नहीं बदले हैं।",
    },
    "zh": {
        "loudness_meter_help_text": "红线是目标，蓝色数值是最后一个输出实际复测的响度，并会随每个文件上下移动。评分汇总最近8个复测输出。如果红色面板显示“查看警告”，请暂停处理或等待完成，然后打开“警告”以确定相关文件。",
        "loudness_score_check": "查看警告",
        "loudness_score_tooltip": "评分使用最近8个实际复测输出。100表示完全一致，50表示RMS偏差0.60 LU，0表示1.20 LU或更大。红色面板表示“警告”按钮中至少有一项响度警告可供查看。",
        "save_dialog_location": "位置",
        "save_dialog_filename": "文件名",
        "save_dialog_filetype": "格式",
        "save_dialog_save": "保存",
        "save_dialog_cancel": "取消",
        "version_changes": "• CSV保存窗口使用LUFScale中选择的语言，不受macOS语言影响。\n• 红色评分与±0.60 LU的QC容差一致，并显示“查看警告”。\n• Deutsch、Nederlands和Polski已从列表中移除；保留9种语言和9份指南。\n• 响度表只保留目标和最新复测值。\n• 音频引擎和QC阈值保持不变。",
    },
}

_OVERVIEW_LAST_LINES_12408 = {
    "es": "• Nueve idiomas, cada uno con su guía PDF.",
    "it": "• Nove lingue, ciascuna con la propria guida PDF.",
    "pt": "• Nove idiomas, cada um com o seu guia PDF.",
    "ru": "• Девять языков, для каждого отдельное руководство PDF.",
    "ja": "• 9言語それぞれに専用PDFガイドがあります。",
    "hi": "• नौ भाषाएँ, हर एक का अपना PDF guide।",
    "zh": "• 九种语言，每种都有独立 PDF 指南。",
}
for _language, _last_line in _OVERVIEW_LAST_LINES_12408.items():
    _overview_lines = EXTRA_TEXTS[_language]["help_overview"].splitlines()
    TRANSLATION_UPDATES_12408[_language]["help_overview"] = "\n".join(
        [*_overview_lines[:-1], _last_line]
    )

for _language, _updates in TRANSLATION_UPDATES_12408.items():
    if _language not in {"fr", "en"}:
        EXTRA_TEXTS[_language].update(_updates)
