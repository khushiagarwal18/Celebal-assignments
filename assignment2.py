class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        """Add node to the end of the list"""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all elements of the list"""
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        try:
            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index must be 1 or greater.")

            if n == 1:
                print(f"Deleting node at position {n} with value '{self.head.data}'")
                self.head = self.head.next
                return

            current = self.head
            prev = None
            count = 1

            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if not current:
                raise IndexError(f"Index {n} is out of range.")

            print(f"Deleting node at position {n} with value '{current.data}'")
            prev.next = current.next

        except IndexError as e:
            print("Error:", e)


if __name__ == "__main__":
    ll = LinkedList()

    print("Adding nodes to the list...")
    for val in [10, 20, 30, 40, 50]:
        ll.append(val)

    print("\nOriginal List:")
    ll.print_list()

    print("\nDeleting 3rd node:")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete 10th node (out of range):")
    ll.delete_nth_node(10)

    print("\nDeleting remaining nodes:")
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete from empty list:")
    ll.delete_nth_node(1)
