string = input("write your string : ")
length = 0
lowercase = string.lower()

for c in string:
    length += 1
print(length)

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
    counts = vowel_counts.values()
    total_vowels = sum(counts)
print(total_vowels)