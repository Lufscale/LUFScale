"""Preserve the original visual guide while sizing cards for complete text."""
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from guide_scope import SCOPE_COPY, MAC_DISTRIBUTIONS, BEST_ATTEMPT_COPY


def build(g, output, language, language_name, regular, bold):
    labels = g.DOC_LABELS[language]
    scope = SCOPE_COPY[language]
    names = ['translate','excerpt','doc_text','combined_doc_text','guide_paragraphs','guide_leading_lines',
             'draw_card','draw_formula_card','draw_page_header','draw_footer','draw_log_legend']
    original = {name:getattr(g,name) for name in names}
    tr = original['translate']

    def translate(lang,key,*args,**kwargs):
        text=tr(lang,key,*args,**kwargs)
        if key=='quality_control_tooltip':
            return scope['qc']+'\n\n'+g.technical_copy(lang,'retries')+'\n\n'+g.technical_copy(lang,'qc_off')
        if key=='guide_license_feature' and 'macos' in str(g.PROJECT_ROOT).lower():
            lines=text.splitlines()
            return '\n'.join([lines[0],MAC_DISTRIBUTIONS[lang],lines[-1]])
        return text

    def footer(c,*args):
        original['draw_footer'](c,language_name,c.getPageNumber(),regular)

    def capture(page_function):
        records=[]
        def card(c,x,y,w,h,title,body,*args,**kwargs):
            records.append({'title':title,'body':body,'wide':w>400,'formula':None,'leading':1.28})
        def formula(c,x,y,w,h,title,formula,body,*args,**kwargs):
            records.append({'title':title,'body':body,'wide':False,'formula':formula})
        g.draw_card=card;g.draw_formula_card=formula
        g.draw_page_header=lambda *a,**k:735
        g.draw_footer=lambda *a,**k:None
        g.draw_log_legend=lambda *a,**k:None
        dummy=canvas.Canvas(BytesIO(),pagesize=g.A4)
        page_function(dummy,language,language_name,labels,regular,bold)
        for name in ['draw_card','draw_formula_card','draw_page_header','draw_log_legend']:
            setattr(g,name,original[name])
        g.draw_footer=footer
        return records

    c=canvas.Canvas(str(output),pagesize=g.A4,pageCompression=1,initialFontName=regular,lang=language)
    c.setTitle(f'LUFScale {g.APP_VERSION} - {language_name}')
    c.setAuthor(f'LUFScale - {g.APP_AUTHOR}')
    c.setCreator('LUFScale guide generator')

    def height(item,width):
        if item['formula'] is not None:
            p=Paragraph(g.rich(item['body']),g.style('body',regular,g.DOCUMENT_BODY_SIZE))
            _,_,fh=g.fit_paragraph(item['formula'],g.MATH_FONT,width-43,58,
                max_size=10.5,min_size=6.2,alignment=g.TA_CENTER,raw_html=True,leading_factor=1.95)
            return 63+fh+p.wrap(width-34,2000)[1]
        p,_,th=g.fit_paragraph(item['title'],bold,width-33,24,max_size=9.2,min_size=6.4)
        p=Paragraph(g.rich(item['body']),g.style('body',regular,g.DOCUMENT_BODY_SIZE,leading=g.DOCUMENT_BODY_SIZE*item.get('leading',1.28)))
        return max(56,26+th+p.wrap(width-33,3000)[1])

    top=None

    def finish():
        nonlocal top
        if top is not None:
            footer(c);c.showPage();top=None

    def section(title,subtitle,need):
        nonlocal top
        if top is None or top-need-(62 if subtitle else 38)<58:
            finish()
            top=original['draw_page_header'](c,title,subtitle,regular,bold)-4
        else:
            top-=14
            th=g.draw_paragraph(c,title,52,top,g.PAGE_WIDTH-104,35,bold,
                max_size=13,min_size=10,color=g.BLUE_DARK)
            top-=th+5
            if subtitle:
                sh=g.draw_paragraph(c,subtitle,52,top,g.PAGE_WIDTH-104,30,regular,
                    max_size=8.4,min_size=6.3,color=g.MUTED)
                top-=sh+8

    def pages(title,subtitle,records,workflow=False,legend=False,continuation=False,balance=False,gap=10):
        nonlocal top
        # Long prose benefits from the existing full-width card style.
        # Avoid tall two-column rows where a short neighbour leaves a large void.
        records=[dict(item) for item in records]
        half=(g.PAGE_WIDTH-116)/2
        for item in records:
            if item['formula'] is None and not item['wide'] and height(item,half)>185:
                item['wide']=True
        rows=[]
        i=0
        while i<len(records):
            row=[records[i]];i+=1
            if not row[0]['wide'] and i<len(records) and not records[i]['wide']:
                row.append(records[i]);i+=1
            width=g.PAGE_WIDTH-104 if len(row)==1 else (g.PAGE_WIDTH-116)/2
            rows.append((row,width,max(height(item,width) for item in row)))
        if not continuation:
            section(title,subtitle,rows[0][2]+(82 if workflow else 0))
        if workflow:
            g.draw_workflow(c,top,language,regular,bold);top-=82
        forced_breaks=set()
        if balance:
            dummy=canvas.Canvas(BytesIO(),pagesize=g.A4)
            full_top=original['draw_page_header'](dummy,title,subtitle,regular,bold)-4
            simulated=top
            for idx,(_,_,rh) in enumerate(rows):
                if simulated-rh<58:
                    forced_breaks.add(idx);simulated=full_top
                simulated-=rh+10
            if forced_breaks:
                boundary=max(forced_breaks)
                last_used=sum(row[2]+10 for row in rows[boundary:])
                previous_start=top if len(forced_breaks)==1 else full_top
                previous_boundary=max([b for b in forced_breaks if b<boundary],default=0)
                previous_used=full_top-previous_start+sum(row[2]+10 for row in rows[previous_boundary:boundary])
                while last_used<400 and boundary>previous_boundary+1:
                    transfer=rows[boundary-1][2]+10
                    if previous_used-transfer<400:break
                    forced_breaks.remove(boundary);boundary-=1;forced_breaks.add(boundary)
                    last_used+=transfer;previous_used-=transfer
        for idx,(row,width,h) in enumerate(rows):
            if top-h<58 or idx in forced_breaks:
                finish()
                top=original['draw_page_header'](c,title,subtitle,regular,bold)-4
            if top-h<58:
                raise ValueError('Full card exceeds page: '+row[0]['title'])
            for col,item in enumerate(row):
                x=52+col*(width+12)
                if item['formula'] is None:
                    original['draw_card'](c,x,top-h,width,h,item['title'],item['body'],regular,bold,body_leading_factor=item.get('leading',1.28))
                else:
                    original['draw_formula_card'](c,x,top-h,width,h,item['title'],item['formula'],item['body'],regular,bold)
            top-=h+gap
        if legend:
            if top-120<58:
                finish()
                top=original['draw_page_header'](c,title,'',regular,bold)-4
            original['draw_log_legend'](c,language,52,top-120,g.PAGE_WIDTH-104,120,regular,bold)
            top-=130

    quick_steps = {'es': ['Añada archivos o carpetas de audio.', 'Elija la carpeta de destino.', 'Elija un preajuste y una operación.', 'Inicie el tratamiento y siga el progreso.'], 'it': ['Aggiungere file o cartelle audio.', 'Scegliere la cartella di destinazione.', 'Scegliere un profilo e un’operazione.', 'Avviare e seguire l’avanzamento.'], 'pt': ['Adicione ficheiros ou pastas de áudio.', 'Escolha a pasta de destino.', 'Escolha um perfil e uma operação.', 'Inicie e acompanhe o progresso.'], 'ru': ['Добавьте аудиофайлы или папки.', 'Выберите папку назначения.', 'Выберите профиль и операцию.', 'Запустите обработку и следите за ходом.'], 'ja': ['音声ファイルやフォルダを追加します。', '保存先フォルダを選びます。', 'プリセットと操作を選びます。', '処理を開始し、進行状況を確認します。'], 'hi': ['ऑडियो फ़ाइलें या फ़ोल्डर जोड़ें।', 'गंतव्य फ़ोल्डर चुनें।', 'प्रीसेट और क्रिया चुनें।', 'प्रोसेसिंग शुरू करके प्रगति देखें।'], 'zh': ['添加音频文件或文件夹。', '选择输出文件夹。', '选择预设和操作。', '开始处理并查看进度。'], 'ko': ['오디오 파일이나 폴더를 추가합니다.', '대상 폴더를 선택합니다.', '프리셋과 작업을 선택합니다.', '처리를 시작하고 진행 상황을 확인합니다.'], 'id': ['Tambahkan berkas atau folder audio.', 'Pilih folder tujuan.', 'Pilih preset dan operasi.', 'Mulai pemrosesan dan pantau kemajuannya.'], 'tr': ['Ses dosyaları veya klasörleri ekleyin.', 'Hedef klasörü seçin.', 'Ön ayarı ve işlemi seçin.', 'İşlemi başlatın ve ilerlemeyi izleyin.']}
    try:
        g.translate=translate;g.draw_footer=footer
        # Keep the original illustrated quick start, including the four numbered steps.
        # Its short captions are navigation summaries, with full explanations below.
        if language in quick_steps:
            steps=quick_steps[language]
            keys=['source_selection_tooltip','destination_path_tooltip','preset_tooltip']
            g.doc_text=lambda lang,key,*a:steps[keys.index(key)]
            g.excerpt=lambda *a:steps[3]
        g.page_quick_start(c,language,language_name,labels,regular,bold)
        # All detailed sections retain their complete translated text.
        g.excerpt=lambda text,*a:g.sanitize(text).strip()
        g.doc_text=lambda lang,key,*a:translate(lang,key)
        g.combined_doc_text=lambda lang,keys,*a,separator='\n\n':separator.join(translate(lang,key) for key in keys)
        g.guide_paragraphs=lambda lang,key,*a:translate(lang,key)
        g.guide_leading_lines=lambda lang,key,*a:translate(lang,key)

        cards=capture(g.page_audio)
        # Explain format scope once before the settings, without renaming UI controls.
        cards.insert(0,{'title':scope['title'],'body':scope['body'],'wide':True,'formula':None})
        for item in cards:
            if item['title']==translate(language,'peak'):
                item['body']+='\n\n'+scope['peak']
        pages(translate(language,'settings')+' - '+translate(language,'audio_tab')+' / '+translate(language,'options_tab'),
              translate(language,'help_title'),cards)
        pages(labels['processing'],translate(language,'guide_analysis_method'),capture(g.page_processing),workflow=True,legend=True)
        # Retain the original preset table, troubleshooting cards and reference panel.
        recommended=capture(g.page_recommended)
        section(labels['recommended'],'',160)
        g.draw_preset_table(c,language,52,top-122,g.PAGE_WIDTH-104,regular,bold)
        nh=g.draw_paragraph(c,labels['preset_note'],52,top-132,g.PAGE_WIDTH-104,32,
            regular,max_size=7.8,min_size=6.2,color=g.MUTED)
        top-=142+nh
        checks=g.USEFUL_CHECKS_COPY[language]
        cw=(g.PAGE_WIDTH-124)/3
        ch=max(height(item,cw) for item in recommended[:3])
        section(checks['heading'],'',ch)
        for index,item in enumerate(recommended[:3]):
            original['draw_card'](c,52+index*(cw+10),top-ch,cw,ch,item['title'],item['body'],regular,bold)
        top-=ch+10
        pages(labels['recommended'],'',recommended[3:],continuation=True)
        finish()
        cards=capture(g.page_technical)
        for item in cards:
            item['leading']=1.0 if item['title']==g.PLATFORM_BUILD_COPY[language]['title'] else 1.08
            if item['title']=='MP3':item['title']=scope['mp3']
            if item['title']==translate(language,'quality_control'):
                item['body']=scope['qc']+'\n\n'+g.technical_copy(language,'retries')
        pages(labels['technical'],translate(language,'source_safety'),cards,gap=6)
        finish()
        formula_cards=capture(g.page_formulas)
        formula_cards=[formula_cards[i] for i in [0,1,2,3,4,6,5,7]]
        pages(labels['formulas'],'L = LUFS, TP = dBTP, G = dB',formula_cards)
        cards=capture(g.page_compliance)
        for index,item in enumerate(cards):
            if index in {1,3,4}:item['title']='MP3 - '+item['title']
            if index==5:item['body']=BEST_ATTEMPT_COPY[language]
            if index==7:item['formula']=item['formula'].replace('retry ⇔','retry<sub>MP3</sub> ⇔')
        cards.insert(0,{'title':scope['title'],'body':scope['formulas'],'wide':True,'formula':None})
        pages(labels['technical']+' - '+translate(language,'quality_control'),g.COMPLIANCE_COPY[language]['subtitle'],cards,balance=True)
        finish()
        c.save()
    finally:
        for name,value in original.items():setattr(g,name,value)
