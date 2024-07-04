class Solution(object):
    def merge(self, inter):
        inter.sort(key=lambda i:i[0])
        output=[inter[0]]
        for start,end in inter[1:]:
            prevEND= output[-1][1]
            if start<=prevEND:
                output[-1][1]= max(end,prevEND)
            else:
                output.append([start,end])
        return output