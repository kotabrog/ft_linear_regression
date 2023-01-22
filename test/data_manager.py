import pandas as pd
import numpy as np
import random


class DataManager:
    def __init__(self):
        self.data = None

    def read_csv(self, file_path):
        self.data = pd.read_csv(file_path)

    def genarate_data(self, theta0, theta1, x_min, x_max, sigma=10.0, num=10, seed=42):
        random.seed(seed)
        x = [random.uniform(x_min, x_max) for _ in range(num)]
        y = [theta0 + (theta1 * a) + random.gauss(mu=0.0, sigma=sigma) for a in x]
        self.data = pd.DataFrame({'km': x, 'price': y})

    def to_csv(self, output_path):
        if self.data is not None:
            self.data.to_csv(output_path, index=False)


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    data_manager = DataManager()
    data_manager.genarate_data(3, -2, -10, 10, sigma=1.0, num=20)

    print(data_manager.data)

    x = data_manager.data.km
    y = data_manager.data.price
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlabel("km")
    plt.ylabel("price")
    ax.scatter(x, y, s=100, c='r', alpha=0.3)
    plt.show()

    data_manager.to_csv('test.csv')

    data_manager.read_csv('test.csv')

    print(data_manager.data)
