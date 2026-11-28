class Node:
    data: str
    next: "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    head: Node
    
    def __init__(self, head=None):
        self.head = head
    
    def print_all(self):
        if not self.head:
            print("No nodes in the structure.")
        else:
            current_node = self.head
            result = ''
            while current_node is not None:
                if result == '':
                    result += current_node.data
                else:
                    result = result + ' -> ' + current_node.data
                current_node = current_node.next
            print(f"\t{result}")
    
    def enqueue(self, new_node):
        if self.head is None:
            self.head = new_node
            result = new_node.data
        else:
            result = self.head.data + ' -> '
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
                result += current_node.data + ' -> '
            current_node.next = new_node
            result += new_node.data
        print(f"\t{result}")
    
    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None
            print(f"Removing {current_node.data}")
        else:
            print("No nodes in structure")
        

def main():
    node_1 = Node('A')
    node_2 = Node('B')
    node_3 = Node('C')
    
    #Creating structure
    q = Queue()
    
    print("\nAdding nodes")
    q.enqueue(node_1)
    q.enqueue(node_2)
    q.enqueue(node_3)
        
    print("\nRemoving first node")
    q.dequeue()
    
    print("\nShowing full structure")
    q.print_all()

if __name__ == '__main__':
    main()