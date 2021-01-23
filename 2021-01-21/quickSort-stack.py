class Stack():
    def _init_(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()

def partition(myList, start, end):
    pivot = myList[end]
    left = start
    right = end

    while left < right:
        while left < right and myList[left] <= pivot:
            left+=1
        while left < right and myList[right] >= pivot:
            right-=1
        if left != right:
            myList[left],myList[right] = myList[right],myList[left]
        
    myList[end], myList[left] = myList[left],pivot
    return left

def quick_sort(mylist):
    stack = Stack()
    start = 0
    end = len(mylist) - 1

    if start < end:
        stack.push((start,end))
        while not stack.is_empty():
            start,end = stack.pop()
            mid = partition(myList, start, end)
            if start < mid - 1:
                stack.push((start, mid-1))
            if mid + 1 < end:
                stack.push((mid+1, end))