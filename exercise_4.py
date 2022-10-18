# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# importing the required packages
import random
import copy
import time
import sys
import resource

# create a randomized array with the given length
def create_random_array(array_length):
  array = list(range(0, array_length))
  shuffle_array(array)
  return array

# shuffle array
def shuffle_array(array):
  random.shuffle(array)

# shellsort implementation (shell sequence)
# code imported from: https://www.programiz.com/dsa/shell-sort
# the ascending parameter was added on top of the implementation
def shellsort(array, n, ascending=True):
  # Rearrange elements at each n/2, n/4, n/8, ... intervals
  interval = n // 2

  if ascending == True:
    while interval > 0:
      for i in range(interval, n):
        temp = array[i]
        j = i
        while j >= interval and array[j - interval] > temp:
          array[j] = array[j - interval]
          j -= interval

        array[j] = temp
      interval //= 2
  else:
    while interval > 0:
      for i in range(interval, n):
        temp = array[i]
        j = i
        while j >= interval and array[j - interval] < temp:
          array[j] = array[j - interval]
          j -= interval

        array[j] = temp
      interval //= 2

# shellsort implementation receiving the gaps as prop
# code inspired from: https://www.programiz.com/dsa/shell-sort
# and https://stackoverflow.com/questions/72005446/how-to-implement-different-sequences-in-shell-sort-in-python
# the ascending was added on top of the implementation
def shellsort_gaps(array, n, gap_sequence, ascending=True):
  if ascending == True:
    for gap in gap_sequence:
      for offset in range(gap):
        for i in range(offset, n, gap):
          temp = array[i]
          j = i
          while j >= gap and array[j - gap] > temp:
            array[j] = array[j - gap]
            j -= gap

          array[j] = temp

  else:
    for gap in gap_sequence:
      for offset in range(gap):
        for i in range(offset, n, gap):
          temp = array[i]
          j = i
          while j >= gap and array[j - gap] < temp:
            array[j] = array[j - gap]
            j -= gap

          array[j] = temp

