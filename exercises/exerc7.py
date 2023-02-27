try:
    total = float(input("Enter total value: "))
    part = float(input("Enter value: "))

    percentage = part / total * 100

    print(f"That is {percentage:.1f}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero!")
