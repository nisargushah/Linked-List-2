# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## Space Complexity O(1)
## Time Complexity O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        ## Need to find length of both linkedList:
        currA = headA
        currB = headB
        lenA,lenB = 0,0
        
        while currB.next is not None:
            currB = currB.next
            lenB += 1
        while currA.next is not None:
            currA = currA.next
            lenA += 1
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
            
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA
        
            
