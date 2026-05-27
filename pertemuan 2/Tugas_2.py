class universitas:
    nama = ""
    daerah = ""
    
    def perkenalan(self):
        print(f"Selamat datang di {self.nama} yang berada di {self.daerah}")

    def muqaddimah(self, nama):
        print(f"Hallo {nama}! Selamat datang di {self.nama} yang berada di daerah {self.daerah}")

class Mahasiswa:
    pass

kampusA = universitas()
kampusB = universitas()

print(kampusA)
print(kampusB)

Mahasiswa1 = Mahasiswa()
Mahasiswa1.nama = "Arfarizqhi Akbar"
Mahasiswa1.prodi = "Teknik Informatika"
Mahasiswa1.nim = "462025611013" 

Mahasiswa2 = Mahasiswa()
Mahasiswa2.nama = "Dias Rizky"
Mahasiswa2.prodi = "Teknik Informatika"
Mahasiswa2.nim = "462025611054" 

print(Mahasiswa1.nama)
print(Mahasiswa1.prodi)
print(Mahasiswa1.nim)

print(Mahasiswa2.nama)
print(Mahasiswa2.prodi)
print(Mahasiswa2.nim)

kampusA.nama = "UNIDA Gontor"
kampusA.daerah = "Siman"

kampusB.nama = "UNIDA Gontor"
kampusB.daerah = "Robitoh"

print(kampusA.nama)
print(kampusA.daerah)
print(kampusB.nama)
print(kampusB.daerah)

kampus= universitas()
kampus.nama = kampusB.nama
kampus.daerah = kampusB.daerah
kampus.perkenalan()

informasi= universitas()
informasi.nama = "Universitas Darussalam Gontor"
informasi.daerah = "Siman, Ponorogo"
informasi.muqaddimah("Arfarizqhi")