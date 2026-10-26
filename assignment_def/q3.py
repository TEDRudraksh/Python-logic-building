
def character_count():
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
    return vc,cc,sc

result = character_count()
print(result)
