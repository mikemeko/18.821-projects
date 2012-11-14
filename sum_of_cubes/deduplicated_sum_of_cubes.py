"""
Script to find some numbers that can be obtained as a sum of cubes in two
different ways.
"""

__author__ = 'mikemeko@mit.edu'

class Deduplicator(list):
  """
  A list that has a representative sum of cubes that can be written in two
  different ways. This is to capture the fact that if a^3 + b^3 = c^3 + d^3,
  then for any x, (ax)^3 + (bx)^3 = (cx)^3 + (dx)^3.
  """
  def __init__(self, rep_sum_of_cubes, first_pair, cubes):
    list.__init__(self)
    self.rep_sum_of_cubes = rep_sum_of_cubes
    self.first_pair = first_pair
    self.cubes = cubes
  def belongs(self, sum_of_cubes):
    return (sum_of_cubes % self.rep_sum_of_cubes == 0 and
        sum_of_cubes / self.rep_sum_of_cubes in self.cubes)
  def __str__(self):
    return '%d %s' % (self.rep_sum_of_cubes, str(self.first_pair))

def find_groups(N):
  """
  Finds deduplicated groups of numbers that can be written as a sum of cubes.
  N: number of cubes to store.
  """
  # dictionary mapping cubes to their cube-roots
  cubes = {}
  for n in xrange(1, N + 1):
    cubes[n] = n**3

  # dictionary mapping sums of cubes to a list of pairs whose cubes sum to them
  sums_of_cubes = {}
  for m in xrange(1, N + 1):
    for n in xrange(m, N + 1):
      sum_mn = cubes[m] + cubes[n]
      sums_of_cubes[sum_mn] = sums_of_cubes.get(sum_mn, []) + [(m,n)]

  # a sorted list of subms of cubes that can be expressed so in multiple ways
  mult_sums_of_cubes = sorted([item for item in sums_of_cubes.items() if
      len(item[1]) > 1], key=lambda item: item[0])

  # deduplicated sums of cubes - note that the creation of the groups relies on
  # seeing the sums of cubes in sorted order.
  groups = []
  for (sum_of_cubes, pairs) in mult_sums_of_cubes:
    for group in groups:
      if group.belongs(sum_of_cubes):
        group.append(sum_of_cubes)
        break
    else:
      new_group = Deduplicator(sum_of_cubes, pairs, cubes)
      new_group.append(sum_of_cubes)
      groups.append(new_group)
  return groups

if __name__ == '__main__':
  for group in find_groups(100):
    print group
