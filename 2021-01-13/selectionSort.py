def selectionSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums
        

