import os
import time
from termcolor import colored, cprint


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, value, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Position not valid")

        self.items.insert(position, value)
        print(colored(f"Inserted '{value}' at index {position}", "green"))
        self.animate_insert(value)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Position not valid")

        removed = self.items.pop(position)
        print(colored(f"Removed '{removed}'", "red"))
        self.animate_delete(removed)
        return removed

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            raise IndexError("No items available")
        return " -> ".join(self.items)

    def __str__(self):
        return " -> ".join(reversed(self.items)) if self.items else "Empty Stack"

    def animate_insert(self, value):
        for _ in range(2):
            print(colored(f"Adding {value}...", "yellow"))
            time.sleep(0.4)
            self.clear_screen()

    def animate_delete(self, value):
        for _ in range(2):
            print(colored(f"Removing {value}...", "magenta"))
            time.sleep(0.4)
            self.clear_screen()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def stack_operations():
    stack = Stack()

    cprint("STACK OPERATIONS PROGRAM", "cyan", attrs=["bold"])

    while True:
        print("\nCurrent Stack:", colored(str(stack), "blue"))

        print("1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Check Empty")
        print("5. Stack Size")
        print("6. Traverse")
        print("7. Exit")

        try:
            option = int(input("\nEnter choice: "))
        except ValueError:
            cprint("Enter numbers only!", "red")
            continue

        if option == 1:
            item = input("Enter item: ")
            pos = int(input("Enter position: "))
            stack.insert(item, pos)

        elif option == 2:
            pos = int(input("Enter delete position: "))
            stack.delete(pos)

        elif option == 3:
            cprint("Top Element: " + stack.peek(), "blue")

        elif option == 4:
            cprint("Empty" if stack.is_empty() else "Not Empty", "blue")

        elif option == 5:
            cprint("Total Elements: " + str(stack.size()), "blue")

        elif option == 6:
            cprint("Stack: " + stack.traverse(), "blue")

        elif option == 7:
            cprint("Program Closed", "cyan")
            break

        else:
            cprint("Choose from 1 to 7", "red")


if __name__ == "__main__":
    stack_operations()
