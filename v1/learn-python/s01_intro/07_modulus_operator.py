# type cast
# int_input   = int(input())
# float_input = float(input())
# str_input   = str(input())
int_input = int(input("Input > "))

# modulus operator
# Have you seen a table online where each row has a different color?
# This is a perfect example of where the remainder comes into play
remainder = int_input % 2

# string template
template = "Number {} is {}."
if remainder == 0:
    print(template.format(int_input, 'even'))
else:
    print(template.format(int_input, 'odd'))