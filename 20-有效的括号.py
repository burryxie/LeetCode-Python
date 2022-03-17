'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = []
        for i in s:
            if i in ['(','{','[']:
                tmp.append(i)
            elif i in [')','}',']']:
                if tmp:
                    if i == ')' and tmp[-1] != '(':
                        return False 
                    elif i == '}' and tmp[-1] != '{':
                        return False 
                    elif i == ']' and tmp[-1] != '[':
                        return False 
                    else:
                        tmp.pop()
                else:
                    return False 
        

        if tmp:
            return False 
        else:
            return True 