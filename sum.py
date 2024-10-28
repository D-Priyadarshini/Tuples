'''
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
'''
n = int(input())
lst = []
for i in range(n):
  s = int(input())
  lst.append(s)
t = tuple(lst)
sum = 0
for i in tuple:
  sum += i
print(sum)


"""
n = int(input())
sum = 0
for i in range(n):
  sum +=  int(input())
print(sum)""" 






