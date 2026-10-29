# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

def long():
    s = "babad"
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                if len(sub) > len(longest):
                    longest = sub

    return longest

result = long()
print(result)