class DetectSquares(object):

    def __init__(self):
        self.ptcounter= defaultdict(int)
        self.pts=[]

    def add(self, point):
        self.ptcounter[tuple(point)]+=1
        self.pts.append(point)
        

    def count(self, point):
        res=0
        px,py=point
        for x,y in self.pts:
            if(abs(py-y)!= abs(px-x)) or x==px or y==py:
                continue
            res+= self.ptcounter[(x,py)] * self.ptcounter[(px,y)]
        return res       


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)