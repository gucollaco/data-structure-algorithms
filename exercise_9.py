# -*- coding: utf-8 -*-
# Gustavo Martins Collaço

# importing the required packages
from __future__ import print_function
import random
import time

# shuffle array
def shuffle_array(array):
  random.shuffle(array)

# create a randomized array with the given length
def create_random_array(array_length):
  array = list(range(0, array_length))
  shuffle_array(array)
  return array

# ____________________________________________________________________________________________________
# Hashing with chaining
# Code imported from: https://github.com/shreyasvedpathak/Data-Structure-Python/blob/master/Hashing/hashingChaining.py
# and Linked list imported from https://github.com/shreyasvedpathak/Data-Structure-Python/blob/master/LinkedList/linkedlist.py

class _Node:
    '''
    Creates a Node with two fields:
    1. element (accesed using ._element)
    2. link (accesed using ._link)
    '''
    __slots__ = '_element', '_link'

    def __init__(self, element, link):
        '''
        Initialses _element and _link with element and link respectively.
        '''
        self._element = element
        self._link = link


class LinkedList:
    '''
    Consists of member funtions to perform different
    operations on the linked list.
    '''

    def __init__(self):
        '''
        Initialses head, tail and size with None, None and 0 respectively.
        '''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''
        Returns length of linked list
        '''
        return self._size

    def isempty(self):
        '''
        Returns True if linked list is empty, otherwise False.
        '''
        return self._size == 0

    def addLast(self, e):
        '''
        Adds the passed element at the end of the linked list.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
        else:
            self._tail._link = newest

        self._tail = newest
        self._size += 1

    def addFirst(self, e):
        '''
        Adds the passed element at the beginning of the linked list.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._link = self._head
            self._head = newest
        self._size += 1

    def addAnywhere(self, e, index):
        '''
        Adds the passed element at the passed index position of the linked list.
        '''
        newest = _Node(e, None)

        i = index - 1
        p = self._head

        if self.isempty():
            self.addFirst(e)
        else:
            for i in range(i):
                p = p._link
            newest._link = p._link
            p._link = newest
            print(f"Added Item at index {index}!\n\n")
        self._size += 1

    def addSorted(self, e):
        '''
        Adds passed element at a position that making linked list sorted.
        '''
        newest = _Node(e, None)

        if self.isempty():
            self.addFirst(e)
        else:
            curr = prev = self._head
            while curr and curr._element < e:
                prev = curr
                curr = curr._link
            # if no element is found to be smaller than e, curr will point to head.
            # that means, it should be the first element.
            if curr == self._head:
                self.addFirst(e)
            else:
                newest._link = prev._link
                prev._link = newest
                self._size += 1


    def removeFirst(self):
        '''
        Removes element from the beginning of the linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty. Cannot perform deletion operation.")
            return

        e = self._head._element
        self._head = self._head._link
        self._size = self._size - 1

        if self.isempty():
            self._tail = None

        return e

    def removeLast(self):
        '''
        Removes element from the end of the linked list.
        Returns the removed element.
        '''
        if self.isempty():
            print("List is Empty. Cannot perform deletion operation.")
            return

        p = self._head
        if p._link == None:
            e = p._element
            self._head = None
        else:
            while p._link._link != None:
                p = p._link
            e = p._link._element
            p._link = None
            self._tail = p

        self._size = self._size - 1
        return e

    def removeAnywhere(self, index):
        '''
        Removes element from the passed index position of the linked list.
        Returns the removed element.
        '''
        p = self._head
        i = index - 1

        if index == 0:
            return self.removeFirst()
        elif index == self._size - 1:
            return self.removeLast()
        else:
            for x in range(i):
                p = p._link
            e = p._link._element
            p._link = p._link._link

        self._size -= 1
        return e

    def display(self):
        '''
        Utility function to display the linked list.
        '''
        if self.isempty() == 0:
            p = self._head
            while p:
                print(p._element, end='-->')
                p = p._link
            print("NULL")
        else:
            print("Empty")

    def search(self, key):
        '''
        Searches for the passed element in the linked list.
        Returns the index position if found, else -1.
        '''
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._link
            index += 1
        return -1

class HashChain:
    '''
    Initialises hashtable size and hashtable with respective head nodes using LinkedList() class.
    '''

    def __init__(self, hashsize=10) -> None:
        self._hashsize = hashsize
        self._hashtable = [0] * self._hashsize
        for i in range(self._hashsize):
            self._hashtable[i] = LinkedList()

    def hashcode(self, key):
        '''
        Returns Hash value using simple Mod operator.
        '''
        return key % self._hashsize

    def insert(self, element):
        '''
        Inserts element in hashtable.
        '''
        index = self.hashcode(element)
        self._hashtable[index].addSorted(element)

    def search(self, key):
        '''
        Returns index position if the element is found in the table, else False.
        '''
        position = self.hashcode(key)
        return self._hashtable[position].search(key)

    def display(self):
        '''
        Utility funtion to display Hashtable.
        '''
        for i in range(self._hashsize):
            print(f'[{i}] -- ', end='')
            self._hashtable[i].display()
        print()
