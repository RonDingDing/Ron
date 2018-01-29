
class Node(object):

    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val

    def equal(self, val):
        if self.val == val:
            return True
        elif self.val > val:
            return self.left.equal(val)
        elif self.val < val:
            return self.right.equal(val)
        else:
            return False
