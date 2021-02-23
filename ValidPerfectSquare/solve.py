class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 0
        e = 2 ** 31 - 1
        while True:
            if abs(s - e) == 1:
                return s ** 2 == num or e ** 2 == num

            mid = (s + e) // 2
            if mid ** 2 == num: return True
            elif mid ** 2 > num: e = mid
            else: s = mid
