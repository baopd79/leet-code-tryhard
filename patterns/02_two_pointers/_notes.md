# Two Pointers Pattern Notes

## heading : khi nào dùng pattern này?

- Dùng để giải quyết các bài toán liên quan đến mảng hoặc chuỗi, đặc biệt là khi cần tìm kiếm cặp phần tử
- Tìm kiếm cặp phần tử thỏa mãn điều kiện nào đó ví dụ: có tổng bằng một giá trị nhất định, có hiệu bằng một giá trị nhất định, v.v.
- Tìm kiếm cặp phần tử trong một mảng đã được sắp xếp

## 2 dạng bài toán thường gặp

### dạng 1: two pointers từ hai đầu mảng

- Dùng hai con trỏ, một con trỏ bắt đầu từ đầu mảng và một con trỏ bắt đầu từ cuối mảng, di chuyển hai con trỏ về phía nhau để tìm kiếm cặp phần tử th ỏa mãn điều kiện nào đó, ví dụ: có tổng bằng một giá trị nhất định, có hiệu bằng một giá trị nhất định, v.v.

### dạng 2: two pointers từ một đầu mảng

- Dùng hai con trỏ, cả hai con trỏ bắt đầu từ đầu mảng, di chuyển một con trỏ để tìm kiếm cặp phần tử thỏa mãn điều kiện nào đó, ví dụ: có tổng bằng một giá trị nhất định, có hiệu bằng một giá trị nhất định, v.v.

## Template tư duy

```python
# SOLUTION
# -------------------------------------------------------
    def two_pointers_from_both_ends(nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
# -------------------------------------------------------
```

````python
# SOLUTION
# -------------------------------------------------------
    def two_pointers_from_one_end(nums: List[int], target: int) -> List[int]:
        left = 0
        for right in range(len(nums)):
            while left < right and nums[left] + nums[right] > target:
                left += 1
            if left < right and nums[left] + nums[right] == target:
                return [left, right]
        return []
# -------------------------------------------------------```
## trick quan trọng
- Khi sử dụng two pointers, hãy luôn nhớ cập nhật kết quả sau khi di chuyển con trỏ, tùy thuộc vào điều kiện của bài toán. Điều này giúp đảm bảo rằng bạn luôn có được kết quả chính xác nhất tại mỗi bước của quá trình duyệt qua mảng hoặc chuỗi.
## Các bài toán thường gặp
- [x] Two Sum II - Input array is sorted → Two Pointers từ hai đầu mảng
    -> Dùng hai con trỏ, một con trỏ bắt đầu từ đầu mảng và một con trỏ bắt đầu từ cuối mảng, di chuyển hai con trỏ về phía nhau để tìm kiếm cặp phần tử có tổng bằng target.
- [x] Valid Palindrome → Two Pointers từ hai đầu mảng
    -> Dùng hai con trỏ, một con trỏ bắt đầu từ đầu chuỗi và một con trỏ bắt đầu từ cuối chuỗi, di chuyển hai con trỏ về phía nhau để kiểm tra xem các ký tự có giống nhau hay không, bỏ qua các ký tự không phải là chữ cái hoặc số.
- [x] Reverse String → Two Pointers từ hai đầu mảng
    -> Dùng hai con trỏ, một con trỏ bắt đầu từ đầu mảng và một con trỏ bắt đầu từ cuối mảng, di chuyển hai con trỏ về phía nhau và hoán đổi các phần tử tại hai con trỏ cho đến khi hai con trỏ gặp nhau hoặc vượt qua nhau.
- [x] Reverse Vowels of a String → Two Pointers từ hai đầu mảng
    -> Dùng hai con trỏ, một con trỏ bắt đầu từ đầu chuỗi và một con trỏ bắt đầu từ cuối chuỗi, di chuyển hai con trỏ về phía nhau để tìm kiếm các nguyên âm và hoán đổi chúng cho đến khi hai con trỏ gặp nhau hoặc vượt qua nhau.
- [x] 3Sum → Two Pointers từ một đầu mảng
    -> Sắp xếp mảng và sử dụng hai con trỏ để tìm kiếm cặp phần tử có tổng bằng target - nums[i] cho mỗi phần tử nums[i] trong mảng.
- [x] 4Sum → Two Pointers từ một đầu mảng
    -> Sắp xếp mảng và sử dụng hai con trỏ để tìm kiếm cặp phần tử có tổng bằng target - nums[i] - nums[j] cho mỗi cặp phần tử nums[i] và nums[j] trong mảng.
````
