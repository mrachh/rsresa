from numpy import *
from pylab import *
x = loadtxt('fort.37')
y = loadtxt('fort.38')
figure(1)
plot(x[:,0],x[:,1],'kx')
plot(y[:,0],y[:,1],'k.')
show()
