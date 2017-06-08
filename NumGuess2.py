#!/usr/local/bin/python
import curses
import random

def playAgain(screen) :
  screen.addstr("Do you want to play?\n[LEFT] yes / no [RIGHT]")
  while True :
    event = screen.getch()
    if event == 119 : # 'w'
      screen.clear()
      return True
    if event == 101 : # 'e'
      screen.clear()
      return False

def main(screen):
  MIN = low = 1
  MAX = high = 100
  screen.addstr("I can guess any number between " + str(MIN) + " and " + str(MAX) + " in 7 or less guesses\n(if you don't lie to me)\n")
  curses.curs_set(0)
  while(playAgain(screen)) :
    MIN = low = 1
    MAX = high = 100
    num = guess = numGuess = 0
    
    guess = random.randint(MIN,MAX)
    
    screen.clear()
    event = curses.KEY_UP
    num = int(MAX / 2)
    while True :
      screen.addstr("Choose a number: " + str(num))
      event = screen.getch()
      if event == curses.KEY_UP :
        if num < MAX :
          num += 1
      if event == curses.KEY_DOWN :
        if num > MIN :
          num -= 1
      if event == 10 : # ENTER
        break

      screen.clear()
    
    screen.clear()
    screen.addstr("The number to guess is " + str(num) + "\npress any key to start...")
    screen.getch()

    while(guess != num) :
      screen.clear()
      screen.addstr("I guess " + str(guess))
      screen.addstr("\nHIGHER or LOWER?")
      event = screen.getch()
      
      if event == curses.KEY_UP :
        if guess <= num :
          low = guess
        guess = int((guess+high)/2)
      elif event == curses.KEY_DOWN :
        if guess >= num :
          high = guess
        guess = int((guess+low)/2)
      elif event == 27 :
        break
  
      numGuess += 1
    
    screen.clear()
    if guess == num:
      screen.addstr("I guessed the number in " + str(numGuess) + " guesses! :D\n")
    else :
      screen.addstr("I didn't guess the number D;\n")
  
curses.wrapper(main)
