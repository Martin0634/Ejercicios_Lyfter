class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:
    head: Node
    tail: Node
    
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail
    
    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(f"\t {current_node.data}")
            current_node = current_node.next

    def push_right(self, new_node):
        if self.tail is None:
            current_node = self.head
            self.tail = new_node
            current_node.next = new_node
        else:
            current_node = self.tail
            self.tail = new_node
            current_node.next = new_node

    
    def push_left(self, new_node):
        current_node = self.head
        self.head = new_node
        new_node.next = current_node

    def pop_right(self):
        if self.head and self.tail:
            current_node = self.head
            while (current_node.next is not self.tail):
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
    
    def pop_left(self):
        if self.head:
            self.head = self.head.next

def main():
    first_node = Node("First node")
    my_double_ended_queue = DoubleEndedQueue(first_node)
    print("Nodes Structure:")
    my_double_ended_queue.print_structure()
    
    print("\nPushing right:")
    second_node = Node("Second Node")
    my_double_ended_queue.push_right(second_node)
    my_double_ended_queue.print_structure()
    
    print("\nPushing left:")
    third_node = Node("Third Node")
    my_double_ended_queue.push_left(third_node)
    my_double_ended_queue.print_structure()
    
    print("\nPushing right:")
    fourth_node = Node("Fourth Node")
    my_double_ended_queue.push_right(fourth_node)
    my_double_ended_queue.print_structure()
    
    print("\nPushing left:")
    fifth_node = Node("Fifth Node")
    my_double_ended_queue.push_left(fifth_node)
    my_double_ended_queue.print_structure()
    
    print("\nPop right")
    my_double_ended_queue.pop_right()
    my_double_ended_queue.print_structure()
    
    print("\nPop left")
    my_double_ended_queue.pop_left()
    my_double_ended_queue.print_structure()

if __name__ == '__main__':
    main()