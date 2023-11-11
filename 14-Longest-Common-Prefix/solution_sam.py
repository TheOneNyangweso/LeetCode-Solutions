class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first_val = strs[0]
        
        for letter in first_val:
            for s in strs:
                if s.startswith(res + letter) == False:
                    return res
            res += letter

        return res
                
