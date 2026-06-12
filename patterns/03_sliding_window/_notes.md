<!-- tôi muốn viết notes cho pattern Sliding Window -->
# Sliding Window Pattern Notes
## heading : khi nào dùng pattern này?


- subarray/substring liên tiếp thoả mãn điều kiện
- tìm max/min hoặc đếm số lượng subarray/substring
- từ khoá "độ dài k", dài nhất, ngắn nhất, v.v.

## 2 dạng bài toán thường gặp

### dạng 1: fixed size sliding window
- Tìm kiếm một subarray hoặc substring có độ dài k thỏa mãn một điều kiện nào đó, ví dụ: có tổng lớn nhất, có số lượng phần tử khác nhau tối đa là k, v.v.
### dạng 2: dynamic size sliding window
- Tìm kiếm một subarray hoặc substring liên tục trong một chuỗi hoặc mảng thỏa mãn một điều kiện nào đó, ví dụ: có tổng lớn nhất hoặc nhỏ nhất, hoặc có số lượng phần tử khác nhau tối đa là k, v.v.

##Template tư duy
```python
# SOLUTION
# -------------------------------------------------------   
    def fixed_size_sliding_window(nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        result = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            result = max(result, window_sum)
        return result
# -------------------------------------------------------
```

```python
# SOLUTION
# -------------------------------------------------------
 def dynamic_size_sliding_window(s: str, k: int) -> int:
    left = 0
    char_count = {}
    max_length = 0      
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    return max_length   
# -------------------------------------------------------
```
## trick quan trọng
- Khi sử dụng sliding window, hãy luôn nhớ cập nhật kết quả sau khi mở rộng hoặc thu hẹp cửa sổ, tùy thuộc vào điều kiện của bài toán. Điều này giúp đảm bảo rằng bạn luôn có được kết quả chính xác nhất tại mỗi bước của quá trình duyệt qua chuỗi hoặc mảng.


## Các bài toán thường gặp




- [x] Maximum Average Subarray I → Sliding Window
    -> Dùng sliding window cố định để tính tổng của subarray có độ dài k, cập nhật giá trị max_average khi mở rộng cửa sổ.

- [x] Best Time to Buy and Sell Stock → Sliding Window (động)
    -> Giữ min_price (đáy thấp nhất bên trái) + đỉnh hiện tại, mỗi ngày thử bán để cập nhật max_profit. One pass O(n), O(1).
    
- [] Longest Substring Without Repeating Characters
- [ ] Longest Repeating Character Replacement
- [ ] Minimum Size Subarray Sum
- [ ] Permutation in String
- [ ] Find All Anagrams in a String
- [ ] Longest Substring with At Most K Distinct Characters
- [ ] Longest Substring with At Most Two Distinct Characters
- [ ] Fruit Into Baskets
- [ ] Longest Substring with At Least K Repeating Characters
- [ ] Subarrays with K Different Integers
- [ ] Longest Substring with At Most K Distinct Characters
- [ ] Longest Substring with At Most Two Distinct Characters
- [ ] Fruit Into Baskets
- [ ] Longest Substring with At Least K Repeating Characters
- [ ] Subarrays with K Different Integers