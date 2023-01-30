def read_levels(file):
    guild_levels = {}
    file = open(file, "r")
    for i in file:
        split = i.split(": ")
        guild_levels[split[0].split(" ")[1]] = float(split[1].rstrip())
    return (guild_levels)


if __name__ == "__main__":
    file = open("guild_req_stuff/gained.csv", "w")

    start_levels = read_levels("guild_req_stuff/levels.txt")
    end_levels = read_levels("guild_req_stuff/levels2.txt")
    for i in start_levels:
        try:
            file.write(f"{i}, {end_levels[i] - start_levels[i]}\n")
        except KeyError:
            pass
