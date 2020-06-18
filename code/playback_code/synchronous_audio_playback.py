import pygame

def sync_playback(fileName):
    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()

sync_playback('../../data/sample_test_file.wav')