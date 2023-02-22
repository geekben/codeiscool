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
        st = {}
        res = []
        while q:
            wl = q.pop(0)
            if res and len(wl) >= len(res[0]):
                break
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
 
        return res
