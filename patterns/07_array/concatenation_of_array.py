"""
Concatenation of Array  |  LeetCode #1929  |  Easy
Pattern : Array
Link    : https://leetcode.com/problems/concatenation-of-array/
Date    : 12/4/2026

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:
    Input: nums = [1,2,1]
    Output: [1,2,1,1,2,1]

Example 2:
    Input: nums = [1,3,2,1]
    Output: [1,3,2,1,1,3,2,1]

Constraints:
    n == nums.length
    1 <= n <= 500
    1 <= nums[i] <= 10^4

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(?)]

Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    Tại sao dùng [pattern]?
    [Giải thích logic chính]

Complexity:
    Time : O(?)
    Space: O(?)

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [ ] Mảng rỗng: []
- [ ] 1 phần tử: [x]
- [ ] Tất cả giống nhau: [x, x, x]
- [ ] [Edge case đặc thù của bài này]
"""

from typing import List


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------


# Cách 1: Dùng toán tử + để nối hai mảng
def solution_brute(nums: List[int]) -> List[int]:
    return nums + nums


# Cách 2: Dùng list comprehension để tạo mảng mới
def solution_optimal(nums: List[int]) -> List[int]:
    n = len(nums)
    return [nums[i % n] for i in range(2 * n)]


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------


def test():
    # Happy path — ví dụ bình thường
    # assert solution(...) == ...
    assert solution_brute([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert solution_brute([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert solution_optimal([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert solution_optimal([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]

    # Edge cases
    # assert solution([]) == ...
    assert solution_brute([1]) == [1, 1]
    assert solution_brute([2, 2, 2]) == [2, 2, 2, 2, 2, 2]
    assert solution_optimal([1]) == [1, 1]
    assert solution_optimal([2, 2, 2]) == [2, 2, 2, 2, 2, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test()
