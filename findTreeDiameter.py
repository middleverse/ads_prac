class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.find_diameter_recursive(root)
        return self.treeDiameter

    def find_diameter_recursive(self, node):
        if node is None: 
            return 0

        if node.left is None and node.right is None:
            return 1
        else:
            left_depth = self.find_diameter_recursive(node.left)
            right_depth = self.find_diameter_recursive(node.right)

            current_diameter = left_depth + right_depth + 1
            self.treeDiameter = max(self.treeDiameter, current_diameter)
            return 1 + max(left_depth, right_depth)

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()







