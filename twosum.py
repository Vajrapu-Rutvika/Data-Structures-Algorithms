def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]

        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))

result = two_sum(nums, target)
print(result)