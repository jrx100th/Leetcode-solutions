class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        x =  edges[0][0] 
        res = True
        for i in edges:
            if x not in i:
                res = False
        
        if res:
            return x
        
        y = edges[0][1] 
        res = True
        for i in edges:
            if y not in i:
                res = False
        
        if res:
            return y