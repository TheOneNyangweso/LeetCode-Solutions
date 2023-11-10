class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        elif len(strs) > 1:  # checks if the first character in first word is
            if len(strs[0]) > 0:
                for char in range(len(strs[0])):  # Loops through characters of the first element
                    if strs[0][char] == strs[-1][char]:
                        prefix += strs[0][char]
                    else:
                        return prefix
            else:
                return prefix
        return prefix
