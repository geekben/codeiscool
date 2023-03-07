'''
"{{a,z},a{b,c},{ab,z}}"
"{a,a}"
"{a,b}{a,b}"
"{a,b}{c,{d,e}}"
"{a,b}"
"{a}"
'''
class Solution(object):
    def product(self, e1, e2):
        ret = set()
        for i in e1:
            for j in e2:
                ret.add(i+j)
        return list(ret)
    def add(self, e1 , e2):
        t = set(e1+e2)
        return list(t)


    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        q = []
        item = []

        for i,c in enumerate(expression):
            if c == '{':
                e0 = expression[i-1]
                if i != 0 and (e0 == '}' or (e0 != ',' and e0 != '{')):
                    q.append('*')
                q.append(c)
            elif c == ',':
                while q[-1] == '*':
                    item[-2] = self.product(item[-2], item[-1])
                    item.pop(-1)
                    q.pop(-1)
                q.append('+')
            elif c == '}':
                op = q.pop(-1)
                while op != '{':
                    if op == '+':
                        item[-2] = self.add(item[-2], item[-1])
                    elif op == '*':
                        item[-2] = self.product(item[-2], item[-1])
                    item.pop(-1)
                    op = q.pop(-1)
            else:
                e0 = expression[i-1]
                if i != 0 and (e0 == '}' or (e0 != ',' and e0 != '{')):
                    q.append('*')
                item.append([c])
                
        while q:
            op = q.pop(-1)
            if op == '+':
                item[-2] = self.add(item[-2], item[-1])
            elif op == '*':
                item[-2] = self.product(item[-2], item[-1])
            item.pop(-1)
        # print q,item
        return sorted(item[0])
