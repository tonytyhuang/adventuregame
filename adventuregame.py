# -------------------------------------------------------------------------------
# Name:	adventure_game.py
# Purpose:
# A creative adventure game where you explore a house
#
# Author:		Huang.T
#
# Created:	    20/06/2017
# ------------------------------------------------------------------------------
import os
# create an empty list for rooms
room_list = []
# open a file with descriptions of each room
description = open("room descriptions", "r")
# read each line in file and input it into each room then add each room into the list
room1 = description.readline()
room = [room1,3, 1, None, None]
room_list.append(room)
room2 = description.readline()
room = [room2, 4, None, None, 0]
room_list.append(room)
room3 = description.readline()
room = [room3, 6, 3, None, None]
room_list.append(room)
room4 = description.readline()
room = [room4, 7, 4, 0, 2]
room_list.append(room)
room5 = description.readline()
room = [room5, 8, 5, 1, 3]
room_list.append(room)
room6 = description.readline()
room = [room6, 9, None, None, 4]
room_list.append(room)
room7 = description.readline()
room = [room7, None, 7, 2, None]
room_list.append(room)
room8 = description.readline()
room = [room8, None, 8, 3, 6]
room_list.append(room)
room9 = description.readline()
room = [room9, None, 9, 4, 7]
room_list.append(room)
room10 = description.readline()
room = [room10, None, None, 5, 8]
room_list.append(room)

# variables used to visit each room only once
closet = True
kitchen = True
fr = True
lr = True
gym = True
sc = True
office = True
pool = True
ball = True
# amount of time given
time = 20
# amount of bullets at the beginning of the game
bullets = 0
# variable for which room you are in
current_room = 0
# variable to decide when the game completes
done = False
# introduction to the game
print("*******Archie's Apocalypse*******")
print ("Welcome to Archie's Apocalypse. You are a seventeen year old boy escaping from a group of walkers(zombies)."
       "\nYou are fleeing for your life when you come across a house. You choose to enter."
       "\nYou are out of bullets for your gun. Therefore the goal is to find bullets in the house while remaining "
       "under a 20 minute time limit.\nYou can quit the game by typing \"q\" or \"quit\" and the game "
       "will automatically save.\n")
# ask user if they have a game to continue


def game_save():
    game_saved = raw_input("Do you have a saved game?")
    if game_saved == "y":
        # open the saved file
        save_game = open("saved_game", "r+")
        # change all the variables to the ones in the saved files
        current_room = int(save_game.readline())
        bullets = int(save_game.readline())
        time = int(save_game.readline())
        closet = (save_game.readline())
        kitchen = (save_game.readline())
        fr = (save_game.readline())
        lr = (save_game.readline())
        gym = (save_game.readline())
        sc = (save_game.readline())
        office = (save_game.readline())
        pool = (save_game.readline())
        ball = (save_game.readline())
        save_game.close()
        # remove the saved file
        os.remove("saved_game")
    elif game_saved == "n":
        print("Enjoy the game!")
    else:
        print("Please enter a valid entry(y/n).")
        game_save()

game_save()

