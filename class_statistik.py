from functools import reduce
class statistik:
    def mean (self, daftarangka):
        (reduce(lambda x1,x2: (x1+x2), daftarangka))/len(daftarangka)
    def median(self, daftarangka):
        daftarangka.sort()
        if len (daftarangka) % 2 == 0:
            return (daftarangka[int(len(daftarangka)/2)] + daftarangka[int((len(daftarangka)/2)-1)])/2
        else: 
            return (daftarangka[(round(len(daftarangka)/2))])
    def modus(self, daftarangka):
        max = 1
        perhitungan = 1
        B = list(set(daftarangka))
        for i in B:
            hitung = daftarangka.count(i)
            if hitung > perhitungan:
                perhitungan = hitung
                max = i
        return max

stats = statistik()

print(stats.median([2,3,4,4,4,4,4]))