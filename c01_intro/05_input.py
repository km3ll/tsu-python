# Nesting function (input) calls
age_num2 = int(input("Enter your age: "))
print(f"You have lived for {age_num2 * 12} months.")

# Input function
my_name = "pod"
prompt = "Enter your name: "
your_name = input(prompt)

# Anything the user types is a string
print(f"Hello {your_name}. My name is {my_name}.")

age_num1 = int(input("Enter your age: "))
months = age_num1 * 12
print(f"You have lived for {months} months.")