class StreamChecker(object):
    ws = {}
    ls = ''

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.ws = {}
        self.ls = ''
        for w in words:
            lw = len(w)
            if lw not in self.ws:
                self.ws[lw] = set()
            self.ws[lw].add(w)

        # print self.ws,self.lw


    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.ls += letter
        for i in self.ws.keys():
            if self.ls[-i:] in self.ws[i]:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
