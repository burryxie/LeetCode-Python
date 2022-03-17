'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1,len2 = len(nums1),len(nums2)
        cnt = 0 
        mid = (len1+len2)//2
        idx1,idx2 = 0,0
        while(cnt<mid ):
            val1 = nums1[idx1] if idx1<len1 else None
            val2 = nums2[idx2] if idx2<len2 else None 

            if(val1>val2):
                idx2 += 1
            else:
                idx1 += 1
            cnt += 1
        
        if idx1<len1 and idx2<len2:
            res = (nums1[idx1]+nums2[idx2])/2
        elif idx1 == len1:
            res = nums2[idx2]
        elif idx2 == len2:
            res = nums1[idx1]

        return res

        