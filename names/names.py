import time
from lru_cache import LRUCache
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

binary_search_tree = BinarySearchTree(names_1[0])
duplicates = []  # Return the list of duplicates in this data structure

for name_1 in names_1: # O(n log n)
  binary_search_tree.insert(name_1)

for name_2 in names_2: # O(log n)
  if binary_search_tree.contains(name_2):
    duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"Binary Search Tree runtime: {end_time - start_time} seconds")

# Binary Search Tree: O(n log n)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

lru_cache = LRUCache(10000)
lru_duplicates = []

for name_1 in names_1: # O(n)
  lru_cache.set(name_1, name_1)

for name_2 in names_2:
  if lru_cache.get(name_2): # O(n)
    lru_duplicates.append(name_2)

end_time = time.time()
print (f"{len(lru_duplicates)} duplicates:\n\n{', '.join(lru_duplicates)}\n\n")
print (f"LRU Cache runtime: {end_time - start_time} seconds")

# LRU Cache: O(n)