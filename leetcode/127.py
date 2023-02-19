class Solution(object):
    st = {}
    st2 = {}
    def compareWord(self, a, b):
        if (a,b) in self.st:
            return self.st[(a,b)]
        l = len(a)
        c = 0
        for i in xrange(l):
            if a[i] != b[i]:
                c += 1
            if c == 2:
                self.st[(a,b)] = 2
                return 2
        self.st[(a,b)] = c
        return c
    def ladderLengthInner(self, beginWord, endWord, wordList):
        if (beginWord, endWord) in self.st2:
            return self.st2[(beginWord, endWord)]
        if endWord not in wordList:
            self.st2[(beginWord, endWord)] = 0
            return 0
        ret = 5002
        for i,w in enumerate(wordList):
            cr = self.compareWord(beginWord, w)
            if cr == 1:
                ret = min(ret, \
                    1 + self.ladderLengthInner(w, endWord, wordList[:i]+wordList[i+1:]))
        self.st2[(beginWord, endWord)] = ret
        return ret
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.st2 = {}
        ret = 1 + self.ladderLengthInner(beginWord, endWord, wordList)
        if ret == 5002 or ret == 1:
            ret = 0
        return ret
