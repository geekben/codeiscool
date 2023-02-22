class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        l = len(beginWord)
        ws = set(wordList)
        q = [[beginWord]]
        res = []
        wq = []
        while q:
            wl = q.pop(0)
            if res and len(wl) >= len(res[0]):
                break
            wq.append(wl)
            w = wl[-1]
            for i in xrange(l):
                for n in xrange(97, 123):
                    c = chr(n)
                    nw = w[:i]+c+w[i+1:]
                    if nw in ws and nw not in wl:
                        if nw == endWord:
                            res.append(wl + [nw])
                        if res == []:
                            q.append(wl + [nw])
                            ws.remove(nw)

        if res:
            rl = len(res[0])
            st = [[] for _ in xrange(rl)]
            for i in xrange(rl):
                for r in res:
                    st[i].append(r[i])

            for wl in wq[1:]:
                ll = len(wl)
                w = wl[-1]
                for i in xrange(l):
                    for n in xrange(97, 123):
                        c = chr(n)
                        nw = w[:i]+c+w[i+1:]
                        if nw in st[ll]:
                            ri = st[ll].index(nw)
                            tr = wl + res[ri][ll:]
                            if tr not in res:
                                res.append(tr)
        return res
