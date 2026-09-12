class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)

        if n <= 2:
            return n

        p = 1
        while p <= n:
            p *= 2

        return p
        