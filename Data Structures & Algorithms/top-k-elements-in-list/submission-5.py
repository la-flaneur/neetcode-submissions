class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #key, value pairs of number (key) and value (frequency)
        frequency = [[] for i in range(len(nums) + 1)] #array where frequency is index and 
        #contents are arrays of matching numbers
        
        #get frequency of each number by incrementing value by key
        for n in nums:
            count[n] = 1 + count.get(n,0)
        #sort said frequencies into matching groups
        for n, c in count.items():
            frequency[c].append(n)

        result = []
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result
