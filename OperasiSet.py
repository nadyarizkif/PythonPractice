S=set(range(0,10))
#num = int(input("Enter a number: "))  
A={2,3,5,7}
B={5,7,9}
### a. Tentukan A
print (A)
### b. Tentukan B 
print (B) 
### c. (A n B)
print (A & B)
### d. A u B 
print (A | B )
### e. A n (A u B)
print (A & (A | B))
### f. B n (A u B)
print (B & (A | B))
### g. (A u B) n ( A u B)
print ((A | B) & (A | B))
### h. (A n B) u (A u B)
print ((A & B) | (A | B))
