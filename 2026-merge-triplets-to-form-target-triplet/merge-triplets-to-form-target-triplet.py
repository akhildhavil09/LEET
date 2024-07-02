class Solution:
    def mergeTriplets(self, triplets, target):
        x, y, z = target
        can_contribute_x = can_contribute_y = can_contribute_z = False
        
        for triplet in triplets:
            a, b, c = triplet
            
            # Check if the triplet is valid (does not exceed target)
            if a <= x and b <= y and c <= z:
                # Check if this triplet can contribute to x
                if a == x:
                    can_contribute_x = True
                # Check if this triplet can contribute to y
                if b == y:
                    can_contribute_y = True
                # Check if this triplet can contribute to z
                if c == z:
                    can_contribute_z = True
        
        # Check if we found contributing triplets for all target elements
        return can_contribute_x and can_contribute_y and can_contribute_z
