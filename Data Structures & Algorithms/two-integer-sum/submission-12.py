class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        dicts = {}
        for i,j in enumerate(nums):
            if j not in dicts:
                dicts[j] = i
            else:
                seen[j] = i

        for k in dicts:
            complement = target - k
            if complement in dicts:
                if complement != k: 
                    return sorted([dicts[k], dicts[complement]])
                elif complement in seen:
                    return sorted([dicts[k],seen[complement]])
            
        return []
             