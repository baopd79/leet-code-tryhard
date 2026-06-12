"""
Valid Parentheses  |  LeetCode #20  |  Easy
Pattern : Stack
Link    : https://leetcode.com/problems/valid-parentheses/
Date    :

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Given a string s containing just the characters '(', ')', '{', '}', '['
and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input : s = "()"
    Output: True

Example 2:
    Input : s = "()[]{}"
    Output: True

Example 3:
    Input : s = "(]"
    Output: False

Example 4:
    Input : s = "([)]"
    Output: False

Example 5:
    Input : s = "{[]}"
    Output: True

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    [Mô tả cách đơn giản nhất — O(n^2)]

Optimal:
    [Mô tả ý tưởng tối ưu bằng lời của bạn]
    Tại sao dùng Stack?
    [Giải thích logic chính]

Complexity:
    Time : O(?)
    Space: O(?)

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [ ] Chuỗi rỗng: ""
- [ ] Chỉ có opening brackets: "((("
- [ ] Chỉ có closing brackets: ")))"
- [ ] Độ dài lẻ → luôn False
- [ ] Lồng nhau đúng cách: "{[]}"
"""

# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------

def is_valid(s: str) -> bool:
    # Viết code ở đây
    pass


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------

def test():
    # Happy path
    # assert is_valid("()") == True
    # assert is_valid("()[]{}") == True
    # assert is_valid("{[]}") == True

    # Edge cases
    # assert is_valid("(]") == False
    # assert is_valid("([)]") == False
    # assert is_valid("(((") == False

    print("All tests passed!")


if __name__ == "__main__":
    test()
