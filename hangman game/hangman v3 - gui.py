import tkinter as tk
from tkinter import messagebox
import sqlite3
import random
from PIL import ImageTk, Image
import keyboard



root = tk.Tk()
root.update()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#print(screen_height)

#root.geometry("{}x{}".format(screen_width, screen_height))
root.attributes('-fullscreen', True) #makes the game fullscren

button_width = screen_width / 4
button_height = screen_height / 8

col_background = "#F3F3F3"#FAA5E1
col_buttons = "#A2E678"

font = ("Comic Sans MS", "36")

name = ''

#resets all the global variables needed for the code
def reset_var():
    global word, x_word, lives, guessed_letters, correct_letters, incorrect_letters
    word = ''
    x_word = ''
    lives = 0
    guessed_letters = []
    correct_letters = []
    incorrect_letters = []

#----------------backend of the game----------------

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def word_pick():
    global word, x_word
    with open("wordlist.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split('\n')))
        word = random.choice(words)#this picks a random word from the list
    x_word = ''
    for letters in word:
        x_word=x_word+"*"
        #print(word)
        #print(x_word)
    #return(word, x_word)


#-----------------button commands--------------------
def letter_guessed(letter):
    global guessed_letters, correct_letters, incorrect_letters, x_word, lives
    guessed_letters.append(letter)
    count = -1
    for each in word:
        count = count+1
        if each == letter:
            x_word = replacer(x_word, letter, count)
            #x_word = word
            #print(x_word)
        
    if letter in word:
        hidden_word()
        return True
    else:
        lives = lives +1
        draw_hangman(lives, 'black')
        if lives == 12:
            game_over()
        return False

def already_guessed():
    messagebox.showerror("Letter", "You have already guessed this letter")


def begin_game(Name):
    reset_var()
    col = 'light grey'# the colour of the keyboard
    word_pick()
    global name
    name = Name
    if name == '':
        messagebox.showerror("Name", "You need to enter a name")
    else:
        widget_clear()
        button_close()
        back_button()
        draw_hangman(12, "light grey")
        
        top = ['q','w','e','r','t','y','u','i','o','p']
        mid = ['a','s','d','f','g','h','j','k','l']
        bot = ['z','x','c','v','b','n','m',]

        width = screen_width * 1/14
        height = screen_width * 1/14

        x = screen_width * 2/14
        y = screen_height * 8/14
        
        for letter in top:
            keyboard_spawn(letter, x, y, width, height, col)
            x = x + width

        x = screen_width * 2.5/14
        y = y + height
        for letter in mid:
            keyboard_spawn(letter, x, y, width, height, col)
            x = x + width

        x = screen_width * 3.5/14
        y = y + height
        for letter in bot:
            keyboard_spawn(letter, x, y, width, height, col)
            x = x + width

        hidden_word()

        


        

def keyboard_change_col(index, letter):
    #q  w  e  r  t  y  u  i  o  p
    #26 27 28 29 30 31 32 33 34 35

    #a  s  d  f  g  h  j  k  l
    #36 37 38 39 40 41 42 43 44

    #z  x  c  v  b  n  m
    #45 46 47 48 49 50 51
    
    #q is 25,
    #m is 51
    #need to fix this next
    root.update()#this is needed in order to get the updated posistion of the button
    i = 0
    for widget in root.winfo_children():
        #print(widget)
        if i == index:
            #print(widget)
            #print(str(widget.winfo_rootx()))
            x = widget.winfo_rootx()
            y = widget.winfo_rooty()
            return x,y
        i = i+1

    
#this func auto creates a button and saves a little time and will
#help when i create the keyboard
def button_spawn(root, col, command, text, font, x, y, width, height):
    button = tk.Button(root,
                       bg = col,
                       command=command,
                       text=text,
                       font=font)
    button.place(x=x,
                 y=y,
                 width=width,
                 height=height)
def background():
    global background
    background = tk.Canvas(root,
                           bg = col_background,
                           width = screen_width,
                           height = screen_height)
    background.pack()
    
#button_spawn(root, "blue", button_menu_play, "hi",("Comic Sans MS", "30"), 100, 200, 100, 100)

def letter_pressed(letter, width, height, t):
    match str(letter):
        case 'q': index = 3
        case 'w': index = 4
        case 'e': index = 5
        case 'r': index = 6
        case 't': index = 7
        case 'y': index = 8
        case 'u': index = 9
        case 'i': index = 10
        case 'o': index = 11
        case 'p': index = 12
        
        case 'a': index = 13
        case 's': index = 14
        case 'd': index = 15
        case 'f': index = 16
        case 'g': index = 17
        case 'h': index = 18
        case 'j': index = 19
        case 'k': index = 20
        case 'l': index = 21

        case 'z': index = 22
        case 'x': index = 23
        case 'c': index = 24
        case 'v': index = 25
        case 'b': index = 26
        case 'n': index = 27
        case 'm': index = 28
    try:
        x,y = keyboard_change_col(index, letter)
    except TypeError:
        x,y = -150, -150
    if t == True:
        button_spawn(root, col_buttons, already_guessed,
                     str(letter), font, x, y, width, height)
        
    if t == False:
        button_spawn(root, "red", already_guessed,
                     str(letter), font, x, y, width, height)

    #print(x)
    #print(y)
    #print(letter)
    
#------------------button spawns---------------------#

def game_over():
    widget_clear()

    label = tk.Label(root,
                    text = 'game over',
                    font = font,
                    borderwidth=2,)
    label.place(x=screen_width/2,
                y=screen_height * 6/12)

    label = tk.Label(root,
                     text = word,
                     font = font,
                     borderwidth = 2)
    label.place(x=screen_width/2,
                y = screen_height/3)

    button_close()
    back_button()

    #-----this is all decor------------
    message = tk.Message(root,
                         bg = button_col,
                         text = 'g',
                         font = font)
    message.place(x = screen_width* 1/12,
                  y = screen_height * 1/12)
    
                     

def win_screen():
    global img1, pic
    img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\maxwe\Desktop\python\games\hangman game\photos\firework.jpeg", "r"))


    pic = tk.Label(root, image = img1)
    pic.pack()
    
    
    widget_clear()    
    label = tk.Label(root,
                    text = 'win',
                    font = font,
                    borderwidth=2,)
    label.place(x=screen_width/2,
                y=screen_height * 6/12)

    button_close()
    back_button()

    label = tk.Label(root,
                     text = len(guessed_letters),
                     font = font,
                     borderwidth = 2)
    label.place(x = (screen_width/2) - len(guessed_letters)*13,
                y = screen_height * 7/12)

    label = tk.Label(root,
                     text = word,
                     font = font,
                     borderwidth = 2)
    label.place(x=screen_width/2,
                y = screen_height/3)
    
    

    con = sqlite3.connect('scores.db')
    curs = con.cursor()
    values = [name, len(guessed_letters)]
    print(values)
    names = []
    for row in curs.execute("SELECT * FROM player_score ORDER BY guesses asc"):
        print(row)
        if row[0] not in names:
            names.append(row[0])
            curs.execute("INSERT INTO player_score VALUES(?,?)", values)
            print(row)
    con.commit()
   

    
#shows the hidden word on the screen
def hidden_word():
    for widget in root.winfo_children():#destroys the prvious label so the dont pile up
        if str(widget)[0:7] == '.!label':
            widget.destroy()
            
    label = tk.Label(root,
                    text = x_word,
                    font = font,
                    borderwidth=2,)#label that has the asterisk word
    label.place(x = (screen_width/2) - (len(x_word))*13,
                y = screen_height * 1/20)

    if x_word == word:
        win_screen()

#spawns all the keyboard letterrs      
def keyboard_spawn(letter, x, y, width, height, colour):
    #font = ("Comic Sans MS", "32")
    
    colour = 'light grey'

    
    keyboard = tk.Button(root,
                        text = letter,
                        font = font,
                        command = lambda: letter_pressed(letter, width, height, letter_guessed(letter)),
                        bg = colour)
    keyboard.place(x=x,
                   y=y,
                   width=width,
                   height=height)
                     
                           
        


#this draws the handman in grey and will put the number of lives as
#how many black lines are needed
#initially draws the base grey lines then keeps drawing the black
#lines ontop based on how many libes are left
def draw_hangman(lives, col):
    #widget_clear()
    #back_button()
    #button_close()

    match lives:
        case 1:#bottom horizontal line
            background.create_line(screen_width * 4/10,
                                   screen_height * 5/10,
                                   screen_width * 6/10,
                                   screen_height * 5/10,
                                   width = 3,
                                   fill = col)
        case 2:#left vertical line
            background.create_line(screen_width * 4.2/10,
                                   screen_height * 5/10,
                                   screen_width * 4.2/10,
                                   screen_height * 1.5/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(1, col)
        case 3:#bottom triangle hypotonuse
            background.create_line(screen_width * 4.2/10,
                                   screen_height * 4.6/10,
                                   screen_width * 4.5/10,
                                   screen_height * 5/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(2, col)
        case 4:#top horizontal line
            background.create_line(screen_width * 4/10,
                                   screen_height * 1.5/10,
                                   screen_width * 6/10,
                                   screen_height * 1.5/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(3, col)
        case 5:#top triangle hypotonuse
            background.create_line(screen_width * 4.2/10,
                                   screen_height * 1.9/10,
                                   screen_width * 4.5/10,
                                   screen_height * 1.5/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(4, col)
        case 6:#rope line
            background.create_line(screen_width * 6/10,
                                   screen_height * 1.5/10,
                                   screen_width * 6/10,
                                   screen_height * 2/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(5, col)
        case 7:#head
            background.create_oval(screen_width * 5.85/10,
                                   screen_height * 2/10,
                                   screen_width * 6.15/10,
                                   screen_height * 2.4/10,
                                   width=2,
                                   outline = col)
            draw_hangman(6, col)
        case 8:#torso
            background.create_line(screen_width * 6/10,
                                   screen_height * 2.4/10,
                                   screen_width * 6/10,
                                   screen_height * 3/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(7, col)
        case 9:#left leg
            background.create_line(screen_width * 6/10,
                                   screen_height * 3/10,
                                   screen_width * 5.8/10,
                                   screen_height * 3.4/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(8, col)
        case 10:#right leg
            background.create_line(screen_width * 6/10,
                                   screen_height * 3/10,
                                   screen_width * 6.2/10,
                                   screen_height * 3.4/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(9, col)
        case 11:#left arm
            background.create_line(screen_width * 6/10,
                                   screen_height * 2.7/10,
                                   screen_width * 5.8/10,
                                   screen_height * 2.7/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(10, col)
        case 12:#right arm
            background.create_line(screen_width * 6/10,
                                   screen_height * 2.7/10,
                                   screen_width * 6.2/10,
                                   screen_height * 2.7/10,
                                   width = 3,
                                   fill = col)
            draw_hangman(11, col)
    #background.create_line(

    
def button_close():
    close = tk.Button(root,
                      bg = 'red',
                      command = root.destroy,
                      text = "X",
                      font = ("Comic Sans MS", "30"))
    close.place(x = screen_width - (button_height/2),
                y = 0,
                width = button_height/2,
                height = button_height/2)

#takes you back to the menu
def back_button():
        
    button = tk.Button(root,
                       text = "←",
                       command = menu_screen,
                       bg = "#696969",
                       font = font)
    button.place(x = 0,
                 y = 0,
                 width = 50,
                 height = 50)
    #button_spawn(root, "#696969", menu_screen, "←", ("Comic Sans MS", "30"), 0,0, 50,50)

#spawns the leaderboard screen
def leaderboard_screen():
    #global label
    widget_clear()
    button_close()
    back_button()

    names =[]
    i=1
    con = sqlite3.connect('scores.db')
    curs = con.cursor()
    for row in curs.execute("SELECT * FROM player_score ORDER BY guesses asc"):
        if row[0] not in names and i <= 8:
            #the fisrt label is the names
            label = tk.Label(root,
                             text = row[0],
                             font = font,
                             borderwidth=2,)
            label.place(x = (screen_width * 2/9) +1,#had to add 1 so it doesnt collide with the border
                        y = (screen_height * (i+1)/12) + 1)#same as line above


            #the second label is the scores they got
            label = tk.Label(root,
                             text = row[1],
                             font = font,
                             borderwidth=2,)
            label.place(x = (screen_width * 6/9) +1,#had to add 1 so it doesnt collide with the border
                        y = (screen_height * (i+1)/12) + 1)#same as line above

            #the third label is the first second third etc
            if i==1:
                leaderboard_place_col="gold"
            elif i==2:
                leaderboard_place_col="silver"
            elif i==3:
                leaderboard_place_col="#cd7f32"
            else:
                leaderboard_place_col="black"
            label = tk.Label(root,
                             text = i,
                             font = font,
                             fg = leaderboard_place_col,
                             borderwidth=2,)
            label.place(x = (screen_width * 1/9) +1,#had to add 1 so it doesnt collide with the border
                        y = (screen_height * (i+1)/12) + 1)#same as line above

            i = i+1
            names.append(row[0])

            
    for i in range(1, 5):
        if i == 1:# these if statemnet ensure the vertical lines are in the correst palces
            j = 1
        elif i == 2:
            j = 2
        elif i == 3:
            j = 5
        elif i == 4:
            j = 8
        background.create_line(screen_width * j/9,
                               screen_height * 2/12,
                               screen_width * j/9,
                               screen_height *10/12,
                               width=2)
    for i in range(1,10):
        background.create_line(screen_width* 1/9,
                               screen_height* (i+1)/12,
                               screen_width* 8/9,
                               screen_height* (i+1)/12,
                               width=2)
        

    
    

def widget_clear():
    for widget in root.winfo_children():
        if str(widget) != ".!canvas" :
            widget.destroy()
    background.delete('all')


#spawns in the menu screen buttons
def menu_screen():    

    #play botton
    play = tk.Button(root,
                     text ="Play",
                     font = font,
                     command = lambda: begin_game(entry.get()),
                     bg = col_buttons,)
    play.place(x = (screen_width/2)-(button_width/2),#dead centre
               y = screen_height* 6/10,#
               width = button_width,#standard button width
               height = button_height,)#standard button height

    #leaderboard button
    leaderboard = tk.Button(root,
                            text ="Leaderboard",
                            command = leaderboard_screen,
                            bg = col_buttons,
                            font = font)
    leaderboard.place(x = (screen_width/2)-(button_width/2),#dead centre
               y = screen_height* 8/10,
               width = button_width,#standard button width
               height = button_height)#standard button height

    #label that says name:
    name_label = tk.Label(root,
                          text = "Name:",
                          bg = col_buttons,
                          font = ("Comic Sans MS", "20"))
    name_label.place(x = (screen_width/2) - (button_width/2),
                     y = (screen_height * 5/10)- 45,)

    #this is where you enter your name
    entry = tk.Entry(root,
                    bd = 0,
                    font = ("Comic Sans Ms", "20"),
                    bg = col_buttons,)
    entry.insert(0, name)
    entry.place(x=(screen_width/2) - (button_width/2),
               y= screen_height * 5/10,
               width = button_width)
    

    #----------------------------------------------------------------------
    #these lines are the border for the name input box
    #i just added them for aesthetics icl
    #i could have made them more eeficient with less code but idc
    background.create_line((screen_width/2) - (button_width/2)-1,#top horizontal line
                           (screen_height * 5/10)-1,
                           (screen_width/2) + (button_width/2)+1,
                           (screen_height * 5/10)-1,
                           width=1)
    background.create_line((screen_width/2) - (button_width/2),#bottom line
                           (screen_height * 5/10)+40,
                           (screen_width/2) + (button_width/2)+1,
                           (screen_height * 5/10)+40,
                           width=1)
    background.create_line((screen_width/2) - (button_width/2)-1,#;eft line
                           (screen_height * 5/10)-1,
                           (screen_width/2) - (button_width/2)-1,
                           (screen_height * 5/10)+41,
                           width=1)
    background.create_line((screen_width/2) + (button_width/2),#right line
                           (screen_height * 5/10)-1,
                           (screen_width/2) + (button_width/2),
                           (screen_height * 5/10)+41,
                           width=1)
    #--------------------------------------------------------------------


    button_close()





#button_close()
background()
menu_screen()
#begin_game('max')
#win_screen()


root.mainloop()
