filenames = ["a.txt", "b.txt", "c.txt"]

for file in filenames:
    datei = open(f"../files/{file}", "r")
    inhalt = datei.read()
    datei.close()
    print(inhalt)

