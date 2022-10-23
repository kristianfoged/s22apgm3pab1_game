import sys
import pygame
import pandas as pd

df_game_rounds = pd.read_csv(r'game_rounds.csv')
df_shooting_position = pd.read_csv(r'shooting_positions.csv')
#print(df_game_rounds)
#print(pygame.font.get_fonts())
#print(df_shooting_position)


# https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
import csv
 
filename ="game_rounds.txt"
 
name = input("ENTER NAME: ")
print({name})

# opening the file using "with"
# statement
#with open(filename, 'r') as data:
#  for line in csv.DictReader(data):
   #   print(line)


from csv import DictReader
# open file in read mode
with open("game_rounds.txt", 'r') as f:
     
    dict_reader = DictReader(f)
     
    list_of_dict = list(dict_reader)
   
    print(list_of_dict)