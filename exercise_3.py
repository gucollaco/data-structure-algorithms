# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# importing the required packages
from itertools import permutations

# method to get the permutation for a given word
def get_permutation(word):
  # getting all permutation
  permutation = [''.join(p) for p in permutations(word)]
  return permutation

# get the unique values for a sequence of elements
# method implementation suggestion can be found on: 
# https://stackoverflow.com/questions/9792664/converting-a-list-to-a-set-changes-element-order or
# http://www.martinbroadhurst.com/removing-duplicates-from-a-list-while-preserving-order-in-python.html
def unique(sequence):
  seen = set()
  return [x for x in sequence if not (x in seen or seen.add(x))]

# main function
def main():
  # the quantity of words to be received
  words_qty = input()

  # loop from 0 to the informed quantity of words, getting the permutations for each word
  for _ in range(0, int(words_qty)):
    word = input()

    # truncate the string to 10 characters max, and sort the strings' characters
    word_truncated = str(word[:10])
    word_sorted = ''.join(sorted(word_truncated))
    
    # get the permutation for the sorted informed word
    permutation = get_permutation(word_sorted)
    
    # print each word from the unique values of the permutations array  
    for word in unique(permutation):
      print(word)
    print("")

# calling the main function
if __name__ == "__main__":
  main()
