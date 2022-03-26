#operations i can perform in a list :
numbers=[1,2,5,7,4,5,5]
#add to the end use append
numbers.append(20)
print(numbers)
#add num at index 0
numbers.insert(0,10)
print(numbers)
# remove specific element will remove just the first
numbers.remove(5)
print(numbers)

# this will delete all list values
#numbers.clear()

#remove item from the end of at the list
numbers.pop()
print(numbers)

# is num exists? find its first index it is appeared
print(numbers.index(10))

#chack if any num appeared in the list and get back boolean answer
print(50 in numbers)


# chack how many of the num is appeared in the list
print(numbers.count(5))

numbers.sort()
print("numbers are sorted:"+str(numbers) )

numbers.reverse()
print("numbers are sorted backorders:"+str(numbers) )

#copy the original list
numbers2=numbers.copy()
print(numbers2)

