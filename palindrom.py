a = input("Введите строку: ").lower()

b = []
b.extend(a)

for i in b:
    if ':' in b:
        b.remove(':')
    elif "\\" in b:
        b.remove("\\")
    elif "," in b:
        b.remove(',')
    elif "'" in b:
        b.remove("'")
    elif "." in b:
        b.remove(".")
    elif ";" in b:
        b.remove(';')
    elif " " in b:
        b.remove(" ")
    else:
        break

d = ''.join(b)
b.reverse()
c = ''.join(b)

if c == d:
    print(f"Ваше слово <{a}> палиндром!")
else:
    print(f"Ваше слово <{a}> не палиндром!")
