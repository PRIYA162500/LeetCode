class Solution(object):
    def isSymmetric(self, root):
        queue = [(root.left, root.right)]

        while queue:
            left, right = queue.pop(0)

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True