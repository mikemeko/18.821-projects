"""
Simulator for staircase.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

import random

def get_staircase(num_blocks):
  """
  Returns a random staircase using the given number of blocks. A staircase is
  a tuple whose ith index is the number of blocks in column i.
  """
  staircase = [0 for j in range(num_blocks)]
  for block in range(num_blocks):
    valid_locs = [0]
    for loc in range(1, num_blocks):
      if staircase[loc] < staircase[loc - 1]:
        valid_locs.append(loc)
    loc = random.choice(valid_locs)
    staircase[loc] += 1
  return staircase

def prettify_staircase(staircase):
  """
  Returns a pretty string representing the given staircase.
  """
  staircase_copy = staircase[:]
  s = ''
  while max(staircase_copy) > 0:
    s = ''.join(['x' if e > 0 else ' ' for e in staircase_copy]) + '\n' + s
    for loc in range(len(staircase_copy)):
      staircase_copy[loc] -= 1 if staircase_copy[loc] > 0 else 0
  return s[:-1]

def simulate(num_blocks, num_trials):
  """
  Generates lots of staircases and prints the results.
  """
  print 'Generating %d staircases with %d blocks...' % (num_trials, num_blocks)
  hist = {}
  for trial in range(num_trials):
    staircase = get_staircase(num_blocks)
    staircase_str = serialize_staircase(staircase)
    if staircase_str not in hist:
      hist[staircase_str] = 0
    hist[staircase_str] += 1.0
  for staircase_str in hist:
    print '%s: %.4f' % (
        deserialize_staircase(staircase_str), hist[staircase_str] / num_trials)

def serialize_staircase(staircase):
  """
  Serializes the staircase into a string for use as a dictionary key.
  """
  return '.'.join([str(e) for e in staircase])

def deserialize_staircase(staircase_str):
  """
  Deserializes a staircase string into a staircase.
  """
  return [int(e) for e in staircase_str.split('.')]

if __name__ == '__main__':
  #print prettify_staircase(get_staircase(15))
  simulate(4, 100000)
