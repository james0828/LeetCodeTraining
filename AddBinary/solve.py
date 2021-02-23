class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = ""
        if len(a) > len(b):
            b = (len(a) - len(b)) * '0' + b
        elif len(b) > len(a):
            a = (len(b) - len(a)) * '0' + a
        
        length = len(a)
        
        carry = False
        for i in range(0, length):
            num = ord(a[length-i-1]) + ord(b[length-i-1]) - ord('0')
            if carry:
                num += 1
            if num >= ord('0') + 2:
                num -= 2
                carry = True
            else:
                carry = False
            s = chr(num) + s
        
        if carry:
            s = '1' + s
        
        return s
