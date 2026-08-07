import heapq
from collections import Counter
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext


# ---------------- Huffman Node ---------------- #

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# ---------------- Huffman Functions ---------------- #

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(data):
    if not data:
        return "", {}, {}

    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)

    encoded_data = ''.join(codebook[ch] for ch in data)

    return encoded_data, codebook, frequencies


def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}

    decoded = ""
    current = ""

    for bit in encoded_data:
        current += bit

        if current in reverse_codebook:
            decoded += reverse_codebook[current]
            current = ""

    return decoded


# ---------------- GUI Functions ---------------- #

codebook = {}
encoded_text = ""


def encode_text():
    global codebook, encoded_text

    text = input_box.get()

    if text == "":
        messagebox.showerror("Error", "Please enter some text.")
        return

    encoded_text, codebook, frequencies = huffman_encoding(text)

    output.delete(1.0, tk.END)

    output.insert(tk.END, "Character Frequencies\n")
    output.insert(tk.END, "-------------------------\n")

    for ch, freq in frequencies.items():
        output.insert(tk.END, f"{repr(ch)} : {freq}\n")

    output.insert(tk.END, "\nHuffman Codebook\n")
    output.insert(tk.END, "-------------------------\n")

    for ch, code in codebook.items():
        output.insert(tk.END, f"{repr(ch)} : {code}\n")

    output.insert(tk.END, "\nEncoded Data\n")
    output.insert(tk.END, "-------------------------\n")
    output.insert(tk.END, encoded_text)


def decode_text():
    if not codebook:
        messagebox.showerror("Error", "Please encode first.")
        return

    decoded = huffman_decoding(encoded_text, codebook)

    output.insert(tk.END, "\n\nDecoded Data\n")
    output.insert(tk.END, "-------------------------\n")
    output.insert(tk.END, decoded)

    if decoded == input_box.get():
        messagebox.showinfo("Success", "Original and Decoded text match!")
    else:
        messagebox.showerror("Error", "Decoded text does not match.")


def clear_all():
    global codebook, encoded_text

    codebook = {}
    encoded_text = ""

    input_box.delete(0, tk.END)
    output.delete(1.0, tk.END)


# ---------------- GUI Window ---------------- #

root = tk.Tk()
root.title("Huffman Coding GUI")
root.geometry("750x650")
root.configure(bg="#E8F6F3")

title = tk.Label(
    root,
    text="Huffman Coding Compression",
    font=("Arial", 20, "bold"),
    bg="#117A65",
    fg="white",
    pady=10
)
title.pack(fill=tk.X)

frame = tk.Frame(root, bg="#E8F6F3")
frame.pack(pady=20)

tk.Label(
    frame,
    text="Enter Text:",
    font=("Arial", 13, "bold"),
    bg="#E8F6F3"
).grid(row=0, column=0, padx=10)

input_box = ttk.Entry(frame, width=45, font=("Arial", 12))
input_box.grid(row=0, column=1, padx=10)

button_frame = tk.Frame(root, bg="#E8F6F3")
button_frame.pack()

ttk.Button(
    button_frame,
    text="Encode",
    command=encode_text
).grid(row=0, column=0, padx=10)

ttk.Button(
    button_frame,
    text="Decode",
    command=decode_text
).grid(row=0, column=1, padx=10)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_all
).grid(row=0, column=2, padx=10)

output = scrolledtext.ScrolledText(
    root,
    width=85,
    height=25,
    font=("Consolas", 11)
)
output.pack(pady=20)

root.mainloop()
