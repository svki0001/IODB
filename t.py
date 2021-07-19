s = set()

a = "abc"
b = "def"
c = "ghi"

s.add(a)
s.add(b)
s.add(c)

print(a in s)

xy = "XY"
z = xy.lower()
print(z)


print(f"{42:04d}")

from unidecode import unidecode
print(type(unidecode("text")))