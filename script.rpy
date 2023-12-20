# Определение персонажей игры.
define n = Character('Нил', color="#3a7af0")
define z = Character('Звёздочка', color="#dd7be6")
define m = Character('Медуза', color="#2dbfe4")
define r = Character('Рамон', color="#c21003")
define p = Character('Портальщик', color="#5433e7")
define a = Character('Атрахасис', color="#f1a957")
define ch = Character('Принцесса Чифир', color="#f33da7")


label start: #начало новеллы

    scene bg city
    with fade

    '''
    Эта история началась совсем в непримечательном мире под названием Ксэдо,
    который представлял из себя один заполонённый многоэтажными высотками город.
    
    Жители как всегда вели свою жизнь в заботах, но это не их будут приключения,
    а маленького мальчика. Получится ли ему исполнить свои желания или новый мир окажется куда опаснее,
    чем он думал?

    А вот и настало время познакомится с главным героем. Чем же он там занимается?
    '''
    scene bg room
    with fade
    show nil at left

    n '''
    *вздыхает и осматривает свою комнату*
    {w}Эх, надоело ходить в школу. 
    {w}Приходится сидеть и слушать эти скучные предметы изо дня в день одно и тоже.

    *начинает кричать* Я требую приключений! 
    {w}Пусть хоть солнце взорвётся, хоть что-то произойдет захватывающее!

    *становится грустным* Да кого обманываю? 
    {w}Я ведь скромный и пугливый, а ещё у меня нет друзей, которые бы пришли ко мне на вырочку.

    Но и тут не повезло, всех классных друзей разобрали. 
    {w}А я как дурачок хожу один и читаю фантастические комиксы.

    *говорит одушевленно* В них всё так здорово, главный герой в центре внимания и его любят. 
    {w}Но столько опасностей, что аж до мурашек в моих кудряшках.

    *снова приуныл* Я бы вряд ли со всем этим справился.
    '''

    menu:
        'Что же хочется мне?'
        
        'Хочу приключений!':
            jump adventures
        'Меня всё устраивает':
            n 'Хорошо, что завтра выходной, дочитаю свой любимый комикс про героя Грома.
            {w}Что-то я засиделся, уже ночь на дворе, пора в кровать. *ложится спать*'

            scene bg hell
            with fade 
            show ram at right
            r 'Хе-хе-хе, скоро встретимся, дружок.'
            hide ram

            "Начни новеллу заново и прими правильное решение, чтоб узнать, что же произойдёт..."

    return

label adventures: #начало приключений 

    scene bg bang 
    with fade
    "Я услышал тебя. 
    {w}Раскрой все свои тайны, расскажи свои секреты.
    {w}Скажи, на что я уже знал ответы. 
    {w}Я заберу тебя. Но не скажу, а намекну, что впереди. "

    scene bg tree
    with fade

    show nil at left
    n '...'
    n 'Где это я?'
    hide nil

    show zvezda at right
    z 'Охаё! Ты чего? Ты находишься на поляне духов! Но как ты сюда попал?'
    hide zvezda

    show meduza at right
    m 'Ну, что ты к нему пристаёшь? Он сам не знает. 
    {w}Я, кстати, Медуза, а это моя сумашедшая сестрёнка Звёздочка. *показывает в её сторону*'
    hide meduza

    show nil at left
    n 'Единственное, что я помню, это то, что сидел у себя в комнате, а теперь нахожусь тут. 
    {w}Но это место не похоже ни на одно, где я бывал. Я же в Ксэдо?'
    hide nil

    show zvezda at right
    z 'Ты меня не слушаешь. Я же говорю, что ты в лесу духов! А что это твоё Ксэдо?'
    hide zvezda

    show nil at left
    n 'Ксэдо - это название города, в котором я родился, ходил в школу и жил. *взгрустнул*'
    hide nil

    show zvezda at right
    z 'Не слышала о таком. Что ж, тогда добро пожаловать в наш мир! *улыбнулась*'
    hide zvezda

    show meduza at right 
    m 'Да, милости просим. Как тебя хоть зовут?'
    hide meduza

    show nil at left
    n 'Точно, простите, ещё не пришёл в себя от происходящего. Я Нил.'

    show nil at left
    n 'Подождите, со мной кто-то говорил. Я слышал чей-то голос, но он не похож на ваш.'
    hide nil

    show zvezda at right
    z 'Когда я заметила тебя, лежащим под деревом без сознания, рядом никого не было. 
    {w}Мне было очень любопытно кто ты такой, поэтому я побежала за братом, чтобы похвастаться находке.'
    hide zvezda

    show meduza at right
    m 'Да, так и было. Когда уже вместе мы подошли к тебе, ты открыл глаза.'
    hide meduza

    show zvezda at right
    z 'А что тебе говорил голос?'
    hide zvezda

    show nil at left
    n 'Что-то про тайные желания... и, вроде, про какой-то процесс. Ничего не понятно.
    {w}Не знаете, кто может мне помочь попасть обратно домой?'
    hide nil
    
    show zvezda:
        xalign 0.65 yalign 0.95
    show meduza:
        xalign 0.98 yalign 0.95
    '*после недолгих раздумий вместе начинают оживленно галдеть, что через какое-то время переходит в ссору брата и сестры*'
    hide zvezda 
    hide meduza

    show nil at left
    menu:
        'Я должен что-то сделать'
        
        'Грубо разрешить спор':
            n 'Прекратите шуметь!!!' 
            hide nil
            show zvezda at right
            z 'Замолчи, когда я говорю.'
            hide zvezda

            show meduza at right
            m 'Сама замолчи, в отличие от тебя, я знаю, к кому нужно пойти.'
            hide meduza

            show zvezda at right
            z 'Да ну? Я лучше знаю, кто нам поможет в этом вопросе.'
            hide zvezda

            show meduza at right
            m 'Конечно-конечно, иди дальше собирать цветочки.'
            hide meduza

            show zvezda at right
            z 'Не указывай мне, что делать!'
            hide zvezda

            show nil at left
            n 'Может уже закончите с выяснениями семейных отношений?'
            hide nil

            show meduza at right
            m 'Прости... {w}Ты прав.'
            hide meduza

            show zvezda at right
            z 'Ладно, проехали, но потом ты у меня получишь, братик.'
            hide zvezda

            show nil at left
            n 'Так и куда мы держим путь?'
            hide nil

            show zvezda at right
            z 'Молчи, мы идём к Принцессе Чифир. Она очень мудрая, точно сможет помочь.'
            hide zvezda

            show meduza at right
            m '...'
            hide meduza

            show nil at left
            n 'Чуприк, а ты к кому хотел повести нас или тоже к принцессе?'
            hide nil

            show meduza at right
            m 'Мне всё равно. Пошлите к принцессе.'
            hide meduza

            show zvezda at right
            z 'Да не дуйся ты. Говори уж, к кому хотел предложить идти.'
            hide zvezda

            show meduza at right
            m 'К Атрахахису. Он умный и имеет шкафы, забитые разными книжками. 
            {w}Явно сможем там найти то, что ищет наш друг, Нил.'
            hide meduza

            show zvezda at right
            z 'Решать тебе, Нил.'
            hide zvezda

            show nil at left
            $ zlo = True

            menu:
                'К кому сначало пойти?'
                'К Принцессе Чифирке':
                    jump princess_chifir1

                'К Атрахахису':
                    jump atrahacic1


        'Мирно уладить конфликт':
            n 'Ребята не ссорьтесь, я выслушаю любые идеи.' 
            hide nil
            show zvezda at right
            z 'Хорошо, но я первая расскажу.'
            hide zvezda

            show meduza at right
            m 'Мне всё равно, валяй.'
            hide meduza

            show zvezda at right
            z '*хлопает радостная в ладоши*
            Наверное, братик ты уже догадался и возможно сам хотел это предложить'
            hide zvezda

            show nil at left
            n 'Ну не томи же, говори уже, кто это такой?'
            hide nil

            show zvezda at right
            z 'Это Принцесса Чифирка!'
            hide zvezda

            show meduza at right
            m 'Я вообще-то хотел предложить Атрахасиса, он умный и имеет шкафы, забитые разными книжками. 
            {w}Явно сможем там найти то, что ищет наш друг, Нил. '
            hide meduza

            show zvezda at right
            z 'А Принцесса очень мудрая, точно поможет. '
            hide zvezda

            show meduza at right
            m 'Решать тебе, Нил, а мы составим тебе компанию, чтоб не страшно было блуждать.'
            hide meduza

            show nil at left
            n 'Тут нужно подумать.'
            $ dobro = True

            menu:
                'К кому сначало пойти?'
                'К Принцессе Чифирке':
                    jump princess_chifir1

                'К Атрахасису':
                    jump atrahacic1
    return

