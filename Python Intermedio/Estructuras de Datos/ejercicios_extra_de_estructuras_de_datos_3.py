class Node:
    data: str
    next: "Node"
    prev: "Node"
    
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    head: Node
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            node.prev = current_node
            current_node.next = node
        
    def print_forward(self):
        if self.head:
            result = ''
            current_node = self.head
            while current_node is not None:
                if result == '':
                    result += current_node.data
                else:
                    result += ' -> ' + current_node.data
                current_node = current_node.next
            print(f"\t{result}")
        else:
            print("No nodes in structure")
    
    def print_backward(self):
        if self.head:
            result = ''
            current_node = self.head
            while current_node is not None:
                if result == '':
                    result += current_node.data
                else:
                    result = current_node.data + ' -> ' + result
                current_node = current_node.next
            print(f"\t{result}")
        else:
            print("No nodes in structure")
    
    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            current_node.prev = node
            node.next = current_node
            self.head = node
    
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
    #creating structure
    dll = DoubleLinkedList()
    
    #first node
    print("Appending nodes")
    dll.append('A')
    dll.append('B')
    dll.append('C')
    
    print("Print forward")
    dll.print_forward()
    
    print("\nPrint backwards")
    dll.print_backward()
    
    print("\nPrepending node")
    dll.prepend('X')
    print("Print forward")
    dll.print_forward()
    
    print("\nPrint backwards")
    dll.print_backward()
    
    print("\nDeleting node")
    dll.delete('B')
    print("Print forward")
    dll.print_forward()
    print("\nPrint backwards")
    dll.print_backward()

if __name__ == '__main__':
    main()