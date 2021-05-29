"""
# Q1 - Solution 1
sentence = input("Enter the word to see is it palindrome? : ")
if sentence == sentence[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")
"""

"""
# Q1 - Solution 2
s = input("write here to check : ")
def isPalindrome(s):
    return s == s[::-1]
print(s[::-1])
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
"""

"""
# Q1 - Solution 3 (Desired Solution)
# Ters çevirip tüm harfleri küçük harfe çevirdik. casefold lower'a göre daha çok karakter çevirir.
def is_palindrome(string):
    return string.casefold() == string[::-1].casefold()
    # .casefold() converts more characters into lower case. More than .lower()

# ters çevrilip küçük harlere dönüşen stringi for döngüsüne alır sadece alphanumeric olanları yazdırır (isalnum)
def palindrome_sentence(sentence):
    string = ""
    for i in sentence:
        if i.isalnum():  # .isalnum() checks is it alphanumeric. If yes it's means True
            string += i
    print(string)  # string'i istenen formatta çıktı olarak yazdır.
    return is_palindrome(string)  # palindrome olup olmdığını kontrol et (string.casefold() == string[::-1].casefold())

# kullanıcıdan girdi aldık. Eğer palindrome fonksiyonu (2. def) true verirse doğru yaz depilse yanlış yaz.
word = input("Write smth to check if it is palindrome : ")
if palindrome_sentence(word):
    print(f"{word} is a palindrome statement")
else:
    print(f"{word} is not a palindrome statement.")
"""

"""
# Q2 Solution - 1
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

def print_sudoku(sudoku):
  print("- "*15)
  for i, row in enumerate(sudoku):
    print(("| {}  {}  {}  " * 3)[2:].format(*[x for x in row]))
    if i == 2:
      print("- "*15)
    elif i == 5:
      print("- "*15)
    elif i == 8:
      print("- "*15)
print_sudoku(sudoku)

"""
