class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length1 = len(num1)
        length2 = len(num2)
        if length1 > length2:
            num2 = (length1 - length2) * '0' + num2
        elif length2 > length1:
            num1 = (length2 - length1) * '0' + num1

        carry = False
        ans = ""
        length = len(num1)
        ord0 = ord('0')
        for i in range(0, length):
            tmp = ord(num1[length - 1 - i]) + ord(num2[length - 1 - i]) - ord0
            if carry:
                carry = False
                tmp += 1

            if tmp >= 10 + ord0:
                carry = True
                ans += chr(tmp - 10)
            else:
                ans += chr(tmp)
        
        if carry:
            ans += '1'
        
        return ans[::-1]
