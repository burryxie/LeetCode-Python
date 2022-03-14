'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0 
        res = ListNode(0)
        cur = res 

        while(l1 or l2 or flag):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 

            tmp = v1+v2+flag 
            flag = tmp // 10
            tmp = tmp % 10

            cur.next = ListNode(tmp)
            cur = cur.next

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        
        return  res.next 
