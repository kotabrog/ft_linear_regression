import pickle


class LinearRegression:
    def __init__(self, theta0=0, theta1=0, learning_rate=1):
        self.theta0 = theta0
        self.theta1 = theta1
        self.learning_rate = learning_rate
        print(learning_rate)


    def predict(self, mileage):
        return self.theta0 + (self.theta1 * mileage)


    def _train_one(self, x, y):
        self.theta0, self.theta1 = (self.theta0 - self.learning_rate * (sum([self.predict(mileage) for mileage in x]) - sum(y)) / len(x),
                                    self.theta1 - self.learning_rate * sum([(self.predict(mileage) - price) * mileage for mileage, price in zip(x, y)]) / len(x))


    def train(self, x, y, epoch=1, verbose=False):
        if len(x) != len(y):
            raise RuntimeError("len(x) != len(y)")
        if len(x) == 0:
            raise RuntimeError("len(x) == 0")
        if epoch < 1:
            raise RuntimeError("epoch < 1")
        max_x = max(x)
        max_y = max(y)
        max_value = max(max_x, max_y)

        norm_x = x / max_value
        norm_y = y / max_value

        for i in range(epoch):
            self._train_one(norm_x, norm_y)
            if verbose:
                print("{}/{}: theta0:".format(i, epoch), self.theta0, "theta1:", self.theta1)

        self.theta0 *= max_value


    def dump(self, file='data.pickle'):
        l = [self.theta0, self.theta1]
        with open(file, 'wb') as p:
            pickle.dump(l, p)


    def load(self, file='data.pickle'):
        with open(file, mode='rb') as f:
            s = pickle.load(f)
            self.theta0, self.theta1 = s
