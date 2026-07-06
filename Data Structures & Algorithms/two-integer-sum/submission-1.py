class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    if i < j:
                        return [i,j]
                    else:
                        return [j,i]
                j +=1