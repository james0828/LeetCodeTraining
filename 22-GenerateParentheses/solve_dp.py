class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tmp = [[0]]
        for i in range(1, n):
            tmp = self.calculate(tmp, i+1)
        
        s = []

        for i in tmp:
            ans = ""
            for j in range(n * 2):
                if j in i:
                    ans += '('
                else:
                    ans += ')'
            if not ans in s:
                s.append(ans)
        
        return s
    
    def calculate(self, l, s):
        big = s * 2
        ans = []
        for i in l:
            for k in range(i[-1]+1, big-1):
                ans.append(i + [k])
        
        return ans
