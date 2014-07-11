
try:
    input = raw_input
except NameError:
    pass

def swm(array, winw):
    sumw = 0
    for i in range(winw):
        sumw += array[i]
    maxw = sumw
    for i in range(len(array)-winw):
        sumw += array[i+winw] - array[i]
        if sumw > maxw:
            maxw = sumw
    return maxw

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
