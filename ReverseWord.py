x=input('Masukan kalimat: ')
def balikkata(x):
    daftarkata=x.split()
    kata2=''
    for kata in daftarkata:
        kata2+=kata[::-1]
        kata2+=' '
    return kata2
print (balikkata(x))