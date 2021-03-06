# Write a function called total that takes a filename as its only argument and returns the sum of the numbers in that file.
# You may assume that the file is formatted in such a way that each number is an integer and occupies its own line.
# You may not assume you know how many numbers are in the file.
def total(filename):
     total_all = 0
     with open(filename) as f:
         for line in f:
             total_all += int(line)
     return total_all




# The file numbers.txt in this directory follows these guidelines and should add up to 4753817

# After you've written your function, you can run test.py to ensure your function works on other files as well.
