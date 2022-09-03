'''Problem
You are conducting a contest at your college. This contest consists of two problems and  participants. You know the problem that a candidate will solve during the contest.

You provide a balloon to a participant after he or she solves a problem. There are only green and purple-colored balloons available in a market. Each problem must have a balloon associated with it as a prize for solving that specific problem. You can distribute balloons to each participant by performing the following operation:

Use green-colored balloons for the first problem and purple-colored balloons for the second problem
Use purple-colored balloons for the first problem and green-colored balloons for the second problem
You are given the cost of each balloon and problems that each participant solve. Your task is to print the minimum price that you have to pay while purchasing balloons.

Input format

First line:  that denotes the number of test cases ()
For each test case: 
First line: Cost of green and purple-colored balloons 
Second line:  that denotes the number of participants ()
Next  lines: Contain the status of users. For example, if the value of the  integer in the  row is , then it depicts that the  participant has not solved the  problem. Similarly, if the value of the  integer in the  row is , then it depicts that the  participant has solved the  problem.
Output format
For each test case, print the minimum cost that you have to pay to purchase balloons.

Sample Input
2
9 6
10
1 1
1 1
0 1
0 0
0 1
0 0
0 1
0 1
1 1
0 0
1 9
10
0 1
0 0
0 0
0 1
1 0
0 1
0 1
0 0
0 1
0 0
Sample Output
69
14
'''
for _ in range(int(input())):
    g,p=map(int,input().split())
    sum_cost=0
    p1,p2=[],[]
    for _ in range(int(input())):
        x,y=map(int,input().split())
        p1.append(x)
        p2.append(y)
    sump1=sum(p1)
    sump2=sum(p2)
    # print(sump1,sump2)
    if sump1<sump2:
        if g>p:
            for i in p1:
                sum_cost+=i*g
            for i in p2:
                sum_cost+=i*p
        else:
            for i in p1:
                sum_cost+=i*p
            for i in p2:
                sum_cost+=i*g
    else:
        if g>p:
            for i in p1:
                sum_cost+=i*p
            for i in p2:
                sum_cost+=i*g
        else:
            for i in p1:
                sum_cost+=i*g
            for i in p2:
                sum_cost+=i*p
    print(sum_cost) 