label atrahacic1: #ушли к учёному
    #помочь найти книгу
    show meduza at right
    m 'Он недалеко от поляны духов живёт.'
    hide meduza

    show zvezda at right
    z 'Даже отсюда виден вход в его библиотеку.'
    hide zvezda

    show meduza at right
    m 'Атрахасис домосед, постоянно с книжками в объятиях.'
    hide meduza

    show zvezda at right
    z 'Есть такое, но он тебе понравится.'
    hide zvezda

    show meduza at right
    m 'Да, у него полно разных увлекательных историй. И мы к тому же рядом с тобой.'
    hide meduza

    show nil at left
    n 'Спасибо вам ребята!'
    hide nil

    show zvezda at right
    z 'Пошлите уже! *потянула Нила и брата за лапы*'

    scene bg corridor
    with fade

    z '*подтолкнула Медузу вперед* Сам его и зови.'
    hide zvezda

    show meduza at right
    m 'А почему не ты? Боишься, что накажет за разрисованную книгу?'
    hide meduza

    show zvezda at right
    z 'Не боюсь я! Просто далеко мне до твоего статуса "любимчика".'
    hide zvezda

    show meduza at right
    m 'Ха-ха-ха, завидуешь?'
    hide meduza

    show zvezda at right
    z 'Я сейчас тебя прибью, за такие шуточки!'
    hide zvezda

    show meduza at right
    m 'Ладно-ладно. АТРАХАСИС, ТЫ ДОМА?'
    hide meduza

    show nil at left
    n 'А он мог куда-то уйти? Вы же сказали, что он домосед.'
    hide nil

    show zvezda at right
    z 'Иногда бывает находит на него. Уходит гулять так, что и не найдёшь, пока сам не появится.'
    hide zvezda

    show meduza at right
    m 'АТРАХАСИС!'
    hide meduza

    show zvezda at right
    z 'АТРАХА-А-А-А-СИ-И-И-И-С!!!'
    hide zvezda

    'Проходите в библиотеку.'

    show meduza at right
    m 'Ха-ха-ха, действительно, сложно не услышать такую сирену.'
    hide meduza

    show zvezda at right
    z 'Ты рано или поздно дошутишься, братик.'
    hide zvezda

    show nil at left
    n 'Не ссорьтесь, наш уже ждет Атрахасис.'
    hide nil

    'Что вы там всё стоите?'

    show meduza at right
    m 'Идём-идём.'
    hide meduza

    scene bg library
    with fade

    show zvezda at right
    z 'Атрахасис, мы к тебе по делу пришли.'
    hide zvezda

    'Так-так, по какому же?'

    show nil at right
    n '*шепотом* А где он? Или он невидимый дух?'
    hide nil

    show atra at left
    a 'Хо-хо, насмешил ты старика малец. Звёздочка, Медуза, а кто это с вами?'
    hide atra

    show meduza at right
    m 'Это Нил, он не знает, как попал в наш мир и хочет вернуться домой.'
    hide meduza

    show zvezda at right
    z 'Поэтому мы пришли сюда за твоей помощью.'
    hide zvezda

    show atra at left
    a 'Так-так, надо подумать...'
    hide atra

    show nil:
        xalign 0.32 yalign 0.95
    show zvezda:
        xalign 0.65 yalign 0.95
    show meduza:
        xalign 0.98 yalign 0.95
    '*все замерли в ожидании*'
    hide nil
    hide zvezda
    hide meduza

    show atra at left
    a 'Вспомнил! Читал о таком.'
    hide atra
    
    show nil at right
    n 'Что же там рассказывалось?'
    hide nil
    
    show atra at left
    a 'С удовольствием бы поделился с вами знаниями, но помогите и вы мне кое с чем.'
    hide atra

    show zvezda at right
    z 'С чем же тебе нужна помощь Атрахасис?'
    hide zvezda

    show atra at left
    a 'Как знаете у меня самая большая коллекция книг и иногда так сложно найти нужную.'
    hide atra

    show zvezda at right
    z 'Ох, мы тут надолго останемся.'
    hide zvezda

    show meduza at right
    m 'А что за книгу мы должны отыскать?'
    hide meduza

    show atra at left
    a 'Звёздочка и Медуза знают о ней, она самая-самая моя любимая. 
    {w}Я редко когда с ней расставался, но вот напасть, уже который день никак не могу её найти.'
    hide atra

    show nil at right
    n 'Мы её разыщем, не волнуйтесь. Есть какие-то отличительные черты?'
    hide nil

    show atra at left
    a 'Так-так... Она несильно толстая и у неё на корешке золотыми буквами иероглифы написаны.'
    hide atra

    show zvezda at right
    z 'Приступаем! Живо-живо! Я хочу побыстрее с этим закончить.'
    hide zvezda

    show meduza at right
    m 'Нужно тут осмотреться и разделиться.'
    hide meduza

    menu:
        'Где может быть книга?'

        'На втором этаже':      
            jump nevern_otvet1_1

        'На столе':
            jump nevern_otvet1_1

        'В центре зала': ### правильный ответ
            show nil at right
            n 'Давайте посмотрим там?'
            hide nil

            'через час поисков'

            show zvezda at right
            z 'Мы нашли её!'
            hide zvezda

            show atra at left
            a 'Ох, счастье моё, я уже везде обыскался.'
            hide atra

            show zvezda at right
            z 'Теперь можешь нам рассказать историю, как Нил к нам попал?!'
            hide zvezda

            show atra at left
            a 'Так-так, сейчас-сейчас...Что случилось с нашем Нилом называется перемещение между схожими мирами.'
            hide atra

            show nil at right
            n 'Перемещение? Но как это могло произойти?'
            hide nil
            
            show atra at left
            a 'Так-так... *листает книгу* 
            {w}Это произошло в ходе какого-то сильного взаимодействия на одну из границ.'
            hide atra
            
            show meduza at right
            m 'А мы могли почувствовать это взаимодействие?'
            hide meduza

            show atra at left
            a 'Да, такое сложно не почувствовать, но это стряслось не с нашей стороны. 
            {w}Я бы такое сразу запечатлел в летописи.'
            hide atra

            show nil at right
            n 'Но я тоже ничего не почувствовал. *старается вспомнить* 
            {w}Только лёг спать, не уж то я даже такое событие проспал? А что случилось с другими жителями?'
            hide nil

            show atra at left
            a 'Этого в книге не сказано, поэтому вероятнее всего никто не знает.'
            hide atra

            show nil at right
            n '*расстроился* И вернуться неизвестно как?'
            hide nil

            show atra at left
            a 'Увы, это так...'
            hide atra
            
            show nil at right
            n 'Спасибо вам, Атрахасис!'
            hide nil

            show atra at left
            a 'Считай и ничем не помог, ведь у тебя появилось много новых вопросов.'
            hide atra
            
            show nil at right
            n 'Не без этого, даже ощущаю себя героем комикса.'
            hide nil

            show atra at left
            a 'Что такое комикс?'
            hide atra
            
            show nil at right
            n 'Комиксы - это книжки, в которых истории изображены в картинках. 
            {w}А герои - это главные персонажи, которыми восхищаются другие за их доблестные деяния.'
            hide nil
            
            show atra at left
            a 'Звучит интересно.'
            hide atra
            
            show nil at right
            n 'Я бы дал почитать свои комиксы, у меня их много. Но они все остались дома.'
            hide nil
            
            show zvezda at right
            z 'Не расстраивайся, мы же с тобой!'
            hide zvezda

            show meduza at right
            m 'Пошлите дальше, можем сможем узнать больше информации.'
            hide meduza

            show zvezda at right
            z 'Пошлите! Пока Атрахасис!'
            hide zvezda

            show atra at left
            a 'До новых встреч, ребятки!'
            hide atra
            $ dada = True

            scene bg tree
            menu: 
                'Продолжить приключения':
                    jump princess_chifir2

        'В левых стеллажах':
            jump nevern_otvet1_1

    return

