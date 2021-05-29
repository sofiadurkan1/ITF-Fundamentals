# permütasyon sorusu çözüldü
"""
def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])
"""

#hocanın permutasyon çözümü
"""
solution = [[]]
#solution-1 = [[1],[2],[3]]
#solution-2 = [[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]]
#solution-3 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
num =[1,2,3]
num_set = set(num)
for index in range(len(num)) :
    solution =[i+[j] for i in solution for j in num_set.difference(set(i))]
    print(solution)
print(solution)
"""
# Eren Bey'in açıklamalı oarak attığı:
"""
solution = [[]]
num = [1,2,3]  # bu listenin permütasyonunu (her ihtimalini) yazdırmamız isteniyor
num_set = set(num)
for index in range(len(num)) :  # num eleman sayısı kadar iterate et (yani 3 kere)
  solution = [i + [j] for i in solution for j in num_set.difference(set(i))]  
  print(solution)  # her iterasyon çıktısı
solution   # istenen sonuç
"""

# değişik sorular
"""
def count(mylist):
    return len(set(mylist))
print(count((1, 1, 3)))
"""

# dğişik sorular if olmadan diğer çözüm Emre Bey'in cevabı:
"""
equal = (lambda *numbers:numbers.count(max(numbers, key=numbers.count)))
print(equal(1, 1, 2))
"""

# değişik sorular Hoca'nın cevabı:
"""
equall = lambda x,y,z: [x,y,z].count(max([x,y,z], key=[x,y,z].count)) \
          if [x,y,z].count(max([x,y,z], key=[x,y,z].count)) > 1 else 0
"""
