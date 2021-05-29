"""
fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
x = 3
while x > 0:
    try:
        a = int(input("bir numara ver : "))
        print("Your fruit is", fruits[a])
        break
    except IndexError:
        print("verdiğiniz numara bir meyve için tanımlı değildir. Tekrar deneyiniz")
        x -= 1
        print(x, "hakkınız kaldı!")
    except ValueError:
        print("lütfen bir sayı giriniz. Tekrar dene!")
        x -= 1
        print(x, "hakkınız kaldı" )
    else:
        print("congratulation, you gave a valid number.")
        break
    finally:
        print("Afiyet ola.")
"""

"""
sea = open("fishes.txt", "r")
print(sea.read())
sea.close()
"""

"""
sea = open("fishes.txt", 'r')

print(sea.read(33))  # displays the first 33 chars of the text
print()
print(sea.read(25))  # displays the next 25 chars of the text
print()
sea.seek(0)  # changes the stream (cursor) position to zero
print(sea.read(33))  # displays the first 33 chars again
print()
print(sea.tell())  # returns the current stream (cursor) position

sea.close()
"""

"""
sea = open("içerdema.txt", "r")
print(sea.read(109))
print(sea.read(13))
print(sea.tell())
print(sea.seek(45))
print(sea.read(64))
sea.close()
"""

"""
sea = open("fishes.txt", 'r')

print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))
print(sea.readline(13))

sea.close()
"""

"""
rumi = open("rumi.txt", 'r')

print(rumi.readline())
print(rumi.readline())
print(rumi.readline(18))
rumi.close()
"""

"""
sea = open("rumi.txt", 'r')

print(sea.readlines()[0])

sea.close()
"""

"""
rumi = open("rumi.txt", "r")
for line in rumi.readlines():
    print(line)
rumi.close()
"""

"""
with open("benim_ilk_dosyam.txt", "w", encoding = "utf-8") as dosyam :
    dosyam.write("bu benim ilk satırım. \namma aslında ikinci satırım. \nBu da benim üçüncü satırım.")
"""

"""
with open("dummy_file.txt", 'w', encoding="utf-8") as file:
    file.write('My first sentence')
    file.write('My second sentence,')
    file.write('My third sentence\n')
    file.write('My fourth sentence ')
    file.write('My last sentence')

with open("dummy_file.txt", 'r', encoding="utf-8") as file:
    print(file.read())
"""


fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
with open("fruits3.txt", 'w', encoding="utf-8") as file:
    for basket in fruits:
        file.write(basket + '\n')
with open("fruits3.txt", 'r', encoding="utf-8") as file:
    print(file.read())