## KONVERSI NILAI
# nilai >=82: A
# nilai 72 - 81:B
# nilai 62 - 71: C
# nilai 52 - 61: D
# nilai < 52 :E
nilai = 98
if nilai >= 82:
    print('Selamat anda mendapatkan nilai A!')
elif nilai>=72 and nilai<=81:
    print ('Anda mendapatkan nilai B')
elif nilai>=62 and nilai<=71:
    print ('Anda mendapatkan nilai C')
elif nilai>=52 and nilai<=61:
    print ('Sayang sekali, anda mendapatkan nilai D')
else:
    print ('Anda mendapatkan nilai E, belajar lebih giat!')
   

## GANJIL GENAP
angka=input('Masukan angka: ')
if (int(angka)%2 == 0):
    print ('angka %s adalah angka GENAP' %(angka))
else:
    print ('angka %s adalah angka GANJIL' %(angka))


### PANGKAT DAN KUADRAT 
def pangkatB(x,y):
    if (y==1):
        return x
    else:
        return x * pangkatB(x,y-1)

# FAKTORIAL
def faktorial (x):
    if x<=2:
        return x
    else:
        return x * faktorial (x-1)
print(faktorial(5))