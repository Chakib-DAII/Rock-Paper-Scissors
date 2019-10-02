import random as rd
import time
import uuid
import hashlib

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha512(salt.encode() + user_password.encode()).hexdigest()

loose = ('the computer wins')
win = ('you win')
lives = 5
score = 0
drew = 0
computerLives = 7

def intro():
    print("                               ___           ___           ___           ___               ")                                                     
    print("                              /\  \         /\  \         /\__\         /|  |              ")                                                   
    print("                             /::\  \       /::\  \       /:/  /        |:|  |              ")                                                 
    print("                            /:/\:\__\     /:/\:\  \     /:/  /         |:|  |              ")                                               
    print("                           /:/ /:/  /    /:/  \:\  \   /:/  /  ___   __|:|  |              ")                                             
    print("                          /:/_/:/__/___ /:/__/ \:\__\ /:/__/  /\__\ /\ |:|__|____          ")                                             
    print("                          \:\/:::::/  / \:\  \ /:/  / \:\  \ /:/  / \:\/:::::/__/          ")                                             
    print("                           \::/~~/~~~~   \:\  /:/  /   \:\  /:/  /   \::/~~/~              ")                                             
    print("                            \:\~~\        \:\/:/  /     \:\/:/  /     \:\~~\               ")                                             
    print("                             \:\__\        \::/  /       \::/  /       \:\__\              ")                                             
    print("                              \/__/         \/__/         \/__/         \/__/              ")                                             
    print("                                                                                 ___         ___           ___         ___           ___     ")
    print("                                                                                /  /\       /  /\         /  /\       /  /\         /  /\    ")
    print("                                                                               /  /::\     /  /::\       /  /::\     /  /:/_       /  /::\   ")
    print("                                                                              /  /:/\:\   /  /:/\:\     /  /:/\:\   /  /:/ /\     /  /:/\:\  ")
    print("                                                                             /  /:/~/:/  /  /:/~/::\   /  /:/~/:/  /  /:/ /:/_   /  /:/~/:/  ")
    print("                                                                            /__/:/ /:/  /__/:/ /:/\:\ /__/:/ /:/  /__/:/ /:/ /\ /__/:/ /:/___")
    print("                                                                            \  \:\/:/   \  \:\/:/__\/ \  \:\/:/   \  \:\/:/ /:/ \  \:\/:::::/")
    print("                                                                             \  \::/     \  \::/       \  \::/     \  \::/ /:/   \  \::/~~~~ ")
    print("                                                                              \  \:\      \  \:\        \  \:\      \  \:\/:/     \  \:\     ")
    print("                                                                               \  \:\      \  \:\        \  \:\      \  \::/       \  \:\    ")
    print("                                                                                \__\/       \__\/         \__\/       \__\/         \__\/    ")
    print("      ___           ___                       ___           ___           ___           ___           ___      ")   
    print("     /\  \         /\  \          ___        /\  \         /\  \         /\  \         /\  \         /\  \     ")    
    print("    /::\  \       /::\  \        /\  \      /::\  \       /::\  \       /::\  \       /::\  \       /::\  \    ")    
    print("   /:/\ \  \     /:/\:\  \       \:\  \    /:/\ \  \     /:/\ \  \     /:/\:\  \     /:/\:\  \     /:/\ \  \   ")    
    print("  _\:\~\ \  \   /:/  \:\  \      /::\__\  _\:\~\ \  \   _\:\~\ \  \   /:/  \:\  \   /::\~\:\  \   _\:\~\ \  \  ")    
    print(" /\ \:\ \ \__\ /:/__/ \:\__\  __/:/\/__/ /\ \:\ \ \__\ /\ \:\ \ \__\ /:/__/ \:\__\ /:/\:\ \:\__\ /\ \:\ \ \__\ ")    
    print(" \:\ \:\ \/__/ \:\  \  \/__/ /\/:/  /    \:\ \:\ \/__/ \:\ \:\ \/__/ \:\  \ /:/  / \/_|::\/:/  / \:\ \:\ \/__/ ")    
    print("  \:\ \:\__\    \:\  \       \::/__/      \:\ \:\__\    \:\ \:\__\    \:\  /:/  /     |:|::/  /   \:\ \:\__\   ")    
    print("   \:\/:/  /     \:\  \       \:\__\       \:\/:/  /     \:\/:/  /     \:\/:/  /      |:|\/__/     \:\/:/  /   ")    
    print("    \::/  /       \:\__\       \/__/        \::/  /       \::/  /       \::/  /       |:|  |        \::/  /    ")    
    print("     \/__/         \/__/                     \/__/         \/__/         \/__/         \|__|         \/__/     ")
    print('                                                                                                                 made by chakib Daii')
    print('---------------------------------------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------------------------------------------------------------------')
    print("rules : ")
    print("You start with",lives, "lives.")
    print("if you win, you get an extra life.")
    print("if you loose, you loose a life.")
    print("if you drow lives dtay the same")
    print('---------------------------------------------------------------------------------------------------------------------------------------')
    print("to see list of rules type : rules")
    print('---------------------------------------------------------------------------------------------------------------------------------------')
    print("to exit the game type : exit")
    print('---------------------------------------------------------------------------------------------------------------------------------------')

    print("to display lives the game type : display lives")
    print('---------------------------------------------------------------------------------------------------------------------------------------')

    print("to display score the game type : display score")
    print('---------------------------------------------------------------------------------------------------------------------------------------')

    print("to display drew the game type : display drew")
    print('---------------------------------------------------------------------------------------------------------------------------------------')
    print("the computer has lives aswell")
    print("can you beat the computer ? ")
    print("Good luck")
    print('---------------------------------------------------------------------------------------------------------------------------------------')


