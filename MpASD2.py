class PipinStore:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AdminPipinStore:
    def __init__(self):
        self.head = None

    def ingpo_stok(self):
        print("List Diamond Ready :")
        current = self.head
        while current:
            print(f"{current.data.name}. {current.data.name} : Rp {current.data.price}")
            current = current.next

    def tambah_amount_depan(self, name, price):
        new_node = Node(PipinStore(name, price))
        new_node.next = self.head
        self.head = new_node
        print(f"{name} harganya Rp {price} paling depan yahh.")

    def tambah_amount_blakang(self, name, price):
        new_node = Node(PipinStore(name, price))
        if not self.head:
            self.head = new_node

            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{name} harganya Rp {price} paling blakang yahh.")

    def tambah_amount_pilih(self, tempat, name, price):
        if tempat < 1:
            print("Yang bener plis.")
            return
        if tempat == 1:
            self.tambah_amount_depan(name,price)
            return
        new_node = Node(PipinStore(name,price))
        current = self.head
        count = 1
        while current and count < tempat - 1:
            current = current.next
            count += 1
        if not current:
            print("Ga sampe sgitu list nya :).")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"{name} harganya Rp {price} di urutan {tempat} yahh.")

    def hapus_amount_depan(self):
        if not self.head:
            print("Kosong banh.")
            return
        self.head = self.head.next
        print("Yang paling depan dah tehapus.")

    def hapus_amount_blakang(self):
        if not self.head:
            print("Kosong banh.")
            return
        if not self.head.next:
            self.head = None
            print("Yang paling blakang dah tehapus.")
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        print("Yang paling blakang dah tehapus.")

    def hapus_amount_pilih(self, tempat):
        if tempat < 1:
            print("Kosong banh.")
            return
        if tempat == 1:
            self.hapus_amount_depan()
            return
        current = self.head
        count = 1
        while current and count < tempat - 1:
            current = current.next
            count += 1
        if not current or not current.next:
            print("Ga sampe sgitu banh.")
            return
        current.next = current.next.next
        print(f"Yang nomor {tempat} dah tehapus.")

    def update_harga(self, list_amount, harga_baru):
        current = self.head
        found = False
        while current:
            if current.data.name == list_amount:
                current.data.price = harga_baru
                print(f"Harga {current.data.name} diganti jadi Rp {harga_baru} yahh.")
                found = True
                break
            current = current.next
        if not found:
            print("Gaada pilihannya banh.")

if __name__ == "__main__":
    admin = AdminPipinStore()

    while True:
        print("-"*50)
        print("Mau Ngapain Nihh? \n")
        print("1. Cek List Diamond Ready")
        print("2. Tambah Amount (Depan)")
        print("3. Tambah Amount (Blakang)")
        print("4. Tambah Amount (Pilih)")
        print("5. Update Harga Diamond")
        print("6. Hapus Amount (Depan)")
        print("7. Hapus Amount (Blakang)")
        print("8. Hapus Amount (Pilih)")
        print("9. Keluar Ajah")
        print("-"*50)

        choice = input("Masukkan pilihan loe : ")
        print("-"*50)

        if choice == "1":
            admin.ingpo_stok()
        elif choice == "2":
            name = input("Masukkan Amount Baru : ")
            price = int(input("Masukkan Harga : "))
            admin.tambah_amount_depan(name, price)
        elif choice == "3":
            name = input("Masukkan Amount Baru : ")
            price = int(input("Masukkan Harga : "))
            admin.tambah_amount_blakang(name, price)
        elif choice == "4":
            tempat = int(input("Urutan Ke-"))
            name = input("Masukkan Amount Baru : ")
            price = int(input("Masukkan Harga : "))
            admin.tambah_amount_pilih(tempat, name, price)
        elif choice == "5":
            list_amount = input("Nama Diamond yang Mau Diupdate : ")
            harga_baru = int(input("Masukkan Harga Baru : "))
            admin.update_harga(list_amount, harga_baru)
        elif choice == "6":
            admin.hapus_amount_depan()
        elif choice == "7":
            admin.hapus_amount_blakang()
        elif choice == "8":
            tempat = int(input("Hapus Urutan Ke-"))
            admin.hapus_amount_pilih(tempat)
        elif choice == "9":
            print("Makasi Yahh :D.")
            print("-"*50)
            break
        else:
            print("Gaada pilihannya banh.\n") 