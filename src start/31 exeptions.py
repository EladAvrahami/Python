try:
    age = int(input('age: '))
    income =20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("age cant be zero")
except ValueError:
    print('invalid value')

