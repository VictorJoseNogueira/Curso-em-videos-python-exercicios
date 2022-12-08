import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex0021.mp3')
pygame.mixer.music.play()
input('press "enter" to stop')

pygame.event.wait()
