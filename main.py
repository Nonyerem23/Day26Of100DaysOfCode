import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  # while True:
  #   # Start taking user input and doing something with it
  #  print('come here')
  #  # restart = int(input('')) 

while True:
  # clear the screen
  os.system('clear')

  # Show the menu
  print("Welcome to the music player!")
  time.sleep(2)
  print('Press 1 to play')
  time.sleep(2)
  print('Press 2 to pause')
  time.sleep(2)
  print('Type 3 to exit')
  time.sleep(2)

  # take user's input
  userplay = int(input(' -> '))
  if userplay == 1:
    print('Here are the nice tunes!')
  elif userplay == 2:
    print('You have to play the music first')
  elif userplay == 3:
    break
  else:
    print('Sorry, it is not available')
print('Thank you for using the music player!')
  # check whether you should call the play() subroutine depending on user's input
if True:
    play()

