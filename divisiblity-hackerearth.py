'''Problem
You are provided an array  of size  that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by .

Note: View the sample explanation section for more clarification.

Input format

First line: A single integer  denoting the size of array 
Second line:  space-separated integers.
Output format

If the number is divisible by , then print . Otherwise, print .

Constraints

Sample Input
5
85 25 65 21 84
Sample Output
No'''

N = int(input())
data = [int(x) for x in input().split()]


# Write your code here
num=0
for i in data:
    num=(num*10)+ i%10

# ans = 
if num%10==0:
    ans='Yes'
else:
    ans='No'
print(ans)
