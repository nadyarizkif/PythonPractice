## TRANSLATE DAY
days = {'monday':'senin', 'tuesday': 'selasa', 
'wednesday' : 'rabu', 'thursday': 'kamis', 
'friday':'jumat', 'saturday':'sabtu','sunday':'minggu'}

hari2=input('masukan hari (enter a day): ')
if hari2.lower() in days.keys(): 
    print (f'The Indonesian for {hari2} is {days.get(hari2.lower())}')
elif hari2.lower() in days.values():
    print (f'Bahasa Inggris untuk {hari2} adalah {list(days.keys())[list(days.values()).index(hari2.lower())]}')
else:
    print ('kata yang anda masukan bukan merupakan nama hari (the word you entered is wrong)')

## Menghitung Hari
Hari =  ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
today = (input('hari apa ini? ')).lower()
x = (int(input('Masukan jumlah hari yang dicari: ')))
then = Hari[(Hari.index(today) + (x%7))%7]
print (then)
