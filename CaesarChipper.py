alphabet= 'abcdefghijklmnopqrstuvwxyz'
def caesarchipper(kalimat,key):
    output=''
    for i in range(len(kalimat)):
        if kalimat.lower()[i] in alphabet:
            output+= alphabet [((alphabet.index(kalimat.lower()[i]))+key)%26]
        else:
            output+=kalimat[i]
    return output
kalimat = input ("Masukan kalimat yang akan di-encode: ")
key= int(input ('Masukan key (angka): '))
print(caesarchipper(kalimat,key))