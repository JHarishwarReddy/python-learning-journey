#creating list and accessing
fruits =["apple","banana","mango","orange","grape"]

print(fruits[0])
print(fruits[1])
print(fruits[-2])
print(fruits[-3])

#length of list
print(f"Total fruits={len(fruits)}")

#slicing
print(fruits[0:3])
print(fruits[2:])
print(fruits[1:2])

#methods
#adding
fruits.append("strawberry")
fruits.insert(1,"pineapple")
print(f"After adding : {fruits}")

#remove
fruits.remove("banana")
fruits.pop()
fruits.pop(0)
print(f"After removing: {fruits}")

#sort
fruits.sort()
fruits.sort(reverse=True)
print(f"After sorting : {fruits}")

#check,counting, find index
if "mango" in fruits:
    print(f"mango is in fruits & count : {fruits.count("mango")}\n in index :{fruits.index("mango")}")
else:
    print("Mango is not in fruits")

#loops 
for fruit in fruits:
    print(fruit)
#index number
for i,fruit in enumerate(fruits):
    print(f"{i+1}. {fruit}")
#filter
print("\n fruit with more than 5 letters")
for fruit in fruits:
    if len(fruit) > 5:
        print(f" - {fruit}")
# build new list
upper_fruits=[]
captial_fruits=[]
for fruit in fruits:
    upper_fruits.append(fruit.upper())
    captial_fruits.append(fruit.capitalize())
print(f"\n Upper_fruits : {upper_fruits} \n Captial_fruits : {captial_fruits}")