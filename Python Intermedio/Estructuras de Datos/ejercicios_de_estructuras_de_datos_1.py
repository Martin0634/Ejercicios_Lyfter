class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    top: Node

    def __init__(self, top):
        self.top = top

    def print_structure(self):
        current_node = self.top
    
        while (current_node is not None):
            print(f"\t {current_node.data}")
            current_node = current_node.next
    
    def push(self, new_node):
        current_node = self.top
        self.top = new_node
        new_node.next = current_node
        
    def pop(self):
        if self.top:
            self.top = self.top.next

def main():
    first_node = Node("First node")
    my_stack = Stack(first_node)

    second_node = Node("Second node")
    my_stack.push(second_node)

    third_node = Node("Third node")
    my_stack.push(third_node)

    print("Nodes Structure:")
    my_stack.print_structure()

    print("\nPop node:")
    my_stack.pop()
    my_stack.print_structure()

    print("\nPush new node:")
    new_node = Node("The new node")
    my_stack.push(new_node)
    my_stack.print_structure()

if __name__ == '__main__':
    main()