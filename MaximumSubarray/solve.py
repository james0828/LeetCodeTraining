class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        minv = 0
        acc = 0
        for num in nums:
            acc += num
            
            if acc - minv > ans:
                ans = acc - minv
            
            if acc < minv:
                minv = acc

        return ans
