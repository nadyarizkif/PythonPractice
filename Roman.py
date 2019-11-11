
from functools import reduce
def gantiangka (x):
    output = ''
    string = str(x)
    angka = list(string)
    angka.reverse()
    for i in range(len(angka)):
        if i==0:
            if int(angka[i]) > 4 and int(angka[i]) < 9: 
                output += 'v'
                if int(angka[i]) %5 !=0: 
                    output += ('i' * int(angka[i])%5)
            elif int(angka[i])==4:
                output += 'iv'
            elif int(angka[i]) < 4 and int(angka[i])>0:
                output += ('i' * int(angka[i]))
            elif int(angka[i])== 9:
                output += 'ix'
        elif i == 1:
            if int(angka[i]) > 4 and int(angka[i]) < 9:
                output += 'L'
                if int(angka[i]) %5 !=0:
                    output += ('X' * int(angka[i])%5)
            elif int(angka[i])==4:
                output += 'XL'
            elif int(angka[i]) < 4 and int(angka[i])>0:
                output += ('X' * int(angka[i]))
            elif int(angka[i]) == 9:
                output += 'XC'
        elif i == 2:
            if int(angka[i]) > 4 and int(angka[i]) < 9:
                output += 'D'
                if int(angka[i]) %5 !=0:
                    output += ('C' * int(angka[i])%5)
            elif int(angka[i])==4:
                output += 'CL'
            elif int(angka[i]) < 4 and int(angka[i])>0:
                output += ('C' * int(angka[i]))
            elif int(angka[i])== 9:
                output += 'CM'   
        elif i == 3:
            if int(angka[i]) < 4 and int(angka[i]) > 0:
                output += ('M' * int(angka[i]))
    output2 = list(output)
    output2.reverse()
    return reduce(lambda x1, x2 : x1+x2, output2)

print (gantiangka (1233))      