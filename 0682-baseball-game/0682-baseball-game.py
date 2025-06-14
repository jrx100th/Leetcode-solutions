class Solution:
    def calPoints(self, operations: List[str]) -> int:
        game = []
        for op in operations:
            if op != "C" and op!= "D" and op!= "+":
                game.append(int(op))
            if op == "C":
                game.remove(game[-1])
            if op == "D":
                game.append(2*game[-1])
            if op == "+":
                game.append(game[-1]+game[-2])

        return sum(game)