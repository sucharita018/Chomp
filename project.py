import random
import numpy as np
import emoji


cookie = emoji.emojize(":cookie:")  #🍪
poison = emoji.emojize(":skull:")   #💀
chocolate = np.full((2, 12), cookie, dtype=object)
chocolate[1, 0] = poison

def main():
    print("Welcome to the 2x12 chomp game! First we do a toss to decide who goes first")
    display_chocolate(chocolate)
    player_toss = input("h/t?: ")
    goes_first = toss(player_toss)
    last_chocolate = np.full((2, 12), " ", dtype=object)
    last_chocolate[1,0] = poison
    if goes_first:
        n = 0
        while not np.array_equal(chocolate, last_chocolate):
            your_turn = input("your turn (write: row,column): ").split(",")
            chocolate_change(int(your_turn[0]),int(your_turn[1]))
            display_chocolate(chocolate)
            n += 1
            if np.array_equal(chocolate, last_chocolate):
                break
            next_chocolate()
            display_chocolate(chocolate)
            n += 1
        if n % 2 == 1:
            print("congratulations! you win")
        else:
            print("you lose :|")

    if not goes_first:
        n = 0
        while not np.array_equal(chocolate, last_chocolate):
            next_chocolate()
            display_chocolate(chocolate)
            n += 1
            if np.array_equal(chocolate, last_chocolate):
                break
            your_turn = input("your turn: ").split(",")
            chocolate_change(int(your_turn[0]),int(your_turn[1]))
            display_chocolate(chocolate)
            n += 1
        if n % 2 == 0:
            print("congratulations! you win")
        else:
            print("you lose :|")

def toss(ip):
    options = ["h", "t"]
    if ip == random.choice(options):
        print("you go first!")
        return True
    else:
        print("you go second")
        return False


def chocolate_change(r,c):
    global chocolate
    chocolate[:r+1, c:] = " "
    return chocolate

def next_chocolate():
    global chocolate
    pairs = [(i, j) for i in range(2) for j in range(12) if chocolate[i, j] == cookie]

    if pairs:
        pair = random.choice(pairs)
        print(f"Computer's turn: {pair}")
        chocolate_change(pair[0], pair[1])
    return chocolate

def display_chocolate(chocolate):
    for row in chocolate:
        #print(row)
        print(" ".join(row))

    print()


if __name__ == "__main__":
    main()