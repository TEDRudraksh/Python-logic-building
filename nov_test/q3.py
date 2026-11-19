# Q3. Longest Palindromic Substring

# Write a program to find the longest palindromic substring in a given string.
# Input: babad
# Output: bab


# Note: aba is also a valid answer.


s = "babad"
r = ""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        string = s[i:j]
        if string==string[::-1]:
            if len(string)>len(r):
                r = string

print(r)




