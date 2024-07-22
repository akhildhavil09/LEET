class Solution(object):
    def reorderList(self, head):
        # toritoise and hare finding mid
        slow,fast= head ,head
        while fast and fast.next and slow:
            fast= fast.next.next
            slow=slow.next
        
        # reversing the second half
        curr= slow.next
        slow.next, prev= None, None
        while curr:
            tmp=curr.next
            curr.next= prev
            prev= curr
            curr=tmp
        
        # merging the first and 2nd half
        first_half= head
        while prev:
            next_first= first_half.next
            next_second= prev.next
            first_half.next= prev
            prev.next= next_first
            first_half=next_first
            prev= next_second


        