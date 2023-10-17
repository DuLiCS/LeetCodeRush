def jump(nums):
    if not nums or len(nums) == 1:
        return 0

    jumps, end, farthest = 0, 0, 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest

    return jumps

nums = [2,3,1,1,4]
print(jump(nums))