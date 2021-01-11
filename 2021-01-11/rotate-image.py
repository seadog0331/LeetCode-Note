matrix = [ \
  [1,2,3], \
  [4,5,6], \
  [7,8,9] \
],

class Solution:
    def rotate(matrix) -> None:
        length = len(matrix)
        print(length)
        for i in range(length):
            for j in range(i+1,length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

Solution.rotate(matrix)