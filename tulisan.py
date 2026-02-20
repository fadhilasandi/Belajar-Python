print("Dune dari Frank Herbert")
print('Warhammer 40K')

#Kutip di dalam kutip
print("Pemimpin Utama dari Ultramarines adalah 'Roboute Guilliman'")

#memasukkan String ke variabel
a = "House of Harkonnen"
print(a)

#Kalimat ganda
b = """Pada Millenium ke 31- Kaisar memberikan gelar Kepala Perang
kepada Horus Lupercal dari Luna Wolves (yang selanjutnya menjadi Sons of Horus)
yang merupakan putra terfavoritnya"""
print(b)

#String ke Array
c = "Astra Militarum"
print(c[4])

#String Loop
for d in "Astartes":
    print(d)

#panjang String
e = "Ultramarines"
print(len(e))

#Cek String
teks = "Blood Angels"
print("Angels" in teks)

tex = "Iron Hands"
if "Iron" in tex:
    print("Ya, Iron ada di dalam teks ini.")

#cek IF NOT
f = "Salamanders"
print("Ironside" not in f)

g = "Space Wolves"
if "Ragnarsson" not in g:
    print("Tidak ada kata Ragnarsson di dalam kalimat ini.")