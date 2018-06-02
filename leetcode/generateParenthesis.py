class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        r = {}
        r[0] = [""]

        for i in range(1, n+1):
            t = []
            for j in range(0, i):
                for k in r[j]:
                    for l in r[i-j-1]:
                        t.append('('+k+')'+l)
            r[i] = t

        return r[n]


if __name__ == "__main__":
    print Solution().generateParenthesis(1)
    print Solution().generateParenthesis(2)
    print Solution().generateParenthesis(3)
    r = Solution().generateParenthesis(4)
    print r
    e = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    for i in e:
        if i not in r:
            print i

