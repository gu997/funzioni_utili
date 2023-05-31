from joblib import Parallel, delayed
import numpy as np
import CoolProp.CoolProp as CP
lib="REFPROP"

fluids="CO2"

mix   = CP.AbstractState(lib, fluids)
n=10
P_gc=np.linspace(70,100,n)#95

def process(i):
    mix   = CP.AbstractState(lib, fluids)
    mix.update(CP.PT_INPUTS, i*10**5, 273.15+40)
    return i * i
    

results = Parallel(n_jobs=10)(delayed(process)(i) for i in P_gc)

#results = Parallel(n_jobs=10)(delayed(process)(i) for i in range(10))
print(results)



#from joblib import Parallel, delayed
#import math
import time

# =============================================================================
# def sqrt_func(i, j):
#     time.sleep(0.5)
#     return math.sqrt(i**j)
# 
# results = Parallel(n_jobs=10)(delayed(sqrt_func)(i, j) for i in range(5) for j in range(2))
# print(results)
# =============================================================================



"metodo 2"
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped

@background
def your_function(argument):
    #time.sleep(5)
    print('function finished for '+str(argument))



for i in range(10):
    your_function(i)
    
print('\nloop finished')



import multiprocessing
from joblib import Parallel, delayed

num_cores = multiprocessing.cpu_count()

if __name__ == "__main__":
    processed_list = Parallel(n_jobs=num_cores)(delayed(process)(i) for i in P_gc)