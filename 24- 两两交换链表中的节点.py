'''
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head or head.next==None):
            return head 

        dummy = ListNode(-9)
        
        pre,cur = dummy,head

        while(cur and cur.next):
            next = cur.next 

            pre.next = next 
            cur.next = next.next 
            next.next = cur 

            pre = cur 
            cur = cur.next 


        return dummy.next



        # if((head is None) or (head.next is None)):
        #     return head
        
        # next = head.next 
        # head.next = self.swapPairs(next.next)
        # next.next = head 

        # return next



