# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# importing the required packages
import random
import copy
import time
import sys
import resource

# change recursion limit to avoid python maximum recursion depth exceeded runtime error
sys.setrecursionlimit(500000)

# change resource limits to avoid python segmentation fault (core dumped) error
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


# shuffle array
def shuffle_array(array):
  random.shuffle(array)

# recursive sequential search method
def recursive_sequential_search(numbers_array, index, last_index, target):
  # when element couldn't be found
  if index > last_index:
    return None
  # if found, we return the value (here we will check the left index)
  if numbers_array[index] == target:
    return index
  # if found, we return the value (here we will check the right index)
  if numbers_array[last_index] == target:
    return last_index

  return recursive_sequential_search(numbers_array, index + 1, last_index - 1, target)

# recursive binary search method
def recursive_binary_search(numbers_array, numbers_array_left_index, numbers_array_right_index, target):
  # when element couldn't be found
  if numbers_array_left_index > numbers_array_right_index:
    return None

  else:
    # get middle index based on the given left and right indexes
    middle_index = (numbers_array_left_index + numbers_array_right_index) / 2

    # return the index if found on middle position
    if target == numbers_array[middle_index]:
      return middle_index

    # when target is greater than the middle value, it should look on the right side
    elif target > numbers_array[middle_index]:
      return recursive_binary_search(numbers_array, middle_index + 1, numbers_array_right_index, target)
    
    # when target is smaller than the middle value, it should look on the left side
    else:
      return recursive_binary_search(numbers_array, numbers_array_left_index, middle_index - 1, target)
      
# method that will call the recursive_sequential_search method
def recursive_sequential(numbers_array, index, numbers_array_last_index, target_one, target_two):
  # measuring the time to find the target one through this method
  start_time_one = time.time()
  index_target_one = recursive_sequential_search(numbers_array, index, numbers_array_last_index, target_one)
  print("\n--- recursive sequential search ---")
  print("index target one: " + str(index_target_one))
  print("seconds: " + str(time.time() - start_time_one))

  # measuring the time to find the target two through this method
  start_time_two = time.time()
  index_target_two = recursive_sequential_search(numbers_array, index, numbers_array_last_index, target_two)
  print("\n--- recursive sequential search ---")
  print("index target two: " + str(index_target_two))
  print("seconds: " + str(time.time() - start_time_two))
  return

# method that will call the recursive_binary_search method
def recursive_binary(numbers_array, numbers_array_left_index, numbers_array_right_index, target_one, target_two):
  # first execution
  # the recursive_binary_search method expects the numbers array to be sorted
  numbers_array_sorted = copy.deepcopy(numbers_array)
  start_time_one = time.time()
  numbers_array_sorted.sort()
  
  # here we will have the sorted_index value, which will be the same as the value that corresponds to that index, as this numbers array is sorted
  sorted_index_target_one = recursive_binary_search(numbers_array_sorted, numbers_array_left_index, numbers_array_right_index, target_one)
  print("\n--- recursive binary search ---")
  print("target one found")
  print("seconds: " + str(time.time() - start_time_one))
  
  # second execution
  # the recursive_binary_search method expects the numbers array to be sorted
  numbers_array_sorted_two = copy.deepcopy(numbers_array)
  start_time_two = time.time()
  numbers_array_sorted_two.sort()
  
  sorted_index_target_two = recursive_binary_search(numbers_array_sorted_two, numbers_array_left_index, numbers_array_right_index, target_two)
  print("\n--- recursive binary search ---")
  print("target two found")
  print("seconds: " + str(time.time() - start_time_two))

  # once we have the sorted_index value, that we got through the recursive_binary_search method,
  # we can call the recursive_sequential_search passing the sorted_index as the target
  original_index_target_one =  recursive_sequential_search(numbers_array, numbers_array_left_index, numbers_array_right_index, sorted_index_target_one)
  original_index_target_two =  recursive_sequential_search(numbers_array, numbers_array_left_index, numbers_array_right_index, sorted_index_target_two)

  print("\n")
  print("index target one: " + str(original_index_target_one))
  print("index target two: " + str(original_index_target_two))
  return

# main function
def main():
  # constants
  numbers_array_length = 100000
  numbers_array = list(range(0, numbers_array_length))
  shuffle_array(numbers_array)

  target_one = 9
  target_two = 99999
  recursive_sequential(numbers_array, 0, numbers_array_length - 1, target_one, target_two)
  recursive_binary(numbers_array, 0, numbers_array_length - 1, target_one, target_two)

# calling the main function
if __name__ == "__main__":
  main()