# function for basketball room
def bball():
    """
    Mini game quiz for basketball room
    :return: string - amount of bullets and time left after mini game
    """
    # description for mini game
    print("You find humans outside. The leader walks up to you and asks you computer science questions."
          "\nIf you cannot solve the question, they will steal away your bullets but if you can solve it,"
          "they will give you bullets. \n")
    # ask the first question
    question_1 = raw_input("Dean: \"What is the name for code written in high level languages?\"")
    # check the answer
    if question_1 == "source code" or question_1 == "Source code":
        print("Wow! You must be a real nerd eh!")
        global bullets
        bullets += 1
        print("Bullet count: " + (str(bullets)))
        global time
        time -= 1
        print("Time remaining: " + (str(time)))
    else:
        print("Nope! Incorrect! Hahaha give me your bullets!")
        bullets -= 1
        print("Bullet count: " + (str(bullets)))
        time -= 1
        print("Time remaining: " + (str(time)))
    # ask the second question
    question_2 = raw_input("Dean: \"The steps involved in executing one instruction is called what?\"")
    # check the answer
    if question_2 == "Machine Cycle" or question_2 == "machine cycle" or question_2 == "Machine cycle" or \
                    question_2 == "Instruction Cycle" or question_2 == "instruction cycle" or \
                    question_2 == "Instruction cycle":
        print("WHAT! Where did you learn all this...")
        bullets += 1
        print("Bullet count: " + (str(bullets)))
        time -= 1
        print("Time remaining: " + (str(time)))
    else:
        print("Wow... that was such an easy question but you got it wrong.")
        bullets -= 1
        print("Bullet count: " + (str(bullets)))
        time -= 1
        print("Time remaining: " + (str(time)))
    # ask the third question
    question_3 = raw_input("\"Ok last question, would you describe yourself as handsome?\"(y/n)")
    # check the answer
    if question_3 == "y":
        print("I like your confidence! Here's a bullet for your troubles!")
        bullets -= 1
        print("Bullet count: " + (str(bullets)))
        time -= 1
        print("Time remaining: " + (str(time)))
    if question_3 == "n":
        print("Nice and humble attitude! I like it. Here's a bullet for your troubles!")
        bullets -= 1
        print("Bullet count: " + (str(bullets)))
        time -= 1
        print("Time remaining: " + (str(time)))


# mini game for the pool room
def pool_game():
    """
    what happens in pool room
    :return: string - time remaining
    """
    print("The water in the pool starts flooding out. It wastes you time to avoid it.")
    global time
    time -= 3
    print("Time remaining: " + (str(time)))


# guessing password game function
def get_word():
    """
    takes a random word from the file
    :return: string - the randomn word
    """
    # open the file
    sourcefile = open("words.txt", 'r+')
    # read all the lines in the file
    source_list = sourcefile.readlines()
    # close the file
    sourcefile.close()
    # find number of words
    for i in range(len(source_list)):
        number = (i + 1)
    # get a random word
    from random import randint
    word = (source_list[(randint(0, number - 1))])
    return word


def update_board(current_board, letter, positions):
    """
    update the word board
    :param current_board: list - current state of the board
    :param letter: string - letter that was guessed
    :param positions: list - list of positions where letters exist
    :return: list - new updated board
    """
    # find number of positions where letter exists
    for i in range(len(positions)):
        # replace place on current board with that letter
        current_board[positions[i]] = letter
    return current_board


def check_guess(word, guess_letter):
    """
    check if letter exists in word
    :param word: string - selected word
    :param guess_letter: string - guessed letter
    :return: list - positions of letter in the word
    """
    pos = []
    for i in range(len(word)):
        if word[i] == guess_letter:
            pos.append(i)
    return pos


def display_board(word_board):
    """
    display the word board
    :param word_board: list - the current word board
    :return: string - the word board
    """
    print(" ".join(word_board))


def ask_letter(guessed_letters):
    """
    get a guessed letter
    :param guessed_letters: list - list of guessed letters
    :return: string - the letter guessed
    """
    # ask user for guess
    guess = raw_input("Enter a single letter: ")
    return guess


def display_lock_board(phase_int):
    """
    What prints after incorrect guess
    :param phase_int: integer - number of wrong guesses
    :return: string - what prints after a number of wrong guesses
    """
    # print a different string for each separate number of wrong tries
    if phase_int == 1:
            print ("5 tries left!")
    elif phase_int == 2:
            print ("4 tries left!")
    elif phase_int == 3:
            print ("3 tries left!")
    elif phase_int == 4:
            print ("2 tries left!")
    elif phase_int == 5:
            print ("1 try left!")
    elif phase_int == 6:
            print ("No more tries.")


def playGame(word):
    """
    Run the body of the game
    :param word: string - random word generated to guess
    :return: string - whether if you won or lost
    """
    # initialize game
    hangman_board_int = 0
    max_guesses = 6

    # initialize guessed_letters to empty list
    guessed_letters = []

    # initialize word_board
    word_board = ["_"] * (len(word) - 1)

    game_over = False
    won = False

    while not game_over:
        letter = ask_letter(guessed_letters) # get letter from the user
        positions = check_guess(word, letter)

        if len(positions) > 0:
            word_board = update_board(word_board, letter, positions)
        else:
            hangman_board_int += 1

        display_board(word_board)
        display_lock_board(hangman_board_int)

        if "".join(word_board).lower().strip() == word.lower().strip():
            won = True
            game_over = True

        if hangman_board_int == max_guesses:
            game_over = True

        guessed_letters.append(letter)
        print("Guessed Letters: " + "".join(guessed_letters))

    if won:
        return "Won"
    else:
        return "Lost"


