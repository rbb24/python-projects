from converters8 import convert
from parsers8 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet an {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
