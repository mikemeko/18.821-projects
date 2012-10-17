"""
Visualization for number squares simulation.
"""

__author__ = 'Justin Venezuela (jven@mit.edu)'

from Tkinter import BOTH
from Tkinter import Canvas
from Tkinter import Tk
from simulator import Simulator
import math

class Visualization(Tk):
  """
  Window displaying a pretty version of the given simulation, with the state
  shown around a circle of the given diameter. Pressing enter steps through
  the simulation and refreshes the visualization.
  """

  def __init__(self, simulator, diameter = 300, margin = 50, parent = None):
    Tk.__init__(self, parent)
    self.simulator = simulator
    self.diameter = diameter
    self.margin = margin
    self.parent = parent
    self.text_labels = []
    self.initialize()

  def initialize(self):
    """
    Setup work for UI.
    """
    self.title('Number Squares')
    # Set window size. Don't allow resizing.
    self.minsize(width = self.diameter + 2 * self.margin,
        height = self.diameter + 2 * self.margin)
    self.resizable(width = False, height = False)
    # Draw circle.
    self.canvas = Canvas(self)
    self.canvas.create_oval(self.margin, self.margin,
        self.diameter + self.margin, self.diameter + self.margin,
        outline = 'black', fill = 'white', width = 2)
    self.canvas.pack(fill = BOTH, expand = 1)
    # Bind arrow keys to step through simulation.
    self.bind('<Left>', lambda event: self.step_backward())
    self.bind('<Right>', lambda event: self.step_forward())
    # Draw initial state.
    self.draw_state()

  def draw_state(self):
    """
    Writes the numbers in the state of the simulation to the visualization.
    Does not update the simulator.
    """
    # Delete all of the old text labels.
    for text_label in self.text_labels:
      self.canvas.delete(text_label)
    self.text_labels = []
    # Make new text labels, adding them to the list.
    state = self.simulator.state
    num_points = len(state)
    for idx in range(num_points):
      text_loc = self._get_text_loc(num_points, idx)
      number = state[idx]
      text_label = self.canvas.create_text(text_loc[0], text_loc[1],
          text = str(number), font = ('Helvetica', '24'),
          fill = 'red' if number == 0 else 'blue')
      self.text_labels.append(text_label)

  def step_backward(self):
    """
    Steps the simulation backward and refreshes the UI.
    """
    self.simulator.step_backward()
    self.draw_state()

  def step_forward(self):
    """
    Steps the simulation forward and refreshes the UI.
    """
    self.simulator.step_forward()
    self.draw_state()

  def _get_text_loc(self, num_points, idx):
    """
    Returns the coordinates of point <idx> when <num_points> points are spaced
    evenly on the circumference of the circle. The first (0th) point will be
    placed north.
    """
    text_radius = (self.diameter + self.margin) * 0.5
    center = (self.margin + self.diameter / 2, self.margin + self.diameter / 2)
    angle = (2 * math.pi * idx) / num_points - (math.pi / 2)
    displacement = (text_radius * math.cos(angle),
        text_radius * math.sin(angle))
    return [int(center[i] + displacement[i]) for i in range(2)]

if __name__ == '__main__':
  s = Simulator([5, 9, 3, -6, 4])
  Visualization(s).mainloop()
