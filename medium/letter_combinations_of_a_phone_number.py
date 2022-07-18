from typing import List
import sys
sys.path.append('../common')
from lc_stats import LC


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        button_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        output_list = []
        num_list = [x for x in digits]

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return button_map[digits]
        else:
            target = [len(button_map[x]) - 1 for x in digits]
            current = [0 for _ in range(len(target))]
            working_index = len(target) - 1
            while True:
                new_str = ''
                for idx, val in enumerate(current):
                    new_str += button_map[num_list[idx]][val]
                output_list.append(new_str)
                if target == current:
                    break
                if current[working_index] + 1 > target[working_index]:
                    while True:
                        try:
                            current[working_index] = 0
                            working_index -= 1
                            if current[working_index] + 1 <= target[working_index]:
                                current[working_index] += 1
                                working_index = len(target) - 1
                                break
                        except IndexError:
                            print("Error")
                            break
                else:
                    current[working_index] += 1
        return output_list 

    def set_lc_stats(self, runtime, memory_used, faster_than, lc_num, url, title):
        self.lc = LC(runtime, memory_used, faster_than, lc_num, url, title)

s = Solution()
test_str = '234'
print(s.letterCombinations(test_str))

s.set_lc_stats(25, 14, .9914, 17, 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/', 'Letter Combinations of a Phone Number')
print(s.lc)