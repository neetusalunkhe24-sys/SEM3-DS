import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return "Queue is full. Cannot enqueue."
        self.queue.append(item)
        return f"Enqueued: {item}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."
        return f"Dequeued: {self.queue.pop(0)}"

    def peek(self):
        if self.is_empty():
            return "Queue is empty."
        return f"Front of Queue: {self.queue[0]}"

    def traverse(self):
        if self.is_empty():
            return "Queue is empty."
        return "Queue: " + " -> ".join(map(str, self.queue))

    def display_list(self):
        if self.is_empty():
            return "Queue is empty."
        return "\n".join([f"{i+1}. {item}" for i, item in enumerate(self.queue)])


def create_queue():
    global q
    try:
        size = int(size_entry.get())
        q = Queue(size)
        messagebox.showinfo("Success", f"Queue of size {size} created.")
    except:
        messagebox.showerror("Error", "Enter a valid size.")


def enqueue():
    if q is None:
        messagebox.showerror("Error", "Create Queue first.")
        return
    item = item_entry.get()
    output.config(text=q.enqueue(item))
    item_entry.delete(0, tk.END)


def dequeue():
    if q is None:
        return
    output.config(text=q.dequeue())


def peek():
    if q is None:
        return
    output.config(text=q.peek())


def traverse():
    if q is None:
        return
    output.config(text=q.traverse())


def display():
    if q is None:
        return
    output.config(text=q.display_list())


def check_empty():
    if q is None:
        return
    if q.is_empty():
        output.config(text="Queue is Empty")
    else:
        output.config(text="Queue is Not Empty")


def check_full():
    if q is None:
        return
    if q.is_full():
        output.config(text="Queue is Full")
    else:
        output.config(text="Queue is Not Full")


q = None

root = tk.Tk()
root.title("Queue GUI")
root.geometry("500x500")

tk.Label(root, text="Maximum Queue Size").pack()

size_entry = tk.Entry(root)
size_entry.pack()

tk.Button(root, text="Create Queue", command=create_queue).pack(pady=5)

tk.Label(root, text="Enter Item").pack()

item_entry = tk.Entry(root)
item_entry.pack()

tk.Button(root, text="Enqueue", command=enqueue).pack(fill="x")
tk.Button(root, text="Dequeue", command=dequeue).pack(fill="x")
tk.Button(root, text="Peek", command=peek).pack(fill="x")
tk.Button(root, text="Traverse", command=traverse).pack(fill="x")
tk.Button(root, text="Display List", command=display).pack(fill="x")
tk.Button(root, text="Check Empty", command=check_empty).pack(fill="x")
tk.Button(root, text="Check Full", command=check_full).pack(fill="x")

output = tk.Label(root, text="", fg="blue", justify="left", font=("Arial", 12))
output.pack(pady=20)

root.mainloop()
