import argparse
import csv

import linear_regression

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('data_name')
    parser.add_argument('--output_name')
    parser.add_argument('--learning_rate', type=float)
    parser.add_argument('--epoch', type=int)
    parser.add_argument('--verbose', action='store_true')

    args = parser.parse_args() 

    if args.learning_rate is None:
        model = linear_regression.LinearRegression()
    else:
        model = linear_regression.LinearRegression(args.learning_rate)

    with open(args.data_name) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        l_T = [list(x) for x in zip(*l)]
        x, y = l_T
        x = [float(data) for data in x[1:]]
        y = [float(data) for data in y[1:]]
        print(x, y)

    epoch = 1 if args.epoch is None else args.epoch
    model.train(x, y, epoch=epoch, verbose=args.verbose)

    if args.output_name is not None:
        model.dump(args.output_name)
    else:
        model.dump()
