def enumPat(s,n):
    if n < 1 or s < n:
        print "Error arg"
        return []
    if s == n:
        return [[")"]*s]

    if n == 1:
        return [["("]*(s-1) + [")"]]

    r = []
    r0 = enumPat(s-1, n)
    for i in r0:
        r.append(["("]+i)
    if (s-n < n):
        r1 = enumPat(s-1, n-1)
        for i in r1:
            r.append([")"]+i)
    return r


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    for i in enumPat(n*2, n):
        print ''.join(i)

if __name__ == "__main__":
    generateParenthesis(1)
    generateParenthesis(2)
    generateParenthesis(3)
    generateParenthesis(4)
