# 定义二叉树类
class BinaryTree:
    def _init(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get(self):
        return self.data
    
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, node):
        self.left = node
    
    def setRight(self. node):
        self.right = node

# 实例化二叉树
binaryTree = BinaryTree(0)
binaryTree.setLeft(BinaryTree(1))
binaryTree.setRight(BinaryTree(2))
binaryTree.getLeft().setLeft(BinaryTree(3))
binaryTree.getLeft().setRight(BinaryTree(4))
binaryTree.getRight().setLeft(BinaryTree(5))
binaryTree.getRight().setRight(BinaryTree(6))

def preorderTraversal(now, result=[]):
    if now == None:
        return result
    result.append(now.data)
    preorderTraversal(now.left, result)
    preorderTraversal(now.right, result)
    return result

print(preorderTraversal(binaryTree))

def intermediateTraversal(now, result=[]):
    if now == None:
        return result
    intermediateTraversal(now.left, result)
    result.append(now.data)
    intermediateTraversal(now.right, result)
    return result

print(intermediateTraversal(binaryTree))

