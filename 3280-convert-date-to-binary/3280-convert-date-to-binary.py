class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return str(bin(int(date[0:4])))[2:]+"-"+str(bin(int(date[5:7])))[2:]+"-"+str(bin(int(date[8:])))[2:]
