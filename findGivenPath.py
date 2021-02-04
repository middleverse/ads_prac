class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
    if root is None:
        if len(sequence) == 0:
            return True
        else:
            return False
    if root.left is None and root.right is None:
        if sequence[0] == root.val and len(sequence) == 1:
            return True
        else:
            return False
    return find_path(root.left, sequence[1:]) or find_path(root.right, sequence[1:])


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
