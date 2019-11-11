## CARI KATA
cari2='coding'
x2=nama4.upper().replace(cari2.upper(),'')
jml2=(len(nama4)-len(x2))/len(cari2)
print (int(jml2))
print (f'Jumlah Kata\'{cari2}\'ada =' {jml2})

### CARI HURUF ###
kalimat = input('masukan kalimat: ')
huruf = input ('masukan huruf yang dicari: ')
kalimat2= kalimat.upper().replace(huruf.upper(), '')
jumlah=len(kalimat)-len(kalimat2)
print ('jumlah huruf %s dalam kalimat "%s" adalah sebanyak %d'%(huruf, kalimat, jumlah))
