## SOAL 1:
## setiap angka genap dikalikan 2 
## semua angka hasilnya dijumlahkan satu sama lain
from functools import reduce
hasil = reduce (lambda x,y: x + y, (map(lambda x :x*2, filter (lambda x: x%2 == 0, list(range(101))))))
print (hasil)

## CEK PRIMA 
def prima (x):
    if x == 2:
        prime =  True
    elif x > 2:
        for i in range (2, x):
            if x % i == 0:
                prime = False
                break
            else:
                prime = True 
    else: 
        prime= False
    return prime

## LIST PRIMA
prime = lambda n : [x for x in range (2,n) if not 0 in map(lambda z: x % z, range(2,x))]
print ('.'.join(map(str, prime(100))))
