# 取数组中位数
def quickSelect(nums,i,j,k):
    n = len(nums)
    if len(nums) == 0:
        return None
    pivot = nums[-1]
    # while i <= n-1:
    while j < n-1:
        if nums[j] >= pivot:
            j+=1
        if nums[j] < pivot:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j+=1

    nums[i],nums[-1] = pivot,nums[i]
    if k < i:
        quickSelect(nums[:i],0,0,k)
    elif k > i:
        quickSelect(nums[i:],0,0,k)

    return nums,i

nums = [3, 7]
k = len(nums)//2 
temp_nums,i = quickSelect(nums,0,0,k)
a = temp_nums[k]
if len(nums)%2 != 0:
    print(a)
else:
    k = k-1
    temp_nums,i = quickSelect(nums,0,0,k)
    b = temp_nums[k]
    print((a+b)/2)
