def calc():
    angka1 = float(input('Masukan angka 1: '))
    angka2 = float (input('Masukan angka 2: '))
    operator = (input ('Masukan operator (+, -, *, /, **): '))
    if operator=='+':
        print (angka1 + angka2)
    elif operator =='-':
        print (angka1 - angka2)
    elif operator == '*':
        print (angka1 * angka2)
    elif operator=='/':
        print (angka1 / angka2)
    elif operator=='**':
        print (angka1 ** angka2)
    else:
        print (f'operator {operator} tidak terdaftar')
calc ()