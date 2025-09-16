text = input()

vowel_values = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

sum_vowels = 0

for char in text:
    if char in vowel_values:
        sum_vowels += vowel_values[char]

print(sum_vowels)
