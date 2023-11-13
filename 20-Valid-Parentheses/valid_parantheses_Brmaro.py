class Solution:
    def isValid(self,s):
        stack = []
        if sum([1 for b in s if b in "{[("]) != sum([1 for b in s if b in "}])"]):
            return False
        if s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False
        if len(s) % 2 == 0:
            for bracket in s:
                if bracket == "{" or bracket == "(" or bracket == "[":
                    stack.append(bracket)
                if not stack and (bracket == "}" or bracket == ")" or bracket == "]"):  # once we encounter a closing it is automatically a False
                    return False
                elif bracket == "}" and stack[-1] == "{" and stack:
                    stack.pop()
                elif bracket == ")" and stack[-1] == "(" and stack:
                    stack.pop()
                elif bracket == "]" and stack[-1] == "[" and stack:
                    print(5)
                    stack.pop()
            return True if len(stack) == 0 else False
        else:
            return False
