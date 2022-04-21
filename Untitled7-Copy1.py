#!/usr/bin/env python
# coding: utf-8

# In[1]:


num =int(input("Enter a number to generate its pattern = "))
for i in range(1,num + 1):
    for j in range(1,i + 1):
        print(j,end = " ")
    print()
    


# In[3]:


num = 2
for i in range(2,50):
    j = 2
    while(j<=(i/2)):
        if (i % j == 0):
            break
        j += 1
    if (j > i/j):
        print(i, "is a prime number")
print ("Bye Bye !!")


# In[6]:


num = int(input("Enter a number: "))
fact = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbbers")
elif num == 0:
    print("The factorial of 0 is 1")
else: 
    for i in range (1, num + 1):
        fact = fact * i
    print("factorial of ",num, " is ",fact)


# In[7]:


num = int(input("Enter the number to be checked"))
flag = 0
if num > 1 : 
    for i in range (2<int(num/2)):
        flag = 1
        break
    if flag == 1:
        print(num , "is not a prime number")
    else:
          print(num, "is a prime number ")
else:
    print ("Entered number is < = 1,execute again! ")


# In[ ]:




