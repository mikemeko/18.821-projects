import math
import random
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
    # history is a stack, where the head is the current state
    self.history = [start]

  def step_backward(self):
    '''
    Go back to the previous state if there is one. Does nothing otherwise.
    '''
    if len(self.history) > 1:
      self.history.pop()
      self.state = self.history[-1]

  def step_forward(self):
    '''
    Advance the state by one step if the simulation is not done. Does nothing
    otherwise.
    '''
    if not self.done():
      self.state = tuple(
        abs(self.state[i] - self.state[(i+1) % self.n]) for i in self.indices)
      self.history.append(self.state)

  def done(self):
    '''
    Returns True if the state is all 0's,
    False otherwise.
    '''
    return not any(self.state)

  def get_game_length(self):
    '''
    Returns the number of steps until the simulation terminates, or None
    if the simulation does not terminate.
    '''
    return self._save_state(self._run)

  def is_key_order(self):
      if len(self.state) != 4:
          return False
      theState = self.state
      a = theState[0]
      b = theState[1]
      c = theState[2]
      d = theState[3]
      if (a <= d and d <= b and b <= c) or (d <= b and b <= c and c <= a) or (b <= c and c <= a and a <= d) or (c <= a and a <= d and d <= b)\
      or (a <= c and c <= b and b <= d) or (c <= b and b <= d and d <= a) or (b <= d and d <= a and a <= c) or (d <= a and a <= c and c <= b):
        return True
      
  
  def _run(self, sayIfClose = False):
    visited = set()
    # This loop is guaranteed to terminate: it is impossible to loop
    # indefinitely without repeating.
    num_steps = 0
    print self.state
    if self.is_key_order() and sayIfClose:
      print 'Almost There'
    while not self.done():
      if self.is_key_order() and sayIfClose:
          print 'Almost There'
      self.step_forward()
      print self.state
      num_steps += 1
      if self.state in visited:
        return None
      visited.add(self.state)
    return num_steps

  def _save_state(self, f, *args, **kwargs):
    '''
    Returns the result of calling the function |f|, but ensures that the state
    of this simulator before the function call is preserved.
    '''
    current_state = self.state
    current_history = self.history[:]
    out = f(*args, **kwargs)
    self.state = current_state
    self.history = current_history
    return out  

  def __str__(self):
    return str(self.state)

if __name__ == '__main__':
  # interesting case: one value (x) followed by n-1 0's
  w = .0419471094
  x = .1513124413
  y = .2432144123
  z = .3123524232
  
  #Simulator([random.random() for i in range(5)])._run(False)
  #Simulator([random.randint(0,1000) for i in range(3)])._run(False)
  Simulator((.43, .21, .122, .131))._run()
  x = 1
#  for n in xrange(50):
#    print '%d: %s' % (n, 'WIN' if
#        Simulator([x] + [0] * (n - 1)).get_game_length() != None else 'LOSE')
