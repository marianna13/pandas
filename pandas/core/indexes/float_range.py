class float_range:
    '''
    Modified Python built-in function range that accepts floats as arguments.

    Parameters
    ----------
    start : float (default: 0)
        If "stop" is not given, interpreted as "stop" instead.
    stop : float (default: 0)
    step : float (default: 1)

    Attributes
    ----------
    start
    stop
    step
    current
    '''
    def __init__(self, start=0, stop=0, step=1):
      if start and not stop:
        stop, start = start, 0
      self.start = start
      self.current = start - step
      self.stop = stop
      self.step = step
    
    def __iter__(self):
      return self
    
    def __next__(self):
      self.current += self.step
      if self.current < self.stop:
        return self.current
      raise StopIteration