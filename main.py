import visualizer
from visualizer import Visualizer


def main():
    with open("input.txt") as f:
        visualization = visualizer.load(f)

    Visualizer.visualize(visualization)


if __name__ == "__main__":
    main()