while True :
    print('to begin fill in the below information')
    username = input('please enter your username : ')
    password = input('Please enter your password : ')
    accountsFile = open("accounts.txt",'r')
    data = accountsFile.readlines()
    for line in data:
        userPass = line.split()
        if username in userPass and check_password(userPass[1],password):
            print('access granted')
            intro()
            while True :
                rps = str.lower(input("Rock, paper, scissors ? "))
                computer = ("rock", "paper", "scissors")
                computer = rd.choice(computer)
                #rock
                if rps == "rock" and computer == "paper":
                    print("the computer choose", computer,"\n")
                    print(loose,"\n\n")
                    lives -= 1
                elif rps == "rock" and computer == "scissors":
                    print("the computer choose", computer,"\n")
                    print(win,"\n\n")
                    computerLives -= 1
                    score += 1
                #paper
                elif rps == "paper" and computer == "rock":
                    print("the computer choose", computer,"\n")
                    print(win,"\n\n")
                    computerLives -= 1
                    score += 1
                elif rps == "paper" and computer == "scissors":
                    print("the computer choose", computer,"\n")
                    print(loose,"\n\n")
                    lives -= 1
                #scissors
                elif rps == "scissors" and computer == "paper":
                    print("the computer choose", computer,"\n")
                    print(win,"\n\n")
                    computerLives -= 1
                    score += 1
                elif rps == "scissors" and computer == "rock":
                    print("the computer choose", computer,"\n")
                    print(loose,"\n\n")
                    lives -= 1
                #duplicates
                elif rps == "rock" and computer == "rock":
                    print("the computer choose", computer,"\n")
                    print("you Drew\n\n")
                    drew += 1
                elif rps == "scissors" and computer == "scissors":
                    print("the computer choose", computer,"\n")
                    print("you Drew\n\n")
                    drew += 1
                elif rps == "paper" and computer == "paper":
                    print("the computer choose", computer,"\n")
                    print("you Drew\n\n")
                    drew += 1
                #system
                elif rps == "rules":
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    print("rules")
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    print("- Rock loses against Paper.")
                    print("- Rock beats Scissors.")
                    print("- Paper loses against Scissors.")
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                elif rps == "display lives":
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    print("Lives : ", lives)
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    
                elif rps == "display score":
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    print("score : ", score)
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    
                elif rps == "display drew":
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    print("drew : ", drew)
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                #exit
                elif rps == "exit":
                    exit();
                else:
                    print("unvalid input, please try again !")    

                #lives
                if lives == 0 or rps == "test":
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    print("Thanks for playing.")
                    print("You run out of lives.")
                    print("You get", score, "Correct!")
                    print("You drew", drew,"times.")
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    rps = input("Type 'exit' to exit : ")
                    time.sleep(5)
                    #exit
                    if rps == "exit":
                        exit();
                if computerLives == 0:
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    print("Thanks for playing.")
                    print("You Win. The computer lost all it's lives.")
                    print("You get", score, "Correct!")
                    print("You drew", drew,"times.")
                    print('---------------------------------------------------------------------------------------------------------------------------------------')
                    rps = input("Type 'exit' to exit : ")
                    time.sleep(5)
                    #exit
                    if rps == "exit":
                        exit();
                
        else :
            print("your username or password is incorrect ")
            print('---------------------------------------------------------------------------------------------------------------------------------------')
                
