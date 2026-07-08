class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}

        for num in nums:
            if num in table:
                table[num] +=1
            else:
                table[num] = 1

       
        sorted_table = sorted(table.items(), key = lambda pair:pair[1] )

        by_k = list(sorted_table[-k::1])
        final =[]
        for num in by_k:
            final.append(num[0])

        return final
        
