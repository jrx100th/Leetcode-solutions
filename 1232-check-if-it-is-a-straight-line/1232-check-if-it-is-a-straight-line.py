class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range (2, len(coordinates)) :   
            result = ( (coordinates[1][0] - coordinates[0][0]) * (coordinates[i][1] - coordinates[0][1]) ) - ((coordinates[1][1] - coordinates[0][1]) * (coordinates[i][0] - coordinates[0][0])) 
            if result  !=  0  :   
                return  False   
        return  True   