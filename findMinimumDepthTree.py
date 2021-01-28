from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):

    current_level = 0
    queue = deque()
    queue.append(root)

    while queue:
        current_level += 1
        for _ in range(len(queue)):
            current_node = queue.popleft()
            if not current_node.left and not current_node.right:
                return current_level
            queue.append(current_node.left) 
            queue.append(current_node.right)           
    return -1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
