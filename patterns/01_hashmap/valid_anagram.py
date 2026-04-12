"""
Valid Anagram  |  LeetCode #242  |  Easy
Pattern : HashMap
Link    : https://leetcode.com/problems/valid-anagram/
Date    : 12/4/2026

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(?)]
    Sắp xếp cả hai chuỗi và so sánh chúng.
    Nếu chúng giống nhau, trả về true; ngược lại, trả về false.


Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    Tại sao dùng [pattern]?
    [Giải thích logic chính]
    dùng dict, đếm số lần xuất hiện của mỗi ký tự trong s và t.
    Nếu dict cuối cùng giống nhau, trả về true; ngược lại, trả về false
    logic chính:
    1. nếu len(s) != len(t), trả về false ngay lập tức (vì anagram phải có cùng số lượng ký tự)
    2. tạo một dict để đếm số lần xuất hiện của mỗi ký tự trong s và t.
    3. duyệt qua cả hai chuỗi cùng một lúc, tăng số đếm cho ký tự trong s và giảm số đếm cho ký tự trong t.
    4. sau khi duyệt xong, nếu tất cả giá trị trong dict đều bằng 0, trả về true; ngược lại, trả về false.


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


def solution_brute_force(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def solution_optimal(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    for i in t:
        count[i] = count.get(i, 0) - 1
    for v in count.values():
        if v != 0:
            return False
    return True


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------


def test():
    # Happy path — ví dụ bình thường
    assert solution_brute_force("anagram", "nagaram") == True
    assert solution_brute_force("rat", "car") == False
    assert solution_optimal("anagram", "nagaram") == True
    assert solution_optimal("rat", "car") == False
    # assert solution(...) == ...

    # Edge cases
    # assert solution([]) == ...
    assert solution_brute_force("", "") == True
    assert solution_optimal("", "") == True
    assert solution_brute_force("a", "a") == True
    assert solution_optimal("a", "a") == True
    assert solution_brute_force("a", "b") == False
    assert solution_optimal("a", "b") == False
    assert solution_brute_force("aaa", "aaa") == True
    assert solution_optimal("aaa", "aaa") == True
    assert solution_brute_force("aabbcc", "abcabc") == True
    assert solution_optimal("aabbcc", "abcabc") == True
    assert solution_brute_force("aabbcc", "abcabd") == False
    assert solution_optimal("aabbcc", "abcabd") == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
