from joblib import Parallel, delayed
import numpy as np
import CoolProp.CoolProp as CP
import multiprocessing
import timeit
import os
import sys
#from objectt import f
#from objectt import Funz

lib="REFPROP"

fluids="CO2"

mix   = CP.AbstractState(lib, fluids)
m=1000


# =============================================================================
# class Funz:  
#     def __init__(self,mix):        
#        self.mix = mix
#        
#     def imp(self,i):
#        self.mix.update(CP.PT_INPUTS, i*10**5, 273.15)
#        h=self.mix.hmass()
#        return h
# =============================================================================


def process_obj(i):
    
    sys.path.append('D:\guglielmo_vaccaro\python\parallel')
    from objectt import Funz
# =============================================================================
#     from objectt import Funz
#     mix   = CP.AbstractState(lib, fluids)
#     funz=Funz(mix)
#         
#     h=funz.imp(i)
# =============================================================================
    mix   = CP.AbstractState(lib, fluids)
    funz=Funz(mix)
    h=funz.imp(i)

    #h=f(i)
    return h


def process(i):
    mix   = CP.AbstractState(lib, fluids)
    #m=1000#0
    TT=np.linspace(273.15,273.15+40,m)
    for k in range(m):
        mix.update(CP.PT_INPUTS, i*10**5, TT[k])
        h=mix.hmass()
    return h

def process2(i):
    #m=10000
    TT=np.linspace(273.15,273.15+40,m)
    a=0
    for k in range(m):
        h=CP.PropsSI('H', 'P',i*10**5 ,'T',TT[k],'REFPROP::CO2')
        a=a+1
    
    return a






if __name__ == "__main__":
    
    
    n=10
    P_gc=np.linspace(70,100,n)#95
    
    
    
    num_cores = multiprocessing.cpu_count()-1
    
    # Start up the timer
    tic = timeit.default_timer()
    
    processed_list = Parallel(n_jobs=num_cores)(delayed(process_obj)(i) for i in P_gc)
    
    toc = timeit.default_timer()
    print('Took {0:g} seconds to carry out the evaluations w/ {1:d} processes'.format(toc-tic, num_cores))
    
    
    # Start up the timer
    tic = timeit.default_timer()
    
    processed_list = Parallel(n_jobs=num_cores)(delayed(process2)(i) for i in P_gc)
    
    toc = timeit.default_timer()
    print('Took {0:g} seconds to carry out the evaluations w/ {1:d} processes'.format(toc-tic, num_cores))






