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
    current_level_nodes = [root]
    while True:
        result.append(addNodes(current_level_nodes, result)) # result now has current level nodes
        new_current_level_nodes = []
        for node in current_level_nodes:
            if node.left is not None:
                new_current_level_nodes.append(node.left)
            if node.right is not None:
                new_current_level_nodes.append(node.right)
        if len(new_current_level_nodes) == 0:
            break
        current_level_nodes = new_current_level_nodes

    return result


def addNodes(nodes, result):
    current_level_result = []
    for i in range(len(nodes)):
        current_level_result.append(nodes[i].val)
    return current_level_result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
