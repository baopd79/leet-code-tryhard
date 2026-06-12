"""
Reverse String  |  LeetCode #344  |  Easy
Pattern : Two Pointers
Link    : https://leetcode.com/problems/reverse-string/
Date    :

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Write a function that reverses a string. The input string is given as an
array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input : s = ["h", "e", "l", "l", "o"]
    Output: ["o", "l", "l", "e", "h"]

Example 2:
    Input : s = ["H", "a", "n", "n", "a", "h"]
    Output: ["h", "a", "n", "n", "a", "H"]

Constraints:
    1 <= s.length <= 10^5
    s[i] is a printable ASCII character.

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(n)]

Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    Tại sao dùng Two Pointers?
    [Giải thích logic chính]

Complexity:
    Time : O(?)
    Space: O(?)

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [ ] Mảng 1 phần tử: ["a"]
- [ ] Mảng 2 phần tử: ["a", "b"]
- [ ] Số phần tử lẻ vs chẵn
"""

from typing import List


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------

def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # Viết code ở đây
    pass


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------

def test():
    # Happy path
    # s = ["h","e","l","l","o"]; reverse_string(s); assert s == ["o","l","l","e","h"]
    # s = ["H","a","n","n","a","h"]; reverse_string(s); assert s == ["h","a","n","n","a","H"]

    # Edge cases
    # s = ["a"]; reverse_string(s); assert s == ["a"]

    print("All tests passed!")


if __name__ == "__main__":
    test()
