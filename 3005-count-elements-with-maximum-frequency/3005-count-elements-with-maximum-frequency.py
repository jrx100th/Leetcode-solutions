class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        counter = dict(sorted(counter.items(), key = lambda x:x[1], reverse = True))

        n = 0
        current_max = 0
        for num in counter:
            if counter[num] > current_max:
                current_max = counter[num]
            while counter[num] == current_max:
                n+=current_max
                break
        return n