import tkinter as tk
from cipher import caesar

def encrypt():
    output.delete(1.0, tk.END)
    output.insert(tk.END, caesar(input_text.get("1.0", tk.END), int(shift.get())))

def decrypt():
    output.delete(1.0, tk.END)
    output.insert(tk.END, caesar(input_text.get("1.0", tk.END), -int(shift.get())))

root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Input").pack()
input_text = tk.Text(root, height=6)
input_text.pack()

tk.Label(root, text="Shift").pack()
shift = tk.Entry(root)
shift.pack()

tk.Button(root, text="Encrypt", command=encrypt).pack()
tk.Button(root, text="Decrypt", command=decrypt).pack()

output = tk.Text(root, height=6)
output.pack()

root.mainloop()