def output_result(result):
    """
    Output the result of the game
    :param result: string - if you won or lost
    :return: string - result of your game
    """
    # find whether you won or lost
    if result == "Won":
        print("Congratulations! You have guessed the password. You find a map of the escape route from the house. "
              "You gain an extra 5 minutes!")
        global time
        time += 5
        print("Time remaining: " + (str(time)))
    elif result == "Lost":
        print("Sorry, you got locked out of the computer.")
        time -= 2
        print("Time remaining: " + (str(time)))
    else:
        print ("Error in the result")


def main():
    word = get_word()
    result = playGame(word)
    output_result(result)


# game for the staircase
def staircase_game():
    # describe siutation
    print("When you go up the stairs you find the door is locked. You need to use a bullet to break it open.")
    global bullets
    # find if you have bullets
    if bullets == 0:
        print("You have no bullets so you can't open the door.")
    else:
        choose = raw_input("Do you choose to open the door with a bullet?(y/n) ")
        if choose == "y":
            bullets -= 1
            print("Bullet count: " + (str(bullets)))
            print("You find that there are two separate room upstairs.")
            choice = raw_input("Which room do you choose to enter?(1/2)")
            if choice == "1":
                print("You entered the storage room and the room is filled with boxes.")
                another_choice = raw_input("Do you choose to look through the room?(y/n) ")
                if another_choice == "y":
                    print ("It took you four minutes but you found a box of 3 bullets!")
                    bullets += 1
                    print("Bullet count: " + (str(bullets)))
                    global time
                    time -= 4
                    print("Time remaining: " + (str(time)))
                    print("Unfortunately you have no time to visit the other room and go back downstairs.")
                elif another_choice == "n":
                    print("You exit the room.")
                else:
                    print("Please enter a valid entry, \"y\" or \"n\"")
            elif choice == "2":
                print("You entered a bathroom. A dead body lays in the bath tub.\nYou get scared"
                      " and lose 2 minutes recovering from the sight.")
                time -= 2
                print("Time remaining: " + (str(time)))
                print("Unfortunately you have no time to visit the other room and go back downstairs.")
            else:
                print("Please use a valid entry, \"1\", \"2\"")
        elif choose == "n":
            print("You may continue exploring the house.")
        else:
            print("Please enter a valid entry, \"y\" or \"n\"")


# situation for gym
def gym_game():
    print("You here a growling noise. From the window a zombie climbs through! "
          "You are forced to use a bullet to kill it.")
    global bullets
    # remove one bullet
    bullets -= 1
    print("Bullet count: " + (str(bullets)))
    global time
    # remove one minute
    time -= 1
    print("Time remaining: " + (str(time)))

correct = True
# create a blank list and create a 2d list
board_game = []
for i in range(3):
    board_game.append([" "]*3)


def print_board(board):
    """
    print the board
    :param board: list - board
    :return: list - 2d list
    """
    for i in range(len(board)):
        print [str(x) for x in board[i]]


def get_valid_index(prompt):
    """
    get the user input of the index
    :param prompt: string
    :return: string - the user input index
    """
    while True:
        try:
            index = int(input(prompt))
            # set parameters for what index can be
            if 0 <= index <= 2:
                return index
            print "Must be 0, 1 or 2!"
        except ValueError:
            print "Must be an integer!"


def game_is_over(board):
        """
        Find the result of the game
        :param board: list - the board
        :return: string - if won or lost
        """
        # check if board matches the pattern perfectly
        if board[0][0] == board[0][1] == board[0][2] == board[1][1] == board[2][1] == "x":
            print_board(board_game)
            print ("Congratulations! You solved the pattern and found 5 bullets!")
            global bullets
            bullets += 5
            print("Bullet count: " + (str(bullets)))
            global time
            time -= 1
            print("Time remaining: " + (str(time)))
            return True
        # if pattern is wrong, restart the game
        elif board_game[1][0] == "x" or board_game[1][2] == "x" or board_game[2][0] == "x" or board_game[2][2] == "x":
            print("Sorry, that is the wrong position. Please try again.")
            time -= 0.5
            print("Time remaining: " + (str(time)))
            for i in range(3):
                board_game[0][i] = " "
                board_game[1][i] = " "
                board_game[2][i] = " "


