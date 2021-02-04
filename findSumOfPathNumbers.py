class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
    return find_sum(root, 0)

def find_sum(node, sum):
    if node is None:
        return 0
    
    sum = sum * 10 + node.val

    if node.left is None and node.right is None:
        return sum
    else:
        return find_sum(node.left, sum) + find_sum(node.right, sum)
    

def list_to_int(nums):
    strs = [str(i) for i in nums]
    concat_str = "".join(strs)
    value = int(concat_str)
    return value

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
