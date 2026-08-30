"""Multilingual PDF-guide editorial revision 1.24.26."""

from __future__ import annotations


TRANSLATION_UPDATES_12426: dict[str, dict[str, str]] = {
    "fr": {
        "guide_quality_priority_title": "Priorité : qualité et stabilité du niveau final",
        "guide_quality_priority_body": "LUFScale privilégie la mesure complète, la normalisation vers la cible et la remesure finale. Il ne cherche pas l’encodage le plus rapide : il vise un niveau perçu cohérent et stable entre les fichiers, et signale toute sortie hors tolérance.",
        "guide_analysis_method": "Utilise automatiquement la mesure historique complète, seule méthode validée sur le corpus de référence. Les variantes Rapide et Adaptatif ne sont plus proposées.",
        "guide_estimated_total_help": "Temps total estimé : 12 min - fin vers 14:30. « 12 min » est la durée totale estimée et « 14:30 » l’heure de fin prévue. Si la fin dépasse minuit, le nombre de jours s’ajoute automatiquement devant l’heure, par exemple « 2 j. 14:30 ».",
        "version_changes": "• Le guide affiche l’icône de l’application et présente clairement la priorité donnée à la qualité et à la stabilité du niveau final.\n• Les textes de la page Réglages sont agrandis et les espacements superflus sont retirés.\n• La page Traitement ne contient plus l’encart de version et explique précisément l’estimation de durée et d’heure de fin.\n• La page des préréglages est remontée et allégée.\n• Les douze guides utilisent la même organisation mise à jour.",
    },
    "en": {
        "guide_quality_priority_title": "Priority: quality and final-level stability",
        "guide_quality_priority_body": "LUFScale prioritizes full measurement, normalization toward the target, and final remeasurement. It does not seek the fastest encode: it aims for consistent, stable perceived loudness across files and flags any output outside tolerance.",
        "guide_analysis_method": "Automatically uses the full historical measurement, the only method validated on the reference corpus. Fast and Adaptive are no longer offered.",
        "guide_estimated_total_help": "Estimated total time: 12 min - finishing around 14:30. “12 min” is the estimated total duration and “14:30” the expected finish time. If completion passes midnight, the day count is automatically added before the time, for example “2 d. 14:30”.",
        "version_changes": "• The guide shows the application icon and clearly states its quality and final-level stability priority.\n• Settings-page text is larger and unnecessary gaps are removed.\n• The Processing page no longer has a version card and now explains duration and finish-time estimates precisely.\n• The preset page is raised and simplified.\n• All twelve guides use the same updated organization.",
    },
    "es": {
        "guide_quality_priority_title": "Prioridad: calidad y estabilidad del nivel final",
        "guide_quality_priority_body": "LUFScale prioriza la medición completa, la normalización hacia el objetivo y la medición final. No busca codificar lo más rápido posible: procura una sonoridad percibida coherente y estable entre archivos y señala toda salida fuera de tolerancia.",
        "guide_analysis_method": "Utiliza automáticamente la medición histórica completa, la única validada en el corpus de referencia. Rápido y Adaptativo ya no se ofrecen.",
        "guide_estimated_total_help": "Tiempo total estimado: 12 min - fin hacia las 14:30. «12 min» es la duración total estimada y «14:30» la hora prevista de fin. Si se supera la medianoche, se añade automáticamente el número de días antes de la hora, por ejemplo «2 d. 14:30».",
        "version_changes": "• La guía añade el icono y explica la prioridad de calidad y estabilidad.\n• Los textos son mayores y se eliminan espacios innecesarios.\n• La estimación de tiempo queda explicada y se elimina el bloque de versión.\n• Se simplifica la página de preajustes.\n• Las doce guías comparten la nueva organización.",
    },
    "it": {
        "guide_quality_priority_title": "Priorità: qualità e stabilità del livello finale",
        "guide_quality_priority_body": "LUFScale privilegia la misura completa, la normalizzazione verso l’obiettivo e la misura finale. Non cerca la codifica più veloce: punta a una sonorità percepita coerente e stabile tra i file e segnala ogni uscita fuori tolleranza.",
        "guide_analysis_method": "Usa automaticamente la misura storica completa, l’unico metodo convalidato sul corpus di riferimento. Rapido e Adattivo non sono più proposti.",
        "guide_estimated_total_help": "Tempo totale stimato: 12 min - fine verso le 14:30. «12 min» è la durata totale stimata e «14:30» l’ora prevista di fine. Se si supera la mezzanotte, il numero di giorni viene aggiunto automaticamente prima dell’ora, per esempio «2 g. 14:30».",
        "version_changes": "• La guida aggiunge l’icona e chiarisce la priorità di qualità e stabilità.\n• I testi sono più grandi e gli spazi superflui rimossi.\n• La stima del tempo è spiegata e il riquadro versione eliminato.\n• La pagina dei preset è semplificata.\n• Le dodici guide condividono la nuova struttura.",
    },
    "pt": {
        "guide_quality_priority_title": "Prioridade: qualidade e estabilidade do nível final",
        "guide_quality_priority_body": "LUFScale privilegia a medição completa, a normalização para o alvo e a medição final. Não procura a codificação mais rápida: visa uma sonoridade percebida coerente e estável entre ficheiros e assinala qualquer saída fora da tolerância.",
        "guide_analysis_method": "Utiliza automaticamente a medição histórica completa, o único método validado no corpus de referência. Rápido e Adaptativo deixaram de ser propostos.",
        "guide_estimated_total_help": "Tempo total estimado: 12 min - fim por volta das 14:30. «12 min» é a duração total estimada e «14:30» a hora prevista de fim. Se ultrapassar a meia-noite, o número de dias é acrescentado automaticamente antes da hora, por exemplo «2 d. 14:30».",
        "version_changes": "• O guia acrescenta o ícone e explica a prioridade de qualidade e estabilidade.\n• Os textos aumentam e os espaços desnecessários são removidos.\n• A estimativa de tempo é explicada e o bloco da versão removido.\n• A página de predefinições é simplificada.\n• Os doze guias partilham a nova organização.",
    },
    "ru": {
        "guide_quality_priority_title": "Приоритет: качество и стабильность итогового уровня",
        "guide_quality_priority_body": "LUFScale отдаёт приоритет полному измерению, нормализации к цели и итоговой проверке. Цель не в самой быстрой кодировке, а в согласованной и стабильной воспринимаемой громкости файлов; выход за допуск отмечается предупреждением.",
        "guide_analysis_method": "Автоматически используется полный исторический эталонный замер - единственный метод, проверенный на эталонном наборе. Быстрый и адаптивный варианты больше не предлагаются.",
        "guide_estimated_total_help": "Общее расчётное время: 12 мин - завершение около 14:30. «12 мин» - расчётная общая длительность, а «14:30» - ожидаемое время окончания. После полуночи перед временем автоматически добавляется число дней, например «2 д. 14:30».",
        "version_changes": "• В руководство добавлены значок и пояснение приоритета качества и стабильности.\n• Текст увеличен, лишние интервалы удалены.\n• Оценка времени разъяснена, блок версии удалён.\n• Страница наборов упрощена.\n• Все двенадцать руководств используют новую структуру.",
    },
    "ja": {
        "guide_quality_priority_title": "優先事項：品質と最終音量の安定性",
        "guide_quality_priority_body": "LUFScaleは全体測定、目標へのノーマライズ、出力の再測定を優先します。最速のエンコードではなく、ファイル間で一貫し安定した知覚音量を目指し、許容範囲外の出力を警告します。",
        "guide_analysis_method": "基準コーパスで検証済みの完全な履歴方式を自動的に使用します。高速方式と適応方式は選択肢から削除されました。",
        "guide_estimated_total_help": "推定合計時間：12分 - 14:30頃に完了。「12分」は推定総時間、「14:30」は予定終了時刻です。日付をまたぐ場合は、時刻の前に日数が自動表示されます（例：『2日。14:30』）。",
        "version_changes": "• アイコンと品質・安定性の優先説明を追加しました。\n• 文字を大きくし、不要な空きを削除しました。\n• 時間予測を説明し、バージョン枠を削除しました。\n• プリセットページを簡潔にしました。\n• 12言語で同じ新構成を使用します。",
    },
    "hi": {
        "guide_quality_priority_title": "प्राथमिकता: गुणवत्ता और अंतिम स्तर की स्थिरता",
        "guide_quality_priority_body": "LUFScale पूर्ण माप, लक्ष्य तक normalisation और अंतिम पुनर्माप को प्राथमिकता देता है। इसका लक्ष्य सबसे तेज encoding नहीं, बल्कि files के बीच एक समान व स्थिर perceived loudness है; tolerance से बाहर output पर warning दी जाती है।",
        "guide_analysis_method": "Reference corpus पर सत्यापित पूर्ण historical measurement अपने-आप उपयोग होता है। Fast और Adaptive विकल्प अब उपलब्ध नहीं हैं।",
        "guide_estimated_total_help": "अनुमानित कुल समय: 12 min - लगभग 14:30 पर समाप्ति। ‘12 min’ अनुमानित कुल अवधि और ‘14:30’ अपेक्षित समाप्ति समय है। आधी रात पार होने पर समय से पहले दिनों की संख्या अपने-आप जुड़ती है, जैसे ‘2 दिन। 14:30’।",
        "version_changes": "• Guide में icon और quality/stability priority जोड़ी गई है।\n• Text बड़ा और अतिरिक्त gaps हटाए गए हैं।\n• Time estimate समझाया और version card हटाया गया है।\n• Preset page सरल की गई है।\n• सभी 12 guides नई समान संरचना उपयोग करती हैं।",
    },
    "zh": {
        "guide_quality_priority_title": "优先目标：质量与最终响度稳定性",
        "guide_quality_priority_body": "LUFScale优先进行完整测量、向目标标准化并最终复测。目标不是最快编码，而是让文件之间的感知响度一致稳定，并对超出容差的输出给出警告。",
        "guide_analysis_method": "自动使用完整的历史参考测量，这是唯一经过参考语料验证的方法。快速和自适应方式不再提供。",
        "guide_estimated_total_help": "预计总时间：12分钟 - 约14:30完成。“12分钟”是预计总时长，“14:30”是预计结束时刻。跨过午夜时，会自动在时刻前加入天数，例如“2天。14:30”。",
        "version_changes": "• 指南增加应用图标以及质量与稳定性说明。\n• 放大文字并移除多余空白。\n• 解释时间估算并删除版本卡片。\n• 简化预设页面。\n• 十二种语言采用相同的新结构。",
    },
    "ko": {
        "guide_quality_priority_title": "우선순위: 품질과 최종 음량의 안정성",
        "guide_quality_priority_body": "LUFScale는 전체 측정, 목표 정규화, 최종 재측정을 우선합니다. 가장 빠른 인코딩보다 파일 간 일관되고 안정적인 체감 음량을 목표로 하며 허용 범위를 벗어난 출력은 경고합니다.",
        "guide_analysis_method": "기준 자료에서 검증된 전체 길이 분석 방식을 자동으로 사용합니다. 빠른 분석과 적응형 분석은 제공하지 않습니다.",
        "guide_estimated_total_help": "예상 총 시간: 12분 - 약 14:30에 완료됩니다. ‘12분’은 예상 총 소요 시간이고 ‘14:30’은 예상 종료 시각입니다. 자정을 넘으면 시각 앞에 날짜 수가 자동으로 추가됩니다(예: ‘2일. 14:30’).",
        "version_changes": "• 앱 아이콘과 품질·안정성 우선 설명을 추가했습니다.\n• 글자를 키우고 불필요한 간격을 없앴습니다.\n• 시간 예측을 설명하고 버전 카드를 삭제했습니다.\n• 프리셋 페이지를 간결하게 했습니다.\n• 12개 언어 안내서가 같은 새 구성을 사용합니다.",
    },
    "id": {
        "guide_quality_priority_title": "Prioritas: kualitas dan kestabilan tingkat akhir",
        "guide_quality_priority_body": "LUFScale mengutamakan pengukuran penuh, normalisasi menuju target, dan pengukuran ulang akhir. Tujuannya bukan pengodean tercepat, melainkan kenyaringan yang konsisten dan stabil antarberkas; keluaran di luar toleransi diberi peringatan.",
        "guide_analysis_method": "Secara otomatis memakai pengukuran historis penuh, satu-satunya metode yang divalidasi pada korpus acuan. Metode Cepat dan Adaptif tidak ditawarkan.",
        "guide_estimated_total_help": "Perkiraan waktu total: 12 mnt - selesai sekitar 14:30. ‘12 mnt’ adalah perkiraan durasi total dan ‘14:30’ waktu selesai. Jika melewati tengah malam, jumlah hari otomatis ditambahkan sebelum waktu, misalnya ‘2 h. 14:30’.",
        "version_changes": "• Panduan menambahkan ikon serta penjelasan prioritas kualitas dan kestabilan.\n• Teks diperbesar dan jarak berlebih dihapus.\n• Perkiraan waktu dijelaskan dan kartu versi dihapus.\n• Halaman prasetel disederhanakan.\n• Dua belas panduan memakai susunan baru yang sama.",
    },
    "tr": {
        "guide_quality_priority_title": "Öncelik: kalite ve son düzey kararlılığı",
        "guide_quality_priority_body": "LUFScale tam ölçüme, hedefe normalleştirmeye ve son yeniden ölçüme öncelik verir. Amaç en hızlı kodlama değil, dosyalar arasında tutarlı ve kararlı algılanan ses yüksekliğidir; tolerans dışındaki çıkışlar uyarıyla belirtilir.",
        "guide_analysis_method": "Referans derlem üzerinde doğrulanan tek yöntem olan tam tarihsel ölçümü otomatik olarak kullanır. Hızlı ve Uyarlanabilir yöntemler sunulmaz.",
        "guide_estimated_total_help": "Tahmini toplam süre: 12 dk - yaklaşık 14:30’da biter. ‘12 dk’ tahmini toplam süre, ‘14:30’ beklenen bitiş saatidir. Gece yarısı aşılırsa gün sayısı saatin önüne otomatik eklenir; örneğin ‘2 g. 14:30’.",
        "version_changes": "• Kılavuza simge ve kalite/kararlılık önceliği açıklaması eklendi.\n• Metin büyütüldü ve gereksiz boşluklar kaldırıldı.\n• Süre tahmini açıklandı ve sürüm kartı kaldırıldı.\n• Ön ayar sayfası sadeleştirildi.\n• On iki kılavuz aynı yeni düzeni kullanır.",
    },
}


__all__ = ["TRANSLATION_UPDATES_12426"]
