'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        left,right = 0,len(num)-1
        while(left<right):
            if(num[left]!=num[right]):
                return False
            left += 1
            right -= 1
        
        return True
        
