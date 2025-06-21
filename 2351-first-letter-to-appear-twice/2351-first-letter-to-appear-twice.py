class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        seen = set()

        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
            else:
                return s[i]
        # learn dictionaries in a better and effecient way