'''
给定 n 个非负整数, 表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''

from traceback import print_tb


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 解法一：按层处理。即按1、2、...最高高度遍历每一层。
        max_height = max(height) #最高高度

        res = 0
        for i in range(1,max_height+1):
            tmp_res = 0
            flag = False #是否可以蓄水
            for j in range(0,len(height)):
                if(height[j]>=i):
                    flag = True
                    res += tmp_res
                    tmp_res = 0
                elif(flag):
                    tmp_res += 1
            

        return res 


if __name__=="__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = Solution().trap(height)
    print(res)
    print(max(height))