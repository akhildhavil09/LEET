class Solution(object):
    def carFleet(self, target, position, speed):
        newdict={}
        for index in range(len(position)):
            newdict[position[index]]=speed[index]


        stack=[]
        position=sorted(position)
        for index in range(len(position)-1,-1,-1):
            curp=position[index]
            ETA= (target-curp)/ float(newdict[curp])

            if stack and ETA <= stack[-1]:
                continue
            stack.append(ETA)
        return len(stack)



        
        