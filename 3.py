# Write your solution for algorithm 3 below
# Write an algorithm that takes in an unsorted numerical list as an argument 
# and creates a new sorted list in descending order (use the sorted() function).
# The sorted() function sorts in ascending order, 
# but it can sort in descending order by adding a reverse parameter with a boolean value of True.

a = [6, 3, 4, 1, 8]
a_sorted = sorted(a, reverse=True)

print(a_sorted)