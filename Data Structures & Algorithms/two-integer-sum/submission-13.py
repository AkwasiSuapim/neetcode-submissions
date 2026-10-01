class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index,number in enumerate(nums):
            compliment = target - number
            if compliment in seen:
                return [seen[compliment],index]
            else:
                seen[number] = index
