# Fungsi untuk mencari nilai faktorial dari suatu bilangan
def faktorial(bilangan):
    if (bilangan == 1 or bilangan == 2):
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

    for x in range(1, bilangan+1):
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
