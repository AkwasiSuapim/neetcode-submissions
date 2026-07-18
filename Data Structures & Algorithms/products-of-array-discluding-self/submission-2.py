class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        right = []
        for i in range(len(nums)):
            if i ==0:
                left.append(nums[i])
                right.append(nums[::-1][i])
            else:
                left.append(left[i-1]*nums[i])
                right.append(nums[::-1][i]* right[i-1])
        
        for i in range(len(nums)):
            if i == 0:
                lefty = 1
                righty = right[::-1][i +1]
            elif i ==len(nums)-1:
                lefty = left[i-1]
                righty = 1
            else:
                lefty = left[i-1]
                righty = right[::-1][i +1]
            nums[i] = righty *lefty

        return nums


    
        