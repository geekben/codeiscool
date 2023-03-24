class StreamChecker(object):
    words = None
    ws = {}
    lw = []
    ls = ''
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.lw = []
        self.ws = {}
        self.ls = ''
        for i,w in enumerate(words):
            if w[-1] not in self.ws:
                self.ws[w[-1]] = [i]
            else:
                self.ws[w[-1]].append(i)
            self.lw.append(len(w))
        # print self.ws,self.lw


    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.ls += letter
        #self.ll += 1
        if letter not in self.ws:
            return False
        for i in self.ws[letter]:
            if self.ls[(-1*self.lw[i]):] \
                    == self.words[i]:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