label atrahacic2: #ушли к учёному
    #помочь найти книгу
    show meduza at right
    m 'Он недалеко от поляны духов живёт.'
    hide meduza

    show zvezda at right
    z 'Даже отсюда виден вход в его библиотеку.'
    hide zvezda

    show meduza at right
    m 'Атрахасис домосед, постоянно с книжками в объятиях.'
    hide meduza

    show zvezda at right
    z 'Есть такое, но он тебе понравится.'
    hide zvezda

    show meduza at right
    m 'Да, у него полно разных увлекательных историй. И мы к тому же рядом с тобой.'
    hide meduza

    show nil at left
    n 'Спасибо вам ребята!'
    hide nil

    show zvezda at right
    z 'Пошлите уже! *потянула Нила и брата за лапы*'

    scene bg corridor
    with fade

    z '*подтолкнула Медузу вперед* Сам его и зови.'
    hide zvezda

    show meduza at right
    m 'А почему не ты? Боишься, что накажет за разрисованную книгу?'
    hide meduza

    show zvezda at right
    z 'Не боюсь я! Просто далеко мне до твоего статуса "любимчика".'
    hide zvezda

    show meduza at right
    m 'Ха-ха-ха, завидуешь?'
    hide meduza

    show zvezda at right
    z 'Я сейчас тебя прибью, за такие шуточки!'
    hide zvezda

    show meduza at right
    m 'Ладно-ладно. АТРАХАСИС, ТЫ ДОМА?'
    hide meduza

    show nil at left
    n 'А он мог куда-то уйти? Вы же сказали, что он домосед.'
    hide nil

    show zvezda at right
    z 'Иногда бывает находит на него. Уходит гулять так, что и не найдёшь, пока сам не появится.'
    hide zvezda

    show meduza at right
    m 'АТРАХАСИС!'
    hide meduza

    show zvezda at right
    z 'АТРАХА-А-А-А-СИ-И-И-И-С!!!'
    hide zvezda

    'Проходите в библиотеку.'

    show meduza at right
    m 'Ха-ха-ха, действительно, сложно не услышать такую сирену.'
    hide meduza

    show zvezda at right
    z 'Ты рано или поздно дошутишься, братик.'
    hide zvezda

    show nil at left
    n 'Не ссорьтесь, наш уже ждет Атрахасис.'
    hide nil

    'Что вы там всё стоите?'

    show meduza at right
    m 'Идём-идём.'
    hide meduza

    scene bg library
    with fade

    show zvezda at right
    z 'Атрахасис, мы к тебе по делу пришли.'
    hide zvezda

    'Так-так, по какому же?'

    show nil at right
    n '*шепотом* А где он? Или он невидимый дух?'
    hide nil

    show atra at left
    a 'Хо-хо, насмешил ты старика малец. Звёздочка, Медуза, а кто это с вами?'
    hide atra

    show meduza at right
    m 'Это Нил, он не знает, как попал в наш мир и хочет вернуться домой.'
    hide meduza

    show zvezda at right
    z 'Поэтому мы пришли сюда за твоей помощью.'
    hide zvezda

    show atra at left
    a 'Так-так, надо подумать...'
    hide atra

    show nil:
        xalign 0.32 yalign 0.95
    show zvezda:
        xalign 0.65 yalign 0.95
    show meduza:
        xalign 0.98 yalign 0.95
    '*все замерли в ожидании*'
    hide nil
    hide zvezda
    hide meduza

    show atra at left
    a 'Вспомнил! Читал о таком.'
    hide atra
    
    show nil at right
    n 'Что же там рассказывалось?'
    hide nil
    
    show atra at left
    a 'С удовольствием бы поделился с вами знаниями, но помогите и вы мне кое с чем.'
    hide atra

    show zvezda at right
    z 'С чем же тебе нужна помощь Атрахасис?'
    hide zvezda

    show atra at left
    a 'Как знаете у меня самая большая коллекция книг и иногда так сложно найти нужную.'
    hide atra

    show zvezda at right
    z 'Ох, мы тут надолго останемся.'
    hide zvezda

    show meduza at right
    m 'А что за книгу мы должны отыскать?'
    hide meduza

    show atra at left
    a 'Звёздочка и Медуза знают о ней, она самая-самая моя любимая. 
    {w}Я редко когда с ней расставался, но вот напасть, уже который день никак не могу её найти.'
    hide atra

    show nil at right
    n 'Мы её разыщем, не волнуйтесь. Есть какие-то отличительные черты?'
    hide nil

    show atra at left
    a 'Так-так... Она несильно толстая и у неё на корешке золотыми буквами иероглифы написаны.'
    hide atra

    show zvezda at right
    z 'Приступаем! Живо-живо! Я хочу побыстрее с этим закончить.'
    hide zvezda

    show meduza at right
    m 'Нужно тут осмотреться и разделиться.'
    hide meduza

    menu:
        'Где может быть книга?'

        'На втором этаже':      
            jump nevern_otvet1_2

        'На столе':
            jump nevern_otvet1_2

        'В центре зала': ### правильный ответ
            show nil at right
            n 'Давайте посмотрим там?'
            hide nil

            'через час поисков'

            show zvezda at right
            z 'Мы нашли её!'
            hide zvezda

            show atra at left
            a 'Ох, счастье моё, я уже везде обыскался.'
            hide atra

            show zvezda at right
            z 'Теперь можешь нам рассказать историю, как Нил к нам попал?!'
            hide zvezda

            show atra at left
            a 'Так-так, сейчас-сейчас...Что случилось с нашем Нилом называется перемещение между схожими мирами.'
            hide atra

            show nil at right
            n 'Перемещение? Но как это могло произойти?'
            hide nil
            
            show atra at left
            a 'Так-так... *листает книгу* 
            {w}Это произошло в ходе какого-то сильного взаимодействия на одну из границ.'
            hide atra
            
            show meduza at right
            m 'А мы могли почувствовать это взаимодействие?'
            hide meduza

            show atra at left
            a 'Да, такое сложно не почувствовать, но это стряслось не с нашей стороны. 
            {w}Я бы такое сразу запечатлел в летописи.'
            hide atra

            show nil at right
            n 'Но я тоже ничего не почувствовал. *старается вспомнить* 
            {w}Только лёг спать, не уж то я даже такое событие проспал? А что случилось с другими жителями?'
            hide nil

            show atra at left
            a 'Этого в книге не сказано, поэтому вероятнее всего никто не знает.'
            hide atra

            show nil at right
            n '*расстроился* И вернуться неизвестно как?'
            hide nil

            show atra at left
            a 'Увы, это так...'
            hide atra
            
            show nil at right
            n 'Спасибо вам, Атрахасис!'
            hide nil

            show atra at left
            a 'Считай и ничем не помог, ведь у тебя появилось много новых вопросов.'
            hide atra
            
            show nil at right
            n 'Не без этого, даже ощущаю себя героем комикса.'
            hide nil

            show atra at left
            a 'Что такое комикс?'
            hide atra
            
            show nil at right
            n 'Комиксы - это книжки, в которых истории изображены в картинках. 
            {w}А герои - это главные персонажи, которыми восхищаются другие за их доблестные деяния.'
            hide nil
            
            show atra at left
            a 'Звучит интересно.'
            hide atra
            
            show nil at right
            n 'Я бы дал почитать свои комиксы, у меня их много. Но они все остались дома.'
            hide nil
            
            show zvezda at right
            z 'Не расстраивайся, мы же с тобой!'
            hide zvezda

            show meduza at right
            m 'Пошлите дальше, можем сможем узнать больше информации.'
            hide meduza

            show zvezda at right
            z 'Пошлите! Пока Атрахасис!'
            hide zvezda

            show atra at left
            a 'До новых встреч, ребятки!'
            hide atra
            $ dada = True

            scene bg garden
            menu: 
                'Продолжить приключения':
                    jump came_to_villain
                'Неизвестный путь' if da and dada:
                    jump portal

        'В левых стеллажах':
            jump nevern_otvet1_2

    return

