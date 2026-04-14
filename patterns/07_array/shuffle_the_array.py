"""
Shuffle the Array  |  LeetCode #1470  |  Easy
Pattern : Array
Link    : https://leetcode.com/problems/shuffle-the-array/
Date    : 12/4/2026

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7]
    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
    Input: nums = [1,2,3,4,4,3,2,1], n = 4
    Output: [1,4,2,3,3,2,4,1]

Example 3:
    Input: nums = [1,1,2,2], n = 2
    Output: [1,2,1,2]

Constraints:
    1 <= n <= 500
    nums.length == 2 * n
    1 <= nums[i] <= 10^3

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:

    [Mô tả cách đơn giản nhất — O(?)]
    Tạo một mảng mới có kích thước 2n.
    Duyệt qua mảng nums từ 0 đến n-1, và lần lượt gán giá trị vào mảng mới theo thứ tự x1, y1, x2, y2, ..., xn, yn.
    Cụ thể, gán ans[2*i] = nums[i] và ans[2*i + 1] = nums[i + n].
    Trả về mảng mới.


Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    Tại sao dùng [pattern]?
    [Giải thích logic chính]
    Cách tiếp cận tối ưu vẫn là tạo một mảng mới, nhưng chúng ta có thể gán giá trị trực tiếp trong một vòng lặp duy nhất.
    Duyệt qua mảng nums từ 0 đến n-1, và gán giá trị vào mảng mới theo thứ tự x1, y1, x2, y2, ..., xn, yn.
    Cụ thể, gán ans[2*i] = nums[i] và ans[2*i + 1] = nums[i + n].
    Trả về mảng mới.

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

from typing import List, Optional


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------


def shuffle_solution_1(nums: List[int], n: int):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res

def shuffle_solution_2(nums: List[int], n: int):
    return [num for i in range(n) for num in (nums[i], nums[i + n])]    





# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------


def test():
    # Happy path — ví dụ bình thường
    # assert solution(...) == ...

    # Edge cases
    # assert solution([]) == ...

    print("All tests passed!")


if __name__ == "__main__":
    test()
