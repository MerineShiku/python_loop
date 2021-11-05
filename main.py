students = ["mike", "beyonce", "kanye"]
for x in students:
  print ("hi " + x)


y = range (10)
z = list(range(10)) #convert to list
print(z)



#odd numbers 
print(list(range(1, 10, 2)))

#getting every 3 number 
print(list(range(80, 100, 3)))



#for x in range (10):
# print (x+1)  #the numbers will run from 1 instead of 0 to 10 instead of 9


#nested loops

#for i in range (5):
   #for j in range(0):
   #  print (j, end ="")
#print()


#while loop
m = 1
while m<10:
  print (m)
  m +=1


''' 
 Q2. Write a program to print first 10 integers and their squares using while loop
'''

i = 1
while i<=10:
   print(i, i*i)
   i+=1

'''
Q3. Write for loop statement to print the following series:
10, 20, 30 … … 300
'''

i = 10
while i <= 300:
   print(i, end = " , ")
   i+=10
print()  


'''
Q4. Write a while loop statement to print the following series
105, 98, 91 ………7.

'''

i = 105
while i >= 7:
  print(i, end = " ,")
  i -=7
print()

'''  
Q5. Write a program to print first 10 natural number in reverse order using while loop.

'''
n = 10
while n >=1:
  print(n, end =",")
  n -= 1
print()

'''  
Write a program to print sum of first 10 Natural numbers.

'''

num = 10
sum = 0
while num >=1:
  sum +=num
  num -=1
  print(sum)


#Q7. Write a program to print sum of first 10 Even numbers.


num = 2
sum = 0
while num <= 20:
   sum = sum + num
   num= num + 2
print(sum)


'''
Q10. Write a program to check whether a number is prime or not using while loop.

'''

num1 = int(input("Enter any number : "))
k=0
if num1 == 0 or num1 == 1:
    print("Not a prime number ")
else:
   i = 2
   while(i<num1):
     if num1 % i == 0:
       k = k+1
     i = i+1
if k == 0 :
        print( num1,"is prime number")
else:
        print(num1, "is not prime number")

# Program to show the use of break statement inside loops 
#break and stops

i = 1
while i <=10:
  i +=1
  if i == 5:
    break
  print (i, end = "")
print()


# Another example for break statement inside loops 

for  i in range (1, 10):
     if i==3: 
      break
     print(i)



# Program to show the use of continue statement inside loops
#skips and continue

i = 0
while i < 10:
  i +=1
  if i == 4:
    continue
  print (i)





