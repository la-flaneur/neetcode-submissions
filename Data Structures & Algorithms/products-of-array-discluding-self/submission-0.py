class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if j != i:
                    output[i] = output[i]*nums[j]
                j += 1
            i += 1
        
        return output