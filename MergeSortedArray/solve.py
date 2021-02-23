class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s1 = m - 1
        s2 = n - 1
        for i in range(m+n):
            index = m + n - i - 1
            if s1 == -1:
                nums1[index] = nums2[s2]
                s2 -= 1
            elif s2 == -1:
                nums1[index] = nums1[s1]
                s1 -= 1
            else:
                if nums1[s1] > nums2[s2]:
                    nums1[index] = nums1[s1]
                    s1 -= 1
                else:
                    nums1[index] = nums2[s2]
                    s2 -= 1
