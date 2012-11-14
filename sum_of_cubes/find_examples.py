"""
Finds examples of numbers n that can be expressed as the sum of two cubes in
multiple ways.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

def gcd(a, b):
  """
  Returns gcd of a, b.
  """
  assert a >= 0 and b >= 0, 'Inputs must be non-negative.'
  a, b = max(a, b), min(a, b)
  while b > 0:
    a, b = b, a % b
  return a

def find_two_cube_sums(relatively_prime = True, count = -1,
    verbose = True):
  """
  Prints numbers that can be expressed as the sum of cubes in at least two
  ways. If relatively_prime, the sum must be cube-free. If count is >= 0,
  function returns sums after count sums are found.
  """
  d = {}
  s = 0
  num_sums = 0
  ans = []
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
        if verbose:
          print output
        if count >= 0 and n not in ans:
          ans.append(n)
          num_sums += 1
          if num_sums >= count:
            return ans
      else:
        d[n] = [(a, b)]
    s += 1

def find_multiple_cube_sums():
  """
  Prints numbers that can be expressed as the sum of two cubes in many
  different ways, as well as the number of such representations.
  """
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

def show_two_cube_sum_histogram(num_sums, relatively_prime = True):
  cube_sums = find_two_cube_sums(relatively_prime = relatively_prime,
      count = num_sums, verbose = False)
  log_to_num = [0 for k in range(len(str(max(cube_sums))))]
  for n in cube_sums:
    l = len(str(n))
    for ll in range(l, len(log_to_num)):
      log_to_num[ll] = log_to_num[ll] + 1
  print make_histogram(log_to_num)

def make_histogram(log_to_num):
  h1 = '10^k'
  h2 = 'Cube sums <= 10^k'
  output = '%s | %s\n' % (' ' * (len(h1) + 1), ' ' * (len(h2) + 1))
  output += ' %s | %s \n' % (h1, h2)
  output += '_%s_|_%s_\n' % ('_' * len(h1), '_' * len(h2))
  for l in range(1, len(log_to_num)):
    output += ' %s | %s \n' % (str(l).center(len(h1)),
        str(log_to_num[l]).center(len(h2)))
  return output

if __name__ == '__main__':
  #find_two_cube_sums()
  #find_multiple_cube_sums()
  show_two_cube_sum_histogram(num_sums = 1000)
