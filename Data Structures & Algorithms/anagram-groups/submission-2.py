class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.strs = strs
        self.groups = {}

        for word in self.strs:
            sign = "".join(sorted(word))
            if sign in self.groups:
                self.groups[sign].append(word)

            else:
                self.groups[sign] = [word]
        return list(self.groups.values())