name=['Bon','Bob','Jon ','Yaron','mosh','jacob']
print(name )
#anothe way to print all the list
print(name[:])
print(name [0])
print(name [2])
print(name [-1])
print(name [-2])
#this will show me oll the obj from index 2  to the end of the list
print(name [2:])
#print range until not includ
print(name [2:4])

print()
# refactor one of the list obj :
print("# refactor one of the list obj :")
name[0]='BonBon'
print(name)

# exercise:
numbers=[3,6,2,8,4,10]
max=numbers[0]
for num in numbers:
    if num>max:
        max=num
print(max)




