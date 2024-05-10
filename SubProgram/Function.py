def countHitungVolumeBalok(panjang,lebar, tinggi):
    volume_balok = panjang*lebar*tinggi
    return volume_balok

balok_pertama = countHitungVolumeBalok(5,10,4)
print(balok_pertama)

balok_kedua = countHitungVolumeBalok(4,15,8)
print(balok_kedua)

# Positional-or-Keyword
def greeting(name, message):
    return "Halo " + name + "! ," + message

print(greeting("Aldrin", "Keep Going!"))
print(greeting(message="Keep Smile! ", name="Abdillah"))

# Var-Positional (Variadic Positional Parameter)
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(4, 2, 1, 3))

# Var-Keyword (Variadic Keyword Parameter)
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(name="Hikmah Aldrin Abdillah", age="19", job="Front End Developer"))

# function expression
count_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(count_luas_persegi_panjang(5,10))
