import time
from colorama import init, Fore, Style

init(convert=True, autoreset=True)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def add_at_position(self, value, pos):
        if pos < 0:
            print("Invalid Position")
            return

        new_node = Node(value)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range.")
            return

        new_node.next = current.next
        current.next = new_node

    def remove_value(self, value):
        if self.head is None:
            print("List is Empty.")
            return

        if self.head.value == value:
            self.head = self.head.next
            print("Node Deleted.")
            return

        previous = None
        current = self.head

        while current and current.value != value:
            previous = current
            current = current.next

        if current is None:
            print("Value not found.")
            return

        previous.next = current.next
        print("Node Deleted.")

    def remove_position(self, pos):
        if self.head is None:
            print("List is Empty.")
            return

        if pos == 0:
            self.head = self.head.next
            print("Node Deleted.")
            return

        current = self.head
        count = 0

        while current and count < pos - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            print("Invalid Position.")
            return

        current.next = current.next.next
        print("Node Deleted.")

    def traverse(self):
        if self.head is None:
            print("Linked List is Empty.")
            return

        current = self.head
        print("Linked List:", end=" ")

        while current:
            print(current.value, end=" -> ")
            current = current.next

        print("NULL")


def menu():
    print("\n====== Singly Linked List ======")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete by Value")
    print("5. Delete by Position")
    print("6. Traverse List")
    print("7. Exit")


def main():
    sll = SinglyLinkedList()

    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                value = int(input("Enter value: "))
                sll.add_front(value)

            elif choice == 2:
                value = int(input("Enter value: "))
                sll.add_last(value)

            elif choice == 3:
                value = int(input("Enter value: "))
                pos = int(input("Enter position: "))
                sll.add_at_position(value, pos)

            elif choice == 4:
                value = int(input("Enter value to delete: "))
                sll.remove_value(value)

            elif choice == 5:
                pos = int(input("Enter position to delete: "))
                sll.remove_position(pos)

            elif choice == 6:
                sll.traverse()

            elif choice == 7:
                print("Program Terminated.")
                break

            else:
                print("Please enter a valid option.")

        except ValueError:
            print("Enter valid integer input.")


if __name__ == "__main__":
    main()
