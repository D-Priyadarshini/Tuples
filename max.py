'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
n = int(input())
lst = []
for i in range(n):
  s = int(input())
  lst.append(s)
t = tuple(lst)
a = t[0]
for i in t:
  if i > a:
    a = i
print(a)
