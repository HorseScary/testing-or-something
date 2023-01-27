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
        10: "diz",
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

    if number <= 10 or number % 10 == 0:
        frenchNumber = french_numbers[number]
    elif number % 10 == 1:
        return (f"{french_numbers[(int(number/10))*10]} et un")
    else:
        return (f"{french_numbers[int(number/10)*10]} {french_numbers[number%10]}")
    return (frenchNumber)
