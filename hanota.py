import tkinter as tk
import time

# Inisialisasi window tkinter
root = tk.Tk()
root.title("Tower of Hanoi - DFS Visualization")
canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

# Posisi tiang (A, B, C)
peg_x = [100, 300, 500]
peg_y = 250
peg_width = 10
peg_height = 150

# Global stacks
A = [1, 2, 3]  # cakram terbesar di bawah (3), terkecil di atas (1)
B = []
C = []

# Disk height and width
disk_height = 20
disk_colors = {1: "red", 2: "white", 3: "green"}

# Gambar seluruh tiang dan cakram
def draw_tower():
    canvas.delete("all")
    for x in peg_x:
        canvas.create_rectangle(x - peg_width // 2, peg_y - peg_height, x + peg_width // 2, peg_y, fill="black")

    def draw_disks(stack, x_pos):
        total_disks = len(stack)
        for i, disk in enumerate(stack):  # menggambar dari bawah ke atas
            width = disk * 30
            y = peg_y - (total_disks - i) * disk_height
            canvas.create_rectangle(
                x_pos - width // 2, y, x_pos + width // 2, y + disk_height,
                fill=disk_colors[disk], outline="black"
            )

    draw_disks(A, peg_x[0])
    draw_disks(B, peg_x[1])
    draw_disks(C, peg_x[2])
    root.update()
    time.sleep(0.5)

def get_name(peg):
    if peg is A:
        return "A"
    elif peg is B:
        return "B"
    elif peg is C:
        return "C"
    return "?"

def move(src: list[int], tar: list[int]):
    pan = src.pop()
    tar.append(pan)
    print(f"Move disk {pan} from {get_name(src)} to {get_name(tar)}")
    draw_tower()

def dfs(i: int, src: list[int], buf: list[int], tar: list[int]):
    if i == 1:
        move(src, tar)
        return
    dfs(i - 1, src, tar, buf)
    move(src, tar)
    dfs(i - 1, buf, src, tar)

def solve_hanota():
    draw_tower()
    dfs(len(A), A, B, C)
    print("\nFinal State:")
    print("A =", A)
    print("B =", B)
    print("C =", C)

if __name__ == "__main__":
    solve_hanota()
    root.mainloop()
