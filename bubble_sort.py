import random

def bubble_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

    return nums

nums: list[int] = []

while len(nums) < 10:
    num: int = random.randint(1, 100)
    if num not in nums:
        nums.append(num)

print(f'入力: {nums}')
print(f'出力: {bubble_sort(nums)}')
