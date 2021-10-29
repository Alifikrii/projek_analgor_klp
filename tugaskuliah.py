
import pandas as pd
import time

start_time = time.time()

f = open('random/Random10^6ke3.txt', 'r')
datas = []
for number in f:
    datas.append(int(number))
f.close()
print("panjang  ", len(datas) )

def median_of_medians(arr):
    if arr is None or len(arr) == 0:
        return None
    return select_pivot(arr, len(arr) // 2)


def select_pivot(arr, k):
    # Divide array into chunks of 5
    chunks = [arr[i: i + 5] for i in range(0, len(arr), 5)]

    sorted_chunks = [sorted(chunk) for chunk in chunks]

    # take the median of each chunk
    medians = [chunk[len(chunk) // 2] for chunk in sorted_chunks]

    # find the median of medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = select_pivot(medians, len(medians) // 2)

    # partition the array around the pivot
    p = partition(arr, pivot)

    # is the pivot position at the k position?
    if k == p:
        # select that pivot
        return pivot

    if k < p:
        return select_pivot(arr[0:p], k)
    else:
        return select_pivot(arr[p + 1:len(arr)], k - p - 1)


def partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    i = 0

    while i <= right:
        if arr[i] == pivot:
            i += 1

        elif arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        else:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
    return left

# proses baca data


pivot = median_of_medians(datas)
print(pivot)

finished_time = time.time() - start_time
print(f"Running Time =>", finished_time)

