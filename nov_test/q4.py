# Q4. String Compression

# Write a program to compress a string by replacing consecutive repeated characters with the character followed by its frequency.
# Input: aaabbccccdaa

# Output: a3b2c4d1a2


s = "aaabbccccdaa"
r = ""
c = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        c+=1

    else: 
        r+= s[i] + str(c)
        c=1
r+= s[i] + str(c)

print(r)    


