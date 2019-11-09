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