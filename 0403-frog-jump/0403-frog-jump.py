class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_pos= set(stones)
        memo={}

        def dfs(position, jump_size):
            if position==stones[-1]:
                return True
            
            if (position,jump_size) in memo:
                return memo[(position,jump_size)]
            
            for next_jump in (jump_size-1, jump_size, jump_size+1):
                if next_jump>0 and (position+next_jump) in stone_pos:
                    if dfs(position+next_jump,next_jump):
                        memo[(position,jump_size)]= True
                        return True
            memo[(position,jump_size)]= False
            return False
        if stones[1]!=1:
            return False
        return dfs(1,1)