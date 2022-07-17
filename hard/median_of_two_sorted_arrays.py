from typing import List
import sys
sys.path.append('../common')
from lc_stats import LC

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_nums = nums1 + nums2
        combined_nums.sort()
        if (len(combined_nums) % 2) == 0:
            middle_location_right = int(len(combined_nums) / 2)
            middle_location_left = middle_location_right - 1
            return (combined_nums[middle_location_left] + combined_nums[middle_location_right]) / 2
        else:
            middle_location = int(len(combined_nums) / 2)
            return combined_nums[middle_location] / 1

    def set_lc_stats(self, runtime, memory_used, faster_than, lc_num, url, title):
        self.lc = LC(runtime, memory_used, faster_than, lc_num, url, title)
    
    def get_lc_stats(self):
        return self.lc

s = Solution()
nums1 = [1,2]
nums2 = [3,4]
s.findMedianSortedArrays(nums1, nums2)

s.set_lc_stats(102, 14.1, .8787, 4, 'https://leetcode.com/problems/median-of-two-sorted-arrays/', 'Median of Two Sorted Arrays')
print(s.get_lc_stats())
