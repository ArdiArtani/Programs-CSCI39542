"""
Name: Ardi Artani
Email: ARDI.ARTANI96@myhunter.cuny.edu
Resources: textbook.ds100.org, datatechnotes.com/2019/10/accuracy-check-in-python-mae-mse-rmse-r.html
"""
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def mse_loss(theta, y_vals):
    return np.mean((y_vals - theta) ** 2)

def mae_loss(theta, y_vals):
    return np.mean(abs(y_vals - theta))

# thetas: estimates for the population parameter for the percent tips in values, and
# tips: the tips observed, assumed to be a positive percentage, ranging from 0 to 100.
# For each theta in thetas, it should compute the mean squared error between theta and tips. Return an iterable of the values computed.
def mse_estimates(thetas,tips):
    values_ = []
    i = 0
    for theta_ in thetas:
        value_ = mse_loss(theta_, tips[i])
        values_.append(value_)
        i += 1
    return values_


# thetas: estimates for the population parameter for the percent tips in values, and
# tips: the tips observed, assumed to be a positive percentage, ranging from 0 to 100.
# For each theta in thetas, it should compute the mean absolute error between theta and tips. Return an iterable of the values computed.
# Note: for each of these functions, your returned value will be an iterable with the same length as thetas.
def mae_estimates(thetas,tips):
    values_ = []
    i = 0
    for theta_ in thetas:
        value_ = mae_loss(theta_, tips[i])
        values_.append(value_)
        i += 1
    return values_


thetas = np.array([12, 13, 14, 15, 16])
y_vals = np.array([12.1, 12.8, 14.9, 16.3, 17.2, 18.0])
mse_losses = mse_estimates(thetas,y_vals)
abs_losses = mae_estimates(thetas,y_vals)
plt.scatter(thetas, mse_losses, label='MSE')
plt.scatter(thetas, abs_losses, label='MAE')
plt.title(r'Loss vs. $ \theta $ when $ \bf{y}$$= [ 12.1, 12.8, 14.9, 16.3, 17.2 ] $')
plt.xlabel(r'$ \theta $ Values')
plt.ylabel('Loss')
plt.legend()
plt.show()
