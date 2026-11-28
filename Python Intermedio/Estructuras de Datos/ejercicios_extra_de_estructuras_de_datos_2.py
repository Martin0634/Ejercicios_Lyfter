class Node:
    data: str
    next: "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node
    
    def __init__(self, head=None):
        self.head = head
    
    def print_all(self):
        if not self.head:
            print("No nodes in structure")
        else:
            current_node = self.head
            result = ''
            while current_node is not None:
                if result == '':
                    result += str(current_node.data)
                else:
                    result += ' -> ' + str(current_node.data)
                current_node = current_node.next
            print(f"{result}")
    
    def insert_front(self, new_node):
        current_node = self.head
        new_node.next = current_node
        self.head = new_node
        self.print_all()
    
    def insert_back(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            self.print_all()
    
    def delete(self, data):
        if self.head:
            if self.head.next is not None:
                current_node = self.head
                if current_node.data == data:
                    deleting_node = current_node
                    self.head = current_node.next
                    current_node.next = None
                else:
                    while current_node.next.data != data:
                        current_node = current_node.next
                    deleting_node = current_node.next
                    
                    if deleting_node is None:
                        print("Data is not in structure")
                    else:
                        current_node.next = deleting_node.next
                        deleting_node.next = None
                        print(f"Removing: {deleting_node.data}")
            else:
                print("No nodes in structure")
        else:
            print("No nodes in structure")

def main():
    node_1 = Node(10)
    node_2 = Node(20)
    node_3 = Node(30)
    
    print("Creating structure")
    ll = LinkedList()
    
    print("\nAdding nodes front")
    ll.insert_front(node_1)
    ll.insert_front(node_2)

    print("\nAdding node back")
    ll.insert_back(node_3)
    
    print("\nDeleting a Node")
    ll.delete(10)
    
    print("\nShowing full structure")
    ll.print_all()

if __name__ == '__main__':
    main()