class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == int(str(x)[::-1]) if x >= 0 else False
