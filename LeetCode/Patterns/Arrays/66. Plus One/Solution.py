class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the array from the last element to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        # If the loop finishes, it means all digits were 9 (e.g., [9, 9, 9] became [0, 0, 0])
        # We need to add a 1 at the beginning of the array
        return [1] + digits