label nevern_otvet1_1: #Неверный ответ
    show nil at right
    n 'Давайте посмотрим там?'
    hide nil

    'через час поисков'

    show zvezda at right
    z 'Её тут нет.'
    hide zvezda

    show atra at left
    a 'Не смогли мне помочь, а ведь именно в ней было написано про перемещения между мирами.'
    hide atra

    show nil at right
    n 'Перемещения между мирами?'
    hide nil

    show meduza at right
    m 'Значит есть и другие миры?'
    hide meduza

    show atra at left
    a 'Да, всё верно. Но увы больше ничего нового рассказать не могу.'
    hide atra

    show nil at right
    n 'Всё равно спасибо, я даже об этом не подумал, хотя столько комиксов про героев прочитал. *воодушевился*'
    hide nil

    show atra at left
    a 'Что такое комиксы?'
    hide atra

    show zvezda at right
    z 'Меня больше интересуют "герои", кто они такие?'
    hide zvezda

    show nil at right
    n 'Комиксы - это книжки, в которых истории изображены в картинках. 
    {w}А герои - это главные персонажи, которыми восхищаются другие за их доблестные деяния.'
    hide nil

    show atra at left
    a 'Звучит интересно.'
    hide atra

    show nil at right
    n 'Я бы дал почитать свои комиксы, у меня их много. Но они все остались дома.'
    hide nil

    show zvezda at right
    z 'Не расстраивайся, мы же с тобой!'
    hide zvezda

    show meduza at right
    m 'Пошлите дальше, можем сможем узнать больше информации.'
    hide meduza

    show zvezda at right
    z 'Пошлите! Пока Атрахасис!'
    hide zvezda

    show atra at left
    a 'До новых встреч, ребятки!'
    hide atra

    scene bg corridor
    with fade
    menu: 
        'Продолжить приключения':
            jump princess_chifir2

    return

label nevern_otvet1_2: #Неверный ответ
    show nil at right
    n 'Давайте посмотрим там?'
    hide nil

    'через час поисков'

    show zvezda at right
    z 'Её тут нет.'
    hide zvezda

    show atra at left
    a 'Не смогли мне помочь, а ведь именно в ней было написано про перемещения между мирами.'
    hide atra

    show nil at right
    n 'Перемещения между мирами?'
    hide nil

    show meduza at right
    m 'Значит есть и другие миры?'
    hide meduza

    show atra at left
    a 'Да, всё верно. Но увы больше ничего нового рассказать не могу.'
    hide atra

    show nil at right
    n 'Всё равно спасибо, я даже об этом не подумал, хотя столько комиксов про героев прочитал. *воодушевился*'
    hide nil

    show atra at left
    a 'Что такое комиксы?'
    hide atra

    show zvezda at right
    z 'Меня больше интересуют "герои", кто они такие?'
    hide zvezda

    show nil at right
    n 'Комиксы - это книжки, в которых истории изображены в картинках. 
    {w}А герои - это главные персонажи, которыми восхищаются другие за их доблестные деяния.'
    hide nil

    show atra at left
    a 'Звучит интересно.'
    hide atra

    show nil at right
    n 'Я бы дал почитать свои комиксы, у меня их много. Но они все остались дома.'
    hide nil

    show zvezda at right
    z 'Не расстраивайся, мы же с тобой!'
    hide zvezda

    show meduza at right
    m 'Пошлите дальше, можем сможем узнать больше информации.'
    hide meduza

    show zvezda at right
    z 'Пошлите! Пока Атрахасис!'
    hide zvezda

    show atra at left
    a 'До новых встреч, ребятки!'
    hide atra

    scene bg corridor
    with fade
    menu: 
        'Продолжить приключения':
            jump came_to_villain

    return

