#Task 5

# inisialisasi total sebagai peyimpan value inputan
total = 0

# buat kondisi berakhir apabila -1 dimasukkan
while True:
    angka = int(input("masukkan angka (masukkan -1 untuk mengakhiri): "))
    if angka == -1:
        break
    total += angka

# print hasil
print("Jumlah dari seluruh angka yang dimasukkan:", total)

