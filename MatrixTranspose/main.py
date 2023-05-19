#Kullanıcıdan alınan matrisin transpozunu bulalım:
satir = int(input("satir sayisini giriniz : "))
sutun = int(input("sutun sayisini giriniz : "))
#matrisi oluşturalım:
import random
m=[[0 for x in range(sutun)] for y in range(satir)]
mtmp = [[0 for x in range(satir)] for y in range(sutun)]

for i in range(satir):
    for j in range(sutun):
        m[i][j]=random.randint(0,9)
        mtmp[j][i]=m[i][j]
print(m)
print(mtmp)