# heapsort implementation
# code imported from: https://www.programiz.com/dsa/heap-sort
# the ascending parameter was added on top of the implementation
def heapsort(arr, ascending=True):
  def heapify(arr, n, i):
    if ascending == True:
      # Find largest (when ascending) among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2

      if l < n and arr[i] < arr[l]:
        largest = l

      if r < n and arr[largest] < arr[r]:
        largest = r

      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

    else:
      # Find smallest (when descending) among root and children
      smallest = i
      l = 2 * i + 1
      r = 2 * i + 2

      if l < n and arr[i] > arr[l]:
        smallest = l

      if r < n and arr[smallest] > arr[r]:
        smallest = r

      # If root is not smallest, swap with smallest and continue heapifying
      if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


  n = len(arr)

  # Build max heap
  for i in range(n//2, -1, -1):
    heapify(arr, n, i)

  for i in range(n-1, 0, -1):
    # Swap
    arr[i], arr[0] = arr[0], arr[i]

    # Heapify root element
    heapify(arr, i, 0)

# quicksort (rightmost) implementation
# code inspired from: https://www.programiz.com/dsa/quick-sort
# and https://stackoverflow.com/questions/71642317/how-to-choose-middle-element-of-the-array-as-the-pivot-in-quicksort
# the ascending parameter was added on top of the implementation
def quicksort(array, low, high, ascending=True, use_central_pivot=False):
  # function to find the partition position
  def partition(array, low, high):
    if use_central_pivot == True:
      array[(low+high)//2], array[high] = array[high], array[(low+high)//2]

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    if ascending == True:
      # when ascending is True
      for j in range(low, high):
        if array[j] <= pivot:
          # if element smaller than pivot is found
          # swap it with the greater element pointed by i
          i = i + 1

          # swapping element at i with element at j
          (array[i], array[j]) = (array[j], array[i])
    else:
      # when ascending is False
      for j in range(low, high):
        if array[j] >= pivot:
          # if element greater than pivot is found
          # swap it with the greater element pointed by i
          i = i + 1

          # swapping element at i with element at j
          (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1

  if low < high:
    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quicksort(array, low, pi - 1, ascending)

    # recursive call on the right of pivot
    quicksort(array, pi + 1, high, ascending)

# mergesort implementation
# code imported from: https://www.programiz.com/dsa/merge-sort
# the ascending parameter was added on top of the implementation
def mergesort(array, ascending=True):
  if len(array) > 1:

    #  r is the point where the array is divided into two subarrays
    r = len(array)//2
    L = array[:r]
    M = array[r:]

    # Sort the two halves
    mergesort(L, ascending)
    mergesort(M, ascending)

    i = j = k = 0

    if ascending == True:
      # Until we reach either end of either L or M, pick larger among
      # elements L and M and place them in the correct position at A[p..r]
      while i < len(L) and j < len(M):
        if L[i] < M[j]:
          array[k] = L[i]
          i += 1
        else:
          array[k] = M[j]
          j += 1
        k += 1
    else:
      # Until we reach either end of either L or M, pick larger among
      # elements L and M and place them in the correct position at A[p..r]
      while i < len(L) and j < len(M):
        if L[i] > M[j]:
          array[k] = L[i]
          i += 1
        else:
          array[k] = M[j]
          j += 1
        k += 1

    # When we run out of elements in either L or M,
    # pick up the remaining elements and put in A[p..r]
    while i < len(L):
      array[k] = L[i]
      i += 1
      k += 1

    while j < len(M):
      array[k] = M[j]
      j += 1
      k += 1

# main function
def main():
  # constants
  numbers_array_length = 10
  ciura_sequence = [701, 301, 132, 57, 23, 10, 4, 1]
  knuth_sequence = [29524, 9841, 3280, 1093, 364, 121, 40, 13, 4, 1]

  # keep the results
  keep_shell_asc = []
  keep_shell_ciura_asc = []
  keep_shell_knuth_asc = []
  keep_shell_desc = []
  keep_shell_ciura_desc = []
  keep_shell_knuth_desc = []
  keep_heap_asc = []
  keep_heap_desc = []
  keep_quick_asc = []
  keep_quick_central_asc = []
  keep_quick_desc = []
  keep_quick_central_desc = []
  keep_merge_asc = []
  keep_merge_desc = []

  # we will run each one 10 times, and get the average
  for x in range(0, 10): 

    # creating the arrays that will be ordered by each of the algorithms
    numbers_array_shell_asc = create_random_array(numbers_array_length)
    numbers_array_shell_ciura_asc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_shell_knuth_asc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_shell_desc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_shell_ciura_desc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_shell_knuth_desc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_heap_asc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_heap_desc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_quick_asc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_quick_central_asc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_quick_desc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_quick_central_desc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_merge_asc = copy.deepcopy(numbers_array_shell_asc)
    numbers_array_merge_desc = copy.deepcopy(numbers_array_shell_asc)

    print("________________")
    print("\n--iteration " + str(x+1) + "--")
    print("\n--ascending--")
    # ascending shellsort (shell sequence)
    start_time = time.time()
    shellsort(numbers_array_shell_asc, numbers_array_length, True)
    time_interval = time.time() - start_time
    print("Shellsort (shell sequence): " + str(time_interval))
    keep_shell_asc.append(time_interval)
    # ascending shellsort (ciura sequence)
    start_time = time.time()
    shellsort_gaps(numbers_array_shell_ciura_asc, numbers_array_length, ciura_sequence, True)
    time_interval = time.time() - start_time
    print("Shellsort (ciura sequence): " + str(time_interval))
    keep_shell_ciura_asc.append(time_interval)
    # ascending shellsort (knuth sequence)
    start_time = time.time()
    shellsort_gaps(numbers_array_shell_knuth_asc, numbers_array_length, knuth_sequence, True)
    time_interval = time.time() - start_time
    print("Shellsort (knuth sequence): " + str(time_interval))
    keep_shell_knuth_asc.append(time_interval)
    # ascending heapsort
    start_time = time.time()
    heapsort(numbers_array_heap_asc, True)
    time_interval = time.time() - start_time
    print("Heapsort: " + str(time_interval))
    keep_heap_asc.append(time_interval)
    # ascending quicksort (rightmost pivot)
    start_time = time.time()
    quicksort(numbers_array_quick_asc, 0, numbers_array_length - 1, True)
    time_interval = time.time() - start_time
    print("Quicksort (rightmost pivot): " + str(time_interval))
    keep_quick_asc.append(time_interval)
    # ascending quicksort (central pivot)
    start_time = time.time()
    quicksort(numbers_array_quick_central_asc, 0, numbers_array_length - 1, True, True)
    time_interval = time.time() - start_time
    print("Quicksort (central pivot): " + str(time_interval))
    keep_quick_central_asc.append(time_interval)
    # ascending mergesort
    start_time = time.time()
    mergesort(numbers_array_merge_asc, True)
    time_interval = time.time() - start_time
    print("Mergesort: " + str(time_interval))
    keep_merge_asc.append(time_interval)

    print("\n--descending--")
    # descending shellsort (shell sequence)
    start_time = time.time()
    shellsort(numbers_array_shell_desc, numbers_array_length, False)
    time_interval = time.time() - start_time
    print("Shellsort (shell sequence): " + str(time_interval))
    keep_shell_desc.append(time_interval)
    # ascending shellsort (ciura sequence)
    start_time = time.time()
    shellsort_gaps(numbers_array_shell_ciura_desc, numbers_array_length, ciura_sequence, False)
    time_interval = time.time() - start_time
    print("Shellsort (ciura sequence): " + str(time_interval))
    keep_shell_ciura_desc.append(time_interval)
    # ascending shellsort (knuth sequence)
    start_time = time.time()
    shellsort_gaps(numbers_array_shell_knuth_desc, numbers_array_length, knuth_sequence, False)
    time_interval = time.time() - start_time
    print("Shellsort (knuth sequence): " + str(time_interval))
    keep_shell_knuth_desc.append(time_interval)
    # descending heapsort
    start_time = time.time()
    heapsort(numbers_array_heap_desc, False)
    time_interval = time.time() - start_time
    print("Heapsort: " + str(time_interval))
    keep_heap_desc.append(time_interval)
    # descending quicksort (rightmost pivot)
    start_time = time.time()
    quicksort(numbers_array_quick_desc, 0, numbers_array_length - 1, False)
    time_interval = time.time() - start_time
    print("Quicksort (rightmost pivot): " + str(time_interval))
    keep_quick_desc.append(time_interval)
    # descending quicksort (central pivot)
    start_time = time.time()
    quicksort(numbers_array_quick_central_desc, 0, numbers_array_length - 1, False, True)
    time_interval = time.time() - start_time
    print("Quicksort (central pivot): " + str(time_interval))
    keep_quick_central_desc.append(time_interval)
    # descending mergesort
    start_time = time.time()
    mergesort(numbers_array_merge_desc, False)
    time_interval = time.time() - start_time
    print("Mergesort: " + str(time_interval))
    keep_merge_desc.append(time_interval)

  print("________________")
  print("\n--averages--")

  print("\n--ascending--")
  print("Shellsort (shell sequence): " + str(sum(keep_shell_asc) / len(keep_shell_asc)))
  print("Shellsort (ciura sequence): " + str(sum(keep_shell_ciura_asc) / len(keep_shell_ciura_asc)))
  print("Shellsort (knuth sequence): " + str(sum(keep_shell_knuth_asc) / len(keep_shell_knuth_asc)))
  print("Heapsort: " + str(sum(keep_heap_asc) / len(keep_heap_asc)))
  print("Quicksort (rightmost pivot): " + str(sum(keep_quick_asc) / len(keep_quick_asc)))
  print("Quicksort (central pivot): " + str(sum(keep_quick_central_asc) / len(keep_quick_central_asc)))
  print("Mergesort: " + str(sum(keep_merge_asc) / len(keep_merge_asc)))

  print("\n--descending--")
  print("Shellsort (shell sequence): " + str(sum(keep_shell_desc) / len(keep_shell_desc)))
  print("Shellsort (ciura sequence): " + str(sum(keep_shell_ciura_desc) / len(keep_shell_ciura_desc)))
  print("Shellsort (knuth sequence): " + str(sum(keep_shell_knuth_desc) / len(keep_shell_knuth_desc)))
  print("Heapsort: " + str(sum(keep_heap_desc) / len(keep_heap_desc)))
  print("Quicksort (rightmost pivot): " + str(sum(keep_quick_desc) / len(keep_quick_desc)))
  print("Quicksort (central pivot): " + str(sum(keep_quick_central_desc) / len(keep_quick_central_desc)))
  print("Mergesort: " + str(sum(keep_merge_desc) / len(keep_merge_desc)))

# calling the main function
if __name__ == "__main__":
  main()