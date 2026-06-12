"""
Longest Common Prefix  |  LeetCode #14  |  Easy
Pattern : Array
Link    : https://leetcode.com/problems/longest-common-prefix/
Date    :

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input : strs = ["flower", "flow", "flight"]
    Output: "fl"

Example 2:
    Input : strs = ["dog", "racecar", "car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(n * m)]

Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    Tại sao dùng Array?
    [Giải thích logic chính]

Complexity:
    Time : O(?)
    Space: O(?)

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [ ] Mảng rỗng: []
- [ ] 1 phần tử: ["abc"]
- [ ] Có chuỗi rỗng trong mảng: ["", "abc"]
- [ ] Tất cả giống nhau: ["aa", "aa"]
- [ ] Không có prefix chung: ["abc", "xyz"]
"""

from typing import List


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------

def longest_common_prefix(strs: List[str]) -> str:
    # Viết code ở đây
    pass


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------

def test():
    # Happy path
    # assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    # assert longest_common_prefix(["dog", "racecar", "car"]) == ""

    # Edge cases
    # assert longest_common_prefix([""]) == ""
    # assert longest_common_prefix(["a"]) == "a"
    # assert longest_common_prefix(["abc", "abc"]) == "abc"

    print("All tests passed!")


if __name__ == "__main__":
    test()
