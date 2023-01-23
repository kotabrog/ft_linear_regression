import argparse

import linear_regression

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mileage', type=float)
    parser.add_argument('--file_name')
    parser.add_argument('--theta0', type=float)
    parser.add_argument('--theta1', type=float)

    args = parser.parse_args() 

    model = linear_regression.LinearRegression()

    if args.file_name is not None:
        model.load(args.file_name)
    else:
        if args.theta0 is not None:
            model.theta0 = args.theta0
        if args.theta1 is not None:
            model.theta1 = args.theta1

    print('mileage:', args.mileage, 'predict:', model.predict(args.mileage), 'theta0', model.theta0, 'theta1', model.theta1)
