class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False
        if len(s) %2==0:
            for bracket in s:
                if bracket == "{" or bracket == "(" or bracket == "[":
                    stack.append(bracket)
                    print(1)
                if not stack and (bracket == "}" or bracket == ")" or bracket == "]"):  # once we encounter a closing it is automatically a False
                    print(2)
                    return False
                elif bracket == "}" and stack[-1] == "{" and len(stack) > 0:
                    print(3)
                    stack.pop()
                elif bracket == ")" and stack[-1] == "(" and len(stack) > 0:
                    print(4)
                    stack.pop()
                elif bracket == "]" and stack[-1] == "[" and len(stack) > 0:
                    print(5)
                    stack.pop()
            return True if len(stack) == 0 else False
        else:
            return False
