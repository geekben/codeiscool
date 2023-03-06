class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        an = 0
        bn = 0
        t = 'a'
        ret = 0

        for c in s:
            if c == 'a':
                if t == 'a':
                    pass
                else:
                    if bn > an:
                        an += 1
                    else:
                        t = 'a'
                        ret += bn
                        bn = 0
                        an = 0
            else:
                t = 'b'
                bn += 1
        
        return an + ret
