class Solution:
    def isValid(self, s):
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            else:
                if not stack or stack.pop() != c:
                    return False

        return len(stack) == 0