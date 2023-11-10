class Solution:
    def romanToInt(self, s: str) -> int:
        roman_rep = {'I' : 1,
                    'V' : 5,
                    'X' : 10,
                    'L' : 50,
                    'C' : 100,
                    'D' : 500,
                    'M' : 1000}
        l = list(s[::-1])

        res = 0
        count = 0
        while count < len(l):
            print(res)
            try:
                if roman_rep[l[count]] > roman_rep[l[count + 1]]:
                    res += (roman_rep[l[count]] - roman_rep[l[count + 1]])
                    count += 2
                else:
                    res += roman_rep[l[count]]
                    count += 1
            except: # handle IndexError
                res += roman_rep[l[count]]
                count += 1 

        return res
