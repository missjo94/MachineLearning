import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import sqrt



# Calculate root mean squared error
def rmse_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
    mean_error = sum_error / float(len(actual))
    return sqrt(mean_error)

# Evaluate regression algorithm on training dataset
def evaluate_algorithm(dataset, algorithm):
    test_set = list()
    for row in dataset:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)
    predicted = algorithm(dataset, test_set)
    actual = [row[-1] for row in dataset]
    rmse = rmse_metric(actual, predicted)
    return rmse

# Calculate the mean value of a list of numbers
def mean(values):
    return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

# Calculate the variance of a list of numbers
def variance(values, mean):
    return sum([(x-mean)**2 for x in values])

# Calculate coefficients
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]

# Simple linear regression algorithm
def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test:
        yhat = b0  + b1 * row[0] + row[0]**2 #parabola
        predictions.append(yhat)
    return predictions

def main(argv):
	#Read file
	fileName = argv[1]
	header = ['X','Y']
	data = pd.read_csv(fileName, names=header, header = 1)

	x = data['X']
	y = data['Y']
	plt.plot(x,y,'*')
	plt.show()

	dataset = []
	for xi,yi in zip(x,y):
		dataset.append([xi,yi])
		
	rmse = evaluate_algorithm(dataset, simple_linear_regression)
	print('RMSE: %.3f' % (rmse))

if __name__ == "__main__":
	main(sys.argv)        #python zadatak1.py "ships.csv"
	



