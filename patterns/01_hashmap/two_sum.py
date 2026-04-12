"""
[Tên bài]  |  LeetCode #[số]  |  [Easy / Medium / Hard]
Pattern : Hashmap
Link    : https://leetcode.com/problems/two-sum/editorial/
Date    : [ngày làm] 9/4/2026

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Input : nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]  (vì nums[0] + nums[1] = 2 + 7 = 9)

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    Only one valid answer exists.

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(n^2)]
    Dùng 2 vòng lặp lồng nhau để kiểm tra tất cả cặp số trong mảng.
    Nếu tìm thấy cặp nào có tổng bằng target, trả về chỉ số của chúng.

Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]

    Tại sao dùng [pattern]?
        Hashmap giúp tra cứu complement một cách nhanh chóng, chỉ O(1) thời gian.
        Điều này làm giảm tổng thời gian từ O(n^2) xuống O(n).
    [Giải thích logic chính]

        Dùng một hashmap để lưu trữ các số đã gặp và chỉ số của chúng.
        Khi duyệt qua mảng, với mỗi số nums[i], tính complement = target - nums[i].
        Kiểm tra xem complement đã tồn tại trong hashmap chưa.
        Nếu có, trả về chỉ số của complement và i.
    Nếu không, thêm nums[i] vào hashmap với chỉ số i.

Complexity:
    Time : O(n)
    Space: O(n)  (trường hợp xấu nhất khi tất cả phần tử đều khác nhau)

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

# Brute force: O(n^2) time, O(1) space


def two_sum_brute(nums: List[int], target: int) -> Optional[List[int]]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return None


# Optimal: O(n) time, O(n) space


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None


def two_sum_all(nums: List[int], target: int) -> List[List[int]]:
    num_to_index = {}
    result = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            result.append([num_to_index[complement], i])
        num_to_index[num] = i
    return result


print(two_sum_all([1, 2, 3, 4, 5,2,3], 5))  # [[1, 2], [0, 3]]
print(two_sum_all([1, 3, 2, 4, 3, 6], 6))  # [[2, 3], [1, 4]]


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------
def test():
    # Happy path
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Edge case: 2 phần tử giống nhau
    assert two_sum([3, 3], 6) == [0, 1]

    # Edge case: số âm
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # Edge case: target âm
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

    # Verify brute force cho ra kết quả giống optimal
    import random

    for _ in range(100):
        nums = random.sample(range(-50, 50), 10)
        target = nums[0] + nums[1]
        assert two_sum_brute(nums, target) == two_sum(nums, target)

    print("All tests passed!")


if __name__ == "__main__":
    test()
