class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []

        for i in range(1,max(target)+1):
            if i in target:
                res.append("Push")
            elif i not in target:
                res.append("Push")
                res.append("Pop")
        
        return res