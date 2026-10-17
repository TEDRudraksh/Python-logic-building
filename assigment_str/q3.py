# 3. Count the number of vowels and consonants in a string.

s = "aeiourudraksheefndsf  "
sett = {'a','e','i','o','u','A','E','I','O','U'}

vc = cc = sc = 0

for ch in s:
    if ch in sett:
        vc+=1
    elif ch not in sett and ch.isalpha():
        cc+=1
    else:
        sc+=1
print("vowel",{vc},"consonants",{cc},"special char",{sc})