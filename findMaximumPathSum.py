import math


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class MaximumPathSum:
    def find_maximum_path_sum(self, root):
        self.global_maximum = -math.inf
        self.find_maximum_path_sum_recursive(root)
        return self.global_maximum

    def find_maximum_path_sum_recursive(self, node):
        if node is None:
            return 0
        left_path_sum = max(self.find_maximum_path_sum_recursive(node.left), 0) # compare with 0 to leave out negative sums
        right_path_sum = max(self.find_maximum_path_sum_recursive(node.right), 0)
        # calculate maximum path sum at current node
        local_maximum = left_path_sum + right_path_sum + node.val
        # calculate max path sum seen so far 
        self.global_maximum = max(self.global_maximum, local_maximum)
        return max(left_path_sum, right_path_sum) + node.val


def main():
  maximumPathSum = MaximumPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()
