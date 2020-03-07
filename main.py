print("Hello World")
nama = 'Eko'
print(nama)
usia = 60
print(usia)

#usia = 'empat puluh'
#print(usia)

if usia <= 40:
    print('Msih muda')
    print('Semangat kerja')
elif usia > 40 and usia <= 50:
    print('Tua')
    print('Ibadah')
else:
    print('Tobat')

usia = 5
for u in range(1, usia + 1):
    print('Ulang tahun ke', u)

hari = [] #tipe data array atau list
hari.append('Minggu')
hari.append('Senin')
hari.append('Selasa')
hari.append('Rabu')
hari.append('Kamis')
hari.append('Jumat')
hari.append('Sabtu')
hari.append('Sabgu')

print(hari[0])
print('Panjang hari', len(hari))
print(hari[len(hari) - 1])

for h in hari:
    print(h)

luas_alas = 40
tinggi = 3
luas_segitiga = luas_alas * tinggi / 2
print(luas_segitiga)

luas_alas = 60
tinggi = 3
luas_segitiga = luas_alas * tinggi / 2
print(luas_segitiga)

def hitung_luas_segitiga(luas_alas, tinggi):
    return luas_alas * tinggi / 2

print(hitung_luas_segitiga(90, 3))
print(hitung_luas_segitiga(45, 7))

# NEXT: CLASS, PACKAGE. Googling yaks!
