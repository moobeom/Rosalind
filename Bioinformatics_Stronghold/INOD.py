### Counting phylogenetic ancestors ###

n = 1078
# n = 3 -> 1 internal node with 3 leaves
# n = 4 -> 2 internal nodes with 2 leaves respectively
# n >= 5 -> 2 internal nodes with 2 leaves at both ends and k internal nodes with 1 leaves and 1 internal node
#           n = 2*2 + k -> k = n - 4 -> number of internal nodes = n - 2

print(n - 2)