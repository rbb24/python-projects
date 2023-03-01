def split_names(string_to_split):
    list_of_names = string_to_split.split(",")
    return list_of_names


def count_names(list_with_names):
    amount_names = len(list_with_names)
    return amount_names


list_of_names = input("Enter names separated by commas (no spaces): ")

print(count_names(split_names(list_of_names)))
