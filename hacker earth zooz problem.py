'''Problem
You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if .

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.
Note: The maximum length of this word must be .
Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

Sample Input
zzzoooooo
Sample Output
Yes'''


n=input()
x=''
y=''
t=n[0]
for i in n:
    if t==i:
        x=x+i
        t=i
    else:
        y=y+i
if len(2*x) == len(y):
    print('Yes')
else:
    print('No')
