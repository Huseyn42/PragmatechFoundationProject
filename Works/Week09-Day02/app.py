general=[]

while True:
    
    x=input('Yeni istifadəçi əlavə etmək (1/2):')

    if x=='1':
        ad=input('İstifadəçinin adı:')
        soyad=input('İstifadəçinin soyadı:')
        yaş=input('İstifadəçinin yaşı:')
        email=input('İstifadəçinin email adresi:')
        dict=(ad,soyad,yaş,email)
        general.append(dict)
    else:
        print(general)
        break