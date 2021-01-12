# 定义二叉树类
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for n in nums:            
            if count == 0:
                candidate = n
            if n == candidate:
                count+=1
            if n != candidate:
                count-=1