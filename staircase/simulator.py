"""
Simulator for staircase.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

from math import factorial
from numpy import matrix
from numpy.linalg import det
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

def simulate_staircases(num_blocks, num_trials):
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
  for staircase_str in sorted(hist.keys()):
    print '%s: %.4f' % (deserialize_staircase(staircase_str),
        hist[staircase_str] / num_trials)

def enumerate_staircases(num_blocks):
  """
  Enumerates all possible staircases as well as their probabilities of
  occurring.
  """
  print 'Enumerating all staircases with %d blocks...' % num_blocks
  # staircases[k] is a dictionary mapping a staircase with k+1 blocks to the
  # probability it is created
  staircases = [{} for k in range(num_blocks)]
  staircases[0][serialize_staircase(get_staircase(1))] = 1.0
  for k in range(1, num_blocks):
    for staircase_str, p in staircases[k-1].iteritems():
      staircase = deserialize_staircase(staircase_str)
      staircase = staircase + [0]
      valid_locs = [0]
      for loc in range(1, k + 1):
        if staircase[loc - 1] > staircase[loc]:
          valid_locs.append(loc)
      for loc in valid_locs:
        new_staircase = staircase[:]
        new_staircase[loc] += 1
        new_staircase_str = serialize_staircase(new_staircase)
        if new_staircase_str not in staircases[k]:
          staircases[k][new_staircase_str] = 0
        staircases[k][new_staircase_str] += p / len(valid_locs)
  # Get results for staircases with num_blocks blocks
  for staircase_str in sorted(staircases[num_blocks - 1].keys()):
    print '%s: %.4f' % (deserialize_staircase(staircase_str),
        staircases[num_blocks - 1][staircase_str])

memo = {}
def num_constructions(staircase):
  """
  Finds the number of ways a given staircase can be constructed.
  (Using a recursive formula)
  """
  assert_valid_staircase(staircase)
  # Base case, a staircase of all 1s
  if staircase[-1] == 1:
    return 1
  serialized = serialize_staircase(staircase)
  if serialized not in memo:
    memo[serialized] = 0
    remove_locs = (i for i in xrange(len(staircase) - 1)
      if staircase[i] > staircase[i + 1])
    for i in remove_locs:
      removed_staircase = staircase[:-1]
      removed_staircase[i] -= 1
      memo[serialized] += num_constructions(removed_staircase)
  return memo[serialized] 

def num_constructions_2(staircase):
  """
  Finds the number of ways a given staircase can be constructed.
  (Using an explicit formula)
  """
  assert_valid_staircase(staircase)
  columns = [c for c in staircase if c > 0]
  matrix_rows = [[1.0 / factorial(columns[i] - i + j)
    for j in xrange(len(columns))] for i in xrange(len(columns))]
  # round to guard against floating point error
  return int(round(factorial(sum(columns)) * det(matrix(matrix_rows))))

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

def assert_valid_staircase(staircase):
  """
  Checks the conditions on (unique) staircase representation.
  """
  assert sum(staircase) == len(staircase), 'values must sum to to length'
  for i in xrange(len(staircase) - 1):
    assert staircase[i] >= staircase[i+1], 'decreasing at index %d' % (i + 1)
  assert staircase[-1] >= 0, 'values must be non-negative'

if __name__ == '__main__':
  #print prettify_staircase(get_staircase(15))
  #simulate_staircases(4, 100000)
  #enumerate_staircases(4)
  staircase = [3,3,3,3,0,0,0,0,0,0,0,0]
  #print '%d ways to construct %s' % (num_constructions(staircase), staircase)
  print '%d ways to construct %s' % (num_constructions_2(staircase), staircase)
