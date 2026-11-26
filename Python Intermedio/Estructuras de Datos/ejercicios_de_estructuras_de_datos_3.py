class Node:
    data: str
    left: "Node"
    right: "Node"
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    root: Node
    
    def __init__(self, root):
        self.root = root
    
    def print_structure(self, node):
        if not node:
            return
        else:
            print(node.data)
            self.print_structure(node.left)
            self.print_structure(node.right)
            

def main():
    node_7 = Node('7')
    node_6 = Node('6', node_7)
    node_5 = Node('5')
    node_4 = Node('4')
    node_2 = Node('2', node_4, node_5)
    node_3 = Node('3', node_6)
    
    print("Creating Tree")
    node_1 = Node('1', node_2, node_3)
    new_binary_tree = BinaryTree(node_1)
    new_binary_tree.print_structure(node_1)

if __name__ == '__main__':
    main()