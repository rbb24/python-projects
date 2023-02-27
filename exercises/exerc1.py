reset = input("Do you want to start from scratch? ").strip()
reset = reset.lower()
if reset == "yes":
    with open('../files/luck.txt', 'w') as file:
        file.write("")

while True:
    coin_flip = input("Throw the coin and enter head or tail here: ? ").strip()
    coin_flip = coin_flip.lower()
    if coin_flip == "head" or coin_flip == "tail":
        with open('../files/luck.txt', 'a') as file:
            file.writelines(coin_flip + '\n')

        with open('../files/luck.txt', 'r') as file:
            results = file.readlines()

        count_heads = 0
        total_throws = len(results)
        clean_results = [result.strip('\n') for result in results]
        number_of_heads = clean_results.count("head")
        chance = number_of_heads / total_throws * 100

        print(f"Heads: {chance:.2f}%")

    else:
        print("Your entered neither head or tail. Try again")








