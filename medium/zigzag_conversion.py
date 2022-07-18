import sys
sys.path.append('../common')
from lc_stats import LC


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str_matrix = []
        for num in range(numRows):
            str_matrix.append([])
        max_val = len(str_matrix) - 1
        matrix_val = 0
        direction = 'down'
        if numRows == 1:
            return s
        for l in s:
            str_matrix[matrix_val].append(l)
            if direction == 'down':
                matrix_val += 1
            elif direction == 'up':
                matrix_val -= 1
            if matrix_val == -1:
                direction = 'down'
                matrix_val += 2
            if matrix_val == max_val + 1:
                direction = 'up'
                matrix_val -= 2

        out_str = ''
        for i in str_matrix:
            out_str += ''.join(i)

        return out_str

    def set_lc_stats(self, runtime, memory_used, faster_than, lc_num, url, title):
        self.lc = LC(runtime, memory_used, faster_than, lc_num, url, title)


s = Solution()
test_str = 'PAYPALISHIRING'
num_rows = 3
s.convert(test_str, num_rows)

s.set_lc_stats(65, 14.1, .8687, 6, 'https://leetcode.com/problems/zigzag-conversion/', 'Zigzag Conversion')
print(s.lc)