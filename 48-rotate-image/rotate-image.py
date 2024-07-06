class Solution(object):
    def rotate(self, matrix):
        n= len(matrix)

        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        # reverse
        for i in range(n):
            matrix[i].reverse()