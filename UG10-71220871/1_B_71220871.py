print("~"*10,"\('v')/", "~"*10)
print("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print("~"*10,"\('v')/", "~"*10)
print()
print("Pilihlah salah satu bangun ruang yang ingin dihitung volumenya:")
pilih1= print("1. Limas")
pilih2= print("2. Bola")
pilih3= print("3. Prisma")
pilih4= print("4. Kerucut")
angka= int(input("Masukkan pilihan anda: "))
if angka==1:
    pjg= int(input("Masukkan panjang sisi alas limas: "))#limassegiempat
    tggi= int(input("Masukkan tinggi limas: "))
    lbr=int(input("Masukkan lebar limas: "))
    vlimas= 1/3*pjg*lbr*tggi
    print("Volume limas tersebut adalah",vlimas)
    
elif angka==2:
    r=int(input("Masukkan jari-jari: "))
    vbola= 4/3*22/7*r**3
    print("Volume bola tersebut adalah",vbola)

elif angka==3: 
    print("Pilihlah salah satu dari pilihan di bawah: ")
    print("1. Prisma Segitiga")
    print("2. Prisma Segiempat")
    print("3. Prisma Segilima")
    pilihprisma= int(input("Tentukan pilihan anda: "))
    if pilihprisma==1:
            alas= int(input("Masukkan alas prisma: "))
            tinggipris=int(input("Masukkan tinggi prisma: "))
            vprisma3= (1/2*alas*tinggi)*tinggi
            print("Volume prisma tersebut adalah",vprisma3)
    elif pilihprisma==2:
            luas= int(input("Masukkan luas alas prisma: "))
            tinggipris=int(input("Masukkan tinggi prisma: "))
            vrpisma4= luas*tinggipris
            print("Volume prisma tersebut adalah",vprisma4)
    elif pilihprisma==3:
            sisi= int(input("Masukkan sisi prisma: "))
            tinggipris=int(input("Masukkan tinggi prisma: "))
            vprisma5= (43/25*sisi*sisi)*tinggipris #1,72= 43/2
            print("Volume prisma tersebut adalah",vprisma5)
elif angka==4: 
    jari= int(input("Masukkan jari-jari kerucut: "))
    tinggiker=int(input("Masukkan tinggi kerucut: "))
    vkerucut= 1/3*22/7*jari**2*tinggiker
    print("Volume kerucut tersebut adalah",vkerucut)

