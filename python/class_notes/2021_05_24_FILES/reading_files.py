"""
import os

os.system("cls")

my_file = open("first_file.txt")  # this syntax opens a 'txt' file

print(type(my_file))
print()
print(my_file)

my_file.close()
"""

"""
import os

os.system("cls")

my_fie = open("fishes.txt", 'r')

print(my_fie.read())  # displays the entire text content

my_fie.close()
"""

"""
my_file = open("fishes.txt", 'r')

print(my_file.read(33))
print(my_file.read(25))
print()
my_file.close()
"""

"""
my_file = open("fishes.txt", 'r')

print(my_file.read(3))
print()
print(my_file.read(5))
print()
my_file.seek(0)
print(my_file.read(8))
my_file.close()
"""

"""
my_file = open("fishes.txt", 'r')

print(my_file.read(6))
print("cursor is at", my_file.tell())
print()
print(my_file.read(7))
print("cursor is at", my_file.tell())
print()
my_file.seek(0)
print("cursor is at", my_file.tell())
print()
print(my_file.read(8))
print("cursor is at", my_file.tell())
print()
current_position = my_file.tell()
print("this is the result of current position of cursor : ", current_position)
print()
new_position = current_position - 3
print(my_file.seek(new_position))
print("cursor is at, i mean 3 letter before", my_file.tell())
my_file.close()
"""

"""
my_file = open("rumi.txt", 'r')

print(my_file.read())

my_file.close()
"""
"""
my_file = open("rumi.txt", 'r')
print(my_file.read(35))
print(my_file.read(13))
print(my_file.tell())
my_file.seek(15)
print(my_file.read(20))
my_file.close()
"""

"""
sea = open("fishes.txt", 'r')

print(sea.readline())  # displays the first line of the text
print(sea.readline())  # displays the second line
print(sea.readline())  # each time it goes to the new line

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
sea = open("fishes.txt", 'r')

print(sea.readlines())

sea.close()
"""

"""
sea = open("fishes.txt", 'r')

print(sea.readline())
print(sea.readlines())

sea.close()
"""

"""
sea = open("fishes.txt", 'r')   

print(type(sea.readlines()))

sea.close()
"""

"""
sea = open("fishes.txt", 'r')

for line in sea:
    print(line)

sea.close()
"""

