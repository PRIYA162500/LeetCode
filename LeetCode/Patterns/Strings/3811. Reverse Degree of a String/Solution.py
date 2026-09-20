class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            reverse_pos = ord('z') - ord(s[i]) + 1
            ans += reverse_pos * (i + 1)

        return ans