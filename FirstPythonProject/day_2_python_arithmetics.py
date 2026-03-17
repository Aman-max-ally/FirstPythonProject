#If we want to check the type of our string like integer,float.....
num = 3.55
num1 = 3
print(type(num))
print(type(num1))

#now some arithmetic operation we can perform...
#addition(+)
print(3 + 4)   #output = 7

#subtraction(-)
print(7-6)   #output = 1

#multiplication(*)
print(3*2)   #output = 6

#Division(/)
print(5/2)   #output = 2.5

#Floor Division(//) is basically a type of division but it's drop the decimal value and give output a integer
print(5//2)    #output = 2

#Exponent(**) ; basically means multiplying a number repeatedly
print(3**4)

#Modulus(%) ; we use modulus to check whether a number is even or odd
 #if ( %2) gives the output 1 that means the number is odd.....
#if ( %2) gives the output 0 that means the number is even....
print(25%2) #even
print(44%2) #odd

#Incrementing the values

n = 2
n += 10
print(n)

#To make a negative value positive we use abs() function means absolute
print(abs(-5))

#To round off float values we use round() function
print(round(3.66))
print(round(4.774,1)) # if we want to round off upto a certain decimal place; add comma after number then type the number upto which you want to round off
print(round(4.774,2))


# For comparing two number we can use those....
#1.Equal(==)

m1 = 2
m2 = 4

print(m1 == m2) #false because they are not equal

#2. Not Equal(!=)

print(m1 != m2) #True because they are not equal

#3. Greater Than(>) or Less than(<)

print(m1 > m2) #False because m1 is not greater than m2
print(m1 < m2) #True because m1 is less than m2

#4.Greater or equal and less or equal

print(m1 >= m2) #false because m1 is neither greater nor equal to m2
print(m1 <= m2) # true because m1 is less than m2


#To convert string into integer....

u1 = '50'
u2 = '10'

u1 = int(u1)
u2 = int(u2)

print(u1 + u2)

