import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import linear_regression

if __name__ == '__main__':
    data = pd.read_csv('../data.csv')
    print(data)

    x = data.km
    y = data.price
    print(x)
    print(y)

    x_min, x_max = min(x), max(x)
    print(x_min, x_max)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.xlabel("km")
    plt.ylabel("price")
    ax.scatter(x, y, s=100, c='r', alpha=0.3)

    model = linear_regression.LinearRegression(learning_rate=1e-1)
    # model.load('data.pickle')

    # model.train(x, y, epoch=1, verbose=True)

    # x_l = np.linspace(x_min, x_max, 100)
    # plt.plot(x_l, model.predict(x_l), 'b:')

    model.train(x, y, epoch=1000, verbose=True)

    x_l = np.linspace(x_min, x_max, 100)
    plt.plot(x_l, model.predict(x_l), 'r:', label="my model")

    # model.train(x, y, epoch=100)

    # x_l = np.linspace(x_min, x_max, 100)
    # plt.plot(x_l, model.predict(x_l), 'g:')

    k = np.polyfit(x, y, 1)
    print(k)

    x_l = np.linspace(x_min, x_max, 100)
    plt.plot(x_l, k[1] + k[0] * x_l, 'g:', label="polyfit")

    plt.legend()
    plt.show()
