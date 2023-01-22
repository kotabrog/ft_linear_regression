import argparse

import linear_regression

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mileage', type=float)
    parser.add_argument('--file_name')

    args = parser.parse_args() 

    model = linear_regression.LinearRegression()

    if args.file_name is not None:
        model.load(args.file_name)

    print('mileage:', args.mileage, 'predict:', model.predict(args.mileage), 'theta0', model.theta0, 'theta1', model.theta1)
