# operator matematika phyton (Contoh pakai 3 dan 2) :
# penambahan    : 3 + 2     = 5
# pengurangan   : 3 - 2     = 1
# perkalian     : 3 * 2     = 6
# pembagian     : 3 / 2     = 1.5 (kalau pakai python 3)
# Fungsi tangga : 3 // 2    = 1 (komanya dihilangin)
# Eksponen      : 3 ** 2    = 9 (pangkat)
# Modulus       : 3 % 2     (untuk nentuin ganjil genap (hasil 0 genap, 1 ganjil))
# tanda kurung digunakan untuk mengubah urutan operasi matematika

# operator persamaan (Contoh pakai 3 dan 2) :
# Sama dengan                   : 3 == 2    = False
# Tidak sama dengan             : 3 != 2    = True
# Lebih besar dari              : 3 > 2     = True
# Lebih kecil dari              : 3 < 2     = False
# Lebih besar atau sama dengan  : 3 >= 2    = True
# Lebih kecil atau sama dengan  : 3 <= 2    = False
# hasilnya adalah boolean (nilai benar atau salah)

from math import *
num = 5
print(str(num)) #untuk mengubah jadi string
print(abs(-5)) # memberikan value absolut
print(pow(3,3)) # untuk mempangkat (Contoh 3^3)
print(max(3, 9)) # mengeprint angka yang lebih besar
print(min(3, 9)) # mengeprint angka yang lebih kecil
print(round(3.57495627)) # membulatkan angka
print(floor(3.798)) # membulatkan angka selalu kebawah
print(ceil(3.23)) # membulatkan angka selalu keatas
print(sqrt(9)) # Mengakar angka