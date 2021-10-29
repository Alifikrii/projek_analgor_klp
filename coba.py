import time

waktu1 = time.time()
f = open('random/Random10^4ke1.txt', 'r')
datas = []
for number in f:
    datas.append(int(number))
f.close()

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

datas = quick_sort(datas)
length = len(datas)
l1 = length//2
l2 = l1+1
data1 = datas[l1]
data2 = datas[l2]
median = (data1 + data2) / 2
time = time.time() - waktu1

print(median)
print(time)