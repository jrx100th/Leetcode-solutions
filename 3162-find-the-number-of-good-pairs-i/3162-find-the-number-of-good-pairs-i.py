class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1 = dict(enumerate(nums1))
        nums2 = dict(enumerate(nums2))
        n = 0
        for i in nums1:
            for j in nums2:
                if (nums1[i] % (nums2[j]*k)) == 0:
                    n += 1
        return n