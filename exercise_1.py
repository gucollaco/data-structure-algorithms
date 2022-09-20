# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# importing the required packages
import random
import time
import sys

# change recursion limit to avoid python maximum recursion depth exceeded runtime error
sys.setrecursionlimit(100000)

# function to check if number is prime through recursion
def prime_recursive(num, current_value = 2):
  if (num == 0 or num == 1):
    return False

  if num == current_value:
    return True
  elif (num % current_value) == 0:
    return False
  return prime_recursive(num, current_value + 1)

# function to check if number is prime through iteration
def prime_iteration(num, starting_value = 2):
  if (num == 0 or num == 1):
    return False

  for i in range(starting_value, num):
    if (num % i) == 0:
      return False
  return True

# recursive execution, using the prime_recursive method
def recursive_execution(random_numbers_array, starting_value):
  start_time = time.time()

  current_max = None
  for num in random_numbers_array:
    is_num_prime = prime_recursive(num, starting_value)

    if (is_num_prime and is_num_prime > current_max):
      current_max = num

  print("\n--- recursive method ---")
  print("greatest prime: " + str(current_max))
  print("seconds: " + str(time.time() - start_time))

# iteration execution, using the prime_iteration method
def iteration_execution(random_numbers_array, starting_value):
  start_time = time.time()

  current_max = None
  for num in random_numbers_array:
    is_num_prime = prime_iteration(num, starting_value)

    if (is_num_prime and is_num_prime > current_max):
      current_max = num

  print("\n--- iteration method ---")
  print("greatest prime: " + str(current_max))
  print("seconds: " + str(time.time() - start_time))

# main function
def main():
  # constants
  starting_value = 2
  random_numbers_array = [random.randint(0, 10000) for _ in range(100000)]

  # calling the recursive and iteration methods execution
  recursive_execution(random_numbers_array, starting_value)
  iteration_execution(random_numbers_array, starting_value)

# calling the main function
if __name__ == "__main__":
  main()