import random

def draw():

    # options
    r = "rock"
    p = "paper" or "Paper" or "PAPER"
    s = "scissor" or "Scissor" or "SCISSOR" or "scissors"
    comp_answer = [r, p, s]
    score = 0
    play_num = 0

    # outcome
    win = "WINNER!"
    lose = "LOSER!"

    # start with:
    try_again = input("Ready to play? Type \"Y\" or \"N\": ")
    try_again = try_again.lower()
    if (try_again != "y") and (try_again != "n"):
        try_again = input("Please enter \"Y\" or \"N\": ")

    # game play
    while try_again == "y":
        answer = input("Rock, Paper, Scissor, Shoot! ")
        answer = answer.lower()
        comp_reply = random.choice(comp_answer)

        print("Computer plays: " + comp_reply)
        print()

        # same answers
        if (answer == r and comp_reply == r) or (answer == p and comp_reply == p) or (answer == s and comp_reply == s):
            print("Same draw.")
            play_num -= 1

        # rock/paper combo
        elif (answer == p and comp_reply == r) or (answer == r and comp_reply == p):
            print("Paper beats rock.")
            if answer == p:
                print(win)
                score += 1
            else:
                print(lose)

        # rock/scissor combo
        elif (answer == r and comp_reply == s) or (answer == s and comp_reply == r):
            print("Rock beats scissor.")
            if answer == r:
                print(win)
                score += 1
            else:
                print(lose)

        # paper/scissor combo
        elif (answer == p and comp_reply == s) or (answer == s and comp_reply == p):
            print("Scissor beats paper.")
            if answer == s:
                print(win)
                score += 1
            else:
                print(lose)

        play_num += 1
        print("Your score is " + str(score) + "/" + str(play_num))
        try_again = input("\nPlay again? Type \"Y\" or \"N\": ")
        try_again = try_again.lower()
        if (try_again != "y") and (try_again != "n"):
            try_again = input("Please enter \"Y\" or \"N\": ")

    print("Thanks for playing!")

draw()
