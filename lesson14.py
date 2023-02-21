class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._add_node(val, self.root)

    def _add_node(self, val, node):
        if val < node.val:
            if node.left:
                self._add_node(val, node.left)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._add_node(val, node.right)
            else:
                node.right = TreeNode(val)

    def find_min(self):
        if not self.root:
            return None
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node.val

    def find_max(self):
        if not self.root:
            return None
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node.val

    def remove_node(self, val):
        self.root = self._remove_node(val, self.root)

    def _remove_node(self, val, node):
        if not node:
            return None
        if val == node.val:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_node = self._find_min_node(node.right)
            node.val = min_node.val
            node.right = self._remove_node(min_node.val, node.right)
        elif val < node.val:
            node.left = self._remove_node(val, node.left)
        else:
            node.right = self._remove_node(val, node.right)
        return node

    def _find_min_node(self, node):
        while node.left:
            node = node.left
        return node

    # Print the tree
    def print_tree(self):
        if not self.root:
            return
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.val)
            self._print_tree(node.right)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


tree = Tree()

tree.add_node(10)
tree.add_node(5)
tree.add_node(15)
tree.add_node(2)
tree.add_node(7)
tree.add_node(12)
tree.add_node(20)

print("Binary tree -check: ")
tree.print_tree()
print()

print("Min value:", tree.find_min())
print("Max value:", tree.find_max())
print()

print("Deleted values: 10, 20")
tree.remove_node(10)
tree.remove_node(20)

print("Min value new:", tree.find_min())
print("Max value new:", tree.find_max())
print()

print("Binary tree after delete: ")
tree.print_tree()

