class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(r,c,board,n):
            dupli_r= r
            dupli_c = c

            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1

            c=dupli_c
            r=dupli_r

            while c>=0:
                if board[r][c]=="Q":
                    return False
                c-=1

            c=dupli_c
            r=dupli_r

            while r<n and c<n:
                if board[r][c]=="Q":
                    return False
                r+=1
                c-=1
            
            return True


        def sol(col,board,ans,n):
            if col==n:
                ans.append(list(board))
                return
            for row in range(n):
                if isSafe(row,col,board,n):
                    board[row]=board[row][:col]+"Q"+board[row][col+1:]
                    sol(col+1,board,ans,n)
                    board[row]=board[row][:col]+"."+board[row][col+1:]

        ans=[]
        board=['.'*n for _ in range(n)]
        sol(0,board,ans,n)
        return ans