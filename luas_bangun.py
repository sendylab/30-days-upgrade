print("Selamat datang di Program menghitung luas !!!")
print("\nSilakan pilih dulu bangun ruang yang mau anda hitung")
print("1. Persegi \n2. Persegi Panjang \n3. Lingkaran")

menu = input("\nanda mau nomor berapa? ")

if menu == '1':
    sisi = int(input("Berapa sisi nya? "))
    Luas = sisi**2
    print(f"Luas persegi anda adalah {Luas}")
elif menu == '2':
    P = int(input("Berapa panjang nya? "))
    L = int(input("Berapa lebar nya? "))
    Luas = P * L
    print(f"Luas persegi panjang anda adalah {Luas}")
elif menu == '3':
    pi = 3.14
    r = int(input("Berapa jari-jari nya? "))
    Luas = pi * r**2
    print(f"Luas lingkaran anda adalah {Luas}")