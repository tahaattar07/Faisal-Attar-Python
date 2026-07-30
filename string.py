#Write a program to input a string and display its length without using the len() function.
s = input("Enter a String:")
count = 0
for ch in s:
    count += 1
print("Length:", count)
print()

#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
s = input("Enter a String:")
vowels = constants = special = digits = spaces = 0

for ch in s:
    if ch in "AEIOUaeiou":
        vowels += 1
    elif ch.isalpha():
        constants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
        
print("Vowels:",vowels)
print("Constants:",constants)
print("Digits:",digits)
print("Spaces:",spaces)
print("Special:",special)
print()

#Reverse the given string without using built-in reverse functions.
s = input("Enter a string:")
rev = ""
for ch in s:
    rev = ch + rev
print("Revserse:",rev)

#Check whether the entered string is a palindrome
s = input("Enter a String:")

rev =""
for ch in s:
    rev = ch + rev
if s==rev:
    print("Pallidrome")
else:
    print("Not a Pallidrome")
print()

#Uppercase and Lowercase Count 
s = input("Enter a String:")

upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    else:
        lower += 1
print("Uppercase:",upper)
print("Lowercase:",lower)
print()

#6.	Replace Characters 
s = input("Enter a string:")
old = input("Enter the char to be replace:")
new = input("Enter new Character:")

result = ""

for ch in s:
    if ch == old:
        result = result + new
    else:
        result = result + ch
print(result)
print()

#7.	 Remove Spaces 
s = input("Enter a string:")

result = ""

for ch in s:
    if ch != " ":
        result += ch
print(result)
print()

#8. Frequency of a Character
s = input("Enter a string: ")
ch = input("Enter a char:")

count = 0

for c in s:
    if c == ch:
        count += 1
print(count)
print()

#9. First and Last Character
s = input("Enter a string: ")
if s != "":
    print("First Character:", s[0])
    print("Last Character:", s[-1])
else:
    print("Empty String")
print()

#10. ASCII Values
s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))
print()

#11. Word Count
s = input("Enter a sentence: ")
words = s.split()
print("Total Words =", len(words))
print()

#12. Longest Word
s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)
print()

#13. Shortest Word
s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word:", shortest)
print()

#14. Title Case
s = input("Enter a sentence: ")
print(s.title())
print()

#15. Duplicate Characters
s = input("Enter a string: ")
printed = "" 
for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch
print()

#16. Character Frequency
s = input("Enter a string: ")

done = ""

for ch in s:
    if ch not in done:
        print(ch, "=", s.count(ch))
        done += ch
print()

#17. Anagram Check
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#18. Remove Duplicate Characters
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

#19. Substring Search
s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring Found")
else:
    print("Substring Not Found")

#20. Count Occurrences of a Word
sentence = input("Enter sentence: ")
word = input("Enter word: ")

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences =", count)

#21. Password Validator
password = input("Enter Password: ")

upper = lower = digit = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")

#22. Run-Length Encoding
s = input("Enter string: ")

result = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)

#23. String Compression
s = input("Enter string: ")

result = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

if len(result) < len(s):
    print(result)
else:
    print(s)

#24. Most Frequent Character
s = input("Enter string: ")

max_char = ""
max_count = 0

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print(max_char, "=", max_count)

#25. Second Most Frequent Character
s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_freq) >= 2:
    print(sorted_freq[1])
else:
    print("No second frequent character")

#26. Caesar Cipher
text = input("Enter text: ")
shift = int(input("Enter shift: "))

result = ""

for ch in text:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch)-start+shift)%26+start)
    else:
        result += ch

print("Encrypted:", result)

#. Email Validator
email = input("Enter Email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")

#28. Word Frequency Dictionary
text = input("Enter paragraph: ")

words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for key, value in freq.items():
    print(key, ":", value)

#29. Sentence Reversal
sentence = input("Enter sentence: ")

words = sentence.split()

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")

#30. String Rotation
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")