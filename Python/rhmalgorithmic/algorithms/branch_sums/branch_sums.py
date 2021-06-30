# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    DEFAULT_SUM = 0
    sums = []
    getBranchSums(root, DEFAULT_SUM, sums)
    return sums


def is_leaf_node(node):
    return node.left is None and node.right is None


def getBranchSums(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if is_leaf_node(node):
        sums.append(newRunningSum)
        return

    getBranchSums(node.left, newRunningSum, sums)
    getBranchSums(node.right, newRunningSum, sums)
