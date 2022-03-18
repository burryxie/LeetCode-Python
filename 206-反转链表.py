'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        pre,cur = None,head 
        while(cur):
            tmp = cur.next 
            cur.next = pre 
            pre = cur 
            cur = tmp 
        
        return cur.next 