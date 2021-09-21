# Uros Bojanic 2019/0077

import math
import numpy as np
from matplotlib import pyplot as plt

def BernoullisTrials(n, p, N):
	f = np.zeros(n + 1)
	for simulation in range(0, N):
		countSuccessfulTrials = 0
		for trial in range(0, n):
			if np.random.rand() < p:
				countSuccessfulTrials += 1
		f[countSuccessfulTrials] += 1
	return f / N

def BinomialDistribution(n, p):
	f = np.arange(n + 1) * 1.0
	for x in f.astype(int):
		f[x] = math.comb(n, x) * (p**(x)) * ((1-p)**(n-x))
	return f

def PlotHistogram(a, b, N):
	x = np.arange(len(a))
	fig, ax = plt.subplots()
	w = 0.4
	bar1 = ax.bar(x-w/2, a, w, align='center', alpha=0.5, label='Simulacija')
	bar2 = ax.bar(x+w/2, b, w, align='center', alpha=0.5, label='Binomna raspodela')
	ax.set_xticks(x)
	ax.set_title('Histogram (N={})'.format(N))
	ax.set_xlabel('Broj uspeha')
	ax.set_ylabel('Relativna frekvencija')
	ax.legend()
	plt.ylim([0, 0.3])
	plt.show()

def RunSimulation(n, p, N):
	# Simulate trials and binomial distribution
	relativeFreqSimulation = BernoullisTrials(n=n, p=p, N=N)
	relativeFreqTrue = BinomialDistribution(n=n, p=p)
	np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})
	print("Simulation (n={}, p={}) for {} trials:\n{}".format(n, p, N, relativeFreqSimulation))
	print("Binomial distribution (n={}, p={}) for {} trials:\n{}".format(n, p, N, relativeFreqTrue))
	# Calculate and print error
	absoluteError = np.abs(relativeFreqTrue - relativeFreqSimulation)
	print("Absolute error:\n{}".format(absoluteError))
	RMSE = math.sqrt(np.square(np.subtract(relativeFreqTrue, relativeFreqSimulation)).mean())
	print("Root Mean Square Error: {}\n\n".format(RMSE))
	# Plot histogram
	PlotHistogram(relativeFreqSimulation, relativeFreqTrue, N)

def main():
	# First simulation (100 trials)
	RunSimulation(n=12, p=0.4, N=100)
	# Second simulation (1000 trials)
	RunSimulation(n=12, p=0.4, N=1000)

if __name__=="__main__":
	main()
