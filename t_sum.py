'''Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sampl.e Output:
60
'''
t = tuple(map(int,input().split()))
sum = 0
for i in t:
  sum += i
print(sum)
