class Solution(object):
    dt = {}
    ds = {}
    
    def show(self, s, start, end):
        # return
        print s[start:end], start, end
 
    def clft(self, t):
        d = {}
        for c in t:
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
        return d

    def clfs(self, s):
        d = {}
        for c in s:
            if c not in self.dt.keys():
                continue
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
        return d

    # NOT move end here, ONLY head moves
    def minWindowOne(self, s, t, start, end):
        tds = self.ds
        for i,c in enumerate(s[start:end]):
            # print c, start, end
            if c not in self.dt.keys():
                start += 1
                continue
            if tds[c] > self.dt[c]:
                tds[c] -= 1
                start += 1
            else:
                break
        return start

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lt = len(t)
        ls = len(s)
        if ls < lt or lt == 0:
            return ""

        self.dt = self.clft(t) 
        # self.ds = self.clfs(s)

        # find state[0], the first substring of s contains t
        tdt = dict(self.dt)
        start = -1
        end = -1
        for i,c in enumerate(s):
            if c not in tdt.keys():
                continue
            if start == -1:
                start = i

            if c in tdt.keys():
                tdt[c] -= 1
                if tdt[c] == 0:
                    tdt.pop(c)
            if len(tdt) == 0:
                end = i + 1
                break;
        if end - start == lt:
            return s[start:end]
        elif end - start > lt:
            # self.show(s, start, end)
            pass
        else:
            # print "ERROR1", start, end
            return ""

        # obtain the minWindow of state[0]
        self.ds = self.clfs(s[start:end])
        start = self.minWindowOne(s, t, start, end)
        # self.show(s, start, end)
        res = [start, end]
        reslen = end - start
        if reslen == lt:
            return s[res[0]:res[1]]
        
        for i,c in enumerate(s[end:]):
            if c not in self.dt.keys():
                continue
            elif c != s[start]:
                self.ds[c] += 1 # no need to add cnt when c == start, the end c will take this count
                continue

            start += 1
            tend = end + i + 1
            # print "BEFORE:", start, tend
            start = self.minWindowOne(s, t, start, tend)
            if tend - start < reslen:
                res = [start, tend]
                reslen = tend - start
                if reslen == lt:
                    return s[res[0]:res[1]]
            # print "AFTER:", start, tend

        return s[res[0]:res[1]]

