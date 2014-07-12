import pdb

try:
    input = raw_input
except NameError:
    pass

def quicksort(a,left,right):
    if left >= right:
        return
    p = a[left]
    l = left
    r = right
    while l<r:
        while l<r and a[r] >= p:
            r -= 1
        if l<r:
            a[l] = a[r]
            l += 1
        while l<r and a[l] <= p:
            l += 1
        if l<r:
            a[r] = a[l]
            r -= 1
    a[l] = p
    quicksort(a,left,l-1)
    quicksort(a,l+1,right)


def main():
    array_raw = input("input an array separated by ',':")
    array_s = array_raw.split(',')
    array = []
    for item in array_s:
        array.append(eval(item))
    print(array)
    quicksort(array,0,len(array)-1)
    print(array)

if __name__ == '__main__':
    main()
