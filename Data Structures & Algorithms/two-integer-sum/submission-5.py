class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in nums and nums.index(pair) != i:
                match = [i,nums.index(pair)]
                match.sort()
                return match
