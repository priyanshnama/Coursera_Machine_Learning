import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.metrics import r2_score


class PolyAlgorithm:

    def __init__(self, deg):
        self = PolynomialFeatures(degree=deg)
        train_x_poly = self.fit_transform(train_x)
        clf = linear_model.LinearRegression()
        clf.fit(train_x_poly, train_y)
        print('Coefficients: ', clf.coef_)
        print('Intercept: ', clf.intercept_)
        plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
        xx = np.arange(0.0, 10.0, 0.1)
        yy = clf.intercept_[0] + clf.coef_[0][1] * xx + clf.coef_[0][2] * np.power(xx, 2)
        plt.plot(xx, yy, '-r')
        plt.xlabel("Engine size")
        plt.ylabel("Emission")
        test_x_poly = self.fit_transform(test_x)
        test_y_ = clf.predict(test_x_poly)
        print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
        print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
        print("R2-score: %.2f" % r2_score(test_y_, test_y))
        plt.show()


df = pd.read_csv("../data resources/FuelConsumption.csv")
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
ploy2 = PolyAlgorithm(2)
