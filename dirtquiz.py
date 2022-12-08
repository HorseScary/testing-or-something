import random
dirts = {
    "monosol": "grassland",
    "Aridisol": "desert",
    "alfisol": "forest",
    "oxisol": "rainforest",
    "histisol": "wetland",
    "gelisol": "tundra"
}

print(list(dirts.items())[random.randint(0, 5)])

dirts_correct = 0
dirts_wrong = 0
while True:
    dirt = list(dirts.items())[random.randint(0, 5)]
    print(dirt[0])
    answer = input()
    if answer == dirt[1]:
        print("correct")
        dirts_correct += 1
    elif answer == "exit":
        break
    else:
        print(f"incorrect. {dirt[1]}")
        dirts_wrong += 1
print(f"correct: {dirts_correct}\nincorrect: {dirts_wrong}")
