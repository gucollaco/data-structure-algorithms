# -*- coding: utf-8 -*-
# Gustavo Martins Collaço
# Description: comparing the patience sorting algorithm with other algorithms (mergesort and heapsort)

# importing the required packages
import random
import copy
import time
import sys
import resource
import bisect
import heapq

# change recursion limit to avoid python maximum recursion depth exceeded runtime error
sys.setrecursionlimit(500000)

# change resource limits to avoid python segmentation fault (core dumped) error
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

# create a randomized array with the given length
def create_random_array(array_length):
  array = list(range(0, array_length))
  shuffle_array(array)
  return array

# create an asc ordered array with the given length
def create_asc_array(array_length):
  array = list(range(0, array_length))
  return array

# create a desc ordered array with the given length
def create_desc_array(array_length):
  array = list(range(0, array_length))
  array.reverse()
  return array

# shuffle array
def shuffle_array(array):
  random.shuffle(array)

# Code imported from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Patience_sort#Python_3
def patience_sort(seq):
  piles = []
  for x in seq:
    new_pile = [x]
    i = bisect.bisect_left(piles, new_pile)
    if i != len(piles):
      piles[i].insert(0, x)
    else:
      piles.append(new_pile)

  # priority queue allows us to retrieve least pile efficiently
  for i in range(len(seq)):
    small_pile = piles[0]
    seq[i] = small_pile.pop(0)
    if small_pile:
      heapq.heapreplace(piles, small_pile)
    else:
      heapq.heappop(piles)
  assert not piles

