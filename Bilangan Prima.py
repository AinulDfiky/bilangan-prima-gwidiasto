print("TUGAS - Daftar Bilangan Prima")

print("Gama Widiasto")
print ("04217017")

a = int(input("Masukkan Batas Bilangan Prima : "))
print ("Hasil :")
for b in range(2,a+1):
    prima = True
    for i in range(2,b):
        if (b%i==0):
            prima = False
    if prima == True:
       print (b)
       
print ("SELESAI")
