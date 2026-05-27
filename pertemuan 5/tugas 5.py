class AkunGame:

    def __init__(self, username, password, id_player):
        self.__username = username
        self.__password = password
        self.__id_player = id_player
        self.__diamond = 0

    def get_username(self):
        return self.__username

    def get_id_player(self, password):
        if password == self.__password:
            return self.__id_player
        else:
            return "Password salah! ID pemain tidak dapat diakses."

    def get_diamond(self, password):
        if password == self.__password:
            return self.__diamond
        else:
            return "Password salah! Diamond tidak dapat diakses."

    def tambah_diamond(self, jumlah):
        self.__diamond += jumlah
        print(f"Diamond berhasil ditambahkan sebanyak {jumlah}")

    def beli_item(self, password, harga_item):
        if password == self.__password:
            if harga_item <= self.__diamond:
                self.__diamond -= harga_item
                print(f"Item berhasil dibeli seharga {harga_item} diamond")
            else:
                print("Diamond tidak mencukupi!")
        else:
            print("Password salah! Pembelian gagal.")

    def ubah_password(self, password_lama, password_baru):
        if password_lama == self.__password:
            self.__password = password_baru
            print("Password berhasil diubah.")
        else:
            print("Password lama salah!")

akun1 = AkunGame("rizqi", "abc123", "ID9999")

print("Username :", akun1.get_username())

akun1.tambah_diamond(500)

print("Diamond :", akun1.get_diamond("salah"))

print("Diamond :", akun1.get_diamond("abc123"))

akun1.beli_item("12345", 100)

akun1.beli_item("abc123", 100)

print("Diamond Sekarang :", akun1.get_diamond("abc123"))

akun1.ubah_password("abc123", "321cba")

print("ID Pemain :", akun1.get_id_player("321cba"))