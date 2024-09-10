class Point:
    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        self.name = name
        self.is_pareto = False
        self.is_excluded = False
        self.is_debatable = False
        self.nash_solution = False