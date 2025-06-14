class Solution:
    def judgeCircle(self, moves: str) -> bool:
        n = [0,0]

        for move in moves:
            if move == 'L':
                n[0]-=1
            elif move == 'D':
                n[1]-=1
            elif move == 'U':
                n[1]+=1
            else:
                n[0]+=1

        if n == [0,0]:
            return True
        return False