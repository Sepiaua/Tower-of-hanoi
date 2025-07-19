def hanoi(n, asal, tujuan, bantu):
    if n == 1:
        print(f"Pindahkan disk 1 dari {asal} ke {tujuan}")
    else:
        hanoi(n - 1, asal, bantu, tujuan)
        print(f"Pindahkan disk {n} dari {asal} ke {tujuan}")
        hanoi(n - 1, bantu, tujuan, asal)

# Menjalankan fungsi untuk 3 disk
hanoi(3, 'A', 'C', 'B')
