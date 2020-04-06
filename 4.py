from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [0,10,26,30,35,60]
y = [3,3,3,5,3,3]
width = [0.5,20,20,8,50,0.4]
plt.bar(x, y,width, align='center')
plt.ylabel('change in refractive index')
plt.xlabel('radial distance')
plt.title('STEP INDEX FIBRE 1')
plt.show()
print("Core Diameter= 8μm")
print("Cladding Diameter =60μm")
x2 = [0,10,20,30,35,40,50,60,70]
y2 = [3,3,3,3,5,3,3,3,3]
width = [0.5,20,10,10,10,10,10,20,0.5]
plt.bar(x2, y2,width,color='g',align='center')
plt.ylabel('change in refractive index')
plt.xlabel('radial distance')
plt.title('STEP INDEX FIBRE 2')
plt.show()
print("Core Diameter= 10μm")
print("Cladding Diameter =70μm")
import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
x = [0,10,15,20,25]
y = [0,0,0,0,0]
x2 = [75,85,90,95,100]
y2 = [0,0,0,0,0]
plt.plot(x,y,color='g')
plt.plot(x2,y2,color='g')
x = np.array([25,40,50,60,75 ])
y = np.array([0,2,2.5,2,0])
t, c, k = interpolate.splrep(x, y, s=0, k=4)
N = 100
xmin, xmax = x.min(), x.max()
xx = np.linspace(xmin, xmax, N)
spline = interpolate.BSpline(t, c, k, extrapolate=False)
plt.plot(xx, spline(xx), 'r')
plt.title('GRADED INDEX FIBRE 1')
plt.ylabel('change in refractive index')
plt.xlabel('radial distance')
plt.show()
print("Core Diameter= 50μm")
print("Cladding Diameter =100μm")
x = [0,10,15,20,25]
y = [0,0,0,0,0]
x2 = [225,235,240,245,250]
y2 = [0,0,0,0,0]
plt.plot(x,y,color='b')
plt.plot(x2,y2,color='b')
x = np.array([25,65,125,185,225])
y = np.array([0,2.5,5,2.5,0])
t, c, k = interpolate.splrep(x, y, s=0, k=4)
N = 100
xmin, xmax = x.min(), x.max()
xx = np.linspace(xmin, xmax, N)
spline = interpolate.BSpline(t, c, k, extrapolate=False)
plt.plot(xx, spline(xx), 'g')
plt.title('GRADED INDEX FIBRE 2')
plt.ylabel('change in refractive index')
plt.xlabel('radial distance')
plt.show()
print("Core Diameter= 200μm")
print("Cladding Diameter =250μm")