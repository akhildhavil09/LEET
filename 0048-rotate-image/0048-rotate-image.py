class Solution(object):
    def rotate(self, matrix):
        left,right=0, len(matrix)-1
        while left<right: # if it cross it goes out of bound
            for i in range(right-left): #narrows down the matrix
                top,bottom= left, right

                topleft= matrix[top][left +i] # intiallu [0][0]

                matrix[top][left+i]=matrix[bottom-i][left]
                matrix[bottom-i][left]= matrix[bottom][right-i]
                matrix[bottom][right-i]=matrix[top+i][right]
                matrix[top+i][right]=topleft
            right-=1
            left+=1