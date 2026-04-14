"""
Valid Palindrome  |  LeetCode #125  |  Easy
Pattern : Two Pointers
Link    : https://leetcode.com/problems/valid-palindrome/
Date    :

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input : s = "A man, a plan, a canal: Panama"
    Output: True
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input : s = "race a car"
    Output: False
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input : s = " "
    Output: True
    Explanation: After removing non-alphanumeric characters, s is an empty
                 string "". An empty string reads the same forward and backward.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.

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
- [ ] Chuỗi rỗng hoặc chỉ có spaces: " "
- [ ] Chỉ có 1 ký tự alphanumeric
- [ ] Tất cả là ký tự đặc biệt: "!@#$"
- [ ] Chữ hoa/thường lẫn lộn: "Aa"
"""

# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------

def is_palindrome(s: str) -> bool:
    # Viết code ở đây
    pass


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------

def test():
    # Happy path
    # assert is_palindrome("A man, a plan, a canal: Panama") == True
    # assert is_palindrome("race a car") == False

    # Edge cases
    # assert is_palindrome(" ") == True
    # assert is_palindrome("a") == True

    print("All tests passed!")


if __name__ == "__main__":
    test()
