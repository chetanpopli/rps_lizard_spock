from random import randint
print("          Welcome to")
print("Rock-Paper-Scissors-Lizard-Spock")
max_rounds = input("Enter number of rounds you want to play for: ")
max_rounds = int(max_rounds)
win = 0
lose = 0
moves = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

print("Rules:")
print("Rock         [1]     -- beats -->     Scissors, Lizard")
print("Paper        [2]     -- beats -->     Rock    , Spock")
print("Scissors     [3]     -- beats -->     Paper   , Lizard")
print("Lizard       [4]     -- beats -->     Paper   , Spock")
print("Spock        [5]     -- beats -->     Rock    , Scissors")

for i in range(0, max_rounds):
    print("\nChoose your move number!")
    player = input("")
    player = int(player)
    if player > 5 or player < 1:
        print("Invalid Option, try again")
        break
    print("Player has chosen: " + moves[player - 1])
    computer = randint(1,5)
    print("Computer has chosen: " + moves[computer - 1])
    if player == 1:
        if (computer == 3 or computer == 4):
            print("Player wins this round!")
            win += 1
        elif(computer == 2 or computer == 5):
            print("Computer wins this round")
            lose += 1
        else:
            print("It's a tie!")
    
    elif player == 2:
        if (computer == 1 or computer == 5):
            print("Player wins this round!")
            win += 1
        elif(computer == 3 or computer == 4):
            print("Computer wins this round")
            lose += 1
        else:
            print("It's a tie!")
    
    elif player == 3:
        if (computer == 2 or computer == 4):
            print("Player wins this round!")
            win += 1
        elif(computer == 1 or computer == 5):
            print("Computer wins this round")
            lose += 1
        else:
            print("It's a tie!")

    elif player == 4:
        if (computer == 2 or computer == 5):
            print("Player wins this round!")
            win += 1
        elif(computer == 1 or computer == 3):
            print("Computer wins this round")
            lose += 1
        else:
            print("It's a tie!")

    elif player == 5:
        if (computer == 1 or computer == 3):
            print("Player wins this round!")
            win += 1
        elif(computer == 2 or computer == 4):
            print("Computer wins this round")
            lose += 1
        else:
            print("It's a tie!")
    

print("The Final Score is:")
print("Player:")
print(win)
print("Computer:")
print(lose)

if win > lose:
    print("Player wins!")
elif win < lose:
    print("Computer wins!")
elif win == lose and win == 0:
    print("")
elif win == lose and win > 0:
    print("It's a tie!")
        