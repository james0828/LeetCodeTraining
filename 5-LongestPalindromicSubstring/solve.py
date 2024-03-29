class Solution:
    def longestPalindrome(self, s):
        if not s: return ''
        elif len(s) <= 1: return s
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            length = max(self.expandAroundCenter(s, i, i) \
                         , self.expandAroundCenter(s, i, i+1))
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
            
        return s[start:end+1]
    
    def expandAroundCenter(self, s, l, r):
        L, R = l, r
        
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        
        return R - L - 1
                
