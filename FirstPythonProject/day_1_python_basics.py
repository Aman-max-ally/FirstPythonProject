message = "Aman's world"
#to check the length of our string we use len() function.
print(len(message))

#if we want to print a specific character we use [place of the character from starting]
print(message[10])
print(message[11])
print(message[0])
print(message[1])

#if we want to print a range of character we use [first number place : second number place] This is called slicing
print(message[0:6])#we can left the space before colon to print the message from starting
print(message[7:12])#we can leave the space after colon to print till the end

#to print our string all lower or upper case we use .upper() or .lower() function
print(message.lower())
print(message.upper())

#To count a certain number of character in our string we use .count('')
print(message.count('world'))

#to find the index of certain word,letter in string we use .find('')
print(message.find('m'))
print(message.find('world'))
print(message.find('universe')) #if we try to find the index of certain character in our string that doesnot exist it return output of -1...

#if we want to replace certain word or letter with other word we .replace("","")
message = message.replace("world","universe")
print(message)

# How to add multiple string......

greeting = 'hello'
name = 'Philip'

message = f'{greeting},{name},welcome!'
message = '{},{},sup!'.format(greeting,name)
print(message)