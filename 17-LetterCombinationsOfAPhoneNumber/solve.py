class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        ans = []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, step):
            if index == len(digits):
                ans.append("".join(step))
                return
            
            s = digit_map[digits[index]]
            for i in s:
                step.append(i)
                backtrack(index+1, step)
                step.pop()
        
        backtrack(0, [])
        
        return ans
