x = float(input("Nilai ujian teori: "))
y = float(input("Nilai ujian praktik: "))
z = float (70)
if (x>z) and (y>z):
    print ("Selamat, anda lulus!")
elif (x==z) and (y==z):
    print ("Selamat, anda lulus!")
elif (x==z) and (y>z):
    print ("Selamat, anda lulus!")
elif (x>z) and (y==z):
    print ("Selamat, anda lulus!")
elif (x<z) and (y>z):
    print ("Anda harus mengulang ujian teori.")
elif (x<z) and (y==z):
    print ("Anda harus mengulang ujian teori")
elif (x>z) and (y<z):
    print ("Anda harus mengulang ujian praktik.")
elif (x==z) and (y<z):
    print ("Anda harus mengulang ujian praktik")
else:
    print ("Anda harus mengulang ujian teori dan praktik.")