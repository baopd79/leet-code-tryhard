"""
Merge Sorted Array  |  LeetCode #88  |  Easy
Pattern : Two Pointers
Link    : https://leetcode.com/problems/merge-sorted-array/
Date    :

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of valid elements in nums1
and nums2 respectively.

Merge nums2 into nums1 as one sorted array.

Note: You may assume that nums1 has enough space (total length is m + n) to hold
additional elements from nums2. Do not return anything, modify nums1 in-place instead.

Example 1:
    Input : nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    Output: [1, 2, 2, 3, 5, 6]
    Explanation: We merge [1, 2, 3] and [2, 5, 6] to get [1, 2, 2, 3, 5, 6].

Example 2:
    Input : nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: We merge [1] and [] to get [1].

Example 3:
    Input : nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: We merge [] and [1] to get [1].

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -10^9 <= nums1[i], nums2[i] <= 10^9

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O((m+n) log (m+n))]
    cách đơn giản nhất là hợp nhất 2 mảng nums1 và nums2 thành một mảng mới, sau đó sắp xếp mảng mới. Tuy nhiên, cách này không tận dụng được tính chất đã được sắp xếp của hai mảng đầu vào và có độ phức tạp thời gian O((m+n) log (m+n)).

Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    đầu tiên, chúng ta sử dụng ba con trỏ : p1,p2 và p để theo dõi vị trí hiện tại trong nums1, nums2 và vị trí để chèn phần tử tiếp theo vào nums1.
    Chúng ta sẽ bắt đầu từ cuối của nums1 và nums2, so sánh phần tử tại p1 và p2, và chèn phần tử lớn hơn vào vị trí p trong nums1. Sau đó, chúng ta di chuyển con trỏ tương ứng (p1 hoặc p2) và con trỏ p về phía trước.
    Quá trình này tiếp tục cho đến khi chúng ta đã duyệt hết phần tử của nums2 (p2 < 0). Nếu còn phần tử nào của nums1 chưa được duyệt (p1 >= 0), chúng ta sẽ giữ nguyên chúng vì chúng đã ở đúng vị trí.
    Tại sao dùng Two Pointers?
    [Giải thích logic chính]
    tại vì chúng ta cần duyệt qua cả hai mảng cùng một lúc để so sánh và hợp nhất chúng, nên sử dụng hai con trỏ là một cách tiếp cận hiệu quả để giải quyết vấn đề này.

Complexity:
    Time : O(m + n)
    Space: O(1) - vì chúng ta chỉ sử dụng một số biến phụ để theo dõi vị trí của con trỏ, và không sử dụng thêm mảng nào để lưu trữ kết quả.

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [ ] nums2 rỗng: nums1 = [1], nums2 = [], m = 1, n = 0
- [ ] nums1 rỗng: nums1 = [0], nums2 = [1], m = 0, n = 1
- [ ] Tất cả phần tử nums1 nhỏ hơn nums2
- [ ] Tất cả phần tử nums1 lớn hơn nums2
- [ ] Các phần tử lẫn lộn
"""

from typing import List


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------


def merge_brute_force(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Hợp nhất nums1 và nums2 vào một mảng mới
    merged = nums1[:m] + nums2[:n]
    # Sắp xếp mảng mới
    merged.sort()
    # Sao chép mảng đã sắp xếp trở lại nums1
    for i in range(m + n):
        nums1[i] = merged[i]


def merge_optimal(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------


def test():
    # Happy path
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge_brute_force(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    merge_brute_force(nums1, 1, [], 0)
    assert nums1 == [1]

    # Edge cases
    nums1 = [0]
    merge_brute_force(nums1, 0, [1], 1)
    assert nums1 == [1]

    print("All tests passed!")


if __name__ == "__main__":
    test()
