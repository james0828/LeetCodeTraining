class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        tmp = prices[0]
        
        for price in prices:
            if price > tmp:
                ans += price - tmp
            tmp = price
        
        return ans
