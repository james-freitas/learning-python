import sys

# Read a input, remove spaces(strip) and converts to a number
n = int(raw_input().strip())

# Read space separated input, creates an array converting all to int 
arr = map(int, raw_input().strip().split(' '))

print "Result is: " + str(sum(arr))