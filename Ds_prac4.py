import time
from colorama import init, Fore, Style

init(convert=True, autoreset=True)


class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.start = None

    # Insert at beginning
    def add_first(self, value):
        node = DNode(value)

        if self.start is None:
            self.start = node
        else:
            node.next = self.start
            self.start.prev = node
            self.start = node

    # Insert at end
    def add_last(self, value):
        node = DNode(value)

        if self.start is None:
            self.start = node
            return

        ptr = self.start
        while ptr.next:
            ptr = ptr.next

        ptr.next = node
        node.prev = ptr

    # Insert at specific position
    def add_position(self, value, pos):
        if pos == 0:
            self.add_first(value)
            return

        ptr = self.start
        count = 0

        while ptr is not None and count < pos:
            ptr = ptr.next
            count += 1

        if ptr is None:
            raise IndexError("Invalid Position")

        node = DNode(value)
        node.next = ptr
        node.prev = ptr.prev

        ptr.prev.next = node
        ptr.prev = node

    # Delete first node
    def remove_first(self):
        if self.start is None:
            return

        if self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None

    # Delete last node
    def remove_last(self):
        if self.start is None:
            return

        if self.start.next is None:
            self.start = None
            return

        ptr = self.start

        while ptr.next:
            ptr = ptr.next

        ptr.prev.next = None

    # Delete at position
    def remove_position(self, pos):
        if self.start is None:
            return

        ptr = self.start
        count = 0

        while ptr is not None and count < pos:
            ptr = ptr.next
            count += 1

        if ptr is None:
            raise IndexError("Invalid Position")

        if ptr.prev:
            ptr.prev.next = ptr.next

        if ptr.next:
            ptr.next.prev = ptr.prev

    # Display list
    def traverse(self):
        if self.start is None:
            print(Fore.RED + "List is Empty")
            return

        print(Fore.GREEN + "Doubly Linked List:")

        ptr = self.start
        while ptr:
            print(ptr.value, end=" <-> ")
            ptr = ptr.next

        print("None")

    # Search node
    def find(self, key):
        ptr = self.start

        while ptr:
            if ptr.value == key:
                return True
            ptr = ptr.next

        return False

    # Count nodes
    def count_nodes(self):
        total = 0
        ptr = self.start

        while ptr:
            total += 1
            ptr = ptr.next

        return total


def show_menu():
    print("\n" + Style.BRIGHT + "====== Doubly Linked List Menu ======")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete First Node")
    print("5. Delete Last Node")
    print("6. Delete at Position")
    print("7. Display List")
    print("8. Search Element")
    print("9. Count Nodes")
    print("10. Exit")


def main():
    dll = DoubleList()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                value = int(input("Enter value: "))
                dll.add_first(value)
                print(Fore.GREEN + "Inserted at beginning.")

            elif choice == 2:
                value = int(input("Enter value: "))
                dll.add_last(value)
                print(Fore.GREEN + "Inserted at end.")

            elif choice == 3:
                value = int(input("Enter value: "))
                pos = int(input("Enter position: "))
                dll.add_position(value, pos)
                print(Fore.GREEN + "Node inserted successfully.")

            elif choice == 4:
                dll.remove_first()
                print(Fore.RED + "First node removed.")

            elif choice == 5:
                dll.remove_last()
                print(Fore.RED + "Last node removed.")

            elif choice == 6:
                pos = int(input("Enter position: "))
                dll.remove_position(pos)
                print(Fore.RED + "Node removed.")

            elif choice == 7:
                dll.traverse()

            elif choice == 8:
                value = int(input("Enter value to search: "))
                if dll.find(value):
                    print(Fore.GREEN + "Element Found")
                else:
                    print(Fore.RED + "Element Not Found")

            elif choice == 9:
                print(Fore.BLUE + f"Number of Nodes: {dll.count_nodes()}")

            elif choice == 10:
                print("Thank You!")
                break

            else:
                print(Fore.YELLOW + "Invalid Choice.")

        except ValueError:
            print(Fore.YELLOW + "Please enter valid integer values.")

        except IndexError as e:
            print(Fore.RED + str(e))

        time.sleep(1)


if __name__ == "__main__":
    main()
