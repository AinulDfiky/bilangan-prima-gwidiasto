print("TUGAS - Daftar Bilangan Prima")
print("Gama Widiasto")
print ("04217017")

a = int(input("Masukkan Angka Awal : "))
b = int(input("Masukkan Batas Bilangan Prima : "))
print ("Hasil :")
for x in range(a,b):
    prima = True
    for i in range(2,x):
        if (x%i==0):
            prima = False
    if prima == True:
       print (x)
       
print ("SELESAI")
