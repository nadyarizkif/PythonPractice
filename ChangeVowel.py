def vowel():
    kata=input('masukan kata/kalimat: ')
    huruf=input('masukan huruf vokal tujuan: ')
    kata2= kata.replace('a', huruf).replace('i', huruf).replace('e', huruf).replace('u', huruf).replace('o', huruf).replace('A', huruf.upper()).replace('I', huruf.upper()).replace('E', huruf.upper()).replace('U', huruf.upper()).replace('O', huruf.upper())
    print (kata2)
vowel()