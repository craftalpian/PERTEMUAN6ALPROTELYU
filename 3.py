# # FOR
# daftar_belanja = [['Sayuran', 127800], ['Bumbu masak', 103500], ['Sabun dan Pembersih Rumah', 77350], ['Aneka Minuman', 87780], ['Buah-buahan', 48600], ['Obat-obatan', 64678], ['Aneka Jajanan', 80450]]

# total = 0
# for i in daftar_belanja:
#     barang = i[0]
#     harga = i[1]
#     total += harga
#     print(f"Pembelian {barang} seharga Rp{harga}")
# else:
#     print(f"Total: Rp{total}")

# WHILE
daftar_belanja = [['Sayuran', 127800], ['Bumbu masak', 103500], ['Sabun dan Pembersih Rumah', 77350], ['Aneka Minuman', 87780], ['Buah-buahan', 48600], ['Obat-obatan', 64678], ['Aneka Jajanan', 80450]]

total, i = 0, 0
while i < len(daftar_belanja):
    barang = daftar_belanja[i][0]
    harga = daftar_belanja[i][1]
    total += harga
    i += 1
    print(f"Pembelian {barang} seharga Rp{harga}")

print(f"Total: Rp{total}")