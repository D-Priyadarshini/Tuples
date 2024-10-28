'''
Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. 
So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and 
print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. 
Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
'''
t = tuple(map(int,input().split()))
eve_c = 0
odd_c = 0
for i in t:
  if i%2 == 0:
    eve_c += 1
  else:
    odd_c+=1
if eve_c> odd_c:
  print("Even")
else:
  print("Odd")
