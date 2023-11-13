class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        tmp = []
        count = 0
        dc = {'}': '{',
            ')': '(',
            ']': '['}
        
        if len(s) % 2 != 0:
            return False
        
        for pos, val in enumerate(s):
            if val in dc.values():
                tmp.append(val)
                count += 1
            if tmp and val in dc.keys():
                if dc[val] == tmp[-1]:
                    tmp.pop()
                else:
                    return False  
        print(count)            
        if tmp:
            return False
        elif not tmp and count == 0:
            return False
        else:
            return True
