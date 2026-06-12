"""
Maximum Average Subarray I  |  LeetCode #643  |  Easy
Pattern : Sliding Window
Link    : https://leetcode.com/problems/maximum-average-subarray-i/
Date    :

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this maximum average. Any answer within 10^-5 of
the correct answer will be accepted.

Example 1:
    Input : nums = [1, 12, -5, -6, 50, 3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 + (-5) + (-6) + 50) / 4 = 51 / 4 = 12.75

Example 2:
    Input : nums = [5], k = 1
    Output: 5.00000

Constraints:
    n == nums.length
    1 <= k <= n <= 10^5
    -10^4 <= nums[i] <= 10^4

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(n*k)]
    Dùng 2 vòng lặp lồng nhau để kiểm tra tất cả các subarray có độ dài k.
    Vòng ngoài duyệt từ 0 đến n-k, vòng trong tính tổng của subarray từ i đến i+k-1.
    Cập nhật giá trị max_average nếu tổng hiện tại lớn hơn max_average.
    Trả về max_average sau khi duyệt hết.


Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    Tại sao dùng Sliding Window?
    [Giải thích logic chính]

Complexity:
    Time : O(?)
    Space: O(?)

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [ ] k = n (toàn bộ mảng)
- [ ] k = 1 (mỗi phần tử là 1 cửa sổ)
- [ ] Tất cả số âm: [-1, -2, -3]
- [ ] Tất cả số dương: [1, 2, 3]
- [ ] Số âm và số dương lẫn lộn
"""

from typing import List


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------


def find_max_average_brute_force(nums: List[int], k: int) -> float:
    n = len(nums)
    max_avg = float("-inf")
    # n-k+1 vì mỗi vòng chỉ chạy tới n-k với vòng ngoài( nếu chạy hơn sẽ quá độ dài mảng)
    for i in range(n - k + 1):
        total = 0
        for j in range(i, k + i):
            total += nums[j]
        max_avg = max(max_avg, total / k)
    return max_avg


def find_max_average_optimal(nums: List[int], k: int) -> float:
    window_sum = sum(nums[:k])  # tinh tong va k phan tu dau tien
    max_sum = window_sum
    n = len(nums)
    for i in range(n - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k


print(f" keest qua la : {find_max_average_optimal([1, 12, -5, -6, 50, 3], 4)}")


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------


def test():
    # Happy path
    # assert abs(find_max_average([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-5
    # assert find_max_average([5], 1) == 5.0

    # Edge cases
    # assert find_max_average([0, 4, 0, 3, 2], 5) == 1.8

    print("All tests passed!")


if __name__ == "__main__":
    test()
