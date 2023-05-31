import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import LinearNDInterpolator,NearestNDInterpolator
import timeit


x = np.linspace(-1,1,100)
y =  np.linspace(-1,1,100)
z=  np.linspace(-1,1,100)
X, Y,Z = np.meshgrid(x,y,z)

def f(x, y,z):
    s = np.hypot(x, y)
    phi = np.arctan2(y, x)
    tau = s + s*(1-s)/5 * np.sin(6*phi) 
    return 5*(1-tau) + tau

T = f(X, Y,Z)
# Choose npts random point from the discrete domain of our model function
npts = 27000
px, py, pz = np.random.choice(x, npts), np.random.choice(y, npts), np.random.choice(z, npts)





tic = timeit.default_timer()

interp = LinearNDInterpolator(list(zip(px, py, pz)), f(px,py,pz))

toc = timeit.default_timer()
print('Took {0:g} seconds to carry out the evaluations of interpolation generation'.format(toc-tic))

#Ti = interp(X, Y,Z)

# =============================================================================
# fig, ax = plt.subplots(dpi=200)
# ax.contourf(X[:,:,50], Y[:,:,50], Ti[:,:,50] )
# ax.set_title('LinearNDInterpolator')
# plt.show()
# =============================================================================




'Da qui salvo la funzione interp'


try:
    import cPickle as pickle
except ImportError:
    import pickle
    

tic = timeit.default_timer()
#Pickle, unpickle and then plot again
with open('interpolator.pkl', 'wb') as f:
    pickle.dump(interp, f)
    
toc = timeit.default_timer()
print('Took {0:g} seconds to carry out the upload'.format(toc-tic))
   
    
tic = timeit.default_timer()    

with open('interpolator.pkl', 'rb') as f:
    interp_loaded = pickle.load(f)

toc = timeit.default_timer()
print('Took {0:g} seconds to carry out the download'.format(toc-tic))


#Ti = interp_loaded(X, Y,Z)

# =============================================================================
# fig, ax = plt.subplots(dpi=200)
# ax.contourf(X[:,:,50], Y[:,:,50], Ti[:,:,50] )
# ax.set_title('LinearNDInterpolator loaded')
# plt.show()
# =============================================================================





tic = timeit.default_timer()

tttt = interp_loaded(0, 0,0)

toc = timeit.default_timer()
print('Took {0:g} seconds to carry out the evaluations '.format(toc-tic))