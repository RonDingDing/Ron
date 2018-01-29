
class Node(object):

    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

    def IsSame(self, node):
        res = False
        if((self is None and node is not None) or (self is not None and node is None)
            res = False
        elif self is None and node is None:
            res = True
        elif self.val == node.val:
            res = IsSame(self.left, node.left) and IsSame(self.right, node.right)
            return res
