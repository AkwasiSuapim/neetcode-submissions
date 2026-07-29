class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #get the set form for easy lookup
        #for each num check if num - 1 is in there, if it is, go to the next else put it in a set called start points
        #for each item in start point, check if num +1 exist in the main set, if it does check for num+2 until it doesn't exist, then move to next point in start point

        nums = set(nums)
        start_points = set()

        for num in nums:
            if num -1 in nums:
                continue
            else:
                start_points.add(num)
        
        max_lent = 0

        for point in start_points:
            n = 1
            current_lent = 1

            while (point + n) in nums:
                n += 1
                current_lent += 1

            if current_lent > max_lent:
                max_lent = current_lent

        return max_lent
                