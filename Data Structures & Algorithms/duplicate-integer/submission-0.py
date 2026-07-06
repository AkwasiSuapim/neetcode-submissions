class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # self.duplicate = False
        # lent = len(nums)
        # for i in range(lent):
        #     j = i + 1
        #     while j < lent:
        #         if nums[i] != nums[j]:
        #             j+=1
        #         else:
        #             self.duplicate = True
        #             return self.duplicate
        # return self.duplicate



        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

                    

            
        