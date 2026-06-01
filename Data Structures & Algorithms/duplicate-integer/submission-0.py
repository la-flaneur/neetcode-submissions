class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = []
        for i in range(len(nums)):
            if nums[i] in has:
                return True
            else:
                has.append(nums[i])
        return False