import os
os.system("cls")

"""
myFileList = ['first', 'second', 'third.txt', 'fouth.test', 'fifth.py']

for i in myFileList:
    with open(i, 'w', encoding="utf-8") as newFile:
        newFile.write(i)
"""

"""
for i in range(10):
    with open(str(i), "w") as f:
        f.write(str(i))
"""

"""
for i in range(1, 11):
    with open(str(i)+".txt", "w") as f:
        f.write(str(i))
"""

"""
file_name = ""

for i in range(1, 11):

    file_name = (str(i) + ".txt")

    with open(file_name, "w") as f:
        f.write(file_name)
        f.write("\nend of file" + file_name)

    with open(file_name, "r") as f2:
        print(f2.read())
"""

"""
flowers = ['Jasmine\n', 'Rose\n', 'Lily\n', 'Daisy\n', 'Tulip\n']

with open("flowers.txt", 'w', encoding="utf-8") as file:
    file.writelines(flowers)  # takes an iterator for writing

with open("flowers.txt", 'r', encoding="utf-8") as file:
    print(file.read())

with open("flowers.txt", 'r', encoding="utf-8") as file:
    print(file.readlines())
"""

"""
flowers = ['Jasmine\n', 'Rose\n', 'Lily\n', 'Daisy\n', 'Tulip\n']

with open("flowers.txt", 'w', encoding="utf-8") as ourFile:
    # ourFile.write("this is the text we want to write in the file...")
    ourFile.writelines(flowers)
with open("flowers.txt", "r") as f:
    print(f.read())
"""

"""
# to append Orchid name at the end of the flowers.txt file
with open("flowers.txt", 'a', encoding="utf-8") as file:
    file.write('Orchid\n')

with open('flowers.txt', 'r') as f:
    print(f.read())
"""

"""
append = input("Write anything to append to the end of the .txt file : ")
with open("flowers.txt", 'a', encoding="utf-8") as file:
    file.write(append + '\n')

with open('flowers.txt', 'r') as f:
    print(f.read())
"""

"""
# working with csv files
fruits = ['no,','fruit,' ,'amount\n', '1,','Banana,','4 lb\n', '2,','Orange,','5 lb\n', '3,','Apple,','2 lb\n', '4,','Strawberry,','6 lb\n', '5,','Cherry,','3 lb\n']
with open("fruits.csv", 'w', encoding='utf 8') as file:
    file.writelines(fruits)
"""

"""
# with csv module 
import csv  # loads csv module
with open("our_CSW_file.csv", "r", newline="", encoding="utf-8") as file:
    csv_rows = csv.reader(file)  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows:
        print(row)
"""

"""
import os
os.system("cls")
with open("our_CSV_file.csv") as ourfile:
    print(ourfile.read())
"""

"""
import csv

with open("our_CSW_file.csv", 'r', newline = '', encoding = 'utf-8') as ourFile:
    rows_of_our_file = csv.reader(ourFile)
    for each_row in rows_of_our_file:
        print(each_row)
"""

"""
import csv
with open("fruits.csv", "w", encoding = "utf-8") as file:
    file.write("no,fruit,amount,\n1,Banana,4 lb,\n2,Orange,5 lb,\n3,Apple,2 lb,\n4,Strawberry,6 lb,\n5,Cherry,3 lb)\n")
with open("fruits.csv", "r", newline = "", encoding = "utf-8") as file:
    csv_rows = csv.reader(file)
    for row in csv_rows:
        print(row)
"""