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

'''  
Q5. Write a program to print first 10 natural number in reverse order using while loop.

'''