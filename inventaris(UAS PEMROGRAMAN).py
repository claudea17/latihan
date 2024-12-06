
#program pendataan inventaris buku perpustakaan

import os
def layarbersih(msg):
    input(msg)
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def mainMenu(x):
    if x == "1":
       readali()

    elif x == "2":
        judul = input("masukkan judul buku:")
        create(judul)

    elif x == "3":
        judul = input("input yang dicari:")
        readone(judul)

    elif x == "4":
        judul = input("input judul yang dicari:")
        delete(judul)

    elif x == "5":
        print("program syuting down...")


    else:
        print("option not found.")

#option 2 menambahkan data buku baru

def create(judul):
    buku.append(judul)
    layarbersih("data berhasil ditambahkan,tekan enter untuk melanjutkan...")

#option 1 menambahkan seluruh data buku
def readali():
    print("daftar buku :")
    no = 1
    for item in buku:
        print(str(no),", ",item)
        no += 1
    layarbersih("press any key to continue...")

#option 3 mencari data buku
def readone(judul):
    filter_object = filter(lambda a: judul.lower() in a.lower(),buku )
    p = list(filter_object)
    if(not p):
        layarbersih("data tidak ditemukan.....")
    else:
        print("buku berjudul '" + ",".join(p) + "' berhasil ditemukan")

#options 4 menghapus data buku
def delete(judul):
    if  buku.count(judul)  >= 1:
        buku.remove(judul)
        layarbersih ("buku berhasil dihapus. press any key to continue...")
    else:
        layarbersih("buku tidak ditemukan. harap menetik secara detail untuk keamanan.")
    

#main functiont
buku = ["malin kundang", "bawang merah dan bawang putih", "danau toba", "habis gelap terbitlah terang"]

x = "0"
while x != "s":
    print("program pendataan inventaris buku perpustakaan")
    print("(1) tampilkan semua data buku")
    print("(2) tambahkan data buku")
    print("(3) cari data buku")
    print("(4) hapus data buku")
    print("(5)exit")
    print()

    x = input("pilihan  :  ")  #mengambil input dari pengguna
    mainMenu(x)
