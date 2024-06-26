def inverse(arr, n):
    answer = [0]*len(arr)
    for i in range(len(arr)):
        idx = i
        answer[arr[i]] = i
    return answer

def main():
    n = int(input())
    arr = []
    for i in range(n) :
        val = int(input())
        arr.append(val)
    arr = inverse(arr, n)
    for i in range(n) :
        print(arr[i])

main()

"""
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are required to calculate the inverse of array a.

For definition and constraints check this link
https://www.pepcoding.com/resources/online-java-foundation/getting-started/inverse-of-a-number/ojquestion
The only difference is the range of values is from 0 to n - 1, instead of 1 to n.
Input Format
Input is managed for you
Output Format
Output is managed for you

Constraints
0 <= n < 10^7
For more constraints check this
https://www.pepcoding.com/resources/online-java-foundation/getting-started/inverse-of-a-number/ojquestion
The only difference is the range of values is from 0 to n - 1, instead
of 1 to n
Sample Input
5
4
0
2
3
1
Sample Output
1
4
2
3
0

"""