def lr_game():
    """
    Place the user input's values onto the board
    :return: list - 2d list with the value implemented
    """
    # character to fill the board
    turn = "x"
    # ask for the user input and fill the board
    for i in range(9):
        print_board(board_game)
        row = get_valid_index("Row: ")
        col = get_valid_index("Col: ")

        if board_game[row][col] == " ":
            board_game[row][col] = turn
        else:
            print "That space is taken"
        if game_is_over(board_game) is True:
            break


# function for the game in closet room
def closet_game():
    print("You see three different boxes. One is empty, one contains two bullets and one contains an explosive"
          "\nthat will slow you down. Unfortunately, you only have time to open one box.")
    # image of the boxes
    print(" _______   _______   _______")
    print(" |     |   |     |   |     |")
    print(" |  1  |   |  2  |   |  3  |")
    print(" |     |   |     |   |     |")
    print(" |_____|   |_____|   |_____|")
    # ask user if they want to play the game
    choose = raw_input("Do you choose to open a box?(y/n) ")
    if choose == "y":
        # ask user which box and output result of the chosen box
        boxes = input("Which box do you choose to open?(1/2/3) ")
        if boxes == 1:
            print("Congratulations! You found one bullet!")
            global bullets
            bullets += 2
            print("Bullet count: " + (str(bullets)))
            global time
            time -= 1
            print("Time remaining: " + (str(time)))
        elif boxes == 2:
            print("You opened the explosive. It slowed you down by an extra 2 minutes.")
            time -= 3
            print("Time remaining: " + (str(time)))
        elif boxes == 3:
            print("The box is empty.")
            time -= 1
            print("Time remaining: " + (str(time)))
        else:
            print("Please use a valid entry, \"1\", \"2\", \"3\"")
            closet_game()
    elif choose == "n":
        print("You can continue through the house.")
    else:
        print("Please enter a valid entry, \"y\" or \"n\"")
        closet_game()


# situation for kitchen
def kitchen_game():
    print("You see a fire extinguisher but you're not sure if you want to put out the fire"
          " as it will waste valuable time ")
    # ask user if they want to play
    choose = raw_input("Do you choose to put out the fire?(y/n)")
    # result of choice
    if choose == "y":
        print("After you extinguish the fire, you find a bullet!")
        global bullets
        bullets += 1
        print("Bullet count: " + (str(bullets)))
        global time
        time -= 2
        print("Time remaining: " + (str(time)))
    elif choose == "n":
        print("You may continue exploring the house.")
    else:
        print("Please enter a valid entry, \"y\" or \"n\"")
        kitchen_game()


#game for family room
def fr_game():
    print("In the room two couches are piled on top of each other. Under it you see a box of ammo."
          "\nYou have the ability to lift it but using too much force will cause you to hurt yourself."
          "\nAlong with force, you have to lift it at a correct angle as well.")
    choose = raw_input("Do you choose to lift the couch?(y/n) ")
    if choose == "y":
        lift = False
        while lift is False:
            # ask for user input for force and angle
            force = raw_input("How much force will you like to use(in percentage)?(1-100) ")
            angle = raw_input("What angle will you like to lift the couch(in degrees)?(0-90)")
            # correct force and angle to lift the couch
            if "50" <= force <= "80" and "30" <= angle <= "70":
                print("Congratulations, you lifted the couch and got 4 bullets!")
                global bullets
                bullets += 4
                print("Bullet count: " + (str(bullets)))
                global time
                time -= 1
                print("Time remaining: " + (str(time)))
                lift = True
            # if too much forced used, it slows you down
            elif force > "80" and "0" <= angle <= "90":
                print("You used too much force and hurt yourself. This slowed you down.")
                time -= 3
                print("Time remaining: " + (str(time)))
            elif "1" <= force <= "49" and "30" <= angle <= "70":
                print ("You used too little force. please try again.")
                time -= 0.5
                print("Time remaining: " + (str(time)))
            elif "0" <= angle <= "29" or "71" <= angle <= "90" and "50" <= force <= "80":
                print ("You lifted at the wrong angle. Please try again.")
                time -= 0.5
                print("Time remaining: " + (str(time)))
            else:
                print("Unfortunately you couldn't lift the couch, please try again.")
                time -= 0.5
                print("Time remaining: " + (str(time)))
    elif choose == "n":
        print("You may continue exploring the house.")
    else:
        print("Please enter a valid entry, \"y\" or \"n\"")
        fr_game()


