class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)< sum(cost): return -1
        total,res=0,0
        for g in range(len(gas)):
            total+= gas[g]-cost[g]
            if total<0:
                total=0
                res=g+1
        return res
        