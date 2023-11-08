class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        # Follow up: Could you solve it without converting the integer to a string? 
        # Solution...
        # y = 0
        # n = x / 1
        # while(n > 0):
        #     a = n % 10
        #     y = y * 10 + a
        #     n = n // 10
        if x == y:
            return True
        else:
            return False
