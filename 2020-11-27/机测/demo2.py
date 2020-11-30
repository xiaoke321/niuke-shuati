# TODO 给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
# TODO 括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。



class Solution:
    def isValid(self , s ):
        # write code here
        dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = list()

        for ch in s:
            if stack and ch in dict:
                print(1)
                print(ch)
                if stack[-1] == dict[ch]:
                    print(3)
                    stack.pop()
                else:
                    print(4)
                    return False
            else:
                print(2)
                print(ch)
                stack.append(ch)
        return not stack

if __name__ == '__main__':
    s = Solution()
    result = s.isValid("[]")
    print(result)