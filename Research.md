# Araşdırma Week01-Day05 [9 Iyul 2021]

### Suallar
1. justify-content və align-items xüsusiyyətləri arasındakı fərqləri izah edin
2. align-items və align-content arasındakı fərqləri izah edin
3. box-sizing: border-box xüsusiyyəti hansı hallarda istifadə olunur?
4. inline styling hansı hallarda istifadə oluna bilər
5. css-də !important və inherit ifadələrinin mənası nədir?


### Cavablar
1. justify-content Flex xüsusiyyətinə malik olan konteynerin horizontal istiqamətdə necə yerləşməsini təyin edir. align-items isə əksinə vertical istiqamətdə necə yerləşməsini təyin edir.
2. align-items  Flex konteynerin içindəkilərə standart yerləşmə müəyyən eləyir.
align-content xüsusiyyəti flex-wrap təsir göstərir və onu dəyişdirir.
3. box-sizing: border box xüsusiyyəti etsək, padding və border xüsusiyyəti en və hündürlüyə daxil olacaq və nəticədə divlərin ölçüləri eyni olacaq.
4. inline styling HTML elementlərinin içindəki still atributundan istifadə edir. Bu unikal xüsusiyyətlər yaratmaq üçün faydalıdır. 
5. !important xüsusiyyətini etsək, əvvəlki bütün stilə aid olan elementləri ləğv edir.
inherit bir elementin xüsusiyyətinin onun alt elementlərinə tətbiqinə deyilir.




# Araşdırma Week02-Day05 [16 Iyul 2021]

### Suallar
1. width:100% və width:100vw arasındakı fərqlər nədir və nə vaxt istifadə olunması məsləhətdir sizcə?
2. cm, em, in, mm, pc, pt, and px bu css ölçüləndirmə vahidlərin açıqlamalarını yazın
3. justify-content:space-around xüsusiyyəti ara məsafələri hansı formulaya görə tənzimləyir?
4. css pseudo-class və pseudo-element nədir? Nümunlərlər izah edin
5. meta tag nədir?
6. utf8 nə deməkdir?

### Cavablar
1. 
2. cm-centimeters; em-font size of element; in-inches; mm-millimeters; pc-picas; pt-points; px-pixels
3. 
4. pseudo-class bir elementi fərqli siniflərə bölür. Misal olaraq, link elementinin siniflərə ayrılmasını göstərmək olar. Pseudo-element isə bir elementi alt hissələrə bölür.
Misal olaraq, bir paraqrafın ilk hərfi və yaxudda ilk sətiri kimi.
5. meta tag web səhifələrin məlumat tagidir. Səhifənin məzmunu haqqında ilkin məlumat vermək üçün istifadə edilən meta tagları HTML kodlarında head taglar arasındadır.
6. utf8("Unicode Transformation Format") unicode üçün bir kodlaşdırma sistemidir.



# Araşdırma Week05-Day05 [13 Avqust 2021]

### Suallar

1. Python module və package nədir? Necə istifadə olunur?
2. Module və package arasındakı fərqlər nələrdir?
3. Web Server nədir?
4. WSGI nədir?
5. Web Server və WSGI arasındakı fərqlər nələrdir?
6. HTTP Request nədir?
7. GET,POST request nə deməkdir?
8. Flask framework necə işləyir?
9. URL nədir? Detalları nədən ibarətdir?
10. Virtual environment nədir? Nə üçün istifadə olunur?

### Cavablar

1. Python module içərisində funksiyalar və dəyişənlərdən ibarəti bir python faylıdır. Python package bir neçə modulun birləşməsi ilə yaranır.
2. Package modulların birləşməsidir, modul isə tək bir python faylıdır.
3. Web server komputer ve internet arasında əlaqə quran proqram təminatıdır. Web server informasiyanin saxlanılmasını, təşkilini ve göndərilməsini təmin edir.
4. WSGI (Web Server Gateway Interface) bir interface dir və əsasən python üçün istifadə olunur. Burada əsas məqsəd yazdığımız kodu web serverin başa düşəcəyi şəklə çevirir və nəticədə frameworklər web serverlerden asılı olmadan yarana bilir.
5. Web serverlərdə pythonla yazılmış kodu işlətmək olmur. WSGI isə təkcə python üçün lazımdır və kodları web serverlərin başa düşəcəyi şəklə çevirir.
6. HTTP request istifadəçi tərəfindən yaradılır və host olaraq serverdə yerləşdirilir. Əsas məqsədi həmin serverdəki resurslara daxil olmaqdır.
7. Get request - serverdən datanı tələb etməkdir
   Post request - işlənmiş dataların serverə yerləşdirilməsidir
8. 
9. URL faylın və ya resursun webdə yerləşdiyi ünvanı göstərir və iki hissədən ibarətdir. Birinci hissə protokolu göstərir (http/https), ikinci hissədə isə  domen və ya resursun yerləşdiyi IP ünvanını göstərir. 
10. Virtual environment layihələrdəki python bir-birləri ilə qarışmaması və ya üst-üstə düşməməsi üçün yaradılan virtual bir mühitdir. İstədiyimiz modullarrı bu mühit daxilində hazırlayırsınız və komputerə yüklənmir.
