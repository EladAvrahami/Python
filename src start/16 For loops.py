#iterate code with for loops

for item in 'Python':
    print(item)

print("""
example for iterate an array :""")
for i in ['mosh','elad','sara']:
    print(i)

print("""
example for iterate an array of nums  :""")
for a in [1,2,3,4]:
    print(a)


print("""
example for iterate an array of nums without type all of them in manually with range:""")
for b in range(10):
    print(b)

print("""
using range:""")
for c in range(5,10):
    print(c)

print("""
  using range and third num will tell me how many places to iterate:""")
for d in range(5, 10,2):
    print(d)


print("""
  # more example :""")

prices=[10,20,30]
total=0

for price in prices:
    total+=price
print(f"total is : {total}")