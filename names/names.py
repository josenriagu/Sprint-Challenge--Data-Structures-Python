import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('C:\\lambda\\cs\\week3\\challenge3\\names\\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('C:\\lambda\\cs\\week3\\challenge3\\names\\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
'''
for name_1 in names_1:
   for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

# Reducing for loops to 1 (approx. 1.0865s)
'''
for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)
'''

# Using BST (approx. 0.1096s)

# # form the root node with the first list item
# bst = BinarySearchTree(names_1[0])

# # insert all elements of list 1
# for name in names_1:
#     bst.insert(name)

# for name in names_2:
#     # check for existence of list 2 items in the BST
#     if bst.contains(name):
#         # if found, append to duplicate
#         duplicates.append(name)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# using Set and intersection
'''
duplicates = set(names_2) - set(names_1)
'''
duplicates = set(names_2).intersection(names_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