label princess_chifir1: #ушли к принцессе
    #угадать название кристалла
    show zvezda at right
    z 'Принцесса Чифир обитает в противоположной стороне от поляны духов.'
    hide zvezda

    show nil at left
    n 'Она живет в замке?'
    hide nil

    show meduza at right
    m 'Нет, с чего ты так решил?'
    hide meduza
    
    scene bg tree
    with fade

    show nil at left
    n 'Вы же сами называете её принцессой, а принцессы живут в больших, роскошных замках.'
    hide nil

    show zvezda at right
    z 'Это ты в книжках начитался?'
    hide zvezda

    show nil at left
    n 'Не только. Как тогда Принцесса Чифир получила свой статус "принцессы"?'
    hide nil
    
    show meduza at right
    m 'Хм... *задумался* Если кратко, то это можно назвать традициями её семьи.'
    hide meduza

    show nil at left
    n 'А где тогда живёт Принцесса?'
    hide nil

    show zvezda at right
    z 'Ох, ты будешь сильно шокирован.'
    hide zvezda

    show meduza at right
    m 'Принцесса Чифирка живет в лесу.'
    hide meduza

    show nil at left
    n 'А почему она живёт там, разве не нашлось места получше?'
    hide nil

    show zvezda at right
    z 'Для её способностей это самое подходящее место.'
    hide zvezda

    show nil at left
    n 'У Принцессы есть способности?'
    hide nil

    show zvezda at right
    z 'Удивлён? Её способность заключается в связи с космосом.'
    hide zvezda

    show meduza at right
    m 'Её подпитывают камни, которые растут там. 
    {w}Вроде называются как-то на букву "а", не интересуюсь я этими кристалликами.'
    hide meduza

    show zvezda at right
    z 'А чем ты вообще интересуешься?'
    hide zvezda

    show meduza at right
    m 'У меня и так полно обязанностей, так что мне не до интересов ваших.'
    hide meduza
    
    show zvezda at right
    z 'Эти кристаллики обладают самой сильной энергетической силой и называются адулярами.'
    hide zvezda
    
    show meduza at right
    m 'Ой, кто тут впервые блеснул знаниями?'
    hide meduza

    scene bg garden
    with fade

    show zvezda at right
    z 'Ты сейчас получишь за остроумие.'
    hide zvezda

    show nil at right
    n 'Ребята, нам точно сюда?'
    hide nil

    show zvezda at right
    z 'А? А что такое?'
    hide zvezda

    show nil at right
    n 'Как-то неуютно, как будто кто-то подглядывает.'
    hide nil

    show meduza at right
    m '*оглядывается по сторонам* Никого не вижу. Может показалось?'
    hide meduza

    show zvezda at right
    z 'Нил, тут никто тебе не причинит вреда.'
    hide zvezda

    show nil at right
    n 'Хорошо. *немного расслабился* 
    {w}Идём дальше или будем тут ждать?'
    hide nil

    show zvezda at right
    z 'Нельзя заставлять Принцессу ждать.'
    hide zvezda

    show nil at right
    n 'Ждать? Разве она знает, что мы должны её навестить?'
    hide nil

    show meduza at right
    m 'Это же элементарно, ей уже давно космос об этом рассказал.'
    hide meduza
    
    show chifi at left
    ch 'Похоже вы так и не дойдёте до меня, поэтому решила выйти к вам ребятки.'
    hide chifi
    
    show zvezda at right
    z 'Прости нас, я уговаривала их шевелить булками шустрее.'
    hide zvezda
    
    show meduza at right
    m 'Простите, Нилу показалось, что за ним кто-то подглядывает.'
    hide meduza
    
    show chifi at left
    ch 'Этого не может быть, ведь тут обитаю я со своими помощницами, которые были рядом со мной.'
    hide chifi

    show nil at right
    n 'Простите меня, я не хотел вам достовлять неудобства.'
    hide nil

    show chifi at left
    ch 'Брось, всё хорошо. Давно я не прохаживалась по лесу. 
    {w}Всё время около кристаллов для поддержания информационного потока, чтобы ничего важного не упустить.'
    hide chifi

    show zvezda at right
    z 'Мы пришли к тебе, чтобы узнать как Нилу попасть обратно домой.'
    hide zvezda

    show chifi at left
    ch 'Это я знаю, видела, как ты к нам попал, но чтобы больше сказать, мне нужно быть около камней.'
    hide chifi

    scene bg crystal
    with fade

    show chifi at left
    ch 'Нил, если хочешь получить ответы, то тебе сначала придётся правильно ответить на мой вопрос.'
    hide chifi

    show nil at right
    n 'Я постараюсь.'
    hide nil

    show chifi at left
    ch 'Секундочку...Что же такое спросить?'
    hide chifi

    menu:
        'Какой минерал ценился в древности дороже золота?'

        'Агат':
            jump nevern_otvet2_1
        'Жемчуг':
            jump nevern_otvet2_1
        'Бирюза':
            jump nevern_otvet2_1
        'Лунный камень': #верный ответ
            show chifi at left
            ch 'Вероятно всего, ребята успели тебе рассказать, что я подпитываюсь адулярами?!'
            hide chifi

            show zvezda at right
            z 'Было такое.'
            hide zvezda

            show chifi at left
            ch 'Так вот, у этих камней есть и другое название, которое всем известно, как Лунный камень.'
            hide chifi
            
            show nil at right
            n 'Я смог угадать?'
            hide nil

            show chifi at left
            ch 'Верно! Молодчинка, я и не сомвевалась в тебе!'
            hide chifi

            show nil at right
            n 'Теперь расскажите, что вы знаете?'
            show chifi at left
            ch 'Для тебя, Нилончик, всё что пожелаешь. Задай вопрос мысленно и камни мне ответят.'
            hide chifi

            show nil at right
            n '*закрыл глаза* Задал.'
            hide nil

            show chifi at left
            ch 'Секундочку-секундочку...Мне говорит космос... 
            {w}Вам нужно к обитателю пустыни, но там опасно, так что будьте осторожны.'
            hide chifi

            show nil at right
            n 'Чем может помочь обитатель пустыни?'
            hide nil

            show chifi at left
            ch 'Он тот, кто точно тебе всё расскажет.'
            hide chifi

            show nil at right
            n 'А что там опасного?'
            hide nil

            show chifi at left
            ch 'Ваши дорожки могут разойтись в том походе.'
            hide chifi

            show nil at right
            n 'Как так?'
            hide nil

            show chifi at left
            ch 'Этого я не могу сказать. 
            {w}Даже если узнаешь это, ты не сможешь что-либо с этим сделать.'
            hide chifi

            show nil at right
            n 'Всё так запутанно. Я узнал, что есть другие миры, а теперь мне нужно в пустыню.
            {w}И от этого ничего не проясняется.'
            hide nil

            show chifi at left
            ch 'Прости меня, но это для твоего же блага.'
            hide chifi

            show nil at right
            n 'Медуза, Звёздочка, продолжим приключения?'
            hide nil

            show zvezda at right
            z 'Куда ты, туда и мы.'
            hide zvezda

            show nil at right
            n 'Спасибо вам, Принцесса Чифир, за новую подсказку и вам, ребята, тоже спасибо, что рядом со мной!'
            hide nil
            $ da = True

            scene bg tree
            menu: 
                'Продолжить приключения':
                    jump atrahacic2
                    
    return

