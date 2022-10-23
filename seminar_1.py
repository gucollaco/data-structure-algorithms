# -*- coding: utf-8 -*-
# Gustavo Martins Collaço
# Description: implementation of the patience sorting algorithm

# importing the required packages
import bisect
import heapq

# Code imported from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Patience_sort#Python_3
def patience_sort(seq):
  piles = []
  print("___________")
  print("** phase 1 **")
  for x in seq:
    new_pile = [x]
    i = bisect.bisect_left(piles, new_pile)
    if i != len(piles):
      piles[i].insert(0, x)
    else:
      piles.append(new_pile)
  print("piles", str(piles))
  print("longest increasing subsequence has length = ", len(piles))

  print("___________")
  print("** phase 2 **")
  # priority queue allows us to retrieve least pile efficiently
  for i in range(len(seq)):
    small_pile = piles[0]
    print("piles", piles)
    seq[i] = small_pile.pop(0)
    print("the smallest value is = ", seq[i])
    print("piles", piles)
    if small_pile:
      heapq.heapreplace(piles, small_pile)
    else:
      heapq.heappop(piles)
  assert not piles

# create an asc ordered array with the given length
def create_asc_array(array_length):
  array = list(range(0, array_length))
  return array

# create a desc ordered array with the given length
def create_desc_array(array_length):
  array = list(range(0, array_length))
  array.reverse()
  return array

# foo = [10, 4, 8, 3, 9, 5, 13, 11, 12]
foo = [3, 4, 5, 8, 9, 10, 11, 12, 13]
# foo = [13, 12, 11, 10, 9, 8, 5, 4, 3]
print(foo)
patience_sort(foo)
print(foo)
