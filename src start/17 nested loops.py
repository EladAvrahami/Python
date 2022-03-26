for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers = [5, 2, 5, 2, 2]

print("example 2 ;")
for Xcount in numbers:
  print('x' * Xcount)

print("example 3 using inner loops ;")
for X_count in numbers:
    output = ''
    for count in range(X_count):
        output += 'x'
        print(output)
