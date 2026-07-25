name = "kirthi"
vowels = "aeiou"

# Task 1: Count vowels
count = 0
for i in name:
    if i in vowels:
        count = count + 1

print(f"{count} vowels found")


non_vowel =""
for i in name:
    if i not in vowels:
        non_vowel = non_vowel + i 


print(f"{non_vowel} non-vowels found")
