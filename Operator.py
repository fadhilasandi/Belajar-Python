#Aritmatika
a = 16
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

#Operator Penugasan
#Walrus
nomor = [2, 3, 4, 5, 6]
hitung = len(nomor)
if hitung > 4:
    print(f"List punya {hitung} elemen")

if (hitung := len(nomor)) > 4:
    print(f"List punya {hitung} elemen")

#Operator Perbandingan
c = 6
d = 4

print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)

#Chain Comparisons
e = 6
print(1 < e < 11)

print(1 < e and e < 11)

#Logical Comparison
f = 6
print(f < 6 or f > 11)
print (f > 1 and f < 11)
print(not(f > 4 and f < 11))

#Identity Operators
#Is True
g = {"Taekwondo", "Hapkido"}
h = {"Taekwondo", "Hapkido"}
i = "Karate"

print(g is i)
print(g is h)
print( g == h)

#Is Not True
g = {"Taekwondo", "Hapkido"}
h = {"Taekwondo", "Hapkido"}

print(g is not h)
#Is jika poin variabel memiliki objek yang sama dalam memori
#== jika nilai dari kedua variabel tersebut sama
