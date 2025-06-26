"""
PROGRAM DATETIME
Nama : Elsa Aiziyah
NIM  : 21305144025
Kelas: Matematika E

Input:
Ouput:
"""
print("-"*34)
print("Program usia(hari, tanggal, bulan)")
print("-"*34)

from datetime import date
def usia(hari, bulan, tahun):
    hari1 = date.today().day
    bulan1 = date.today().month
    tahun1 = date.today().year
    d0 = date(tahun, bulan, hari)
    d1 = date(tahun1, bulan1, hari1)
    selisih = d1 - d0
    return selisih.days

hari = int(input("Masukkan Tanggal: "))
bulan = int(input("Masukkan Bulan: "))
tahun = int(input("Masukkan Tahun: "))

print("Usia dalam hari adalah", usia(hari, bulan, tahun))


