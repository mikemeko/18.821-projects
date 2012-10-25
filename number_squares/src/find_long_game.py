"""
Script to find a game that takes a long time.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

from simulator import Simulator

def find_long_game(length):
  assert length >= 0, 'Game length must be non-negative.'
  if length == 0:
    ans = [0, 0, 0, 0]
  elif length == 1:
    ans = [1, 1, 1, 1]
  elif length == 2:
    ans = [1, 0, 1, 0]
  elif length == 3:
    ans = [1, 1, 0, 0]
  else:
    g = [0, 1, 1, 3]
    cur_length = 4
    while cur_length < length:
      d = g[3] - g[2] - g[1]
      assert d > 0, 'Last element must be at least the sum of the other 3.'
      g = [0, d, 2 * g[1] + 2 * d, 2 * g[1] + 2 * g[2] + 3 * d]
      cur_length += 1
    ans = g
  l = Simulator(ans).get_game_length()
  assert l == length, 'Invalid answer %s. Expected length %d, got %d.' % (
      ans, length, l)
  return ans

def main():
  length = int(raw_input('Desired game length?\n>>> '))
  print find_long_game(length)

if __name__ == '__main__':
  main()
