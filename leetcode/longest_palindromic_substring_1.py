
try:
    input = raw_input
except NameError:
    pass

def lps(s):
    n = len(s)
    ret = 1
    begin = 0
    t = [[False for i in range(1000)] for j in range(1000)]
    for i in range(n):
        t[i][i] = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            t[i][i+1] = True
            ret = 2
            begin = i
    for w in range(3,n+1):
        for i in range(n-w+1):
            if s[i] == s[i+w-1] and t[i+1][i+w-2]:
                t[i][i+w-1] = True
                ret = w
                begin = i
    return s[begin:begin+ret]


def main():
    string = input("input a string:")
    print(lps(string))

if __name__ == "__main__":
    main()
