from .tree_node import TreeNode
import graphviz


class BinaryTree(object):
    def __init__(self, value=None):
        if value:
            self.root = TreeNode(value)
            self.depth = 1

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            self.depth = 1
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

    def traverse_pre_order(self):
        self._traverse_pre_order(self.root)

    def _traverse_pre_order(self, root, dot=None):
        if root:
            if dot:
                dot.node(str(root.value), label=str(root.value))
            else:
                print(root.value, end=" ")
            if root.left:
                if dot:
                    dot.edge(str(root.value), str(root.left.value), style="solid")
            if root.right:
                if dot:
                    dot.edge(str(root.value), str(root.right.value), style="solid")
            self._traverse_pre_order(root.left, dot)
            self._traverse_pre_order(root.right, dot)

    def visualize(self):
        b_tree = graphviz.Digraph("Binary Tree")
        self._traverse_pre_order(self.root, b_tree)
        b_tree.render(view=True, cleanup=True)
