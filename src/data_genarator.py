import argparse

import data_manager

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output_name')
    parser.add_argument('theta0', type=float)
    parser.add_argument('theta1', type=float)
    parser.add_argument('--x_min', default=0.0, type=float)
    parser.add_argument('--x_max', default=100.0, type=float)
    parser.add_argument('--sigma', default=10.0, type=float)
    parser.add_argument('--num', default=20, type=int)
    parser.add_argument('--seed', default=42, type=int)

    args = parser.parse_args()

    print(args)

    data = data_manager.DataManager()
    data.genarate_data(args.theta0, args.theta1, args.x_min, args.x_max, args.sigma, args.num, args.seed)
    data.to_csv(args.output_name)
