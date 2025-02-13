gaji_per_jam = int(input("Gaji per jam yang Anda inginkan = "))
jumlah_jam_kerja = int(input("Jumlah jam kerja yang akan dilakukan dalam 1 minggu = "))

pendapatan_kotor = gaji_per_jam * jumlah_jam_kerja * 5
pendapatan_bersih = pendapatan_kotor - ((14/100) * pendapatan_kotor)
outfit = pendapatan_bersih * (10/100)
sisa1 = pendapatan_bersih - outfit
alat_tulis = pendapatan_bersih * (1/100)
sisa2 = sisa1 - alat_tulis
sedekah =  sisa2 * (25/100)
sumbangan_yatim = (sedekah // 1000) * (1000*0.30)
sumbangan_dhuafa = sedekah - sumbangan_yatim

print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak = Rp.", round(pendapatan_kotor))
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak = Rp.", round(pendapatan_bersih))
print("Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris = Rp.", round(outfit))
print("Jumlah uang yang akan Budi habiskan untuk membeli alat tulis = Rp.", round(alat_tulis))
print("Jumlah uang yang akan Budi sedekahkan = Rp.", round(sedekah))
print("Jumlah uang yang akan diterima anak yatim = Rp.", round(sumbangan_yatim))
print("Jumlah uang yang akan diterima kaum dhuafa = Rp.", round(sumbangan_dhuafa))