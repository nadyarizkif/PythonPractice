morse={
    'a':'.-', 'b':'-..', 'c':'-.-.', 'd':'-..',
    'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 
    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
    'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'y':'-.--',
    'z':'--..', ' ':' ', '':''}
keys=list(morse.keys())
values=list(morse.values())
def transmorse (x):
    output=''
    if x[0] in list(morse.keys()):
        for i in range(len(x)):
            output+=morse.get(x.lower()[i])
            output+='/'
    else:
        y= x.split('/')
        for i in y:
            output+=keys[(values.index(i))]
    return output
inputs=input('Masukan kalimat yang akan diubah: ')
print(transmorse (inputs))
