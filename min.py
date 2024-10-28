'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10'''
n = int(input())
lst = []
for i in range(n):
  s = int(input())
  lst.append(s)
t = tuple(lst)
a = t[0]
for i in t:
  if i < a:
    a = i
print(a)
