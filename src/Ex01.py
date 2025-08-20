#1. Write a  Python program to calculate the length of a string.
myString = input("Enter your string: ")


print("The length of your string:", len(myString))
#2. Write a Python program to count the number of characters (character frequency) in a string.
s = "google.com"
freq = {}
for char in s:
   freq[char] = freq.get(char, 0) + 1


print(freq)
#3. Write a  Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead
def string_both_ends(s):
   if len(s) < 2:
       return ""
   return s[:2] + s[-2:]


print(string_both_ends("w3resource"))
print(string_both_ends("w3"))
print(string_both_ends("w"))
#4.Write a  Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def replace_char(s):
   first_char = s[0]
   result = first_char + s[1:].replace(first_char, '$')
   return result


print(replace_char("restart"))
#5. Write a  Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_strings(a, b):
   return b[:2] + a[2:] + " " + a[:2] + b[2:]


print(swap_strings("abc", "xyz"))


#6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def add_ing(s):
   if len(s) < 3:
       return s
   if s.endswith("ing"):
       return s + "ly"
   return s + "ing"


print(add_ing("abc"))
print(add_ing("string"))
print(add_ing("hi"))


#7.
def not_poor(s):
   not_index = s.find("not")
   poor_index = s.find("poor")


   if not_index != -1 and poor_index != -1 and poor_index > not_index:
       return s[:not_index] + "good" + s[poor_index+4:]
   return s


print(not_poor("The lyrics is not that poor!"))
print(not_poor("The lyrics is poor!"))


#8.Write a  Python function that takes a list of words and return the longest word and the length of the longest one.
def longest_word(words):
   longest = max(words, key=len)
   return longest, len(longest)


words = ["Python", "Exercises", "Practice", "Solution"]
word, length = longest_word(words)


print("Longest word:", word)
print("Length of the longest word:", length)


#9. Write a Python program to remove the nth index character from a nonempty string.
def remove_char(s, n):
   return s[:n] + s[n+1:]


print(remove_char("Python", 2))


#10.Write a  Python program to change a given string to a newly string where the first and last chars have been exchanged.
def swap_first_last(s):
   if len(s) <= 1:
       return s
   return s[-1] + s[1:-1] + s[0]


print(swap_first_last("Python"))


#11.Write a Python program to remove characters that have odd index values in a given string.
def remove_odd_index(s):
   return "".join([s[i] for i in range(len(s)) if i % 2 == 0])


print(remove_odd_index("abcdef"))


#12. Write a Python program to count the occurrences of each word in a given sentence.


wordList = myString.split(" ")
wordFreq = {}
for word in wordList:
   wordFreq[word] = wordFreq.get(word, 0) + 1
print("The occurrence of each word in your string:", wordFreq)


#13
s = input("Enter a string: ")
print("Upper:", s.upper())
print("Lower:", s.lower())


#14.Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
def distinct_sorted_words(s):
   words = s.split(",")
   return ",".join(sorted(set(words)))


print(distinct_sorted_words("red,white,black,red,green,black"))


#15.Write a  Python function to create an HTML string with tags around the word(s).
def add_tags(tag, s):
   return f"<{tag}>{s}</{tag}>"


myString = input("Enter your string: ")
htmlTag = input("Enter your HTML tag: ")
print(add_tags(htmlTag, myString))


