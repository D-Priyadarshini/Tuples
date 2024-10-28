'''
Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''
t = tuple(map(int,input().split()))
x = int(input())
count = 0
for i in t:
  if i == x:
    count += 1
print(count)
