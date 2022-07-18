from typing import List
import sys
sys.path.append('../common')
from lc_stats import LC

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        min_num = 1
        for num in nums:
            if num > 0:
                if num != min_num:
                    return min_num
                else:
                    min_num += 1
        return min_num 

    def set_lc_stats(self, runtime, memory_used, faster_than, lc_num, url, title):
        self.lc = LC(runtime, memory_used, faster_than, lc_num, url, title)
    

s = Solution()
test_nums = [3,4,-1,1]
print(s.firstMissingPositive(test_nums))

s.set_lc_stats(868, 69.9, .9542, 41, 'https://leetcode.com/problems/first-missing-positive/', 'First Missing Positive')
print(s.lc)