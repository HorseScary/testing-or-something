import random


def get_number(number):
    french_numbers = {
        1: "un",
        2: "deux",
        3: "trois",
        4: "quatre",
        5: "cinq",
        6: "six",
        7: "sept",
        8: "huit",
        9: "neuf",
        10: "dix",
        11: "onze",
        12: "douze",
        13: "treize",
        14: "quatorze",
        15: "quinze",
        16: "seize",
        20: "vigt",
        30: "trente",
        40: "quarante",
        50: "cinquante",
        60: "soixante"
    }

    if number <= 16 or number % 10 == 0:
        return (french_numbers[number])
    elif number % 10 == 1:
        return (f"{french_numbers[(int(number/10))*10]} et un")
    else:
        return (f"{french_numbers[int(number/10)*10]} {french_numbers[number%10]}")


def quiz(numbers):
    correct = 0
    for i in range(numbers):
        number = random.randint(1, 60)
        if input(f"{number} ") == get_number(number):
            correct += 1
        else:
            print(f"The correct answer is {get_number(number)}")
    return (correct)


if __name__ == "__main__":
    numbers = int(input("How many numbers should I quiz you on? "))

    correct = quiz(numbers)
    print(f"You got {correct} numbers correct and {numbers - correct} wrong.")
    if numbers == correct:
        print("Cracked at da nums!!")
    elif numbers / 2 < numbers-correct:
        print("You fucking suck!")
