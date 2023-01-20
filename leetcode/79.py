class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def valid(p,m,n):
            return p[0] >= 0 and p[1] >= 0 and p[0] < m and p[1] < n

        wl = len(word)
        m = len(board)
        n = 0
        if m != 0:
            n = len(board[0])
        if m*n < wl:
            return False

        t = []
        stat = [[] for _ in xrange(m)]
        c = word[0]
        ht = {}
        for i,line in enumerate(board):
            stat[i] = [-1 for _ in xrange(n)]
            for j,ch in enumerate(line):
                if ch not in ht.keys():
                    ht[ch] = 1
                else:
                    ht[ch] += 1
                if c == ch:
                    t.append([i,j])
                    stat[i][j] = 0
        if len(t) == 0:
            return False
        for c in word:
            if c not in ht.keys():
                return False
            else:
                if ht[c] == 0:
                    return False
                ht[c] -= 1
        
        def deep_search(p, w, b):
            c = w[0]
            y,x = p
            if b[y][x] != c:
                return False
            if len(w) == 1:
                return True
            
            b[y][x] = 0
            u = [y-1,x]
            d = [y+1,x]
            l = [y,x-1]
            r = [y,x+1]
            tw = w[1:]
            if valid(u,m,n) and deep_search(u, tw, b):
                return True
            elif valid(d,m,n) and deep_search(d, tw, b):
                return True
            elif valid(l,m,n) and deep_search(l, tw, b):
                return True
            elif valid(r,m,n) and deep_search(r, tw, b):
                return True

            b[y][x] = c
            return False

        for p in t:
            if deep_search(p, word, board):
                return True
        return False
