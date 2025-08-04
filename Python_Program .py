#Addition
# num1 = float(input("Enter the first number for addition: "))
# num2 = float(input("Enter the second number for addition: "))
# sum_result = num1 + num2
# print(f"Sum : {num1} + {num2}  = {sum_result}")

my_favorite_num = 26
print(f"My favorite number is: {my_favorite_num}")
print(type(my_favorite_num))

temp = 23.45678
print(f"The current temperature is {temp:.2f} degrees Fahrenheit.")

the_earth_is_flat = True
the_earth_is_donut = True
if the_earth_is_flat:
    print("Wow that's really amazing!")
elif the_earth_is_donut:
    print("wow earth is donut shaped")
else:
    print("Wow that's not really amazing!")
weather = "raining"
print("boots" if weather == "raining" else "sneakers")