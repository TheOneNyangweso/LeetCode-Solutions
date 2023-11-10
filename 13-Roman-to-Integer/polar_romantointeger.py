class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,
                  "L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        roman=0
        i=0
        while i < len(s):
            if i + 1 < len(s) and dict_roman[s[i]] < dict_roman[s[i + 1]]:
                roman += dict_roman[s[i + 1]] - dict_roman[s[i]]
                i += 2
            else:
                roman += dict_roman[s[i]]
                i += 1
        return roman
