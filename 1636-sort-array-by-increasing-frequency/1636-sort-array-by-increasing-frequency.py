class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        # Sort: first by frequency (ascending), then by value (descending)
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
