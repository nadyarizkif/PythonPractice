# PALINDROME: apakah kalo suatu kata hurufnya kita balik akan sama, contoh: katak
word = input ('Masukan kata: ')
## palindrom cara 1
def palindrom(x):
    kata=list(x)
    kata2=kata.copy()
    for i in range (round(len(kata)/2)):
        if kata2[i] == kata[(len(kata) - i - 1)]:
            return True
        else:
            return False
            break
print(palindrom (word))

## palindrom cara 2
def palindrom2(kata):
    if kata == kata[::-1]:
        return True 
    else: 
        return False 
print (palindrom2 (word)) 