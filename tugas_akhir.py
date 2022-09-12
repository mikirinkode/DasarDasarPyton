# Fungsi untuk mencari nilai faktorial dari suatu bilangan
# Untuk mencari hasilnya digunakan fungsi rekursif
"""
contoh 4! = 4 * faktorial(4-1)
          = 4 * (3 * faktorial(3-1))
          = 4 * (3 * (2 * faktorial(2-1)))
          = 4 * (3 * (2 * 1))
          = 4 * (3 * 2)
          = 4 * 6
          = 24
"""
def faktorial(bilangan):
    if (bilangan == 0):
        return 1
    elif (bilangan == 1 or bilangan == 2):
        return bilangan
    else:
        return bilangan*faktorial(bilangan-1)

def menuFaktorial():
    print("\n#1 Mencari nilai Faktorial dari suatu bilangan")
    bilangan = int(input("Masukkan bilangan = "))
    print(str(bilangan) + "! = ", end="")
    print(faktorial(bilangan))

# fungsi untuk mencari faktor bilangan
def faktorBilangan(bilangan):
    result = []
    for x in range(1, bilangan + 1):
        # jika bilangan dibagi dengan x dan menghasilkan sisa bagi == 0,
        # maka x merupakan faktor dari bilangan dan tambahkan x ke dalam list
        if (bilangan %x == 0):
            result.append(x)

    return result

def menuFaktorBilangan():
    print("\n#2 Mencari nilai Faktor Bilangan")
    bilangan = int(input("Masukkan bilangan = "))
    print("Faktor Bilangan " + str(bilangan) + " adalah " + str(faktorBilangan(bilangan)))
        

while (True):
    print("\n== Program Tugas Akhir Dasar-Dasar Python ==")
    print("1. Mencari nilai Faktorial")
    print("2. Mencari Faktor Bilangan")
    print("3. Keluar Program")
    pilihanUser = int(input("Pilihan anda [1-3] = "))
    if (pilihanUser == 1):
        menuFaktorial()
    elif (pilihanUser == 2):
        menuFaktorBilangan()
    elif (pilihanUser == 3):
        print("Program Berakhir.")
        break
    else:
        print("Input tidak Valid.")
