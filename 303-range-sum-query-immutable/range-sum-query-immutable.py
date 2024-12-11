class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum=[0]
        current_sum=0
        for num in nums:
            current_sum+= num
            self.prefix_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1]- self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)