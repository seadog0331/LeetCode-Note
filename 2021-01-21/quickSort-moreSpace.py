def quickSort(nums):
    if len(nums) == 0:
        return []
    pivot = nums[0]
    bigger = []
    smaller = []
    for j in range(len(nums)-1):
        if nums[j] > pivot:
            bigger.append(nums[j])
        else:
            smaller.append(nums[j])
    return quickSort(smaller) + [pivot] + quickSort(bigger)