class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        l = len(s)
        for i in range(l):
            if s[l-i-1] != ' ':
                ans += 1
            elif s[l-i-1] == ' ' and ans != 0:
                break

        return ans
