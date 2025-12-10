print ("hitung luas bangun datar")
print ("1. Luas Persegi")
print ("2. Luas Persegi Panjang")
print ("3. Luas Segitiga")
print ("4. Luas Lingkaran")

pilihan = int(input("Masukkan Pilihan"))
if pilihan==1 :
    s = float(input("masukkan sisi"))
    lp = s * s
    print("luas persegi = %f" %(lp))
    
elif pilihan==2 :
    p = float (input("Masukkan panjang"))
    l = float (input("Masukkan lebar"))
    lpp= p * l
    print ("Luas Persegi Panjang = %f" %(lpp))
    
elif pilihan==3 :
    a = float(input("Masukkan sisi a"))
    t = float(input("Masukkan sisi t"))
    tp = a * t * 0.5
    print ("luas segitiga = %f" %(tp))

else :
    r = float(input("masukkan jari-jari"))
    LL = 3.14*r*r
    print ("luas lingkaran = %f" %(LL))
            
            