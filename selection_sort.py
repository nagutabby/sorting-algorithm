import random

def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1):
        current_min_index: int = i
        for j in range(i + 1, len(nums)):
            if nums[current_min_index] > nums[j]:
                current_min_index = j

        nums[i], nums[current_min_index] = nums[current_min_index], nums[i]

    return nums

nums: list[int] = []

while len(nums) < 10:
    num: int = random.randint(1, 100)
    if num not in nums:
        nums.append(num)

print(f'入力: {nums}')
print(f'出力: {selection_sort(nums)}')
