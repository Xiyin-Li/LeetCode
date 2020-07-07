class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        # Store the index and the item to the hashmap, each key has its own hash value
        for i, item in enumerate(nums):
            hashMap[item] = i
        for i, item in enumerate(nums):
            # The best case time complexity for hashMap.get() is O(1) while
            # the worst case time complexity is O(n)(with collision)
            j = hashMap.get(target - item)
            if hashMap.get(target - item) is not None and i !=j :
                return [i,j]
