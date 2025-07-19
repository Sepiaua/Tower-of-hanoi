import tkinter as tk
from tkinter import simpledialog
import time

class HanoiGUI:
    def __init__(self, root, num_disks):
        self.root = root
        self.num_disks = num_disks
        self.canvas = tk.Canvas(root, width=600, height=300, bg="white")
        self.canvas.pack()
        self.towers = [[i for i in range(num_disks, 0, -1)], [], []]
        self.draw_towers()
        self.root.after(500, lambda: self.solve(num_disks, 0, 2, 1))

    def draw_towers(self):
        self.canvas.delete("all")

        # Gambar 3 tiang
        for i in range(3):
            x = 100 + i * 200
            self.canvas.create_rectangle(x - 5, 100, x + 5, 250, fill="gray")

        # Gambar disk
        for t in range(3):
            tower = self.towers[t]
            for i, disk in enumerate(tower):  # ← urutan bawah ke atas
                width = 20 + (self.num_disks - disk + 1) * 20  # Semakin kecil angkanya, semakin pendek
                x = 100 + t * 200
                y = 250 - (len(tower) - i - 1) * 20
                color = f"#%02x%02x%02x" % (50 * disk % 255, 255 - 30 * disk % 255, 100 + 10 * disk % 155)
                self.canvas.create_rectangle(x - width // 2, y - 10, x + width // 2, y, fill=color)
        self.root.update()

    def move_disk(self, dari, ke):
        disk = self.towers[dari].pop()
        self.towers[ke].append(disk)
        self.draw_towers()
        time.sleep(0.4)

    def solve(self, n, dari, ke, bantu):
        if n == 1:
            self.move_disk(dari, ke)
        else:
            self.solve(n-1, dari, bantu, ke)
            self.move_disk(dari, ke)
            self.solve(n-1, bantu, ke, dari)

# Jalankan program
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    num_disks = simpledialog.askinteger("Input", "Masukkan jumlah cakram (1-7):", minvalue=1, maxvalue=7)

    if num_disks:
        root.deiconify()
        root.title(f"Tower of Hanoi - {num_disks} Cakram (Reversed Visual)")
        app = HanoiGUI(root, num_disks)
        root.mainloop()
    else:
        print("Input dibatalkan.")