# heapsort implementation
# code imported from: https://www.programiz.com/dsa/heap-sort
def heapsort(arr):
  def heapify(arr, n, i):
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

  n = len(arr)

  # Build max heap
  for i in range(n//2, -1, -1):
    heapify(arr, n, i)

  for i in range(n-1, 0, -1):
    # Swap
    arr[i], arr[0] = arr[0], arr[i]

    # Heapify root element
    heapify(arr, i, 0)

# mergesort implementation
# code imported from: https://www.programiz.com/dsa/merge-sort
def mergesort(array):
  if len(array) > 1:

    #  r is the point where the array is divided into two subarrays
    r = len(array)//2
    L = array[:r]
    M = array[r:]

    # Sort the two halves
    mergesort(L)
    mergesort(M)

    i = j = k = 0

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
  array_short = 1000
  array_large = 1000000
  
  # keep the results
  keep_patience_short_random = []
  keep_patience_large_random = []
  keep_patience_short_asc = []
  keep_patience_large_asc = []
  keep_patience_short_desc = []
  keep_patience_large_desc = []
  keep_heap_short_random = []
  keep_heap_large_random = []
  keep_heap_short_asc = []
  keep_heap_large_asc = []
  keep_heap_short_desc = []
  keep_heap_large_desc = []
  keep_merge_short_random = []
  keep_merge_large_random = []
  keep_merge_short_asc = []
  keep_merge_large_asc = []
  keep_merge_short_desc = []
  keep_merge_large_desc = []

  # we will run each one 10 times, and get the average
  for x in range(0, 10):
    # short arrays
    array_random_patience_short = create_random_array(array_short)
    array_random_heap_short = copy.deepcopy(array_random_patience_short)
    array_random_merge_short = copy.deepcopy(array_random_patience_short)

    array_asc_patience_short = create_asc_array(array_short)
    array_asc_heap_short = copy.deepcopy(array_asc_patience_short)
    array_asc_merge_short = copy.deepcopy(array_asc_patience_short)

    array_desc_patience_short = create_desc_array(array_short)
    array_desc_heap_short = copy.deepcopy(array_desc_patience_short)
    array_desc_merge_short = copy.deepcopy(array_desc_patience_short)


    # large arrays
    array_random_patience_large = create_random_array(array_large)
    array_random_heap_large = copy.deepcopy(array_random_patience_large)
    array_random_merge_large = copy.deepcopy(array_random_patience_large)

    array_asc_patience_large = create_asc_array(array_large)
    array_asc_heap_large = copy.deepcopy(array_asc_patience_large)
    array_asc_merge_large = copy.deepcopy(array_asc_patience_large)

    array_desc_patience_large = create_desc_array(array_large)
    array_desc_heap_large = copy.deepcopy(array_desc_patience_large)
    array_desc_merge_large = copy.deepcopy(array_desc_patience_large)



    print("________________")
    print("\n--iteration " + str(x+1) + "--")


    print("\n--short arrays randomized (n = 1000)--")

    start_time = time.time()
    patience_sort(array_random_patience_short)
    time_interval = time.time() - start_time
    print("Patience sort (random) (short array): " + str(time_interval))
    keep_patience_short_random.append(time_interval)
    
    start_time = time.time()
    heapsort(array_random_heap_short)
    time_interval = time.time() - start_time
    print("Heap sort (random) (short array): " + str(time_interval))
    keep_heap_short_random.append(time_interval)

    mergesort(array_random_merge_short)
    time_interval = time.time() - start_time
    print("Merge sort (random) (short array): " + str(time_interval))
    keep_merge_short_random.append(time_interval)


    print("\n--short arrays asc (n = 1000)--")

    start_time = time.time()
    patience_sort(array_asc_patience_short)
    time_interval = time.time() - start_time
    print("Patience sort (asc) (short array): " + str(time_interval))
    keep_patience_short_asc.append(time_interval)
    
    start_time = time.time()
    heapsort(array_asc_heap_short)
    time_interval = time.time() - start_time
    print("Heap sort (asc) (short array): " + str(time_interval))
    keep_heap_short_asc.append(time_interval)

    mergesort(array_asc_merge_short)
    time_interval = time.time() - start_time
    print("Merge sort (asc) (short array): " + str(time_interval))
    keep_merge_short_asc.append(time_interval)


    print("\n--short arrays desc (n = 1000)--")

    start_time = time.time()
    patience_sort(array_desc_patience_short)
    time_interval = time.time() - start_time
    print("Patience sort (desc) (short array): " + str(time_interval))
    keep_patience_short_desc.append(time_interval)
    
    start_time = time.time()
    heapsort(array_desc_heap_short)
    time_interval = time.time() - start_time
    print("Heap sort (desc) (short array): " + str(time_interval))
    keep_heap_short_desc.append(time_interval)

    mergesort(array_desc_merge_short)
    time_interval = time.time() - start_time
    print("Merge sort (desc) (short array): " + str(time_interval))
    keep_merge_short_desc.append(time_interval)


    print("\n--large arrays randomized (n = 1000000)--")

    start_time = time.time()
    patience_sort(array_random_patience_large)
    time_interval = time.time() - start_time
    print("Patience sort (random) (large array): " + str(time_interval))
    keep_patience_large_random.append(time_interval)
    
    start_time = time.time()
    heapsort(array_random_heap_large)
    time_interval = time.time() - start_time
    print("Heap sort (random) (large array): " + str(time_interval))
    keep_heap_large_random.append(time_interval)

    mergesort(array_random_merge_large)
    time_interval = time.time() - start_time
    print("Merge sort (random) (large array): " + str(time_interval))
    keep_merge_large_random.append(time_interval)


    print("\n--large arrays asc (n = 1000000)--")

    start_time = time.time()
    patience_sort(array_asc_patience_large)
    time_interval = time.time() - start_time
    print("Patience sort (asc) (large array): " + str(time_interval))
    keep_patience_large_asc.append(time_interval)
    
    start_time = time.time()
    heapsort(array_asc_heap_large)
    time_interval = time.time() - start_time
    print("Heap sort (asc) (large array): " + str(time_interval))
    keep_heap_large_asc.append(time_interval)

    mergesort(array_asc_merge_large)
    time_interval = time.time() - start_time
    print("Merge sort (asc) (large array): " + str(time_interval))
    keep_merge_large_asc.append(time_interval)


    print("\n--large arrays desc (n = 1000000)--")

    start_time = time.time()
    patience_sort(array_desc_patience_large)
    time_interval = time.time() - start_time
    print("Patience sort (desc) (large array): " + str(time_interval))
    keep_patience_large_desc.append(time_interval)
    
    start_time = time.time()
    heapsort(array_desc_heap_large)
    time_interval = time.time() - start_time
    print("Heap sort (desc) (large array): " + str(time_interval))
    keep_heap_large_desc.append(time_interval)

    mergesort(array_desc_merge_large)
    time_interval = time.time() - start_time
    print("Merge sort (desc) (large array): " + str(time_interval))
    keep_merge_large_desc.append(time_interval)

  print("________________")
  print("\n--averages--")

  print("\n--short arrays random (n = 1000)--")
  print("Patience sort: " + str(sum(keep_patience_short_random) / len(keep_patience_short_random)))
  print("Heap sort: " + str(sum(keep_heap_short_random) / len(keep_heap_short_random)))
  print("Merge sort: " + str(sum(keep_merge_short_random) / len(keep_merge_short_random)))

  print("\n--short arrays asc (n = 1000)--")
  print("Patience sort: " + str(sum(keep_patience_short_asc) / len(keep_patience_short_asc)))
  print("Heap sort: " + str(sum(keep_heap_short_asc) / len(keep_heap_short_asc)))
  print("Merge sort: " + str(sum(keep_merge_short_asc) / len(keep_merge_short_asc)))

  print("\n--short arrays desc (n = 1000)--")
  print("Patience sort: " + str(sum(keep_patience_short_desc) / len(keep_patience_short_desc)))
  print("Heap sort: " + str(sum(keep_heap_short_desc) / len(keep_heap_short_desc)))
  print("Merge sort: " + str(sum(keep_merge_short_desc) / len(keep_merge_short_desc)))

  print("\n--large arrays random (n = 1000000)--")
  print("Patience sort: " + str(sum(keep_patience_large_random) / len(keep_patience_large_random)))
  print("Heap sort: " + str(sum(keep_heap_large_random) / len(keep_heap_large_random)))
  print("Merge sort: " + str(sum(keep_merge_large_random) / len(keep_merge_large_random)))

  print("\n--large arrays asc (n = 1000000)--")
  print("Patience sort: " + str(sum(keep_patience_large_asc) / len(keep_patience_large_asc)))
  print("Heap sort: " + str(sum(keep_heap_large_asc) / len(keep_heap_large_asc)))
  print("Merge sort: " + str(sum(keep_merge_large_asc) / len(keep_merge_large_asc)))

  print("\n--large arrays desc (n = 1000000)--")
  print("Patience sort: " + str(sum(keep_patience_large_desc) / len(keep_patience_large_desc)))
  print("Heap sort: " + str(sum(keep_heap_large_desc) / len(keep_heap_large_desc)))
  print("Merge sort: " + str(sum(keep_merge_large_desc) / len(keep_merge_large_desc)))

# calling the main function
if __name__ == "__main__":
  main()