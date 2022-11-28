n = int(input())
arr = []
for i in range(n) :
    val = int(input())
    arr.append(val)
# n = 3
# arr = [10,20,30]

for i in range(len(arr)):

    dummy = []
    for j in range(i, n):
        dummy.append(arr[j])
        for k in dummy:
            print(k, end="	")
        print()
        

"""
1. You are given an array of size 'n' and n elements of the same array.
2. You are required to find and print all the subarrays of the given array. 
3. Each subarray should be space seperated and on a seperate lines. Refer to sample input and output.
Input Format
A number n
n1
n2
.. n number of elements
Output Format
[Tab separated elements of subarray]
..
All subarrays

Constraints
1 <= n <= 10
0 <= n1, n2
 .. n elements <= 10 ^9
Sample Input
3
10
20
30
Sample Output
10	
10	20	
10	20	30	
20	
20	30	
30	
"""