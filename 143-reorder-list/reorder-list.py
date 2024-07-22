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
        first,second= head, prev
        while second:
            tmp1,tmp2= first.next, second.next
            first.next= second
            second.next= tmp1
            first, second= tmp1,tmp2


        