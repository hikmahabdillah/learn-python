class Student:
  # name = "Hikmah"
  # classs = "TI-1F"

  # default constructor
  # def __init__(self):
  #   self.name = 'Hikmah'
  #   self.classs = "TI-1F"
  
  # parameter constructor
  def __init__(self, name, classs):
     self.name = name
     self.classs = classs

# student1 = Student()
# print(student1.name, student1.classs)

# student2 = Student()
# student2.name = "Aldrin"
# print(student2.name, student2.classs)

# student3 = Student()
# student3.name = "Eric"
# student3.classs = "TI-1D"
# print(student3.name, student3.classs)

student4 = Student("Abdillah", "TI-1F")
print(student4.name, student4.classs)

# METHOD

# object method
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

    # static method
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")

    @classmethod
    def introcls_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.introcls_mobil()
mobil_1 = Mobil("white","AldrinCar", 180)
mobil_1.introcls_mobil()

Mobil.intro_mobil()
mobil_1 = Mobil("white","AldrinCar", 180)
mobil_1.intro_mobil()

# call object method
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print("Sebelum ditambahkan: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ")
print(mobil_1.kecepatan)