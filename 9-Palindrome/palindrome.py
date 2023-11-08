class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_string = str(x)
        x_reversed = x_string[::-1]
        if x_string == x_reversed:
            return True
        else:
            return False

