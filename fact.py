'''
Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
t = tuple(map(int,input().split()))
n = int(input())
a = t.count(n)
pr = 1
for i in range(1,a+1):
  pr *= i
print(pr)
