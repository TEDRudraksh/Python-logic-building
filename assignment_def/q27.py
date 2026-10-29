# 27. Find all duplicate characters and their frequencies.

def dup_chr_freq():
    s = "sknajsfafnajsdssfjbfe"

    result = {}
    temp = {}
    for i in s:
        if i in result:
            result[i]+=1
        else:
            result[i] = 1

    for key,value in result.items():
        if value>=2:
            temp[key] = value

    return temp

result = dup_chr_freq()
print(result)