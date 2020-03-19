import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


def sigmoid(x, beta_1, beta_2):
    y = 1 / (1 + np.exp(-beta_1 * (x - beta_2)))
    return y


x = np.arange(-5.0, 5.0, 0.1)
df = pd.read_csv("../data resources/china_gdp.csv")
plt.figure(figsize=(8, 5))
x_data, y_data = (df["Year"].values, df["Value"].values)
y = 1.0 / (1.0 + np.exp(-x))
beta_1 = 0.10
beta_2 = 1990.0
Y_pred = sigmoid(x_data, beta_1, beta_2)
plt.plot(x_data, Y_pred * 15000000000000.)
plt.plot(x_data, y_data, 'ro')
xdata = x_data / max(x_data)
ydata = y_data / max(y_data)
popt, pcov = curve_fit(sigmoid, xdata, ydata)
print(" beta_1 = %f, beta_2 = %f" % (popt[0], popt[1]))
x = np.linspace(1960, 2015, 55)
x = x / max(x)
plt.figure(figsize=(8, 5))
y = sigmoid(x, *popt)
plt.plot(xdata, ydata, 'ro', label='data')
plt.plot(x, y, linewidth=3.0, label='fit')
plt.legend(loc='best')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()
msk = np.random.rand(len(df)) < 0.8
train_x = xdata[msk]
test_x = xdata[~msk]
train_y = ydata[msk]
test_y = ydata[~msk]
popt, pcov = curve_fit(sigmoid, train_x, train_y)
y_hat = sigmoid(test_x, *popt)
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_hat - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((y_hat - test_y) ** 2))
print("R2-score: %.2f" % r2_score(y_hat, test_y))
