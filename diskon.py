menu = {
  "Fried Chiken":15000,
  "Burger Queen":25000,
  "French Fries":1000,
  "Jasmine Tea":5000,
  "Ice Coca Cola":12000
}
print("========== Daftar Menu ==========")
for i in menu:
    print("Daftar Menu : ", i,"/t Harga :",menu[i])
print("Pembelian diatas RP100.000,- mendapatkan diskon 15% ")    
print("==================================================")
beli = input ("pilih menu : ")
jumlah =int (input("jumlah pesenan : "))
bayar = jumlah * menu[beli]

if bayar > 100000:
   diskon = bayar*15/100
   total = bayar - diskon
else:
  total = bayar

print("========== Detail pembayaran ==========")
print("menu yang dipesan        : ",beli)
print("jumlah yang dipesan      : ",jumlah)
print("total Biaya              : ",bayar)
print("Total yang harus dibayar : ",total)