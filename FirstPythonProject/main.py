#I am going to start learning python from scratch
#first,i'm going to perform some arithmetic
#Addition

x = 10
y = 20

grand = x + y
print("the sum of x and y is",grand)

#product
print("the product of x and y is", x*y)


#List

#lists are mutable means after each line of function python return a edited list...
l1 = ["jamie","anish",1,76,55]
l1[0] #output = "jamie"
l1[0 : 2] #output = ["jamie","anish",1]
l1.reverse() # output = [55,76,1,"anish","jamie"]
l1.sort() #Doesn't work because of different data type.. but if all entries are of same data type it will arrange it in increasing order..
l1.append(78) #output = [55,76,1,"anish","jamie",78] #append() add element at the end of the list.
l1.insert(4,0) #output = [55,76,1,0,"anish","jamie"] #.insert(index,adding element)
l1.pop(2) # pop(2) means it will remove the element which is present at index 2.....      
#output=[55,76,0,"anish","jamie"]
l1.remove(1) # .remove(0) means it will remove that particular element which is written within the parenthesis...  #output = [55,76,"anish","jamie"]



