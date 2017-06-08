#!/usr/local/bin/python
import curses
import random

def main(screen):
  curses.curs_set(0)
  while True :
    event = screen.getch()
    screen.addstr(str(event) + '\n')
curses.wrapper(main)
