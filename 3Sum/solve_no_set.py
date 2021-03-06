class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        next_list = [0 for i in range(len(nums))]
        last_list = [0 for i in range(len(nums))]
        
        nums.sort()
        
        index = 0
        while index < len(nums) -1:
            tmp = index
            while index < len(nums) -1 and nums[index] == nums[index+1]: index += 1
            index += 1
            next_list[tmp] = index
        
        index = len(nums)-1
        while index > 0:
            tmp = index
            while index > 0 and nums[index] == nums[index-1]: index -= 1
            index -= 1
            last_list[tmp] = index

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]: continue
            s = i+1
            j = len(nums)-1
            while s < j:
                if nums[s] + nums[j] + num == 0:
                    ans.append([num, nums[s], nums[j]])
                    s = next_list[s]
                    j = last_list[j]
                else:
                    if nums[s] + nums[j] + num > 0:
                        j = last_list[j]
                    else:
                        s = next_list[s]
        
        return ans
