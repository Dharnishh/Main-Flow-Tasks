def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
is_anagram = check_anagram(str1, str2)
print(f"Are '{str1}' and '{str2}' anagrams? {is_anagram}")
