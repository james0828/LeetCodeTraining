class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = 2 ** 31 - 1
        
        while True:
            val = (e + s) // 2
            if val ** 2 == x: return val
            elif val ** 2 > x: e = val
            else: s = val
            
            if abs(s - e) == 1:
                return s
