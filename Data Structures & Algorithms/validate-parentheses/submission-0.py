class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        res = []
        for char in s:
            if char in par:
                if res and res[-1] == par[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        
        return False if res else True