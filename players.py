filename = "playerList"


def store_name():
    playerList = []
    with open(filename) as file:
        for line in file:
            playerList.append({"message": line.rstrip("\n\r")})
    return playerList


def add_name(name):
    with open(filename, "a") as file:
        file.write(name + "\n")
