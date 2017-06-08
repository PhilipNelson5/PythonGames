#!/usr/local/bin/python
import curses
import random
import time
MIN = low = 1
MAX = high = 100
num = guess = numGuess = 0
LEFT = 119  # 'w'
RIGHT = 101 # 'e'

def playAgain(screen) :
  screen.addstr("Do you want to play?\n[LEFT] yes / no [RIGHT]")
  while True :
    event = screen.getch()
    if event == LEFT : 
      screen.clear()
      return True
    if event == RIGHT :
      screen.clear()
      return False

def makeGuess(screen) :
  global guess
  global MAX
  global MIN
  newGuess = guess
  while True :
    screen.clear()
    screen.addstr("Choose a number to guess: " + str(newGuess) + '\n')
    event = screen.getch()
    if event == curses.KEY_UP :
      if newGuess < MAX :
        newGuess += 1
    if event == curses.KEY_DOWN :
      if newGuess > MIN :
        newGuess -= 1
    if event == 10 : # ENTER
      break

  return newGuess

def main(screen):
  global MIN
  global MAX
  global guess
  curses.curs_set(0)
  while(playAgain(screen)) :
    low = 1
    high = 100
    num = guess = numGuess = 0
    
    num = random.randint(MIN,MAX)
    screen.clear()

    screen.addstr("Try to guess the number\npress any key to start...")
    screen.getch()

    while(guess != num) :
      #screen.clear()
      
      guess = makeGuess(screen)
  
      numGuess += 1

      if guess > num :
        screen.addstr("Too high")
        screen.getch()
      elif guess < num :
        screen.addstr("Too low")
        screen.getch()
      elif guess == num :
        screen.addstr("You guessed the number in " + str(numGuess) + " guesses! :D\n")
        break
      
  
curses.wrapper(main)
