import os


os.chdir("{}/Desktop".format(os.environ['USERPROFILE']))
path = "{}/Desktop/Save_and_Secure_Halfcress/gizli_ozne.txt".format(os.environ['USERPROFILE'])
path2 = "{}/Desktop/Save_and_Secure_Halfcress/sifre.txt".format(os.environ['USERPROFILE'])


try:
    os.mkdir("Save_and_Secure_Halfcress")
    print("Program ilk kez açılıyor!")
    print("Lütfen bir kullanıcı adı ve şifre belirleyin.")
    kullanici_adi = input("Kullanıcı adi:   ")
    kullanici_sifre = input("Kullanici sifresi:   ")
    dosya2 = open(path2, "a")
    ehem = "{} : {}".format(kullanici_adi,kullanici_sifre)
    dosya2.write(ehem)
    dosya2.close()
except:
    kullanici_adi = input("Lütfen kullanıcı adınızı girin:  ")
    kullanici_sifre = input("Kullanici sifrenizi girin:   ")

def dogrulama(a,b):

    mekanizma = "{} : {}".format(a,b)
    mekanizma = list(mekanizma)
    dosya2 = open(path2, "r")
    tester = dosya2.read()
    dosya2.close()
    tester = list(tester)

    if tester == mekanizma:
        return True
    else:

        return False






menu = """
#####################=====HOŞ GELDİNİZ=====#####################
#   1] Yeni Sifre Olustur                                      #
#   2] Sifreleri Goruntule                                     #
#                                                              #
#                                                              #
#   3] Cikis                                                   #
#####################################=designed-by-halfcress-####

"""


if dogrulama(kullanici_adi,kullanici_sifre) == True:

    while True:
        os.system("cls") #linux switch clear
        print(menu)
        secim = input("Seciminizi Yapin: ")

        if secim == "1":
            ad = input("Platformun Adi :  ")
            sifre = input("Koyulan Sifre:  ")
            dosya = open(path, "a")
            dosya.write("{} : {} \n".format(ad,sifre))
            dosya.close()
            print("İşlem başarılı Ana Menü için Enter'a basınız.")
            input()
        elif secim == "2":
            dosya = open(path, "r+")
            print(dosya.read())
            dosya.close()
            print("Çıkmak için Enter'a basınız.")
            input()
        elif secim == "3":
            quit()

else:
    print("Hatalı giriş - Program kapatılıyor.")
    quit()


