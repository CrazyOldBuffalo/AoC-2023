from playercard import PlayerCard
from winningcards import WinningCards


def parsecards(line):
    parts = line.strip().split(":")
    card_id = parts[0].split()[1]
    numbers = parts[1].split("|")

    winningarray = [int(num) for num in numbers[0].strip().split()]
    playerarray = [int(num) for num in numbers[1].strip().split()]
    w1 = WinningCards(card_id, winningarray)
    p1 = PlayerCard(playerarray)

    return w1, p1


def main():
    with open("test.txt") as file:
        fulltotal = 0
        total = 0
        for line in file:
            win, player = parsecards(line)
            var = set(win.numbers).intersection(player.numbers)
            total -= 1
            total += len(var)
            fulltotal += 1
            if total < 1:
                break
    print(fulltotal)
main()