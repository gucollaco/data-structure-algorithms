# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# importing the required packages
import random
import copy
import time

# date class
class Date:
  # init method / constructor
  def __init__(self):
    self.day = str(random.randrange(1, 32, 1)).zfill(2)
    self.month = str(random.randrange(1, 13, 1)).zfill(2)
    self.year = str(random.randrange(2000, 2023, 1))
    self.date_key = int(self.year + self.month + self.day)
 
# method to generate random dates
def generate_random_dates(dates_quantity):
  dates = []
  keys = []
  for _ in range(0, dates_quantity):
    date = Date()
    dates.append(date)
    keys.append(date.date_key)
  return dates, keys

# code imported from: https://www.programiz.com/dsa/radix-sort
# using counting sort to sort the elements in the basis of significant places
def counting_sort(array, place):
  size = len(array)
  output = [0] * size
  count = [0] * 10

  # Calculate count of elements
  for i in range(0, size):
    index = array[i] // place
    count[index % 10] += 1

  # Calculate cumulative count
  for i in range(1, 10):
    count[i] += count[i - 1]

  # Place the elements in sorted order
  i = size - 1
  while i >= 0:
    index = array[i] // place
    output[count[index % 10] - 1] = array[i]
    count[index % 10] -= 1
    i -= 1

  for i in range(0, size):
    array[i] = output[i]

# code imported from: https://www.programiz.com/dsa/radix-sort
# main function to implement radix sort
def radix_sort(array):
  # Get maximum element
  max_element = max(array)

  # Apply counting sort to sort elements based on place value.
  place = 1
  while max_element // place > 0:
    counting_sort(array, place)
    place *= 10

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

# main function
def main():
  # constants
  dates_quantity = 10
  dates_radix, keys_radix = generate_random_dates(dates_quantity)
  keys_merge = copy.deepcopy(keys_radix)
  keys_heap = copy.deepcopy(keys_radix)

  # radix_sort time
  start_time = time.time()
  radix_sort(keys_radix)
  time_interval = time.time() - start_time
  print("Radixsort (with counting sort): " + str(time_interval))

  # mergesort time
  start_time = time.time()
  mergesort(keys_merge)
  time_interval = time.time() - start_time
  print("Mergesort: " + str(time_interval))

  # heapsort time
  start_time = time.time()
  heapsort(keys_heap)
  time_interval = time.time() - start_time
  print("Heapsort: " + str(time_interval))

  # prints final arrays
  # print(keys_radix)
  # print(keys_merge)

# calling the main function
if __name__ == "__main__":
  main()