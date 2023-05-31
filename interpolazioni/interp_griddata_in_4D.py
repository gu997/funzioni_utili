import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

x = np.linspace(-1,1,100)
y =  np.linspace(-1,1,100)
z=  np.linspace(-1,1,100)
X, Y,Z = np.meshgrid(x,y,z)

def f(x, y,z):
    s = np.hypot(x, y)
    phi = np.arctan2(y, x)
    tau = s + s*(1-s)/5 * np.sin(6*phi) 
    return 5*(1-tau) + tau+z

T = f(X, Y,Z)
# Choose npts random point from the discrete domain of our model function
npts = 4000
px, py, pz = np.random.choice(x, npts), np.random.choice(y, npts), np.random.choice(z, npts)

fig, ax = plt.subplots(nrows=2, ncols=2,dpi=200)
# Plot the model function and the randomly selected sample points
ax[0,0].contourf(X[:,:,0], Y[:,:,0], T[:,:,0])
#ax[0,0].scatter(px, py, c='k', alpha=0.2, marker='.')
ax[0,0].set_title('Sample points on f(X,Y)')

# Interpolate using three different methods and plot
for i, method in enumerate(('nearest', 'linear')):
    Ti = griddata((px, py, pz), f(px,py,pz), (X, Y,Z), method=method)
    r, c = (i+1) // 2, (i+1) % 2
   
    ax[r,c].contourf(X[:,:,50], Y[:,:,50], Ti[:,:,50] )
    
    #ax[r,c].contourf(X, Y, Ti)
    ax[r,c].set_title("method = '{}'".format(method))

plt.tight_layout()
plt.show()
