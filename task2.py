import random
import numpy as np
from point import Point
from prettytable import PrettyTable
from sympy import diff, symbols

class Task2:

    def __init__(self,num_of_random_pq_points, A : list, B : list, status_quo_point : tuple):
        self.A = A
        self.B = B
        self.num_of_random_pq_points = num_of_random_pq_points
        self.pq_points = []
        self.fpq_points = []
        self.pareto_points = []
        self.debatable_points = []
        self.nash_max = None
        self.status_quo_point = status_quo_point

    def gen_random_pq_points(self):
        for i in range(self.num_of_random_pq_points):
            point = Point(random.random(), random.random(), i)
            self.pq_points.append(point)

    def __calculate_fpq(self, p : float, q : float, coefs : list):
        fpq = coefs[0] * p * q + coefs[1] * q + coefs[2] * p + coefs[3]
        return fpq

    def get_fpq_points(self, coefs1 : list, coefs2 : list):
        for point in self.pq_points:
            fpqA = self.__calculate_fpq(point.x, point.y, coefs1)
            fpqB = self.__calculate_fpq(point.x, point.y, coefs2)
            fpq_point = Point(fpqA,fpqB,point.name)
            self.fpq_points.append(fpq_point)

    def get_pareto_points(self):
        for point in self.fpq_points:
            for point1 in self.fpq_points:
                if (point.x >= point1.x and point.y >= point1.y) and not \
                    (point.x == point1.x and point.y == point1.y):
                    point1.is_excluded = True

        for point in self.fpq_points:
            if not point.is_excluded:
                point.is_pareto = True
                self.pareto_points.append(point)

    def get_debatable_point(self):
        for point in self.pareto_points:
            if (point.x >= self.status_quo_point[0] and point.y > self.status_quo_point[1])\
                    or (point.x > self.status_quo_point[0] and point.y >= self.status_quo_point[1]):
                point.is_debatable = True
                self.debatable_points.append(point)

    def get_nash_max(self):
        nash_values = {}
        for point in self.debatable_points:
            nash_value = (point.x - self.status_quo_point[0]) * (point.y - self.status_quo_point[1])
            nash_values.update({point:nash_value})
        nash_solution_point = max(nash_values,key=lambda x: nash_values[x])
        nash_solution_point.nash_solution = True
        self.nash_max = nash_solution_point


    def show_pareto(self):
        print("Парето-оптимальное множество:")
        pareto_table = PrettyTable()
        pareto_table.field_names = ["№", "f1(p,q)", "f2(p,q)"]
        for point in self.pareto_points:
            pareto_table.add_row([point.name + 1, point.x, point.y])
        print(pareto_table)

    def show_debatable(self):
        print("Переговорное множество:")
        debatable_table = PrettyTable()
        debatable_table.field_names = ["№", "f1(p,q)", "f2(p,q)"]
        for point in self.debatable_points:
            debatable_table.add_row([point.name + 1, point.x, point.y])
        print(debatable_table)

    def show_nash_max(self):
        print(f'Точка с максимальным значением функции Нэша: ({self.nash_max.x},{self.nash_max.y})')
        print()

