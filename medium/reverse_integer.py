import sys
sys.path.append('../common')
from lc_stats import LC

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x_list = [i for i in x]
        x_list.reverse()
        if "-" in x_list:
            ret_val = int(''.join(x_list[0:len(x_list) - 1])) * - 1
            return ret_val if ret_val > -2**31 else 0
        ret_val = int(''.join(x_list))
        return ret_val if ret_val < 2**31 else 0
    
    def set_lc_stats(self, runtime, memory_used, faster_than, lc_num, url, title):
        self.lc = LC(runtime, memory_used, faster_than, lc_num, url, title)

s = Solution()
test_str = '-321'
print(s.reverse(test_str))

s.set_lc_stats(35, 13.9, .904, 7, 'https://leetcode.com/problems/reverse-integer/', 'Reverse Integer')
print(s.lc)
