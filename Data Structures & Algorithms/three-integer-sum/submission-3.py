class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = set()
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] ==nums[i-1]:
                continue
            else:
                j = i + 1
                k = n - 1
                while j < k: 
                    suum = nums[i] + nums[j] + nums[k]
                    if suum == 0:
                        triple = tuple([nums[i],nums[j],nums[k]])
                        arr.add(triple)
                        j += 1
                        k -= 1
                    elif suum > 0:
                        k -= 1
                    else:
                        j += 1
        return [list(num) for num in arr]

                        


                