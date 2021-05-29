"""
# Sudoku sorusunun cevabı in-class hands-on

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

# print(type(sudoku))
# print(len(sudoku))

count = 0  # Bunu her bir satırı alt alta yazmak için kullanacağız.
print("- - - - - - - - - - - - - - - ")
for i in sudoku:  # sudoku içindeki her bir eleman alındı. (Ama bu elemanlar da bir liste)
    for j in range(len(i)):  # her bir i listesinin eleman sayısı kadar j yi dönder.
        print(i[j], " ", end="")  # burada da her bir i listesinin elemanlarını yanyana boşlukla yazdırırız.
        if (j + 1) == 9:  # Her satır bitiminde
            print()  # bir alt satıra geçmeyi sağlar
            count += 1  # bu count sayısını her bir 3 satırda - yatay çizgi oluşturmak için kullandık
            if count % 3 == 0 and count != 0:
                print("- - - - - - - - - - - - - - - ")
        if (j + 1) % 3 == 0 and j != 0 and j != 8:  # her bir 3 elemanda ve sıfıra ve 8e eşit olmadan | koy satır sonunda | olmaması için 8 e eşitlemedik
            print("| ", end="")
"""

"""
# dersteki soru cevabı in-class hands-on
x = [([1], [2, 3], (4, 5, 6))]  # [1, 2, 3, 4, 5, 6]
a = []
for i in x:  # x in içindeki liste yani ([1], [2,3], (4,5,6))
    for j in i:  # liste içindeki her bir liste ve tuple yani [1] ve [2,3] ve (4,5,6)
        for z in j:  # her bir liste ve tuple içindeki elemanları çıkarmış olduk.
            a.append(z)  # her bir çıplak elemanı z listesine attık.
print(a)  # a listemiz artık her bir çıplak elemanı kendi elemanı olarak içerdi.
"""

"""
# üstteki sorunun kısa cevabı yani list comprehension

x = [([1], [2,3], (4,5,6))]
a = {z for i in x for j in i for z in j}
print(a)
"""

"""
# in-class hands-on denemeler comprehension anlama
# uzun yoldan çözme
yList = "selvi vahit ayşe".split()
xList = "elma armut muz".split()
result = []
for i in xList:
    for j in yList:
        result.append(i + j)
print(result)
"""

"""
# in-class hands-on denemeler comprehension anlama
# kısa yoldan çözme
yList = "selvi vahit ayşe".split()
xList = "elma armut muz".split()
result = [i + j for i in xList for j in yList]
print(result)
"""

"""
# in-class hands-on denemeler
result = []
for i in range(4):
    if i % 2 == 0:
            for j in ["bir", "iki", "üç"]:
                result.append(str(i) + "--->" + j)
print(result)
"""

"""
sayılar = ["bir", "iki", "üç"]
result = [str(i) + " -—> " + j for i in range(5) for j in sayılar if i % 2 == 0]
print(result)
"""

"""
# permütason sorusu çözülecekti ama max tekrar eden sayı sorusuna dönüldü.
def equal(a, b, c) :
    numbers = [a, b, c]
    result = numbers.count(max(numbers, key = numbers.count))
    if result > 1:
        return result
    else:
        return 0
print(equal(5, 5, 5))
print(equal(1, 1, 5))
print(equal(1, 2, 3))
"""

"""
# yukarıdaki sorunun jenerik cevabı
a = []
def equals(*args):
    r = max(zip(map(args.count, args), args))
    return ("En cok tekrar eden sayı '{}' {} kez tekrar etmistir.".format(r[1], r[0]))
print(equals(1,3,3))
"""

"""
# klasik dosya okuma yöntemi
with open("fruits.csv", 'r', encoding="utf-8") as file:
    print(file.read())
"""

"""
# module ile okuma yöntemi
import csv  # loads csv module

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file)  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows:
        print(row)
"""

"""
import csv

with open("fruits.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter = '?')  # we specified a char ":" that is not used
                                                  # in the csv file as a value of delimiter
    for row in csv_rows:
        print(row)
"""

"""
Hocam anlamayanlar için özet şöyle.
Working with files konusunda olduğu gibi bir dosya oluşturduk. Ama bu kez .txt yerine .csv uzantılı dosya oluşturduk.
Daha sonra bu .csv dosyalarını önceki derslerde olduğu gibi çağırma yollarını gördük.
3 çeşit çağırma yolu var:
1- Klasik open ve read
2-Csv modülü
3-Pandas kütüphanesi ile
Not: eğer yukarıdaki yazdıklarımdan anlaşılmayan bir yer varsa muhtemelen lms preclass çalışmadınız.
"""

"""
L = ["right 20", "right 30", "left 50", "up 10", "down 20"]
x = y = 0
for i in range (len(L)) :
    if L[i].startswith("r") : x = x + int(L[i].split(" ")[1])
    elif L[i].startswith("l") : x = x - int(L[i].split(" ")[1])
    elif L[i].startswith("u") : y = y + int(L[i].split(" ")[1])
    elif L[i].startswith("d") : y = y - int(L[i].split(" ")[1])
print([x, y])
"""