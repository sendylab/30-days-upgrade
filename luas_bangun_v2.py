# Day 1 - Area Calculator Upgrade

import math
import os

def c():
    os.system('cls' if os.name == 'nt' else 'clear')

def persegi():
    try:
        sisi = float(input("Berapa sisi nya? "))
        luas = sisi**2
        print(f"luas persegi anda adalah {luas}")
    except ValueError:
        print("Sisi harus berupa angka!!")

def persegi_panjang():
    try:
        panjang = float(input("Berapa panjang nya? "))
        lebar = float(input("Berapa lebar nya? "))
        luas = panjang * lebar
        print(f"luas persegi panjang anda adalah {luas}")
    except ValueError:
        print("panjang dan lebar harus berupa angka!!")

def lingkaran():
    try:
        r = float(input("Berapa jari-jari nya? "))
        luas = math.pi * r**2
        print(f"luas lingkaran anda adalah {luas}")
    except ValueError:
        print("jari-jari harus berupa angka!!")

def segitiga():
    try:
        alas = float(input("Berapa alas nya? "))
        tinggi = float(input("Berapa tinggi nya? "))
        luas = alas * tinggi / 2
        print(f"luas segitiga anda adalah {luas}")
    except ValueError:
        print("alas dan tinggi harus berupa angka!!")

print("Selamat datang di Program menghitung luas !!!")
print("\nSilakan pilih dulu bangun datar yang mau anda hitung")

while True:
    print("1. Persegi \n2. Persegi Panjang \n3. Lingkaran \n4. Segitiga")
    menu = input("\nanda mau nomor berapa? ")

    if menu == '1':
        persegi()
    elif menu == '2':
        persegi_panjang()
    elif menu == '3':
        lingkaran()
    elif menu == '4':
        segitiga()
    else:
        print("Pilihan tidak tersedia, silakan jalankan ulang program")
    
    tanya = input("apakah anda ingin menghitung lagi? (y/n) ")
    c()
    if tanya.lower != 'y':
        break