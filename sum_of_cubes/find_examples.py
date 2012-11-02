"""
Finds examples of numbers n that can be expressed as the sum of two cubes in
multiple ways.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

def find_cube_sums_naive():
  d = {}
  s = 0
  while True:
    for a in range(s):
      b = s - a
      n = a * a * a + b * b * b
      if n in d:
        if (a, b) in d[n] or (b, a) in d[n]:
          break
        d[n].append((a, b))
        output = '%d' % n
        for l in d[n]:
          output += ' = %d^3 + %d^3' % (l[0], l[1])
        print output
      else:
        d[n] = [(a, b)]
    s += 1

if __name__ == '__main__':
  find_cube_sums_naive()
