class Solution:
    def __init__(self):
        self.lents = []
    def encode(self, strs: List[str]) -> str:
            for i in strs:
                self.lents.append(len(i))
            coded = ""

            for i in strs:
                coded = coded + i

            return coded   



    def decode(self, s: str) -> List[str]:
        decoder = []
        b = 0
        j = 0
        for i in range(len(self.lents)):
            decoder.append(s[b:b+int(self.lents[j])])
            b += int(self.lents[j])
            j +=1

        return decoder




        
