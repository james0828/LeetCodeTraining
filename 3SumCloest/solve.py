class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        m = abs(ans - target)
        
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num: continue
            b, e = i+1, len(nums)-1
            
            while b < e:
                v = num + nums[b] + nums[e]
                diff = v-target
                if abs(diff) < m:
                    m = abs(v-target)
                    ans = v
                
                if diff > 0:
                    e -= 1
                else:
                    b += 1
        
        return ans
