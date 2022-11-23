# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# importing the required packages
from __future__ import print_function
import random
import time
import copy

# shuffle array
def shuffle_array(array):
  random.shuffle(array)

# create a randomized array with the given length
def create_random_array(array_length):
  array = list(range(0, array_length))
  shuffle_array(array)
  return array

# Binary search tree
# Code imported from: https://gist.github.com/stummjr/cd9974b513419f0554c5
class BSTNode(object):
  def __init__(self, key, value=None, left=None, right=None):
    self.key = key
    self.value = value
    self.left = left
    self.right = right

  def get(self, key):
    if self.key == key:
      return self
    node = self.left if key < self.key else self.right
    if node is not None:
      return node.get(key)

  def add(self, key):
    side = 'left' if key < self.key else 'right'
    node = getattr(self, side)
    if node is None:
      setattr(self, side, BSTNode(key))
    else:
      node.add(key)
  
  def remove(self, key):
    if key < self.key:
      self.left = self.left.remove(key)
    elif key > self.key:
      self.right = self.right.remove(key)
    else:
      if self.right is None:
        return self.left
      if self.left is None:
        return self.right
      t = self.right._min()
      self.key, self.value = t.key, t.value
      self.right._deleteMin()
    return self
  
  def _min(self):
    if self.left is None:
      return self
    else:
      return self.left._min()
  
  def _deleteMin(self):
      if self.left is None:  # encontrou o min, daí pode rearranjar
          return self.right
      self.left = self.left._deleteMin()
      return self

  def traverse(self, visit, order='pre'):
    if order == 'pre':
      visit(self.key)
    if self.left is not None:
      self.left.traverse(visit, order)
    if order == 'in':
      visit(self.key)
    if self.right is not None:
      self.right.traverse(visit, order)
    if order == 'post':
      visit(self.key)

  def print(self, order='pre'):
    self.traverse(print, order)

# Create a tree node
# Code imported from: https://github.com/mordiggian174/AVLTree/blob/main/Node.py
class Node:
  def __init__(self, key):
      self.key = key
      self.parent = None
      self.rightChild = None
      self.leftChild = None         
      self.height = 0
      self.size = 1
  def __str__(self):
      return str(self.key)#+'('+str(self.height)+')'
  def is_leaf(self):
      return self.height == 0
  def max_children_height(self):
      if self.leftChild and self.rightChild:
          return max(self.leftChild.height,self.rightChild.height)
      elif self.leftChild:
          return self.leftChild.height
      elif self.rightChild:
          return self.rightChild.height
      else:
          return -1

  def balance(self):
      return (self.leftChild.height if self.leftChild else -1) -\
              (self.rightChild.height if self.rightChild else -1)

