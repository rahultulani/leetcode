class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_set = (set(nums))
        nums.clear()
        
        for i in (num_set):
            nums.append(i)
        nums.sort()
        return len(nums)

        