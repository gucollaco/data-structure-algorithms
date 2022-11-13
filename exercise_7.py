# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# function to check if the base has a pair with the current top of the stack
def pair_with_top(base, top_of_stack):
  if base == "C":
    return top_of_stack == "F"
  elif base == "F":
    return top_of_stack == "C"
  elif base == "B":
    return top_of_stack == "S"
  elif base == "S":
    return top_of_stack == "B"

# main function
def main():
  while True:
    try:
      # the received sequence
      rnaa_sequence = input()
      rnaa_sequence_list = list(rnaa_sequence)

      # the quantity of pairs we have within the received sequence
      pairs = 0

      # a stack that will help us checking the pairs within the received sequence list
      rnaa_stack = []

      for base in rnaa_sequence_list:
        # if the stack is empty, we simply append the item to the stack
        if len(rnaa_stack) == 0:
          rnaa_stack.append(base)
        # if the stack is not empty, we have two cases
        else:
          # if the current base pairs with the one on the top of the stack, we increment the pairs counter, and pop the top of the stack
          if pair_with_top(base, rnaa_stack[len(rnaa_stack) - 1]):
            pairs += 1
            rnaa_stack.pop()
          # if not, we apppend the item to the stack
          else:
            rnaa_stack.append(base)

      # printing the quantity of pairs found
      print(pairs)

    # while loop breaks on EOF
    except EOFError:
      break
  
# calling the main function
if __name__ == "__main__":
  main()