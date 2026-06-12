"""
Best Time to Buy and Sell Stock  |  LeetCode #121  |  Easy
Pattern : Sliding Window
Link    : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Date    :

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
You are given an array prices where prices[i] is the price of a given stock
on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
    Input : prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price=1), sell on day 5 (price=6). Profit = 6-1 = 5.

Example 2:
    Input : prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: No transaction is profitable, so return 0.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4

-------------------------------------------------------
APPROACH  ← Viết vào đây TRƯỚC KHI CODE
-------------------------------------------------------
Brute force:
    Thử mọi cặp (mua ngày i, bán ngày j) với j > i.
    Hai vòng lặp lồng nhau, cập nhật profit = max(profit, prices[j] - prices[i]).
    -> O(n^2), với n = 10^5 sẽ TLE.

Optimal (cửa sổ động - one pass):
    Coi như 1 cửa sổ [min_price ... ngày hiện tại].
    Duyệt từ trái sang phải, luôn nhớ giá MUA thấp nhất từ đầu tới giờ (min_price).
    Tại mỗi ngày, nếu bán hôm nay thì lời = price - min_price.
    -> Mở rộng cửa sổ sang phải: cập nhật max_profit.
    -> Nếu gặp giá thấp hơn min_price thì "dời điểm mua" (thu cửa sổ về ngày này).

    Tại sao dùng Sliding Window (dạng động)?
    Vì ta chỉ cần đáy thấp nhất bên trái + đỉnh hiện tại, không cần quay lại
    duyệt quá khứ -> mỗi phần tử chỉ thăm 1 lần.
    Bản chất là greedy one-pass. Mỗi ngày tôi coi như bán hôm nay, và để tối ưu profit thì tôi mua ở giá thấp nhất đã gặp trước đó. Có thể nhìn như DP nén trạng thái, nhưng cách trình bày tự nhiên nhất là greedy one-pass.


Brute force thử mọi cặp mua-bán nên O(n²). Optimal thì chỉ cần duyệt một lần, luôn lưu giá mua thấp nhất trước đó. Với mỗi giá hiện tại, coi như bán hôm nay, tính profit và cập nhật max profit.

Complexity:
    Time : O(n)   - duyệt mảng đúng 1 lần
    Space: O(1)   - chỉ giữ 2 biến min_price, max_profit

-------------------------------------------------------
EDGE CASES cần xử lý
-------------------------------------------------------
- [x] 1 phần tử: [x]            -> không bán được -> 0
- [x] Tất cả giống nhau: [x, x] -> profit = 0
- [x] Giá giảm dần liên tục     -> profit = 0
"""

from typing import List


# -------------------------------------------------------
# SOLUTION
# -------------------------------------------------------


def max_profit_brute_force(prices: List[int]) -> int:
    n = len(prices)
    profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = max(profit, prices[j] - prices[i])
    return profit


def max_profit(prices: List[int]) -> int:
    min_price = float("inf")  # giá mua thấp nhất từ đầu tới giờ
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price  # dời điểm mua xuống đáy mới
        else:
            best = max(best, price - min_price)  # thử bán hôm nay
    return best


# -------------------------------------------------------
# TEST CASES  ← Tự viết trước khi submit
# -------------------------------------------------------


def test():
    for solve in (max_profit, max_profit_brute_force):
        # Happy path
        assert solve([7, 1, 5, 3, 6, 4]) == 5
        assert solve([1, 2, 3, 4, 5]) == 4

        # Edge cases
        assert solve([7, 6, 4, 3, 1]) == 0  # giảm dần -> 0
        assert solve([1]) == 0  # 1 phần tử
        assert solve([3, 3, 3]) == 0  # giống nhau
        assert solve([2, 4, 1]) == 2  # đáy nằm sau đỉnh đầu

    print("All tests passed!")


if __name__ == "__main__":
    test()
