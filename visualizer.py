import io
from typing import TextIO, Tuple

import numpy as np
from matplotlib import pyplot as plt

import profit_functions
import vector
from profit_functions import ProfitFunction
from vector import Vector

Domain = (Vector, Vector)


class Visualization:
    def __init__(self, profit_function: ProfitFunction, domain: Domain, iterations: list[list[Vector]]):
        self.profit_function = profit_function
        self.domain = domain
        self.iterations = iterations


class Visualizer:
    @staticmethod
    def visualize(visualization: Visualization):
        for i, iteration in enumerate(visualization.iterations):
            plt.figure(i)
            ax = plt.subplot()
            ax.set_title("Iteration {}".format(i + 1))

            for point in iteration:
                ax.scatter(*point, color="red")

            Visualizer._plot_heightmap_2d(visualization.domain, visualization.profit_function)
            plt.colorbar()

        plt.show()

    @staticmethod
    def _plot_heightmap_2d(domain: (Vector, Vector), profit_fun: ProfitFunction, cmap="viridis"):
        axes = [np.linspace(edge[0], edge[1], 100) for edge in zip(*domain)]
        meshgrid = np.meshgrid(*axes)

        # noinspection PyTypeChecker
        heightmap = profit_fun(Vector(meshgrid))
        extent: Tuple = sum(zip(*domain), ())

        # noinspection PyTypeChecker
        plt.imshow(heightmap, extent=extent, norm='log', cmap=cmap)


def load(input_io: TextIO) -> Visualization:
    profit_function_name = input_io.readline().strip()
    domain_lower_bound = vector.loads(input_io.readline().strip())
    domain_upper_bound = vector.loads(input_io.readline().strip())

    number_of_iterations = int(input_io.readline())
    iterations = list[list[Vector]]()

    for i in range(number_of_iterations):
        number_of_points = int(input_io.readline())
        points = list[Vector]()

        for j in range(number_of_points):
            point_txt = input_io.readline().strip()
            points.append(vector.loads(point_txt))

        iterations.append(points)

    profit_function = profit_functions.loads(profit_function_name)
    domain = (domain_lower_bound, domain_upper_bound)

    return Visualization(profit_function, domain, iterations)


def loads(input_txt: str) -> Visualization:
    return load(io.StringIO(input_txt))
