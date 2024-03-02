#task 3

# Input angka dari user
number = int(input("masukkan angka: "))

# cek apakah angka dibawah 100, diantara 100 dan 200, atau diatas 200
if number < 100:
    print("Kecil")
elif number <= 200:
    print("Sedang")
else:
    print("Besar")