label princess_chifir2: #ушли к принцессе
    #угадать название кристалла
    show zvezda at right
    z 'Принцесса Чифир обитает в противоположной стороне от поляны духов.'
    hide zvezda

    show nil at left
    n 'Она живет в замке?'
    hide nil

    show meduza at right
    m 'Нет, с чего ты так решил?'
    hide meduza
    
    scene bg tree
    with fade

    show nil at left
    n 'Вы же сами называете её принцессой, а принцессы живут в больших, роскошных замках.'
    hide nil

    show zvezda at right
    z 'Это ты в книжках начитался?'
    hide zvezda

    show nil at left
    n 'Не только. Как тогда Принцесса Чифир получила свой статус "принцессы"?'
    hide nil
    
    show meduza at right
    m 'Хм... *задумался* Если кратко, то это можно назвать традициями её семьи.'
    hide meduza

    show nil at left
    n 'А где тогда живёт Принцесса?'
    hide nil

    show zvezda at right
    z 'Ох, ты будешь сильно шокирован.'
    hide zvezda

    show nil at left
    n 'Только не говорите, что она как Атрахасис в горе?'
    hide nil

    show meduza at right
    m 'Ха-ха-ха, конечно нет, у нас и другие места есть.'
    hide meduza

    show zvezda at right
    z 'Принцесса Чифирка живет в лесу.'
    hide zvezda

    show nil at left
    n 'А почему она живёт там, разве не нашлось места получше?'
    hide nil

    show zvezda at right
    z 'Для её способностей это самое подходящее место.'
    hide zvezda

    show nil at left
    n 'У Принцессы есть способности?'
    hide nil

    show zvezda at right
    z 'Удивлён? Её способность заключается в связи с космосом.'
    hide zvezda

    show meduza at right
    m 'Её подпитывают камни, которые растут там. 
    {w}Вроде называются как-то на букву "а", не интересуюсь я этими кристалликами.'
    hide meduza

    show zvezda at right
    z 'А чем ты вообще интересуешься?'
    hide zvezda

    show meduza at right
    m 'У меня и так полно обязанностей, так что мне не до интересов ваших.'
    hide meduza
    
    show zvezda at right
    z 'Эти кристаллики обладают самой сильной энергетической силой и называются адулярами.'
    hide zvezda
    
    show meduza at right
    m 'Ой, кто тут впервые блеснул знаниями?'
    hide meduza

    scene bg garden
    with fade

    show zvezda at right
    z 'Ты сейчас получишь за остроумие.'
    hide zvezda

    show nil at right
    n 'Ребята, нам точно сюда?'
    hide nil

    show zvezda at right
    z 'А? А что такое?'
    hide zvezda

    show nil at right
    n 'Как-то неуютно, как будто кто-то подглядывает.'
    hide nil

    show meduza at right
    m '*оглядывается по сторонам* Никого не вижу. Может показалось?'
    hide meduza

    show zvezda at right
    z 'Нил, тут никто тебе не причинит вреда.'
    hide zvezda

    show nil at right
    n 'Хорошо. *немного расслабился* 
    {w}Идём дальше или будем тут ждать?'
    hide nil

    show zvezda at right
    z 'Нельзя заставлять Принцессу ждать.'
    hide zvezda

    show nil at right
    n 'Ждать? Разве она знает, что мы должны её навестить?'
    hide nil

    show meduza at right
    m 'Это же элементарно, ей уже давно космос об этом рассказал.'
    hide meduza
    
    show chifi at left
    ch 'Похоже вы так и не дойдёте до меня, поэтому решила выйти к вам ребятки.'
    hide chifi
    
    show zvezda at right
    z 'Прости нас, я уговаривала их шевелить булками шустрее.'
    hide zvezda
    
    show meduza at right
    m 'Простите, Нилу показалось, что за ним кто-то подглядывает.'
    hide meduza
    
    show chifi at left
    ch 'Этого не может быть, ведь тут обитаю я со своими помощницами, которые были рядом со мной.'
    hide chifi

    show nil at right
    n 'Простите меня, я не хотел вам достовлять неудобства.'
    hide nil

    show chifi at left
    ch 'Брось, всё хорошо. Давно я не прохаживалась по лесу. 
    {w}Всё время около кристаллов для поддержания информационного потока, чтобы ничего важного не упустить.'
    hide chifi

    show zvezda at right
    z 'Мы пришли к тебе, чтобы узнать как Нилу попасть обратно домой.'
    hide zvezda

    show chifi at left
    ch 'Это я знаю, видела, как ты к нам попал, но чтобы больше сказать, мне нужно быть около камней.'
    hide chifi

    scene bg crystal
    with fade

    show chifi at left
    ch 'Нил, если хочешь получить ответы, то тебе сначала придётся правильно ответить на мой вопрос.'
    hide chifi

    show nil at right
    n 'Я постараюсь.'
    hide nil

    show chifi at left
    ch 'Секундочку...Что же такое спросить?'
    hide chifi

    menu:
        'Какой минерал ценился в древности дороже золота?'

        'Агат':
            jump nevern_otvet2_2
        'Жемчуг':
            jump nevern_otvet2_2
        'Бирюза':
            jump nevern_otvet2_2
        'Лунный камень': #верный ответ
            show chifi at left
            ch 'Вероятно всего, ребята успели тебе рассказать, что я подпитываюсь адулярами?!'
            hide chifi

            show zvezda at right
            z 'Было такое.'
            hide zvezda

            show chifi at left
            ch 'Так вот, у этих камней есть и другое название, которое всем известно, как Лунный камень.'
            hide chifi
            
            show nil at right
            n 'Я смог угадать?'
            hide nil

            show chifi at left
            ch 'Верно! Молодчинка, я и не сомвевалась в тебе!'
            hide chifi

            show nil at right
            n 'Теперь расскажите, что вы знаете?'
            show chifi at left
            ch 'Для тебя, Нилончик, всё что пожелаешь. Задай вопрос мысленно и камни мне ответят.'
            hide chifi

            show nil at right
            n '*закрыл глаза* Задал.'
            hide nil

            show chifi at left
            ch 'Секундочку-секундочку...Мне говорит космос... 
            {w}Вам нужно к обитателю пустыни, но там опасно, так что будьте осторожны.'
            hide chifi

            show nil at right
            n 'Чем может помочь обитатель пустыни?'
            hide nil

            show chifi at left
            ch 'Он тот, кто точно тебе всё расскажет.'
            hide chifi

            show nil at right
            n 'А что там опасного?'
            hide nil

            show chifi at left
            ch 'Ваши дорожки могут разойтись в том походе.'
            hide chifi

            show nil at right
            n 'Как так?'
            hide nil

            show chifi at left
            ch 'Этого я не могу сказать. 
            {w}Даже если узнаешь это, ты не сможешь что-либо с этим сделать.'
            hide chifi

            show nil at right
            n 'Всё так запутанно. Я узнал, что есть другие миры, а теперь мне нужно в пустыню.
            {w}И от этого ничего не проясняется.'
            hide nil

            show chifi at left
            ch 'Прости меня, но это для твоего же блага.'
            hide chifi

            show nil at right
            n 'Медуза, Звёздочка, продолжим приключения?'
            hide nil

            show zvezda at right
            z 'Куда ты, туда и мы.'
            hide zvezda

            show nil at right
            n 'Спасибо вам, Принцесса Чифир, за новую подсказку и вам, ребята, тоже спасибо, что рядом со мной!'
            hide nil
            $ da = True

            menu: 
                'Продолжить приключения':
                    jump came_to_villain
                'Неизвестный путь' if da and dada:
                    jump portal
                    
    return

label nevern_otvet2_1:
    show chifi at left
    ch 'Вероятно всего, ребята успели тебе рассказать, что я подпитываюсь адулярами?!'
    hide chifi

    show zvezda at right
    z 'Было такое.'
    hide zvezda

    show chifi at left
    ch 'Так вот, у этих камней есть и другое название, которое всем известно, как Лунный камень.'
    hide chifi

    show nil at right
    n 'Я не смог угадать.'
    hide nil

    show chifi at left
    ch 'Верно. Но что б ты сильно не расстаивался я всё же тебе поведую один секрет.'
    hide chifi

    show nil at right
    n 'Какой секрет?'
    hide nil

    show chifi at left
    ch 'Я знаю, что Атрахасис рассказал, что есть другие миры.'
    hide chifi

    show nil at right
    n 'Да, всё так и было.'
    hide nil

    show chifi at left
    ch 'Но он не рассказал, что есть кто-то, кто умеет перемещаться между этими мирами. 
    {w}Вам нужно его найти, он всё и расскажет.'
    hide chifi

    show nil at right
    n 'А где его искать?'
    hide nil

    show chifi at left
    ch 'Вы сами к нему попадете, когда уже отчаетесь.'
    hide chifi

    show zvezda at right
    z 'Как-то это устрашающе звучит.'
    hide zvezda

    show meduza at right
    m 'Но что поделаешь, пойдёмте искать его?!'
    hide meduza

    show zvezda at right
    z 'Спасибо, за секретик.'
    hide zvezda

    show chifi at left
    ch 'Да это мелочь, что я могла сделать.'
    hide chifi

    show nil at right
    n 'Спасибо вам, Принцесса Чифир, за новую подсказку и вам, ребята, тоже спасибо, что рядом со мной!'
    hide nil

    show chifi at left
    ch 'До новых встреч! Будьте осторожны.'
    hide chifi
    
    scene bg garden
    menu: 
        'Продолжить приключения':
            jump atrahacic2
                    

    return

