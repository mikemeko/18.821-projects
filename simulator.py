'''
Simulation for the following game:
  - Start with a state of n integers.
  - At each iteration, advance the state as follows:
      state[t+1][i] = abs(state[t][i] - state[t][i+1 % n])
  - Stop if a state of all 0's is reached.
'''

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

class Simulator:
  def __init__(self, start):
    self.state = start
    self.n = len(start)
    self.indices = range(self.n)
  def step(self):
    '''
    Advance the state by one step.
    '''
    self.state = tuple(
      abs(self.state[i] - self.state[(i+1) % self.n]) for i in self.indices)
  def done(self):
    '''
    Returns True if the state is all 0's,
    False otherwise.
    '''
    return not any(self.state)
  def terminates(self):
    '''
    Returns True if the simulation eventually terminates,
    False otherwise.
    TODO(jven): This method should be idempotent.
    '''
    visited = set()
    # This loop is guaranteed to terminate: it is impossible to loop
    # indefinitely without repeating.
    while not self.done():
      self.step()
      if self.state in visited:
        return False
      visited.add(self.state)
    return True
  def __str__(self):
    return str(self.state)

if __name__ == '__main__':
  # interesting case: one value (x) followed by n-1 0's
  x = 1
  for n in xrange(50):
    print '%d: %s' % (n, 'WIN' if Simulator([x] + [0] * (n - 1)).terminates()
        else 'LOSE')
