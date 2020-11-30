# TODO 给定一个二叉树，但会该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
# TODO 列如：
# TODO 给定的二叉树是{3， 9， 20， #， #， 15， 7}

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @param root TreeNode类
# @return int整型二维数组

class Solution:

    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        # 模拟一个队列储存节点
        q = []
        # 首先将根节点入队
        q.append(root)
        # 列表为空时，循环终止
        while len(q) != 0:
            # 使用列表存储同层节点
            tmp = []
            # 记录同城节点的个数
            length = len(q)
            for i in range(length):
                # 将同层节点一次出队
                r = q.pop(0)
                if r.left:
                    # 非空左孩子入队

                    q.append(r.left)
                if r.right:
                    # 非空右孩子入队
                    q.append(r.right)
                tmp.append(r.val)
            result.append(tmp)
        return result




if __name__ == '__main__':
    data = [[1],[2,3],[4,5]]
    tree = TreeNode(data)

    s = Solution()
    result = s.levelOrder(tree)
    print(result)

