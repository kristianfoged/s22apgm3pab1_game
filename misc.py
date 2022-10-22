import sys
import pygame
import pandas as pd

df_game_rounds = pd.read_csv(r'game_rounds.csv')
print(df_game_rounds)
#print(pygame.font.get_fonts())