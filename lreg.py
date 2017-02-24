# Linear regression

from datagen import labels,data_x,data_y

def functiongen():
	# Find y' i.e. mean of y
	ymean=sum(data_y)/float(len(data_y))

	# Find x' i.e. mean of x
	xmean=sum(data_x)/float(len(data_x))

	sigma_xy=0
	sigma_xx=0
	# For every value in x and y compute sigma_xy and sigma_xx
	for i in range(len(data_x)):
		x_t=data_x[i]-xmean
		y_t=data_y[i]-ymean

		sigma_xx+=pow(x_t,2)

		sigma_xy+=(x_t*y_t)

	return xmean,ymean,sigma_xy,sigma_xx

print 'Enter value of Heat Flux:'
x=input()

xmean,ymean,sigma_xy,sigma_xx=functiongen()

result=ymean+((sigma_xy/sigma_xx)*(x-xmean))

print '\n','The skin temperature is : ',result