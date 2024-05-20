class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self): #override
        self.kecepatan += 20

    def super_tambah_kecepatan(self): #super
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "AlxCar", 160)
print(mobil_1.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Hitam", "AlxSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)
mobil_sport_1.super_tambah_kecepatan()
print(mobil_sport_1.kecepatan)

# Override
# when we create a new method in the child class (new class) with the same name as the method in the parent class, it will cause the new method to override the method of the parent class.

