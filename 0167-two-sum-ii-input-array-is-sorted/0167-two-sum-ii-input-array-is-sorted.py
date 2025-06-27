class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ## learn more about binary search and come back to the question
        # and even the two pointer approach

        dicti = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in dicti:
                return [dicti[complement], i+1]
            dicti[numbers[i]] = i+1