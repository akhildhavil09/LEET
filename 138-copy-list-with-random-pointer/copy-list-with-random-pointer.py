class Solution(object):
    def copyRandomList(self, head):
        mpp={None:None}

        curr=head
        while curr:
            copy=Node(curr.val)
            mpp[curr]=copy
            curr=curr.next

        curr=head
        while curr:
            copy= mpp[curr]
            copy.next=mpp[curr.next]
            copy.random= mpp[curr.random]
            curr=curr.next

        return mpp[head]
        