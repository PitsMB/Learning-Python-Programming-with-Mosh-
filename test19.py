#List methods
numbers = [1, 2, 3, 4, 5]

#add something to the list
numbers.append(6)

#insert something to the list
numbers.insert(0, 0)

#remove something on the list
numbers.remove(0)

#this empty the list
numbers.clear()

#this removes the last item on the list
numbers.pop()

#check for the existence of an item on the list
numbers.index(0)
is_number_exist = 1 in numbers

#This counts the occurance of something on the list
numbers.count(5) 

#this sort the list to ascending order
numbers.sort()
#this sort the list to descending order
numbers.reverse()

#this copy the value of a the list
number1 = numbers.copy()