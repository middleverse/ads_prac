class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
    current_sum = root.val
    left, right = False, False
    if root.left:
        left = has_sum_path(root.left, current_sum, sum)
    if root.right:
        right = has_sum_path(root.right, current_sum, sum)
    return left or right

def has_sum_path(node, curr_sum, wanted_sum):
    curr_sum += node.val
    left, right, leaf = False, False, True
    if node.left:   
        leaf = False
        left = has_sum_path(node.left, curr_sum, wanted_sum)
    if node.right:
        leaf = False
        right = has_sum_path(node.right, curr_sum, wanted_sum)
    if leaf:
        if curr_sum == wanted_sum:
            return True
    return left or right

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
