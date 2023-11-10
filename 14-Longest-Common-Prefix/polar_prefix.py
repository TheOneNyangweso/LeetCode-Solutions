class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        t=""
        strs.sort()
        if not strs or not any(strs):
             return ""
        for i in range(len(strs[0])):
            if i < len(strs[-1]) and strs[0][i] == strs[-1][i]:
                t += strs[0][i]
            else:
                break
        return t
   
