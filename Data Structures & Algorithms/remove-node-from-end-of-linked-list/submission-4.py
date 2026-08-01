# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count+=1
        
        remove=count-n
        if remove==0:
            return head.next

        c = head
        for i in range(count-1):
            if(i+1)==remove:
                c.next = c.next.next
                break
            c = c.next
        return head