label nevern_otvet2_2:
    show chifi at left
    ch 'Вероятно всего, ребята успели тебе рассказать, что я подпитываюсь адулярами?!'
    hide chifi

    show zvezda at right
    z 'Было такое.'
    hide zvezda

    show chifi at left
    ch 'Так вот, у этих камней есть и другое название, которое всем известно, как Лунный камень.'
    hide chifi

    show nil at right
    n 'Я не смог угадать.'
    hide nil

    show chifi at left
    ch 'Верно. Но что б ты сильно не расстаивался я всё же тебе поведую один секрет.'
    hide chifi

    show nil at right
    n 'Какой секрет?'
    hide nil

    show chifi at left
    ch 'Я знаю, что Атрахасис рассказал, что есть другие миры.'
    hide chifi

    show nil at right
    n 'Да, всё так и было.'
    hide nil

    show chifi at left
    ch 'Но он не рассказал, что есть кто-то, кто умеет перемещаться между этими мирами. 
    {W}Вам нужно его найти, он всё и расскажет.'
    hide chifi

    show nil at right
    n 'А где его искать?'
    hide nil

    show chifi at left
    ch 'Вы сами к нему попадете, когда уже отчаетесь.'
    hide chifi

    show zvezda at right
    z 'Как-то это устрашающе звучит.'
    hide zvezda

    show meduza at right
    m 'Но что поделаешь, пойдёмте искать его?!'
    hide meduza

    show zvezda at right
    z 'Спасибо, за секретик.'
    hide zvezda

    show chifi at left
    ch 'Да это мелочь, что я могла сделать.'
    hide chifi

    show nil at right
    n 'Спасибо вам, Принцесса Чифир, за новую подсказку и вам, ребята, тоже спасибо, что рядом со мной!'
    hide nil

    show chifi at left
    ch 'До новых встреч! Будьте осторожны.'
    hide chifi
    
    scene bg garden
    menu: 
        'Продолжить приключения':
            jump came_to_villain
                    

    return

label portal:#портальщик
    # если правильно ответят у ученого и принцессе откроется доступ
    scene bg domportal
    with fade
    'Вдруг они пришли в незнакомое место'

    show nil at right
    n 'Что это за место?'
    hide nil

    show zvezda at right
    z 'Впервые вижу это место сама. А ты, бесполезный, что думаешь?'
    hide zvezda

    show meduza at right
    m 'Мы тут ни разу не были, похоже оно недавно появилось тут.'
    hide meduza

    show nil at right
    n 'Это как такое может быть?'
    hide nil

    show zvezda at right
    z 'У нас так устроен мир, какие-то места появляются с обитателями.'
    hide zvezda

    show meduza at right
    m 'Да, а какие-то исчезают бесследно.'
    hide meduza

    show portl at left
    'Мой вам поклон. Вы первые гости, которые меня навестили за столько веков.'
    hide portl
    show nil:
        xalign 0.32 yalign 0.95
    show zvezda:
        xalign 0.65 yalign 0.95
    show meduza:
        xalign 0.98 yalign 0.95
    "*ребята быстро переглянулись между собой*"
    hide nil
    hide zvezda
    hide meduza

    show zvezda at right
    z 'Охаё, новый друг!'
    hide zvezda

    show portl at left
    p 'Я - Портальщик, моё имя говорит само за себя, я то тут, то там.'
    hide portl

    show zvezda at right
    z 'О, здорово! А я - Звезда, а это Медуза и Нил.'
    hide zvezda

    show meduza at right
    m 'Привет!'
    hide meduza

    show zvezda at right
    z 'Раз говоришь, что можешь бывать в разных местах, то и Нила сможешь доставить домой?'
    hide zvezda

    show portl at left
    p 'А Нил не из этих прекрасных мест?'
    hide portl

    show nil at right
    n 'Нет, это была чья-то злая шутка.'
    hide nil

    show portl at left
    p 'Как это так произошло?'
    hide portl

    show nil at right
    n 'Мой мир называется Ксэдо, слышал о таком?'
    hide nil

    show portl at left
    p 'Я много где побывал, но о твоём мире не слыхал.
    {w}Ну ладно, не будем о плохом. Ты помнишь свой дом? Это очень важно.'
    hide portl

    show nil at right
    n 'Да, помню, я не так давно тут странствую.'
    hide nil

    show zvezda at right
    z 'Ну что, Нил, готов?'
    hide zvezda

    show meduza at right
    m 'Вот и пришло время прощаться?*виновато опустил голову*'
    hide meduza

    show nil at right
    n 'Это так неоджиданно после стольких трудностей.
    {w}И с вами мы стали уже как настоящие друзья.'
    hide nil

    show zvezda at right
    z 'Я рада нашему знакомству.'
    hide zvezda

    show meduza at right
    m 'Но принимать решение снова тебе, это твоя жизнь.'
    hide meduza

    show nil at right
    n '*задумался*'

    menu:
        'Воспользоваться порталом':
            n 'Мне очень понравилось у вас и я нашёл самых прикольных друзей, о которых и не мог мечтать.
            {w}Но дома остались родители, которые переживают как и где я нахожусь.'
            hide nil

            show portl at left
            p 'Хорошо, тогда вам нужно попрощаться, а я пока настрою портал.'
            hide portl

            show nil at right
            n 'Звёздочка, Медуза спасибо вам, без вас я бы не смог так далеко пройти.'
            hide nil

            show zvezda at right
            z 'Да ерунда, для этого и нужны друзья!'
            hide zvezda

            show meduza at right
            m 'Как не прискорбно осознавать, но она права.'
            hide meduza

            show zvezda at right
            z 'Вообще офигел? Такой момент портить.'
            hide zvezda

            show nil at right
            n 'Давайте на последок обнимемся.'
            hide nil

            show nil:
                xalign 0.32 yalign 0.95
            show zvezda:
                xalign 0.65 yalign 0.95
            show meduza:
                xalign 0.98 yalign 0.95
            '*собрались вместе*'
            hide nil
            hide zvezda
            hide meduza

            show portl at left
            p 'Всё готово в лучшем виде, можешь проходить.'
            hide portl

            show nil at right
            n 'Я вас не забуду!
            {w}*удаляясь, стал махать лапой*'
            hide nil

            show zvezda at right
            z 'Мы тоже!'
            hide zvezda

            show portl at left
            p 'Когда ступишь внутрь, думай только о месте куда хочешь попасть.'
            hide portl

            show nil at right
            n 'Я понял *шагнул через порог дома*'
            hide nil

            scene bg portal
            with fade

            show nil at left
            n 'Помню свою комнату, это был своего рода мой маленький мир,
            {w}где я мог находится сутками погруженный во вселенные комиксов.'

            scene bg room

            show nil at left
            n 'Уже вижу её. Мама, папа, я вернулся.'

            scene bg portal

            show nil at left
            n 'Так и должно быть?'

            scene bg domportal

            show nil at right
            n 'Я не понимаю, почему я снова тут? Я уже и комнату свою видел, и ощущал, 
            что уже вот-вот и буду на своей кроватке лежать.'
            hide nil

            show portl at left
            p 'Сам нахожусь в недоумении. На самом деле я раньше никого не телепортировал, 
            может он только на мне работает?'
            hide portl

            show nil at right
            n 'А заранее предупредить нельзя было? Я же так надеялся на это.'
            hide nil

            show portl at left
            p 'Приношу свои глубочайшие извинения. Я об этом не подумал.'
            hide portl

            show nil at right
            n 'Эх, теперь куда идти?'

            menu:
                'Продолжить путь':
                    jump came_to_villain
            
        'Остаться в этом мире':
            n 'Мне очень понравилось у вас и я нашёл самых прикольных друзей, о которых и не мог мечтать.
            {w}И я хочу остать тут.'
            hide nil

            show portl at left
            p 'Прекрасное решение! Не нужно терять таких друзей.'
            hide portl

            show nil at right
            n 'Спасибо.'
            hide nil

            show zvezda at right
            z 'Ты же не жалеешь об этом?'
            hide zvezda

            show nil at right
            n 'Конечно нет. Что только теперь делать?'
            hide nil

            show meduza at right
            m 'Надо идти дальше, уверен, что там сможешь узнать всё.'
            hide meduza

            menu:
                'Продолжить путь':
                    jump came_to_villain

    return

