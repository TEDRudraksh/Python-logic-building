def count():   
    s = "ABCEDeen nndeednnnd ##"

    uc = lc = sc = dc = 0

    for ch in s:
        asciii = ord(ch)
        if asciii >= 65 and asciii<=90:
            uc+=1
        elif asciii>=97 and asciii<=122:
            lc+=1
        elif asciii>=48 and asciii<=57:
            dc+=1
        else:
            sc+=1
    return uc,lc,dc,sc

result = count()
print(result)