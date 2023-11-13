class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_list = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                my_list.append(s[i])
            elif s[i] == ")":
                if "(" in my_list and "(" == my_list[-1]:
                    my_list.pop()
                else:
                    return False
            elif s[i] == "]":
                if "[" in my_list and "[" == my_list[-1]:
                    my_list.pop()
                else:
                    return False
            elif s[i] == "}":
                if "{" in my_list and "{" == my_list[-1]:
                    my_list.pop()
                else:
                    return False

        if len(my_list) == 0:
            return True

