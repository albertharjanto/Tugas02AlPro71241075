tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))
bmi = float(input("Masukkan Body Max Index (BMI) yang diharapkan: "))

berat_badan = bmi * ((tinggi_badan)**2)
print(f"Berat badan yang diperlukan adalah: {round(berat_badan,2)} kg")