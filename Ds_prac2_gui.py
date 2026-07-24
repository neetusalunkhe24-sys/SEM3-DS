import tkinter as tk
from tkinter import messagebox


class Stack:
    def __init__(self):
        self.items = []

    def insert(self, value, pos):
        if pos < 0 or pos > len(self.items):
            raise IndexError("Invalid Position")

        self.items.insert(pos, value)

    def delete(self, pos):
        if pos < 0 or pos >= len(self.items):
            raise IndexError("Invalid Position")

        return self.items.pop(pos)

    def peek(self):
        return self.items[-1] if self.items else "Empty"

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def traverse(self):
        return " | ".join(self.items) if self.items else "Empty"


stack = Stack()


def update_stack():
    if stack.items:
        box.config(
            text="\n".join(reversed(stack.items))
        )
    else:
        box.config(text="STACK EMPTY")


def insert_item():
    try:
        value = item.get()
        pos = int(position.get())

        stack.insert(value, pos)

        status.config(
            text=f"Inserted {value}"
        )

        update_stack()

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


def delete_item():
    try:
        pos = int(position.get())

        x = stack.delete(pos)

        status.config(
            text=f"Deleted {x}"
        )

        update_stack()

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


def peek_item():
    status.config(
        text="Top → " + str(stack.peek())
    )


def size_item():
    status.config(
        text="Size → " +
        str(stack.size())
    )


def traverse_item():
    status.config(
        text=stack.traverse()
    )


def empty_item():
    status.config(
        text="YES"
        if stack.empty()
        else "NO"
    )


root = tk.Tk()

root.geometry("900x550")
root.title("Stack Manager")
root.configure(bg="#111111")


# LEFT PANEL
left = tk.Frame(
    root,
    bg="#181818",
    width=430 
)

left.pack(
    side="left",
    fill="y"
)

left.pack_propagate(False)

title = tk.Label(
    left,
    text="STACK\nMANAGER",
    font=("Impact", 26),
    fg="#00C2FF",
    bg="#181818"
)

title.pack(pady=30)

item = tk.Entry(
    left,
    font=("Verdana", 13),
    width=28
)

item.pack(pady=10)

item.insert(0, "Item")


position = tk.Entry(
    left,
    font=("Verdana", 13),
    width=28
)

position.pack()

position.insert(0, "Position")


style = {
    "width": 16,
    "height": 2,
    "font": ("Arial", 10, "bold")
}


buttons = [
    ("Insert", "#0081A7", insert_item),
    ("Delete", "#C1121F", delete_item),
    ("Peek", "#2A9D8F", peek_item),
    ("Size", "#6A4C93", size_item),
    ("Traverse", "#4361EE", traverse_item),
    ("Empty", "#F4A261", empty_item)
]

for text, color, cmd in buttons:

    tk.Button(
        left,
        text=text,
        bg=color,
        fg="white",
        command=cmd,
        **style

    ).pack(pady=6)


# RIGHT PANEL
right = tk.Frame(
    root,
    bg="#202020"
)

right.pack(
    expand=True,
    fill="both"
)

tk.Label(
    right,
    text="STACK VIEW",
    bg="#202020",
    fg="white",
    font=("Bahnschrift", 20)
).pack(pady=20)


box = tk.Label(
    right,
    text="STACK EMPTY",
    width=18,
    height=10,
    bg="#2C2C2C",
    fg="#00E5FF",
    font=("Consolas", 15),
    relief="solid"
)

box.pack()


tk.Label(
    right,
    text="RESULT",
    bg="#202020",
    fg="white",
    font=("Bahnschrift", 18)
).pack(pady=25)


status = tk.Label(
    right,
    text="Ready",
    width=40,
    height=4,
    bg="#101010",
    fg="white",
    font=("Calibri", 13)
)

status.pack()


root.mainloop()
