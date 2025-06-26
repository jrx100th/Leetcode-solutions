class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        res = {}

        for i,value in nums1:
            if i not in res:
                res[i] = value

        for j, val in nums2:
            if j not in res:
                res[j] = val
            else:
                res[j] += val

        return sorted(res.items(), key = lambda x:x)