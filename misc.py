import sys
import pygame
import pandas as pd

df_game_rounds = pd.read_csv(r'game_rounds.csv')
df_shooting_position = pd.read_csv(r'shooting_positions.csv')
#print(df_game_rounds)
#print(pygame.font.get_fonts())
print(df_shooting_position)