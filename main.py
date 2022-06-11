class Mobil:
    def __init__(self,merk, harga):
        self.merk = merk
        self.__harga = harga
    def harga (self):
        harga = self.__harga
        return harga
    def melaju(self):
        return "Mobil ini sedang melaju"



mobil1 = Mobil("Hyundai", 5000000000)

print(mobil1.merk)
print(mobil1.harga())
print(mobil1.melaju())

class Angka:
  def __init__(self, angka):
    self.angka = angka

  def __add__(self, objek):
    return Angka(
      self.angka + objek.angka
    )

x1 = Angka(5)
x2 = Angka(20)
x3 = x1 + x2

print(x3.angka)


# Belajar Encapsulation

class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon


class Karyawan:
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.total_pendapatan = pendapatan
        self.__bonus = 2000000
    def target(self):
        self.total_pendapatan += self.__bonus
    def proyek(self, insentif_proyek):
        self.total_pendapatan += 0.1*insentif_proyek

rindu = Karyawan("Rindu", 30, 5000000)
rindu.target()
rindu.proyek(1000000)
print(rindu.total_pendapatan)



# Belajar Inheritance
class Karyawan:
    def __init__(self, nama, usia, jenis_kelamin):
        self._nama = nama
        self.__usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.total_pendapatan = 0
        self._bonus = 2000000
    def pendapatan(self, pendapatan):
        self.total_pendapatan += pendapatan

class Customer_service(Karyawan):
    def __init__(self, nama, usia, jenis_kelamin):
        super().__init__(nama, usia, jenis_kelamin)
    def target(self):
        self.total_pendapatan += self._bonus


arin = Customer_service("Arin", 23, "Perempuan")
arin.pendapatan(3000000)
arin.target()
print(arin.total_pendapatan)


# BELAJAR POLYMORPHISM
# class 



class Kendaraan:
    def jalan():
        print ("Berjalan")