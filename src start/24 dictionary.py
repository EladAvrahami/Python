# KEY VALUE PARAMS

# each key should be unique
customer = {
    "name": "elad avrahami",
    "age": 30,
    "is_verified": True
}
print( customer["name"])
#erors:
#print( customer["BD "])
#print( customer["Name "])

#way 2
#it will print none and not an eror ********************************************************
print(customer.get("birthday"))

print(customer.get("birthday","jan 1 1980"))

#update values: ****************************************************************************
customer["name"]="Jack smith "
print(customer["name"])

#Add key to dictionary: ********************************************************************
customer["BD"]="Jan 1 1980"
print(customer["BD"])
print(customer)


print("*********************** exercies 2 ***************************")
# ***********************exercies 2***************************
phone= input("enter Phone: ")
digits_mapping={
    "1":"one",
    "2": "Tow",
    "3": "Tree",
    "4": "Four"

}
output=""

for ch in phone:

    output+=digits_mapping.get(ch,"!") +" "
print(output)