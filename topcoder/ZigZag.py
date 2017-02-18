class ZigZag:
    def longestZigZag(self, seq):
        count = 1
        d = 0
        p = seq[0]
        for i in seq[1:]:
            if p == i:
                continue
            elif p < i:
                if d == 1:
                    p = i
                    continue
                else:
                    count += 1
                d = 1
            else:
                if d == -1:
                    p = i
                    continue
                else:
                    count += 1
                d = -1
            p = i

        return count

if __name__ == "__main__":
    import re
    with open("testcases") as f:
        for line in f:
            info = re.findall(r"[0-9\-]+", line)
            para = [int(x) for x in info]
            seq = para[:-1]
            exp = para[-1]
            ret = ZigZag().longestZigZag(seq)
            print seq, exp
            if ret == exp:
                print "SUCCESS"
            else:
                print "FAIL", ret
   
