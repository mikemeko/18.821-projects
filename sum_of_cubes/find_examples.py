"""
Finds examples of numbers n that can be expressed as the sum of two cubes in
multiple ways.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

def gcd(a, b):
  assert a >= 0 and b >= 0, 'Inputs must be non-negative.'
  a, b = max(a, b), min(a, b)
  while b > 0:
    a, b = b, a % b
  return a

def find_cube_sums_naive(relatively_prime = False):
  d = {}
  s = 0
  while True:
    for a in range(s / 2 + 1):
      b = s - a
      if relatively_prime and gcd(a, b) > 1:
        continue
      n = a * a * a + b * b * b
      if n in d:
        d[n].append((a, b))
        output = '%d' % n
        for l in d[n]:
          output += ' = %d^3 + %d^3' % (l[0], l[1])
        print output
      else:
        d[n] = [(a, b)]
    s += 1

def find_multiple_cube_sums_naive():
  d = {}
  s = 0
  m = 2
  while True:
    for a in range(s / 2):
      b = s - a
      n = a * a * a + b * b * b
      if n in d:
        d[n].append((a, b))
        if len(d[n]) >= m:
          output = '%d expressions: %d' % (len(d[n]), n)
          for l in d[n]:
            output += ' = %d^3 + %d^3' % (l[0], l[1])
          print output
          m = len(d[n]) + 1
      else:
        d[n] = [(a, b)]
    s += 1

if __name__ == '__main__':
  find_cube_sums_naive(relatively_prime = True)
  #find_multiple_cube_sums_naive()
