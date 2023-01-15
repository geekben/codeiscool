# coding=utf-8
# 完全二叉堆实现优先级队列（优先级高的先出队）
# 即保证队列在不停加入新元素的情况下，还能维持二叉堆的排序
# 由于每次只取出最高优先级，所以子节点只要比父节点优先级低即可
# 出队O(logN)包含调整修复，入队O(logN)
# item = [val, priority]
class prioriyQueue():
    q = []
    l = 0
    def maxHeapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        lg = -1
        if l < self.l and self.q[i][1] < self.q[l][1]:
            lg = l
        else:
            lg = i
        if r < self.l and self.q[lg][1] < self.q[r][1]:
            lg = r
        if lg != i:
            temp = self.q[lg]
            self.q[lg] = self.q[i]
            self.q[i] = temp
            self.maxHeapify(lg)


    def put(self, item):
        if self.q == []:
            self.q.append(item)
            self.l = 1
        else:
            self.q.append(item)
            self.l += 1
            i = self.l - 1
            p = (i - 1)/2
            while i != 0 and self.q[p][1] < item[1]:
                temp = self.q[p]
                self.q[p] = item
                self.q[i] = temp
                i = p
                p = (i - 1)/2

    def get(self):
        if self.l == 0:
            return None
        ret = self.q[0]
        self.q[0] = self.q[self.l-1]
        self.q.pop()
        self.l -= 1
        self.maxHeapify(0)
        return ret

    def empty(self):
        if self.l == 0:
            return True
        else:
            return False

    def show(self):
        for i in self.q:
            print i
        print self.q

q = prioriyQueue()
a = [2,4,2,1,6,44,2,33,21]
for i,v in enumerate(a):
    q.put(((i,v), v))
print "===="
print q.get()
print "===="
q.show()
print "===="
q.put(((77, 3), 3))
q.show()
print "===="
q.put(((78, 2), 2))
q.show()
print "===="
q.put(((79, 10), 10))
q.show()
print "===="
print q.get()
print "===="
q.show()
