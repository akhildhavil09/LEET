class Solution(object):
    def maxArea(self, height):
        area=0
        l,r= 0 , len(height)-1

        while l<r:
            cur= (r-l)* min(height[l],height[r])
            area= max(area, cur)

            if height[l]<height[r]: l+=1
            else:
                r-=1
        return area
        