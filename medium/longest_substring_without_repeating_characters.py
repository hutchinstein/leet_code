import sys
sys.path.append('../common')
from lc_stats import LC


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        solutions = {}
        temp = []
        for loc, let in enumerate(s):
            if let not in temp:
                temp.append(let)
            else:
                temp = temp[temp.index(let) + 1:]
                temp.append(let)
            solutions[len(temp)] = temp
        try:
            return max(solutions.keys())
        except ValueError:
            return 0

    def set_lc_stats(self, runtime, memory_used, faster_than, lc_num, url, title):
        self.lc = LC(runtime, memory_used, faster_than, lc_num, url, title)

s = Solution()
test_str = 'abcabcbb'
print(s.lengthOfLongestSubstring(test_str))

s.set_lc_stats(91, 14, .6422, 3, 'https://leetcode.com/problems/longest-substring-without-repeating-characters', 'Longest Substring Without Repeating Characters')
print(s.lc)