# AVL tree
# Code imported from: https://github.com/mordiggian174/AVLTree/blob/main/AVLTree.py
class AVLTree():
  def __init__(self, h=[]):
      self.rootNode = None
      self.elements_count = 0
      self.rebalance_count = 0
      for el in h:
          self.insert(el)

  def height(self):
      if self.rootNode:
          return self.rootNode.height
      else:
          -1
          
  def find_in_subtree(self, key, node):
      if node is None:
          return None  # key not found
      if key < node.key:
          return self.find_in_subtree(key,node.leftChild)
      elif key > node.key:
          return self.find_in_subtree(key,node.rightChild)
      else:  # key is equal to node key
          return node
      
  def find(self, key, node=None):
      if node is None:
          node=self.rootNode
      return self.find_in_subtree(key,node)
          
  def recompute_heights(self, startNode):
      changed = True
      node = startNode
      while node and changed:
          old_height = node.height
          node.height = (node.max_children_height() + 1 if
                          (node.rightChild or node.leftChild) else 0)
          changed = node.height != old_height
          node = node.parent

  def find_biggest(self, start_node):
      node = start_node
      while node.rightChild:
          node = node.rightChild
      return node

  def find_smallest(self, start_node):
      node = start_node
      while node.leftChild:
          node = node.leftChild
      return node

  def as_list(self, type=1):
      if not self.rootNode:
          return []
      assert type in [0,1,2], 'wrong type value'
          
      if type == 0:
          return self.preorder(self.rootNode)
      elif type == 1:
          return self.inorder(self.rootNode)
      elif type == 2:
          return self.postorder(self.rootNode)

  def preorder(self, node, retlst=None):
      if retlst is None:
          retlst = []
      retlst += [node.key]
      if node.leftChild:
          retlst = self.preorder(node.leftChild, retlst)
      if node.rightChild:
          retlst = self.preorder(node.rightChild, retlst)
      return retlst

  def inorder(self, node, retlst=None):
      if retlst is None:
          retlst = []
      if node.leftChild:
          retlst = self.inorder(node.leftChild, retlst)
      retlst += [node.key]
      if node.rightChild:
          retlst = self.inorder(node.rightChild, retlst)
      return retlst

  def postorder(self, node, retlst=None):
      if retlst is None:
          retlst = []
      if node.leftChild:
          retlst = self.postorder(node.leftChild, retlst)
      if node.rightChild:
          retlst = self.postorder(node.rightChild, retlst)
      retlst += [node.key]
      return retlst

  def add_as_child(self, parent_node, child_node):
      node_to_rebalance = None
      parent_node.size+=1        
      if child_node.key < parent_node.key:

          if not parent_node.leftChild:
              parent_node.leftChild = child_node
              child_node.parent = parent_node
              if parent_node.height == 0: # in this case trees height could change
                  node = parent_node
                  while node:
                      node.height = node.max_children_height() + 1
                      if not node.balance() in [-1, 0, 1]:
                          node_to_rebalance = node
                          break 
                      node = node.parent
          else:
              self.add_as_child(parent_node.leftChild, child_node)
      else:
          if not parent_node.rightChild:
              parent_node.rightChild = child_node
              child_node.parent = parent_node
              if parent_node.height == 0: # in this case trees height could change
                  node = parent_node
                  while node:
                      node.height = node.max_children_height() + 1
                      if not node.balance() in [-1, 0, 1]:
                          node_to_rebalance = node
                          break 
                      node = node.parent
          else:
              self.add_as_child(parent_node.rightChild, child_node)

      if node_to_rebalance:
          self.rebalance(node_to_rebalance)

  def insert(self, key):
      new_node = Node(key)
      if not self.rootNode:
          self.rootNode = new_node
          assert self.elements_count==0,'Wrong elements_count'
          self.elements_count += 1
      else:
          if not self.find(key):
              self.elements_count += 1
              self.add_as_child(self.rootNode, new_node)
      return self

  def remove_branch(self, node):
      parent = node.parent
      if (parent):
          if parent.leftChild == node:
              parent.leftChild = node.rightChild or node.leftChild
          else:
              parent.rightChild = node.rightChild or node.leftChild
          if node.leftChild:
              node.leftChild.parent = parent
          else:
              node.rightChild.parent = parent
          self.recompute_heights(parent)
      del node
      
      # rebalance
      node = parent
      while (node):
          self.resize(node)
          if not node.balance() in [-1, 0, 1]:
              self.rebalance(node)
              

          node = node.parent

  def remove_leaf(self, node):
      parent = node.parent
      if (parent):
          if parent.leftChild == node:
              parent.leftChild = None
          else:
              parent.rightChild = None
          self.recompute_heights(parent)
      else:
          self.rootNode = None            
      del node
      
      # rebalance        
      node = parent
      while (node):
          self.resize(node)            
          if not node.balance() in [-1, 0, 1]:
              self.rebalance(node)
          node = node.parent

  def remove(self, key):
      node = self.find(key)

      if not node is None:
          self.elements_count -= 1
          if node.is_leaf():
              self.remove_leaf(node)
          elif (bool(node.leftChild)) ^ (bool(node.rightChild)):
              self.remove_branch(node)
          else:
              self.swap_with_successor_and_remove(node)

  def swap_with_successor_and_remove(self, node):
      successor = self.find_smallest(node.rightChild)
      self.swap_nodes(node, successor)
      if node.height == 0:
          self.remove_leaf(node)
      else:
          self.remove_branch(node)

  def swap_nodes(self, node1, node2):
      parent1 = node1.parent
      leftChild1 = node1.leftChild
      rightChild1 = node1.rightChild
      parent2 = node2.parent
      leftChild2 = node2.leftChild
      rightChild2 = node2.rightChild

      # swap heights
      tmp = node1.height
      node1.height = node2.height
      node2.height = tmp
      
      #swap sizes
      
      tmp = node1.size
      node1.size=node2.size
      node2.size=tmp

      if parent1:
          if parent1.leftChild == node1:
              parent1.leftChild = node2
          else:
              parent1.rightChild = node2
          node2.parent = parent1
      else:
          self.rootNode = node2
          node2.parent = None

      node2.leftChild = leftChild1
      leftChild1.parent = node2
      
      node1.leftChild = leftChild2
      node1.rightChild = rightChild2
      if rightChild2:
          rightChild2.parent = node1
          
          
      if not (parent2 == node1):
          node2.rightChild = rightChild1
          rightChild1.parent = node2

          parent2.leftChild = node1
          node1.parent = parent2
      else:
          node2.rightChild = node1
          node1.parent = node2

  def resize(self, node):
      node.size = 1
      if node.rightChild:
          node.size+=node.rightChild.size
      if node.leftChild:
          node.size+=node.leftChild.size
      
  def rebalance(self, node_to_rebalance):
      self.rebalance_count += 1
      A = node_to_rebalance
      F = A.parent  
      if node_to_rebalance.balance() == -2:
          if node_to_rebalance.rightChild.balance() <= 0:
              """Rebalance, ase RRC """
              B = A.rightChild
              C = B.rightChild
              A.rightChild = B.leftChild
              if A.rightChild:
                  A.rightChild.parent = A
              B.leftChild = A
              A.parent = B
              if F is None:
                  self.rootNode = B
                  self.rootNode.parent = None
              else:
                  if F.rightChild == A:
                      F.rightChild = B
                  else:
                      F.leftChild = B
                  B.parent = F
              self.recompute_heights(A)                                                                                        
              self.resize(A)
              self.resize(B)
              self.resize(C)
          else:
              """Rebalance, case RLC """
              B = A.rightChild
              C = B.leftChild
              B.leftChild = C.rightChild 
              if B.leftChild:
                  B.leftChild.parent = B
              A.rightChild = C.leftChild
              if A.rightChild:
                  A.rightChild.parent = A
              C.rightChild = B
              B.parent = C
              C.leftChild = A
              A.parent = C
              if F is None:
                  self.rootNode = C
                  self.rootNode.parent = None
              else:
                  if F.rightChild == A:
                      F.rightChild = C
                  else:
                      F.leftChild = C
                  C.parent = F
              self.recompute_heights(A)
              self.recompute_heights(B)
              self.resize(A)
              self.resize(B)
              self.resize(C)                
              
      else:
          if node_to_rebalance.leftChild.balance() >= 0:
              B = A.leftChild
              C = B.leftChild
              """Rebalance, case LLC """
              A.leftChild = B.rightChild
              if (A.leftChild):
                  A.leftChild.parent = A
              B.rightChild = A
              A.parent = B
              if F is None:
                  self.rootNode = B
                  self.rootNode.parent = None
              else:
                  if F.rightChild == A:
                      F.rightChild = B
                  else:
                      F.leftChild = B
                  B.parent = F
              self.recompute_heights(A)
              self.resize(A)
              self.resize(C)
              self.resize(B)                
              
          else:
              B = A.leftChild
              C = B.rightChild
              """Rebalance, case LRC """
              A.leftChild = C.rightChild
              if A.leftChild:
                  A.leftChild.parent = A
              B.rightChild = C.leftChild
              if B.rightChild:
                  B.rightChild.parent = B
              C.leftChild = B
              B.parent = C
              C.rightChild = A
              A.parent = C
              if F is None:
                  self.rootNode = C
                  self.rootNode.parent = None
              else:
                  if (F.rightChild == A):
                      F.rightChild = C
                  else:
                      F.leftChild = C
                  C.parent = F
              self.recompute_heights(A)
              self.recompute_heights(B)
              self.resize(A)
              self.resize(B)
              self.resize(C)                
              
  def findkth(self, k, root=None):
      if root is None:
          root=self.rootNode
      assert k<=root.size, 'Error, k more then the size of BST'
      leftsize = 0 if root.leftChild is None else root.leftChild.size
      if leftsize>=k:
          return self.findkth(k,root.leftChild)

      elif leftsize==k-1:
          return root.key
      else:
          return self.findkth(k - leftsize - 1, root.rightChild)    

  def __str__(self, start_node=None):
      if start_node == None:
          start_node = self.rootNode
      space_symbol = r" "
      spaces_count = 4 * 2**(self.rootNode.height)
      out_string = r""
      initial_spaces_string = space_symbol * spaces_count + "\n"
      if not start_node:
          return "Tree is empty"
      height = 2**(self.rootNode.height)
      level = [start_node]

      while (len([i for i in level if (not i is None)]) > 0):
          level_string = initial_spaces_string
          for i in range(len(level)):
              j = int((2 * i + 1) * spaces_count / (2 * len(level)))
              level_string = level_string[:j] + (str(
                  level[i]) if level[i] else space_symbol) + level_string[j +
                                                                          1:]
          out_string += level_string
          
          # create next level
          level_next = []
          for i in level:
              level_next += ([i.leftChild, i.rightChild]
                              if i else [None, None])
          # add connection to the next nodes    
          for w in range(height-1):
              level_string = initial_spaces_string
              for i in range(len(level)):
                  if not level[i] is None:
                      shift = spaces_count//(2*len(level))
                      j = (2 * i + 1) * shift
                      level_string = level_string[:j - w - 1] + (
                          '/' if level[i].leftChild else
                          space_symbol) + level_string[j - w:]
                      level_string = level_string[:j + w + 1] + (
                          '\\' if level[i].rightChild else
                          space_symbol) + level_string[j + w:]
              out_string += level_string
          height = height // 2
          level = level_next

      return out_string        

