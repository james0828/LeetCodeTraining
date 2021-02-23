class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        last = True
        for i in range(length):
            if digits[length - i - 1] + 1 != 10:
                digits[length - i - 1] += 1
                last = False
                break
            else:
                digits[length - i - 1] = 0
                
        if last:
            digits.append(1)
            return digits[::-1]
        
        return digits
