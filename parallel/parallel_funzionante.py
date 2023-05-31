''''
in questo script parallelizzo il calcolo dell'entalpia per al variare della pressione 
sia per high level che low level interface di coolprop
'''


from joblib import Parallel, delayed
import numpy as np
import CoolProp.CoolProp as CP
import multiprocessing
import timeit



lib="REFPROP"

fluids="CO2"

mix   = CP.AbstractState(lib, fluids)
m=1000



def process(i):
    mix   = CP.AbstractState(lib, fluids)
    TT=np.linspace(273.15,273.15+40,m)
    for k in range(m):
        mix.update(CP.PT_INPUTS, i*10**5, TT[k])
        h=mix.hmass()
    return h

def process2(i):
    TT=np.linspace(273.15,273.15+40,m)
    for k in range(m):
        h=CP.PropsSI('H', 'P',i*10**5 ,'T',TT[k],'REFPROP::CO2')
        
    
    return h






if __name__ == "__main__":
    
    
    n=10
    P_gc=np.linspace(70,100,n)
    
    
    
    num_cores = multiprocessing.cpu_count()-1
    
    # Start up the timer
    tic = timeit.default_timer()
    
    processed_list = Parallel(n_jobs=num_cores)(delayed(process)(i) for i in P_gc)
    
    toc = timeit.default_timer()
    print('Took {0:g} seconds to carry out the evaluations w/ {1:d} processes'.format(toc-tic, num_cores))
    
    
    # Start up the timer
    tic = timeit.default_timer()
    
    processed_list = Parallel(n_jobs=num_cores)(delayed(process2)(i) for i in P_gc)
    
    toc = timeit.default_timer()
    print('Took {0:g} seconds to carry out the evaluations w/ {1:d} processes'.format(toc-tic, num_cores))