#16.Write a Python function to insert a string in the middle of a string.
def inset_sting_middle(string1, string2):
   return string1[:len(string1)//2] + string2 + string1[len(string1)//2:]
myString1 = input("Enter your first string: ")
myString2 = input("Enter your second string: ")
print("Insert the second string into the middle of the first string: ", inset_sting_middle(myString1, myString2))


#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def insert_end(s):
   return s[-2:] * 4 if len(s) >= 2 else s


print(insert_end("Python"))
print(insert_end("Exercises"))


#18. Write a  Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
def first_three(string):
   if (len(string) < 3):
       return string
   return string[:3]
myString = input("Enter your string: ")
print(first_three(myString))


#19.Write a Python program to get the last part of a string before a specified character.
def last_part_before(string, char):
   string_split = string.split(char)
   return string_split[0]
myString = input("Enter your string: ")
specified_char = input("Enter your specified character to split: ")
print(last_part_before(myString, specified_char))


#20. Write a  Python function to reverse a string if its length is a multiple of 4.
def my_reverse(string):
   if (len(string) % 4 == 0):
       return string[::-1]
   return "Your string's length is not a multiple of 4"
myString = input("Enter your string: ")
print(my_reverse(myString))


#21 Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def convert(string):
   cnt = 0
   for char in string[:4]:
       if char.isupper():
           cnt += 1
   if cnt >= 2:
       return string.upper()
   return string
my_string = input("Enter your string: ")
print(convert(my_string))


#22.Write a  Python program to sort a string lexicographically.
my_string = input("Enter your string: ")
print("Sorted lexicographically string:", "".join(sorted(my_string)))


#23. Write a Python program to remove a newline in Python.
my_string = input("Enter your string: ")
removed_newline_string = my_string.strip()
print(removed_newline_string)


#24. Write a Python program to check whether a string starts with specified characters.
def starting_chars_check(string, chars):
   if chars == string[:len(chars)]:
       return True
   return False
my_string = input("Enter your string: ")
starting_chars = input("Enter the starting characters: ")
if not starting_chars_check(my_string, starting_chars):
   print("No, your string does not start with", starting_chars)
else:
   print("Yes, your string starts with", starting_chars)


#25. Write a Python program to create a Caesar encryption.
def ceasar_encryption(plaintext, key):
   key = key % 26
   ciphertext = ""
   for c in plaintext:
       if c.isalpha():
           if c.islower():
               ciphertext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
           if c.isupper():
               ciphertext += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
       else:
           ciphertext += c
   return  ciphertext


plaintext = input("Enter your plaintext: ")
key = int(input("Enter your key: "))
print(ceasar_encryption(plaintext, key))


#29. Write a Python program to set the indentation of the first line.
def indent_first_line(s, indent=4):
   spaces = " " * indent
   lines = s.splitlines()
   if lines:
       lines[0] = spaces + lines[0]
   return "\n".join(lines)


sample = """Python is fun.
It is widely used in AI, ML and Web Development."""
print(indent_first_line(sample, 6))


#30. Write a Python program to print the following numbers up to 2 decimal places.
def formatted_num(num_list):
   for i in num_list:
       print(f"{i:.2f}")




n = int(input("Enter the number of numbers: "))
my_num_list = []
for i in range(n):
   num = float(input(f"Enter number {i+1}: "))
   my_num_list.append(num)


formatted_num(my_num_list)


#31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
def formatted_num(num_list):
   for i in num_list:
       print(f"{i:+.2f}")




n = int(input("Enter the number of numbers: "))
my_num_list = []
for i in range(n):
   num = float(input(f"Enter number {i+1}: "))
   my_num_list.append(num)


formatted_num(my_num_list)


#32. Write a Python program to print the following positive and negative numbers with no decimal places.
def formatted_num(num_list):
   for i in num_list:
       print(round(i))




n = int(input("Enter the number of numbers: "))
my_num_list = []
for i in range(n):
   num = float(input(f"Enter number {i+1}: "))
   my_num_list.append(num)


formatted_num(my_num_list)


#33. Write a  Python program to print the following integers with zeros to the left of the specified width.
def add_zero(num_list, width):
   for num in num_list:
       print(str(num).zfill(width))




n = int(input("Enter number of integers: "))
w = int(input("Enter width: "))
nums = []
for i in range(n):
   nums.append(int(input(f"Enter integer number {i+1}: ")))
add_zero(nums, w)


#34.  Write a  Python program to print the following integers with '*' to the right of the specified width.
def add_zero(num_list, width):
   for num in num_list:
       print(str(num).ljust(width, "*"))




n = int(input("Enter number of integers: "))
w = int(input("Enter width: "))
nums = []
for i in range(n):
   nums.append(int(input(f"Enter integer number {i+1}: ")))
add_zero(nums, w)


#35. Write a Python program to display a number with a comma separator.
def display_with_comma(num):
   print(f"{num:,}")
n = int(input("Enter an integer: "))
display_with_comma(n)


#36.Write a Python program to format a number with a percentage.
def format_percentage(num):
   print(f"{num * 100}%")
n = float(input("Enter a number: "))
format_percentage(n)


#37.Write a Python program to display a number in left, right, and center aligned with a width of 10.
def aligned(num):
   s = str(num)
   print("Left aligned:", s.ljust(10))
   print("Right aligned:", s.rjust(10))
   print("Center aligned:", s.center(10))
n = float(input("Enter a number: "))
aligned(n)


#38. Write a Python program to count occurrences of a substring in a string.
my_string = input("Enter your string: ")
substr = input("Enter your substring: ")
occurrence = my_string.count(substr)
print(f"Your substring occurrences: {occurrence}")


#39. Write a  Python program to reverse a string.
my_string = input("Enter your string: ")
print(my_string[::-1])


#40. Write a Python program to reverse words in a string.
my_string = input("Enter your string: ")
words = my_string.split(" ")
for i in range(len(words)):
   words[i] = words[i][::-1]
reversed_word_string = " ".join(words)
print(reversed_word_string)


#41. Write a  Python program to strip a set of characters from a string.
def strip_chars(string, chars):
   return "".join(c for c in string if c not in chars)


my_string = input("Enter your string: ")
stripped_chars = input("Enter your set of characters to be strip: ")


print(strip_chars(my_string, stripped_chars))


#42.Write a Python program to count repeated characters in a string.
def count_repeated_chars(s):
   mp = {}
   for c in s:
       if c in mp:
           mp[c] += 1
       else:
           mp[c] = 1;
   for c in mp:
       print(f"{c} {mp[c]}")
my_string = input("Enter your string: ")
count_repeated_chars(my_string)


#43. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
from math import pi




def rectangle_area(length, width):
   return length * width




def cylinder_volume(radius, height):
   return pi * radius**2 * height




rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectange: "))
print(f" The area of the rectangle is {rectangle_area(rectangle_length, rectangle_width):.2f}cm\u00b2")




cylinder_radius = float(input("Enter the radius of the cylinder: "))
cylinder_height= float(input("Enter the height of the cylinder: "))
print(f" The volume of the cylinder is {cylinder_volume(cylinder_radius, cylinder_height):.2f}cm\u00b3")


#44. Write a  Python program to print the index of a character in a string.
my_string = input("Enter your string: ")


for i in range(len(my_string)):
   print(f"Current character {my_string[i]} position at {i}")


#45. Write a  Python program to check whether a string contains all letters of the alphabet.
def contains_all_alphabet(s):
   letters = set(ch.lower() for ch in s if ch.isalpha())
   return len(letters) == 26


my_string = input("Enter your string: ")
if (contains_all_alphabet(my_string)):
   print("YES")
else:
   print("NO")


#46. Write a Python program to convert a given string into a list of words. Sample Output:
my_string = input("Enter your string: ")
words = my_string.split(" ")
print(words)


#47. Write a  Python program to lowercase the first n characters in a string.
def to_lower_first_n_chars(s, n):
   return s[:n].lower() + s[n:]




my_string = input("Enter your string: ")
n = int(input("Enter the number of first characters you want to convert to lowercase: "))


print(to_lower_first_n_chars(my_string, n))


#48. Write a Python program to swap commas and dots in a string.
def swap_commas_dots(s):
   s = s.replace(",", "#")
   s = s.replace(".", ",")
   s = s.replace("#", ".")
   return s;


my_string = input("Enter your string: ")
print(swap_commas_dots(my_string))


#49. Write a Python program to count and display vowels in text.
def vowels_count(s):
   vowels = {"a":0, "e":0, "i":0, "u":0, "o":0}
   for c in s:
       if c in vowels:
           vowels[c] += 1


   for c in vowels:
       if vowels[c] > 0:
           print(f"{c} {vowels[c]}")




my_string = input("Enter your string: ")
vowels_count(my_string)


#50. Write a Python program to split a string on the last occurrence of the delimiter.
def split_on_last_occurrence(text, delimiter):
   # rsplit splits from the right side
   parts = text.rsplit(delimiter, 1)
   return parts


# Example usage
string = "apple-orange-banana-mango"
delimiter = "-"
result = split_on_last_occurrence(string, delimiter)


print("Original string:", string)

