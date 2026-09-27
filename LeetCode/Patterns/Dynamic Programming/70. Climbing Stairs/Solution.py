class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2  # ways to reach step 1 and 2
        for _ in range(3, n+1):
            a, b = b, a + b
        return b
