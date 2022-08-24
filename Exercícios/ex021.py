import pygame

pygame.init()
pygame.mixer.music.load('urss.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# There are another solutions as well, like this one
# import playsound
# playsound.playsound('urss.mp3')
