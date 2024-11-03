#CABRAL MARISHER 
#WD203
class Node:
    def __init__(self,key):
        self.left  = None
        self.right  = None
        self.value = key

def print_tree(root):
    if root:                                                                                                                                       
        print_tree(root.left)
        print(root.value, end= ' ')
        print_tree(root.right)

if __name__== '__main__':

        root = Node(50)

        root.left = Node(30)
        root.left.left = Node(25)
        root.left.right = Node(45)
        root.left.left.left = Node(10)
        root.left.right.left = Node(28)
        root.left.right.right = Node(47)

        root.right = Node(75)
        root.right.left = Node(60)
        root.right.right = Node(90)
        root.right.left.left = Node(59)
        root.right.left.right = Node(69)
        root.right.right.left = Node(76)
        root.right.right.left = Node(80)


        print('Binary Tree: ')
        print_tree(root)





