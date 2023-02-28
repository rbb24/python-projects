def convert_to_cubic_meters(liter_local):
    cubic_meters = liter_local / 1000
    return cubic_meters


liters = float(input("Please input liter value you want to convert: "))
print(convert_to_cubic_meters(liters))
