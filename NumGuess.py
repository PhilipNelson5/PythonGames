#!/usr/local/bin/python
import curses
import random

def playAgain(screen):
  screen.addstr("Do you want to play?\n[LEFT] yes / no [RIGHT]")
  event = screen.getch()
  if event == 119:
    screen.clear()
    return True
  else :
    return False

def main(screen):
  screen.addstr("I can guess any number between 0 and 100 in 7 or less guesses\n(if you don't lie to me)\n")
  while(playAgain(screen)):
    MIN = low = 0
    MAX = high = 100
    num = guess = numGuess = 0
    
    num = random.randint(MIN,MAX)
    guess = random.randint(MIN,MAX)
    
    screen.addstr("The number to guess is " + str(num) + "\npress any key to start...")
    screen.getch()

    while(guess != num):
      screen.clear()
      screen.addstr("I guess " + str(guess))
      screen.addstr("\nHIGHER or LOWER?")
      event = screen.getch()
      
      if event == curses.KEY_UP:
        if guess <= num :
          low = guess
        guess = int((guess+high)/2)
      elif event == curses.KEY_DOWN:
        if guess >= num :
          high = guess
        guess = int((guess+low)/2)
      elif event == 27:
        break
  
      numGuess += 1
    
    screen.clear()
    if guess == num:
      screen.addstr("I guessed the number in " + str(numGuess) + " guesses! :D\n")
    else :
      screen.addstr("I didn't guess the number D;\n")
  
curses.wrapper(main)
