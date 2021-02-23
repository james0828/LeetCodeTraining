class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = False
        length = len(A)
        index = 0
        ans = []
        while True:
            val = K % 10
            if index > length -1:
                tmp = val + 1 if carry else K % 10
                if tmp >= 10:
                    ans.append(tmp - 10)
                    carry = True
                else:
                    ans.append(tmp)
                    carry = False
            else:
                tmp = A[length - index - 1] + val
                if carry:
                    tmp += 1
                if tmp >= 10:
                    A[length - index - 1] = tmp - 10
                    carry = True
                else:
                    A[length - index - 1] = tmp
                    carry = False
            
            index += 1
            
            K = K // 10
            if K == 0 and not carry: break
                            
        
        return ans[::-1] + A