# Returns index of x in arr if present, else -1
# Code imported from: https://www.geeksforgeeks.org/python-program-for-binary-search/
def binary_search(arr, low, high, x):
  # Check base case
  if high >= low:

    mid = (high + low) // 2

    # If element is present at the middle itself
    if arr[mid] == x:
      return mid

    # If element is smaller than mid, then it can only
    # be present in left subarray
    elif arr[mid] > x:
      return binary_search(arr, low, mid - 1, x)

    # Else the element can only be present in right subarray
    else:
      return binary_search(arr, mid + 1, high, x)

  else:
    # Element is not present in the array
    return -1

if __name__ == '__main__':
  array_length = 100000
  random_array = create_random_array(array_length)

  array_random = []
  array_ordered = []
  tree_bst = None
  tree_avl = None

  # keep the results
  keep_array_random_insertion = []
  keep_array_ordered_insertion = []
  keep_tree_bst_insertion = []
  keep_tree_avl_insertion = []

  keep_array_random_search_50 = []
  keep_array_ordered_search_50 = []
  keep_tree_bst_search_50 = []
  keep_tree_avl_search_50 = []

  keep_array_random_search_50000 = []
  keep_array_ordered_search_50000 = []
  keep_tree_bst_search_50000 = []
  keep_tree_avl_search_50000 = []

  # we will run each one 5 times, and get the average
  for x in range(0, 10): 
    print("________________")
    print("\n--Iteration " + str(x+1) + "--")
    # insertion testing 

    # random array filling
    start_time = time.time()
    for i in random_array:
      array_random.append(i)
    time_interval = time.time() - start_time
    print("Random array insertion: " + str(time_interval))
    keep_array_random_insertion.append(time_interval)

    # ordered array filling
    start_time = time.time()
    array_ordered = copy.deepcopy(random_array)
    array_ordered.sort()
    time_interval = time.time() - start_time
    print("Ordered array insertion: " + str(time_interval))
    keep_array_ordered_insertion.append(time_interval)

    # bst filling
    start_time = time.time()
    for idx, x in enumerate(random_array):
      if (idx == 0):
        tree_bst = BSTNode(x)
      else:
        tree_bst.add(x)
    time_interval = time.time() - start_time
    print("BST insertion: " + str(time_interval))
    keep_tree_bst_insertion.append(time_interval)
        
    # avl filling
    start_time = time.time()
    tree_avl = AVLTree(random_array)
    time_interval = time.time() - start_time
    print("AVL insertion: " + str(time_interval))
    keep_tree_avl_insertion.append(time_interval)


    print("\n")
    # get 50 valued element testing 

    # random array
    start_time = time.time()
    element = None
    for item in array_random:
      if item == 50:
        element = item
    time_interval = time.time() - start_time
    print("Random array searching 50 valued element: " + str(time_interval))
    keep_array_random_search_50.append(time_interval)

    # ordered array
    start_time = time.time()
    element = binary_search(array_ordered, 0, len(array_ordered)-1, 50)
    time_interval = time.time() - start_time
    print("Ordered array searching 50 valued element: " + str(time_interval))
    keep_array_ordered_search_50.append(time_interval)

    # bst
    start_time = time.time()
    element = tree_bst.get(50)
    time_interval = time.time() - start_time
    print("BST searching 50 valued element: " + str(time_interval))
    keep_tree_bst_search_50.append(time_interval)
        
    # avl
    start_time = time.time()
    element = tree_avl.find(50)
    time_interval = time.time() - start_time
    print("AVL searching 50 valued element: " + str(time_interval))
    keep_tree_avl_search_50.append(time_interval)


    print("\n")
    # get 50000 valued element testing 

    # random array
    start_time = time.time()
    element = None
    for item in array_random:
      if item == 50000:
        element = item
    time_interval = time.time() - start_time
    print("Random array searching 50000 valued element: " + str(time_interval))
    keep_array_random_search_50000.append(time_interval)

    # ordered array
    start_time = time.time()
    element = binary_search(array_ordered, 0, len(array_ordered)-1, 50000)
    time_interval = time.time() - start_time
    print("Ordered array searching 50000 valued element: " + str(time_interval))
    keep_array_ordered_search_50000.append(time_interval)

    # bst
    start_time = time.time()
    element = tree_bst.get(50000)
    time_interval = time.time() - start_time
    print("BST searching 50000 valued element: " + str(time_interval))
    keep_tree_bst_search_50000.append(time_interval)
        
    # avl
    start_time = time.time()
    element = tree_avl.find(50000)
    time_interval = time.time() - start_time
    print("AVL searching 50000 valued element: " + str(time_interval))
    keep_tree_avl_search_50000.append(time_interval)

  print("\n________________\n")
  print("\n--Averages--")

  print("\n")
  print("Random array insertion: " + str(sum(keep_array_random_insertion) / len(keep_array_random_insertion)))
  print("Ordered array insertion: " + str(sum(keep_array_ordered_insertion) / len(keep_array_ordered_insertion)))
  print("BST insertion: " + str(sum(keep_tree_bst_insertion) / len(keep_tree_bst_insertion)))
  print("AVL insertion: " + str(sum(keep_tree_avl_insertion) / len(keep_tree_avl_insertion)))

  print("\n")
  print("Random array searching 50 valued element: " + str(sum(keep_array_random_search_50) / len(keep_array_random_search_50)))
  print("Ordered array searching 50 valued element: " + str(sum(keep_array_ordered_search_50) / len(keep_array_ordered_search_50)))
  print("BST searching 50 valued element: " + str(sum(keep_tree_bst_search_50) / len(keep_tree_bst_search_50)))
  print("AVL searching 50 valued element: " + str(sum(keep_tree_avl_search_50) / len(keep_tree_avl_search_50)))

  print("\n")
  print("Random array searching 50000 valued element: " + str(sum(keep_array_random_search_50000) / len(keep_array_random_search_50000)))
  print("Ordered array searching 50000 valued element: " + str(sum(keep_array_ordered_search_50000) / len(keep_array_ordered_search_50000)))
  print("BST searching 50000 valued element: " + str(sum(keep_tree_bst_search_50000) / len(keep_tree_bst_search_50000)))
  print("AVL searching 50000 valued element: " + str(sum(keep_tree_avl_search_50000) / len(keep_tree_avl_search_50000)))
