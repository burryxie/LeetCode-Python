'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0,0
        res = 0
        while(right<len(s)):
            tmp_strs = s[left:right]
            tmp_str  = s[right]
            if tmp_str in tmp_strs:
                idx = tmp_strs.index(tmp_str)
                left += idx+1
            
            if right-left+1 > res :
                res = right-left+1
            
            right += 1
        
        return res 