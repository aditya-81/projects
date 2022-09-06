game_on = True

print("WELCOME TO ARCADE GAMING\n")
while game_on:
    game = int(input("ENTER 1 FOR HANGMAN \n ENTER 2 FOR CONNECT4\n ENTER 3 FOR ARCADE PING PONG"))

    if game == 1:
        exec(open(r"D:\study\projects\arcade gaming center\hangman_main.py").read())
    elif game == 2:
        exec(open("connect4.py").read())
    elif game == 3:
        exec(open(r"D:\study\projects\arcade gaming center\ping_pong_main.py").read())
    else:
        print("WRONG INPUT")

    a = input("play again other games?? Y/N")
    if a == "Y" or a == 'y':
        game_on = True
    else:
        game_on = False
