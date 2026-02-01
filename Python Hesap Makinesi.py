def toplama(x,y):
    print(x+y)

def cikartma(x,y):
    print(x-y)   

def carpma(x,y):
    print(x*y)

def bolme(x,y):
    print(x/y)   

sayi1 = int(input("Birinci Sayıyı Yazın: "))

sayi2 = int(input("İkinci Sayıyı Yazın: "))

print("""
1- Toplama
2- Çıkartma
3- Çarpma
4- Bölme                        
""")

secim = int(input("Yapmak İstediğiniz İşlemin Rakamını Yazın: "))

if secim == 1:
    toplama(sayi1,sayi2)

elif secim == 2:
    cikartma(sayi1,sayi2)

elif secim == 3:
    carpma(sayi1,sayi2)

elif secim == 4:
    bolme(sayi1,sayi2)

else:
    print("Hata, Lütfen Yeniden Deneyin!")
