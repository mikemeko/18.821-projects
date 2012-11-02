"""
Tries to find games whose length is a power of two that doesn't terminate.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

from simulator import Simulator

def int_to_game(n, length):
  """
  Turns an integer into a game of the given length by writing n in binary 
  (backwards) then splitting up the bits.
  """
  assert length > 0, 'Given length must be positive.'
  assert n >= 0 and n < 2 ** length, '%d must be between 0 and %d.' % (
      n, 2 ** length)
  g = [0] * length
  for idx in range(length):
    g[idx] = n % 2
    n /= 2
  return g

def main1():
  """
  Looks for game lengths for which all games terminate.
  """
  for length in range(1, 50):
    print 'Looking for non-terminating game of length %d...' % length
    game_found = False
    for n in range(0, 2 ** length):
      g = int_to_game(n, length)
      l = Simulator(g).get_game_length()
      if l is None:
        game_found = True
        print 'FOUND: %s' % g
        break
    if not game_found:
      print 'NONE FOUND'

def main2():
  """
  Looks at which games are possible after a certain number of differences.
  """
  GAME_LENGTH = 16
  # possible_tuples[i] is the set of tuples for which there exists a game
  # whose ith element is that tuple
  possible_tuples = []
  for n in range(0, 2 ** GAME_LENGTH):
    g = int_to_game(n, GAME_LENGTH)
    sim = Simulator(g)
    assert sim.get_game_length() is not None, 'Non-terminating game: %s' % g
    t = 0
    while not sim.done():
      if t >= len(possible_tuples):
        possible_tuples.append(set())
      possible_tuples[t].add(tuple(sim.state))
      sim.step_forward()
      t += 1
    # Add ending tuple as well
    if t >= len(possible_tuples):
      possible_tuples.append(set())
    possible_tuples[t].add(tuple(sim.state))
  print 'Number of possible tuples after t steps:'
  for t in range(len(possible_tuples)):
    print '%d: %d' % (t, len(possible_tuples[t]))

if __name__ == '__main__':
  #main1()
  main2()
