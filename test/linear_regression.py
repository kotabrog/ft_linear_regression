import pickle


class LinearRegression:
    def __init__(self, theta0=0, theta1=0, learning_rate=1e-3):
        self.theta0 = theta0
        self.theta1 = theta1
        self.learning_rate = learning_rate

    def predict(self, mileage):
        return self.theta0 + (self.theta1 * mileage)

    def _train_one(self, x, y):
        # xとyのサイズのerror処理.
        # x, yがサイズ0のときのerror処理
        # self.theta0, self.theta1 = (self.theta0 - self.learning_rate * (sum([self.predict(mileage) for mileage in x]) - sum(y)) / len(x),
        #                             self.theta1 - self.learning_rate * sum([(self.predict(mileage) - price) * mileage for mileage, price in zip(x, y)]) / len(x))
        self.theta0, self.theta1 = (self.learning_rate * (sum([self.predict(mileage) for mileage in x]) - sum(y)) / len(x),
                                    self.learning_rate * sum([(self.predict(mileage) - price) * mileage for mileage, price in zip(x, y)]) / len(x))

    def train(self, x, y, epoch=1, verbose=False):
        # x, y, epochのerror処理
        for i in range(epoch):
            self._train_one(x, y)
            if verbose:
                print("{}/{}: theta0:".format(i, epoch), self.theta0, "theta1:", self.theta1)


    def dump(self, file='data.pickle'):
        l = [self.theta0, self.theta1]
        with open(file, 'wb') as p:
            pickle.dump(l, p)

    def load(self, file='data.pickle'):
        with open(file, mode='rb') as f:
            s = pickle.load(f)
            # error処理
            self.theta0, self.theta1 = s
