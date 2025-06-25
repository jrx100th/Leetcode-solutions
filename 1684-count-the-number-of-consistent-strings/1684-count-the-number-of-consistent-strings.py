class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    n+=1
                    break
        return len(words)-n