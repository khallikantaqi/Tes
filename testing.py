'''
=================================================
Graded Challenge 1

Nama  : Khallikan Taqi Harits
Batch : RMT-53

Program ini dibuat untuk memberikan experience untuk berbelanja,
dimana user dapat menambahkan berbagai barang (items) ke dalam 
tas belanjaannya (ShoppingCart) sehingga nantinya user dapat melihat
apa saja hasil belanjaannya.
=================================================
'''
# (1) Variabel
# title = Shopping_Cart

# (2) Class dan Function
class CartItem:
    def __init__(self, nama_barang, harga_barang):
        self.nama_barang = nama_barang
        self.harga_barang = harga_barang


class ShoppingCart:
    def __init__(self):
        self.items = []

    def tambah_barang(self):
        print("Masukkan nama barang:", end=" ")
        nama = input()

        print("Masukkan harga barang:", end=" ")
        harga = float(input())

        barang = CartItem(nama, harga)
        self.items.append(barang)

        print(f'Barang "{nama}" berhasil dimasukkan.')

    def hapus_barang(self):
        print("Masukkan nama barang yang ingin dihapus:", end=" ")
        nama = input()

        ditemukan = False
        for barang in self.items:
            if barang.nama_barang == nama:
                self.items.remove(barang)
                ditemukan = True
                break

        if ditemukan:
            print(f'Barang "{nama}" berhasil dihapus.')
        else:
            print("Barang tidak ditemukan.")

    def tampilkan_barang(self):
        if len(self.items) == 0:
            print("Keranjang kosong.")
        else:
            print("Barang di Keranjang:")
            index = 1
            for barang in self.items:
                print(f"{index}. {barang.nama_barang} - Rp {barang.harga_barang}")
                index += 1

    def hitung_total(self):
        total = 0
        for barang in self.items:
            total += barang.harga_barang
        return total

    def tampilkan_menu(self):
        print("\n==============================")
        print("Keranjang Belanja Toko Makmur")
        print("==============================")
        print("1. Menambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Lihat Total Belanja")
        print("5. Exit")
        return input("Pilihan: ")

# (3) Runner 
cart = ShoppingCart()

while True:
    pilihan = cart.tampilkan_menu()

    if pilihan == "1":
        cart.tambah_barang()

    elif pilihan == "2":
        cart.hapus_barang()

    elif pilihan == "3":
        cart.tampilkan_barang()

    elif pilihan == "4":
        total = cart.hitung_total()
        print(f"Total belanja: Rp {total}")

    elif pilihan == "5":
        print("Terima kasih sudah belanja.")
        break

    else:
        print("Pilihan tidak valid.")