label came_to_villain: #герой находит злодея
    #путь их будет через пустыню с размышлениями, на мосту может произойти чп с медузой
    scene bg lake
    with fade

    show meduza at right
    m 'Надо подумать над собравшейся информацией.'
    hide meduza

    show nil at right
    n 'Точно! Принцесса говорила, что нужно идти в пустыню.'
    hide nil

    show zvezda at right
    z 'А? Уверен?'
    hide zvezda

    show nil at right
    n 'Что такого, Звёздочка?'
    hide nil

    show zvezda at right
    z 'Принцесса Чифирка ещё говорила, что наши пути могут разойтись. 
    {w}Разве ты такого хочешь?'
    hide zvezda

    show nil at right
    n 'Я верю в то, что можно изменить судьбу. 
    {w}А она лишь одну ветку видела и это не говорит, что именно то случится.'
    hide nil

    show zvezda at right
    z 'Хорошо, только пообщай, что останешься с нами.'
    hide zvezda

    show nil at right
    n 'Обещаю.'
    hide nil

    show zvezda at right
    z 'Тогда пошлите!'
    hide zvezda

    scene bg desert
    with fade

    show meduza at right
    m 'Вот и пески пошли.'
    hide meduza

    show zvezda at right
    z 'Видим, значит в правильном направлении шли.'
    hide zvezda

    show nil at right
    n 'А вы не знаете, кто там дальше живёт?'
    hide nil

    show zvezda at right
    z 'Дай подумать...ОЙ, ЭТО ЖЕ РАМОН!'
    hide zvezda

    show nil at right
    n 'Кто такой Рамон?'
    hide nil

    show zvezda at right
    z 'Что ты снова молчишь? Расскажи ему!'
    hide zvezda

    show meduza at right
    m 'Рамон - это демон во плоти. Делает, что ему угодно и никто ему не указ.'
    hide meduza

    show nil at right
    n 'А я ему зачем?'
    hide nil

    show zvezda at right
    z 'Кто его поймёт? Может развлекался так.'
    hide zvezda

    show nil at right
    n 'Ну и шуточки у него. *начал сердиться*'
    hide nil

    show meduza at right
    m 'Может тогда и не пойдём к нему?'
    hide meduza

    show nil at right
    n 'Нет! Я хочу объяснения получить: почему я?'
    hide nil

    show zvezda at right
    z 'Это же никак не повлияет на нашу дружбу?'
    hide zvezda

    show nil at right
    n 'Ну что ты, Звёздочка? Конечно нет.'
    hide nil

    show zvezda at right
    z 'Нам нужно в ту башню. *показывает направление*'
    hide zvezda

    show nil at right
    n 'Уф, идём!'
    hide nil

    scene bg most
    with fade

    show meduza at right
    m 'Нил, постой, я хотел кое-что тебе сказать.'
    hide meduza

    show nil at right
    n 'Слушаю, что такое?'
    hide nil

    show meduza at right
    m 'Прости меня, я не хотел...'
    hide meduza

    show zvezda at right
    z 'Что вы там застряли?'
    hide zvezda

    show nil at right
    n 'Медуза хотел за что-то извиниться. Не понимаю пока только: за что?'
    hide nil

    show meduza at right
    m '*пугливо посмотрел на сестру* Да, не важно.'
    hide meduza

    show zvezda at right
    z 'Вот, что ты опять делаешь?'
    hide zvezda

    show meduza at right
    m 'Что ты сразу агрессируешь? Ты же ДЕВОЧКА!'
    hide meduza

    show nil at right
    n 'Ну, ребята!'
    hide nil

    show zvezda at right
    z 'Это он начал, но я сейчас это закончу.'
    hide zvezda

    '*после сказанных слов сталкивает брата с моста в огненную пропасть*'

    show nil at right
    n '*стоял в ступоре, не понимая, что сейчас произошло*'
    hide nil

    menu:
        'Подать лапу помощи' if dobro:
            'Ранее ты сделал выбор в добрую сторону, поэтому сейчас можешь спасти Медузу.'

            show nil at right
            n 'Медуза, держись! Зачем ты это сделала?'
            hide nil

            show zvezda at right
            z 'Я не знаю как, так получилось. Он разозлил меня.'
            hide zvezda

            show nil at right
            n '*аккуратно вытаскивает Медузу*'
            hide nil

            show meduza at right
            m 'Спасибо, Нил.'
            hide meduza

            show nil at right
            n 'Ты тут посиди, отдохни.'
            hide nil

            show zvezda at right
            z 'Я тоже останусь с ним. *сказала со слезами на глазах*'
            hide zvezda

            show nil at right
            n '*стоял в расстеренности*'
            hide nil

            show meduza at right
            m 'Всё хорошо, иди.'
            hide meduza

            show nil at right
            n 'Хорошо, тогда когда сможете, догоняйте.'

            menu:
                'Продолжить путь':
                    jump the_end

        'Смотреть как падает' if zlo:
            'Ранее ты сделал выбор в злую сторону, поэтому не смог спасти Медузу.'

            show nil at right
            n '*так и не смог пошевелиться с места*'
            hide nil

            show zvezda at right
            z 'Я не знаю как, так получилось. Он разозлил меня. 
            {w}Нил, иди один дальше, а я пока тут посижу - подумаю.'
            hide zvezda

            show nil at right
            n 'Уверена?'
            hide nil

            show zvezda at right
            z 'Да. *ответила со слезами на глазах*'
            hide zvezda

            show nil at right
            n 'Хорошо, тогда когда сможешь, догоняй.'

            menu:
                'Продолжить путь':
                    jump the_end

    return

label the_end:

    scene bg hell
    with fade

    show nil at right
    n 'Вот ты где прятался от меня?'
    hide nil

    show ram at left
    r 'С чего ты решил, что я прятался?'
    hide ram

    show nil at right
    n 'Потому что подлецы всегда после содеянного прячутся.'
    hide nil

    show ram at left
    r 'А что я такого натворил?'
    hide ram

    show nil at right
    n 'Только не притворяйся, как будто ничего не знаешь.'
    hide nil

    show ram at left
    r 'Я может и злодей. Но ты уверен, что я злодей твой сказки?'
    hide ram

    show nil at right
    n 'Я всё знаю, мне всё рассказали.'
    hide nil

    show ram at left
    r 'Да? И кто и что тебе рассказал?'
    hide ram

    show nil at right
    n 'Всё правду!'
    hide nil

    show ram at left
    r 'А конкретнее?'
    hide ram

    show nil at right
    n 'То, что только ТЫ являешься отрицательным персонажем в этом мире.'
    hide nil

    show ram at left
    r 'Ну и что с того? Не всем же быть паиньками.'
    hide ram

    show nil at right
    n 'Мне нужны объяснения. Может даже извинения.'
    hide nil

    show ram at left
    r 'Ха-ха-ха, ну и забавный ты.'
    hide ram

    show nil at right
    n 'Почему?'
    hide nil

    show ram at left
    r 'Потому что в чужом мире, ты поверил только первым встречным.
    {w}А если б ты встретил меня первым, разве не поверил тогда мне сразу?'
    hide ram

    show nil at right
    n 'К чему ты такое говоришь мне?'
    hide nil

    show ram at left
    r 'Давай я тебе намекну, а ты уж дальше сам разбирайся.'
    hide ram

    show nil at right
    n 'Хорошо, послушаю твою байку.'
    hide nil

    show ram at left
    r 'Так вот, я не единственный, который может ходить по мирам. 
    {w}И я этим пользуюсь потому, что не по мне спокойная мирная жизнь здесь.'
    hide ram

    show nil at right
    n 'И перемещений стало мало, поэтому дошёл до похищения. Всё пока сходится.'
    hide nil

    show ram at left
    r 'Да не нужен ты мне. А вот своим новым друзьям очень даже...'
    hide ram
    
    'Конец'
    return

    