class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
    return count_paths_recursive(root, S, [])
    return -1


def count_paths_recursive(node, S, current_path):
    if node is None:
        return 0
    # push new node on path on to stack
    current_path.append(node.val)
    path_sum, path_count = 0, 0
    # calculate all sub path sums that end with node
    for i in range(len(current_path) - 1, -1, -1): # move backwards
        path_sum += current_path[i]
        if path_sum == S:
            path_count += 1
    # recurse on both sides of node
    path_count += count_paths_recursive(node.left, S, current_path)
    path_count += count_paths_recursive(node.right, S, current_path)
    # pop node off stack
    del current_path[-1]
    return path_count

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
