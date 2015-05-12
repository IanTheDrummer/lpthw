from sys import exit
from random import randint
from Engine import engine
from GameMap import Map

tdc_map = Map('startup')
tdc_game = engine(tdc_map)
tdc_game.play()

