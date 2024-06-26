def printIncreasing(n, a):
    if a > n:
        return 0
    
    print(a)
    a = a+1
    return printIncreasing(n ,a)
a = 1
n = int(input())
printIncreasing(n, a)


# 1. You are given a positive number n. 
# 2. You are required to print the counting from 1 to n.
# 3. You are required to not use any loops. Complete the body of print Increasing function to achieve it. Don't change the signature of the function.

# Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.
# Input Format
# A number n
# Output Format
# 1
# 2
# 3
# ..
# n

# Constraints
# 1 <= n <= 1000
# Sample Input
# 5
# Sample Output
# 1
# 2
# 3
# 4
# 5