## SOAL KAKI AYAM DAN KAMBING:
# di dalam kandang terdapat kambing dan ayam sebanyak 13 ekor. 
# jika jumlah kaki hewan tersebut adalah 32 ekor, maka jumlah kambing dan ayam masing-masing adalah:
hewan = int(input ('ketik jumlah total hewan: '))
kaki = int(input ('ketik jumlah total kaki: '))
K1= int(input ('jumlah kaki hewan pertama adalah: '))
K2= int(input ('jumlah kaki hewan kedua adalah: '))
H1=abs(((kaki-(K2*hewan)))/(K2-K1))
H2=abs(hewan-H1)  
print ('jumlah hewan pertama adalah ',int(H1)) 
print ('jumlah hewan kedua adalah ', int(H2))
print (f'jumlah ayam=  {int(H1)}')

### SOAL IBU DAN ANAK:
## 19 th yang lalu umur anak setengah tahun lebih muda dari 1/4 umur ibunya, 
# umur anak sekarang 19 th lebih tua dari 1/7 umur ibunya. berapa umur ibunya?
T0=19
RasioT0=1/4
KurangT0=1/2
TambahT1=19
RasioT1=1/7
UB=abs(((-(RasioT0*T0)-KurangT0+T0)-TambahT1)/(RasioT1-RasioT0))
UA = (RasioT0*(UB-T0))- KurangT0 + T0
print ('Umur Ibu adalah: ', round(UB))
print ('Umur anak adalah: ', round(UA))