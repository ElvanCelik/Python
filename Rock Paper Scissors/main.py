from tkinter import *
import random
import time

def rock():
    global players_choose
    players_choose = "rock"
    compare()

def paper():
    global players_choose
    players_choose = "paper"
    compare()

def scissors():
    global players_choose
    players_choose = "scissors"
    compare()

def compare():
    global liste
    global score_player
    global score_computer
    global players_choose
    random.shuffle(liste)
    time.sleep(0.3)
    if liste[0] == players_choose:
        choose_computer['text'] = "Computer's Choose : " + liste[0]
    elif liste[0] == 'rock' and players_choose == "scissors":
        choose_computer['text'] = "Computer's Choose : " + liste[0]
        score_computer += 1
        point_computer["text"] = "Computer : " + str(score_computer)
    elif liste[0] == 'rock'and players_choose=="paper":
        choose_computer['text'] = "Computer's Choose : " + liste[0]
        score_player+=1
        point_player["text"] = "Player : " + str(score_player)
    elif liste[0] == 'scissors'and players_choose=="paper":
        choose_computer['text'] = "Computer's Choose : " + liste[0]
        score_computer+=1
        point_computer["text"] = "Computer : " + str(score_computer)
    elif liste[0] == 'scissors'and players_choose=="rock":
        choose_computer['text'] = "Computer's Choose : " + liste[0]
        score_player+=1
        point_player["text"] = "Player : " + str(score_player)
    elif liste[0] == 'paper'and players_choose=="rock":
        choose_computer['text'] = "Computer's Choose : " + liste[0]
        score_computer+=1
        point_computer["text"] = "Computer : " + str(score_computer)
    elif liste[0] == 'paper'and players_choose=="scissors":
        choose_computer['text'] = "Computer's Choose : " + liste[0]
        score_player+=1
        point_computer["text"] = "Player : " + str(score_player)

liste = ["rock", "paper", "scissors"]
score_player = 0
score_computer = 0

window = Tk()
window.title("Rock Paper Scissors")
window.config(bg='lightpink')

width = window.winfo_screenwidth() // 2
height = window.winfo_screenheight() // 2
window.geometry("{}x{}+300+200".format(width, height))
point_player = Label(window, fg='black', font='Arial 14 italic bold', bg='lightgray', text="Player : 0")
point_player.place(x=10, y=50)
point_computer = Label(window, fg='black', font='Arial 14 italic bold', bg='lightgray', text="Computer : 0")
point_computer.place(x=350, y=50)

choose_computer = Label(window, fg='black', font='Arial 14 italic bold', bg='lightgray', text="Computer's Choice : 0")
choose_computer.place(x=200, y=120)

buttonRock = Button(window, text="Rock", command=rock, width=7)
buttonPaper = Button(window, text="Paper", command=paper, width=7)
buttonScissors = Button(window, text="Scissors", command=scissors, width=7)

buttonRock.place(x=50, y=150)
buttonPaper.place(x=50, y=200)
buttonScissors.place(x=50, y=250)

window.mainloop()
