import random

def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break

    return nums

nums: list[int] = []

while len(nums) < 10:
    num: int = random.randint(1, 100)
    if num not in nums:
        nums.append(num)

print(f'入力: {nums}')
print(f'出力: {insertion_sort(nums)}')
