import random
dirts = {
    "monosol": "grassland",
    "aridisol": "desert",
    "alfisol": "forest",
    "oxisol": "rainforest",
    "histisol": "wetland",
    "gelisol": "tundra"
}

dirts = list(dirts.items())

dirts_correct = 0
dirts_wrong = 0
print("Welcome to the HorseScary dirt quiz!\nmode 1: gives dirt location, asks for dirt type\nmode 0: gives dirt type, asks for location")
mode = bool(int(input("mode: ")))

while True:
    if len(dirts) == 0:
        break

    dirt = dirts.pop(random.randint(0, len(dirts) - 1))
    print(dirt[int(mode)])

    answer = input()
    if answer == dirt[int(not mode)]:
        print("correct")
        dirts_correct += 1
    elif answer == "exit":
        break
    else:
        print(f"incorrect. {dirt[(not mode)]}")
        dirts_wrong += 1
print(f"correct: {dirts_correct}\nincorrect: {dirts_wrong}")
