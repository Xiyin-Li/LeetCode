class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            diff = target - nums[i] 
            try:
                # If the diff is not in the list, we continue the for loop
                sec_index = nums.index(diff,i+1)
                result.append(i)
                result.append(sec_index)  
                return result
            except ValueError:
                continue
