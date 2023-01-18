def format_senither(num):
    num = num.rstrip()
    if num.rfind("K") == -1:
        return (num)
    if num.rfind(".") == -1:
        return (num.replace("K", "000"))
    if num.split(".")[1].__len__() == 3:
        return (num.replace(".", "").replace("K", "0"))
    elif num.split(".")[1].__len__() == 2:
        return (num.replace(".", "").replace("K", "00"))


open_levels = open("guild_req_stuff/levels", "r")
open_senither = open("guild_req_stuff/senither", "r")
results = open("guild_req_stuff/results.csv", "a")
player_stats = {}

for i in open_levels:
    player_stats[i.split(" ")[1].replace(":", "")] = [float(i.split(" ")[2])]

for i in open_senither:
    player_stats[i.split(" ")[1].replace(
        ":", "")].append(format_senither(i.split(" ")[2]))

for i in player_stats:
    results.write(f"{i},{player_stats[i][0]},{player_stats[i][1]}\n")
