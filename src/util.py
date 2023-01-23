import numpy as np


def root_mean_squared_error(y, y_pred):
    if len(y_pred) != len(y):
        raise RuntimeError("len(y_pred) != len(y)")
    if len(y) == 0:
        raise RuntimeError("len(y) == 0")
    return np.sqrt(np.mean((np.array(y) - np.array(y_pred)) ** 2))


if __name__ == '__main__':
    y = [1, 2, 3, 4]
    y_pred = [1, 2, 3, 4]
    print(y, y_pred, root_mean_squared_error(y, y_pred))

    y = [1, 2, 3, 4]
    y_pred = [2, 1, 4, 5]
    print(y, y_pred, root_mean_squared_error(y, y_pred))
