# Soal 1:
# 1 2 3 4 5
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

for i in range (0,6):
    x=''
    for j in range (1,6-i):
        x+= f'{j}'
    print (x)

# Soal 2:
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

for i in range (5):
    x = ''
    for j in range (i+1):
        x+=f'{j+1}'
    print (x)


# Soal 3: 
# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3
# 5 4 
# 5 

print ('\n')

for i in range (5):
    x = ''
    for j in range (i,5):
        x+= f'{(5-j)}'
    print (x)


print ('\n')

# Soal 4:
# 1
# 1 1 
# 1 1 1 
# 1 1 1 1
# 1 1 1 1 1 

for i in range (5):
    x='1'
    x = x * (i+1)
    print (x)
