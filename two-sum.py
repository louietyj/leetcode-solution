from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_so_far = {}
        for i, num in enumerate(nums):
            if target - num in seen_so_far:
                return [seen_so_far[target - num], i]
            seen_so_far[num] = i
