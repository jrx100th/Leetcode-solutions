class Solution:
    def groupAnagrams(self, strings: List[str]) -> List[List[str]]:
        tracker = {}
        for string in strings:
            key = str(sorted((string)))
            if key not in tracker:
                tracker[key] = []
            tracker[key].append(string)
        
        return list(tracker.values())
        """dicti = {}
        
        for string in strings:
            key = str((sorted(string)))
            if key not in dicti:
                dicti[key] = []
            dicti[key].append(string)
            
        return list(dicti.values())"""