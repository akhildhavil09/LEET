class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(1)
        cur= dummy
        carry=0

        while l1 or l2 or carry:
            sum_val= carry
            if l1!=None:
                sum_val+=l1.val
                l1=l1.next

            if l2!=None:
                sum_val+=l2.val
                l2=l2.next

            newnode= ListNode(sum_val%10)
            carry= sum_val//10

            cur.next= newnode
            cur=cur.next
        return dummy.next
            

        