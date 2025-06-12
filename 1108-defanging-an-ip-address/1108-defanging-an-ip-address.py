class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        r = ""
        for i in range(len(address)):
            if address[i] == '.':
                r += '[.]'
            else:
                r+=address[i]
            
        return r