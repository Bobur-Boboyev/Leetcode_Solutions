# leetcode link: https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        ls = [""] * numRows

        i = 0
        is_asc = True

        for ch in s:
            ls[i] += ch

            if i == 0:
                is_asc = True
            elif i == numRows - 1:
                is_asc = False

            if is_asc:
                i += 1
            else:
                i -= 1

        return "".join(ls)
