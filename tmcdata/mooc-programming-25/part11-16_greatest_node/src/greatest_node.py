# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    max = root.value

    if root.left_child is not None:
        left_max = greatest_node(root.left_child)
        if left_max > max:
            max = left_max
    if root.right_child is not None:
        right_max = greatest_node(root.right_child)
        if right_max > max:
            max = right_max
    return max

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(13)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(1)

    print(greatest_node(tree))
