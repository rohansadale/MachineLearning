import sys
import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

def main():
	if len(sys.argv) < 1:
		print 'Please enter filename'
	filename = 'data/' + sys.argv[1]
	data = np.loadtxt(filename, delimiter=",")
	median = np.median(data, axis=0)[-1]
	print median
	print data.shape
	data[data[:, -1] < median, -1] = 0
	data[data[:, -1] >= median, -1] = 1
	print data[data[0:5, -1] == 1] 
	np.savetxt(filename+'_new', data, fmt='%5.2f', delimiter=',')

if __name__ == '__main__':
	main()
