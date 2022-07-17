from typing import List
import sys
sys.path.append('../common')
from lc_stats import LC

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for loc, val in enumerate(nums):
            try:
                if nums[loc] + nums[loc + 1] == target:
                    return [loc, (loc + 1)]
            except IndexError:
                quit()
    
    def set_lc_stats(self, runtime, memory_used, faster_than, lc_num, url, title):
        self.lc = LC(runtime, memory_used, faster_than, lc_num, url, title)
    
    def get_lc_stats(self):
        return self.lc


s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))

s.set_lc_stats(807, 15, .3317, 1, 'https://leetcode.com/problems/two-sum/submissions/', 'Two Sums')
print(s.get_lc_stats())
