import argparse

import numpy as np
import matplotlib.pyplot as plt

import linear_regression
import data_manager
import util

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('data_name')
    parser.add_argument('--output_name')
    parser.add_argument('--learning_rate', type=float)
    parser.add_argument('--epoch', type=int)
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--plot', action='store_true')
    parser.add_argument('--polyfit', action='store_true')
    parser.add_argument('--precision', action='store_true')

    args = parser.parse_args() 

    if args.learning_rate is None:
        model = linear_regression.LinearRegression()
    else:
        model = linear_regression.LinearRegression(learning_rate=args.learning_rate)

    data = data_manager.DataManager()
    data.read_csv(args.data_name)

    x = data.data.km
    y = data.data.price

    epoch = 1000 if args.epoch is None else args.epoch
    model.train(x, y, epoch=epoch, verbose=args.verbose)

    if args.output_name is not None:
        model.dump(args.output_name)
    else:
        model.dump()

    print('my model: theta0', model.theta0, 'theta1', model.theta1)

    np_theta = None

    if args.polyfit:
        np_theta = np.polyfit(x, y, 1)
        print('np.polyfit: theta0', np_theta[1], 'theta1', np_theta[0])

    if args.precision:
        print('my model RMSE:', util.root_mean_squared_error(y, model.predict(np.array(y))))

        if args.polyfit:
            print('np.polyfit RMSE:', util.root_mean_squared_error(y, np_theta[1] + np_theta[0] * np.array(y)))

    if args.plot:
        x_min, x_max = min(x), max(x)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.xlabel("km")
        plt.ylabel("price")
        ax.scatter(x, y, s=100, c='r', alpha=0.3)

        x_l = np.linspace(x_min, x_max, 100)
        plt.plot(x_l, model.predict(x_l), 'r-', label="my model")

        if args.polyfit:
            plt.plot(x_l, np_theta[1] + np_theta[0] * x_l, 'g:', label="polyfit")

        plt.legend()
        plt.show()
