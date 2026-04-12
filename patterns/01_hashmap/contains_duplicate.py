"""
Contains Duplicate  |  LeetCode #217  |  Easy
Pattern : HashMap
Link    : https://leetcode.com/problems/contains-duplicate/
Date    : 12/4/2026

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(?)]
    Dùng 2 vòng lặp lồng nhau để kiểm tra tất cả cặp số trong mảng.
    Nếu tìm thấy cặp nào có giá trị bằng nhau, trả về true.
    Nếu duyệt hết mà không tìm thấy, trả về false.

Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]

    Tại sao dùng [pattern]?
    [Giải thích logic chính]
        Dùng một hash set để lưu trữ các số đã gặp.
        Khi duyệt qua mảng, kiểm tra xem số hiện tại đã tồn tại trong hash set chưa.
        Nếu có, trả về true (vì đã có duplicate).
        Nếu không, thêm số vào hash set.
        giải thích hash set là gì?
        hash set là một cấu trúc dữ liệu lưu trữ các phần tử duy nhất, cho phép tra cứu nhanh chóng (O(1) thời gian trung bình).
    Nếu duyệt hết mà không tìm thấy duplicate, trả về false.

Complexity:
    Time : O(n)
    Space: O(n)

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [ ] Mảng rỗng: []
- [ ] 1 phần tử: [x]
- [ ] Tất cả giống nhau: [x, x, x]
- [ ] [Edge case đặc thù của bài này]
"""

from typing import List, Optional


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------
# brute force
def brute_force(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def solution(nums: List[int]) -> bool:
    num_set = set()
    for n in nums:
        if n in num_set:
            return True
        num_set.add(n)
    return False


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------


def test():

    # Happy path — ví dụ bình thường
    # assert solution(...) == ...
    assert solution([1, 2, 3, 1]) == True
    assert solution([1, 2, 3, 4]) == False
    assert brute_force([1, 2, 3, 4]) == False
    assert brute_force([1, 2, 3, 1]) == True

    # Edge cases
    # assert solution([]) == ...
    assert solution([]) == False
    assert solution([1]) == False
    assert solution([1, 1]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test()