# ____________________________________________________________________________________________________

       
# ____________________________________________________________________________________________________
# Hashing with linear probing
# Code imported from: https://github.com/shreyasvedpathak/Data-Structure-Python/blob/master/Hashing/hashingStrategies.py
class HashLP:
    def randomPrime(self, upper):
        '''
        Generates a random prime number for hash_2 function.
        '''
        import random
        
        prime = []
        for num in range(upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime.append(num)
        
        return random.choice(prime)

    def __init__(self, hashsize=10) -> None:
        '''
        Initialises hashtable size and prime number.
        '''
        self._hashsize = hashsize
        self._hashtable = [-1] * self._hashsize
        self._size = 0
        self._q = self.randomPrime(self._hashsize)
        # print(f'[ NOTE: Prime Number chosen: {self._q} ]')

    def isfull(self):
        '''
        Returns True if Hash table is full, otherwise False.
        '''
        return self._size == self._hashsize

    def isempty(self):
        '''
        Returns True if Hash table is empty, otherwise False.
        '''
        return self._size == 0

    def hash_1(self, key):
        '''
        Returns Hash value using simple Mod operator.
        '''
        return key % self._hashsize

    def hash_2(self, key):
        '''
        Returns Hash value using prime number.
        '''
        return self._q - (key % self._q)

    def findnext(self, index_h1, index_h2, method='linear', factor=1):
        '''
        This function is used to calculate the next index position based on
        following parameters if the collision occurs.
        {parameters} :  'index_h1' -- Hash value by hash_1 function
                        'index_h2' -- Hash value by hash_2 function
                        'linear'  -- Linear Probing
                        'quad'   -- Quadratic Probing
                        'double' -- Double Hashing
        {returns} : Returns index when collison occurs.
        '''

        if method == 'linear':
            return (index_h1 + factor) % self._hashsize
        elif method == 'quad':
            return (index_h1 + factor ** 2) % self._hashsize
        elif method == 'double':
            return (index_h1 + (factor * index_h2)) % self._hashsize

    def insert(self, element, method='linear'):
        '''
        Inserts element in hashtable using the passed Method.
        '''
        if self.isfull():
            print('Hash Table is Full !')
            return False

        position = index_h1 = self.hash_1(element)
        index_h2 = self.hash_2(element)

        n = 0
        while self._hashtable[position] != -1:
            n += 1
            position = self.findnext(
                index_h1, index_h2, method=method, factor=n)

        self._hashtable[position] = element
        self._size += 1
        return True

    def search(self, key, method='linear'):
        '''
        Returns index position if the element is found in the table, else False.
        '''
        if self.isempty():
            print('Hashtable is empty')
        else:
            position = index_h1 = self.hash_1(key)
            index_h2 = self.hash_2(key)
            n = 0
            while True:
                if self._hashtable[position] == key:
                    return position
                else:
                    n += 1
                    position = self.findnext(
                        index_h1, index_h2, method=method, factor=n)
                    if position == index_h1 - 1:
                        break
            return

    def display(self):
        '''
        Utility funtion to display Hashtable.
        '''
        if self.isempty():
            print('Hashtable is empty')
        else:
            for i, element in enumerate(self._hashtable):
                print(f'[{i}] -- {element}')
# ____________________________________________________________________________________________________
    
if __name__ == '__main__':
    # some variables
    array_length = 10000

    # keep the results
    keep_hashing_chaining_insert = []
    keep_hashing_chaining_search = []
    keep_hashing_linear_probing_insert = []
    keep_hashing_linear_probing_search = []

    # we will run each one 10 times, and get the average
    for x in range(0, 10):
        # random array to use for this iteration
        random_array = create_random_array(array_length)

        print("________________")
        print("\n--Iteration " + str(x+1) + "--")

        # Hashing with Chaining - Insertion
        hashing_chaining = HashChain(10000)
        start_time = time.time()
        for item in random_array:
            hashing_chaining.insert(item)
        time_interval = time.time() - start_time
        print("Hashing with Chaining - Insertion: " + str(time_interval))
        keep_hashing_chaining_insert.append(time_interval)

        # Hashing with Chaining - Search
        start_time = time.time()
        search_position_hashing_chaining = hashing_chaining.search(999)
        time_interval = time.time() - start_time
        print("Hashing with Chaining - Search: " + str(time_interval))
        keep_hashing_chaining_search.append(time_interval)

        # Hashing with Linear probing (open addressing) - Insertion
        hashing_linear_probing = HashLP(10000)
        start_time = time.time()
        for item in random_array:
            hashing_linear_probing.insert(item)
        time_interval = time.time() - start_time
        print("Hashing with Linear probing (open addressing) - Insertion: " + str(time_interval))
        keep_hashing_linear_probing_insert.append(time_interval)
            
        # Hashing with Linear probing (open addressing) - Search
        start_time = time.time()
        search_position_linear_probing = hashing_linear_probing.search(999)
        time_interval = time.time() - start_time
        print("Hashing with Linear probing (open addressing) - Search: " + str(time_interval))
        keep_hashing_linear_probing_search.append(time_interval)


    print("\n________________\n")
    print("\n--Averages--")

    print("\n")
    print("Hashing with Chaining - Insertion: " + str(sum(keep_hashing_chaining_insert) / len(keep_hashing_chaining_insert)))
    print("Hashing with Chaining - Search: " + str(sum(keep_hashing_chaining_search) / len(keep_hashing_chaining_search)))

    print("\n")
    print("Hashing with Linear probing (open addressing) - Insertion: " + str(sum(keep_hashing_linear_probing_insert) / len(keep_hashing_linear_probing_insert)))
    print("Hashing with Linear probing (open addressing) - Search: " + str(sum(keep_hashing_linear_probing_search) / len(keep_hashing_linear_probing_search)))