# loops when game is not finished
while done is False:
    # output description of each room
    print(room_list[current_room][0])
    # output number of bullets
    print("Number of bullets: " + (str(bullets)))
    # output time remaining
    print("Time remaining: " + (str(time)))
    # finds the room and runs a function in accordance to each
    if current_room == 1:
        # loop makes sure game only runs once
        while closet is True:
            closet_game()
            closet = False
            print("There is a door leading to a room to the north.")
    if current_room == 2:
        while kitchen is True:
            kitchen_game()
            kitchen = False
            print("There is a door to the east and a staircase is to the north.")
    if current_room == 3:
        while fr is True:
            fr_game()
            fr = False
            print("A door leads to a room to the east, west and north")
    if current_room == 4:
        while lr is True:
            print ("You try to open the safe but it is encrypted by a code. It is a 3 by 3 board and you "
                   "have to fill out 5 of the boxes with a pattern.")
            lr_game()
            lr = False
            print("A door is to the north, east and west.")
    if current_room == 5:
        while gym is True:
            gym_game()
            gym = False
            print("A door leads outside to the north. A door is to your west.")
    if current_room == 6:
        while sc is True:
            staircase_game()
            sc = False
            print("A door is to the south and east.")
    if current_room == 7:
        while office is True:
            print("You find a computer that's locked. You try to open it as it can give you valuable information.")
            main()
            office = False
            print("A staircase is to the west and a door is to the south and east.")
    if current_room == 8:
        while pool is True:
            pool_game()
            pool = False
            print("A door to the outside is to the east. A door is to the south and west.")
    if current_room == 9:
        while bball is True:
            bball()
            ball = False
            print("A door to the inside is to the west and south.")

    # ask for user input for direction
    direction = raw_input("Where do you want to go?(n/e/s/w) ")
    # situation if user chooses north
    if direction == 'n' or direction == 'north':
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    # situation if user chooses east
    elif direction == 'e' or direction == 'east':
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    # situation if user chooses south
    elif direction == 's' or direction == 'south':
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    # situation is user chooses west
    elif direction == 'w' or direction == 'west':
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
    # situation if user quits the game
    elif direction == 'q' or direction == 'quit':
        # creates new file to write in
        save_game = open("saved_game", "w+")
        # saves each variable as a string
        save_game.write(str(current_room) + "\n")
        save_game.write(str(bullets) + "\n")
        save_game.write(str(time)+ "\n")
        save_game.write(str(closet)+ "\n")
        save_game.write(str(kitchen)+ "\n")
        save_game.write(str(fr) + "\n")
        save_game.write(str(lr) + "\n")
        save_game.write(str(gym) + "\n")
        save_game.write(str(sc) + "\n")
        save_game.write(str(office) + "\n")
        save_game.write(str(pool) + "\n")
        save_game.write(str(ball))
        save_game.close()
        print("Your game has been saved!")
        # ends the game
        done = True

    else:
        print ("Please use \"n\", \"w\", \"s\" and \"e\" for directions")

    # situation when you run out of time
    if time == 0:
        print("Unfortunately you have run out of time and cannot continue exploring the house.")
        print("You ended up with " + str(bullets) + " bullets! Good job!")
        done = True
    # situation when you visited all the rooms
    if closet is False and kitchen is False and fr is False and lr is False and gym is False and sc is False and office is False \
            and pool is False and bball is False:
        print("Wow! You explored the entire house and got " + str(bullets) + " bullets with " + str(time) +
              " minutes to spare!.")
        done = True
