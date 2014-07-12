import heapq

try:
    input = raw_input
except NameError:
    pass

def swm(array, w):
    pairs = []
    B = []
    for i in range(w):
        pairs.append([-array[i],i])
    heapq.heapify(pairs)
    for i in range(len(array)-w+1):
        B.append(-pairs[0][0])
        if i+w < len(array):
            heapq.heappush(pairs, [-array[i+w],i+w])
            while pairs[0][1] <= i:
                heapq.heappop(pairs)
    return B

def main():
    array_raw = input("input an array separated by ',':")
    winw = eval(input("input the width of the window:"))
    array_s = array_raw.split(',')
    array = []
    for item in array_s:
        array.append(eval(item))
    print(swm(array, winw))
        

if __name__ == "__main__":
    main()
