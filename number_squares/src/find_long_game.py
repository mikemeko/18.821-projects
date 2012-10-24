"""
Script to find a game that takes a long time.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

from simulator import Simulator

import random

def find_long_game():
  n = 0
  longest_length = -1
  longest_game = None
  upper_bound = 100
  time_at_bound = 0
  while True:
    n += 1
    time_at_bound += 1
    if time_at_bound > upper_bound:
      upper_bound *= 10
      time_at_bound = 0
    game = [int(upper_bound * random.random()) for i in range(4)]
    sim = Simulator(game)
    length = sim.get_game_length()
    assert length is not None, 'All length 4 games must terminate!'
    if length > longest_length:
      longest_length = length
      longest_game = game
      print 'Found length %d game: %s' % (length, game)

def main():
  find_long_game()

if __name__ == '__main__':
  main()
