import matplotlib
import numpy as np
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

class Graphics:

    def __init__(self, line_frequency, dotsize, fontsize, annotate_shift):
        self.__line_frequency = line_frequency
        self.__dotsize = dotsize
        self.__fontsize = fontsize
        self.__annotate_shift = annotate_shift

    def __draw_grid(self, graph : plt.gca, major_ticks : tuple , minor_ticks : tuple,
                    x_axis_name : str, y_axis_name : str):
        major_ticks = np.arange(*major_ticks)
        minor_ticks = np.arange(*minor_ticks)
        graph.set_xticks(major_ticks)
        graph.set_xticks(minor_ticks, minor=True)
        graph.set_yticks(major_ticks)
        graph.set_yticks(minor_ticks, minor=True)
        graph.tick_params(axis='both', which='major', labelsize=10)
        graph.tick_params(axis='both', which='minor', labelsize=10)
        graph.grid(which='both')
        plt.xlabel(f'{x_axis_name}')
        plt.ylabel(f'{y_axis_name}')

    def __draw_assymetrical_grid(self, graph: plt.gca,
                    x_major_ticks: tuple, x_minor_ticks: tuple,
                    y_major_ticks: tuple, y_minor_ticks: tuple,
                    x_axis_name: str, y_axis_name: str):
        x_major_ticks = np.arange(*x_major_ticks)
        x_minor_ticks = np.arange(*x_minor_ticks)
        y_major_ticks = np.arange(*y_major_ticks)
        y_minor_ticks = np.arange(*y_minor_ticks)
        graph.set_xticks(x_major_ticks)
        graph.set_xticks(x_minor_ticks, minor=True)
        graph.set_yticks(y_major_ticks)
        graph.set_yticks(y_minor_ticks, minor=True)
        graph.tick_params(axis='both', which='major', labelsize=10)
        graph.tick_params(axis='both', which='minor', labelsize=10)
        graph.grid(which='both')
        plt.xlabel(f'{x_axis_name}')
        plt.ylabel(f'{y_axis_name}')

    def __draw_axis(self, graph, x_range : tuple, y_range : tuple):
        graph.set_xlim(*x_range)
        graph.set_ylim(*y_range)
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

    def __draw_line(self, graph : plt.gca(), start_point : tuple, end_point : tuple,
                    style: str, width : int, color : str):
        x = np.linspace(start_point[0], end_point[0], self.__line_frequency)
        y = np.linspace(start_point[1], end_point[1], self.__line_frequency)
        graph.plot(x, y, linestyle=style, linewidth=width, color=color)

    def draw_generated_pq_points(self, points : list):
        windows_size = (10, 10)
        plt.figure(figsize=windows_size)
        pq_points_graph = plt.gca()

        self.__draw_grid(pq_points_graph, (0, 1.05, 0.05), (0, 1.05, 0.025), 'p', 'q')
        self.__draw_axis(pq_points_graph, (0, 1.05), (0, 1.05))

        for point in points:
            plt.plot(point.x, point.y, 'g.', markersize=self.__dotsize)


    def draw_pareto(self, fpq_points : list, status_quo_point : tuple):
        windows_size = (9, 9)
        plt.figure(figsize=windows_size)
        pareto_graph = plt.gca()

        max_fpqA = max(list(map(lambda point: point.x, fpq_points)))
        max_fpqB = max(list(map(lambda point: point.y, fpq_points)))
        self.__draw_assymetrical_grid(pareto_graph, (0, max_fpqA + 2, 2), (0, max_fpqA + 2, 1),
                                      (0, max_fpqB + 2, 2), (0, max_fpqB + 2, 1),'f1(p,q)','f2(p,q)')

        for point in fpq_points:
            if point.is_pareto and not point.is_debatable:
                plt.plot(point.x, point.y, 'r.', markersize=self.__dotsize)
            elif point.is_debatable and not point.nash_solution:
                plt.plot(point.x, point.y, 'b.', markersize=self.__dotsize)
            elif point.nash_solution:
                plt.plot(point.x, point.y, 'c.', markersize=self.__dotsize)
            else:
                plt.plot(point.x, point.y, 'g.', markersize=self.__dotsize)

        plt.plot(status_quo_point[0], status_quo_point[1], 'm.', markersize=self.__dotsize)

    def draw_model(self, n : int,  res : dict, avg : float, f1_static : bool):
        windows_size = (9, 9)
        plt.figure(figsize=windows_size)
        model_graph = plt.gca()

        if f1_static:
            y = "f2"
        else:
            y = "f1"

        max_fpq = round(max(list(res.values())),1)
        min_fpq = round(min(list(res.values())),1)

        for el in res:
            plt.plot(el, res[el], 'k.', markersize=self.__dotsize)

        nums = list(res.keys())
        values = list(res.values())

        for i in range(1,len(nums),1):
            self.__draw_line(model_graph,(i-1,values[i-1]),(i,values[i]),'-',2,'black')

        self.__draw_line(model_graph, (0,avg), (n,avg), '-', 2, 'blue')

        self.__draw_assymetrical_grid(model_graph, (0, n + 2, 100), (0, n + 2, 50),
                                      (min_fpq-0.1, max_fpq + 0.1, 0.2), (min_fpq-0.1, max_fpq + 0.1 , 0.1),"Номер партии",y)




