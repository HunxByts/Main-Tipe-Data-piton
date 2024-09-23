#!/usr/bin/python
import sys

# pejumlahan = angka_1 + angka_2
# pengurangan  = angka_1 - angka_2
# perkalian = angka_1 * angka_2
# pembagian = angka_1 / angka_2 # di perbaiki untuk menghasilkan nilai desimal bukan menggunakan //
# pangkat = angka_1 ** angka_2

# maxnum = max(angka_1, angka_2)
# minnum = min(angka_1, angka_2)
# pembagian_rounded = round(pembagian, 2)

# print(pengurangan)
# print(pengurangan)
# print(pembagian)
# print(perkalian)
# print(pangkat)
# print(maxnum)
# print(minnum)
# print(pembagian_rounded)


def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

def pangkat(x, y):
    return x ** y


# Menentukan angka max dan minium coyy
def maxangka(x, y):
    return max(x, y)

def minangka(x, y):
    return min(x, y)

print("""

====[] PILIH MENU BERIKUT COYY ====[] 
        []==== CODE BY K1LLU ===[]

1] Penjumlahan
2] Pengurangan 
3] Perkalian 
4] Pembagian
5] Pangkat
6] Maxium angka
7] Minium angka
8] Tampilkan semua 
""")

try:
    pilihmana = int(input("Masukan pilihan mu : "))
except ValueError:
    print("[+] Woy, masukin yang bener kocak!!")
sys.exit()

if pilihmana == 1:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Penjumlahan : {penjumlahan(angka_1, angka_2)}")
elif pilihmana == 2:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Pengurangan : {pengurangan(angka_1, angka_2)}")
elif pilihmana == 3:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Perkalian : {perkalian(angka_1, angka_2)}")
elif pilihmana == 4:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Pembagian : {pembagian(angka_1, angka_2)}")
elif pilihmana == 5:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Pangkat : {pangkat(angka_1, angka_2)}")
elif pilihmana == 6:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Maxium Angka : {maxangka(angka_1, angka_2)}")
elif pilihmana == 7:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Minium Angka : {minangka(angka_1, angka_2)}")
elif pilihmana == 8:
    angka_1 = float(input("[+] Masukan angka pertama : "))
    angka_2 = float(input("[+] Masukan angka kedua : "))
    print(f"[+] Hasil dari Penjumlahan : {penjumlahan(angka_1, angka_2)}")
    print(f"[+] Hasil dari Pengurangan : {pengurangan(angka_1, angka_2)}")
    print(f"[+] Hasil dari Perkalian   : {perkalian(angka_1, angka_2)}")
    print(f"[+] Hasil dari Pembagian   : {pembagian(angka_1, angka_2)}")
    print(f"[+] Hasil dari Pangkat     : {pangkat(angka_1, angka_2)}")
    print(f"[+] Hasil dari Maxium Angka : {maxangka(angka_1, angka_2)}")
    print(f"[+] Hasil dari Minium Angka : {minangka(angka_1, angka_2)}")
else:
    print("[+] Gada menu yang lo pilih kocak!!")