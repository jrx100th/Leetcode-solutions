class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = set()

        for num in range(len(nums1)):
            if nums1[num] in nums2:
                res.add(nums1[num])
        
        for num in range(len(nums2)):
            if nums2[num] in nums1:
                res.add(nums2[num])

        return list(res)