N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))

print(nums)
for i in range(N): # bubbleSort
    for j in range(N - i - 1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

