from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
    if root is None: 
        return []
    result = []
    # iterate through all levels
    # on each level add the nodes to result
    queue = deque()
    queue.append(root)
    while queue:
        size_of_level = len(queue)
        current_level_nodes = []
        for _ in range(size_of_level):
            current_node = queue.popleft()
            current_level_nodes.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level_nodes)
    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
