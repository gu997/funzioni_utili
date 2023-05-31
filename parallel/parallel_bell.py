import timeit

# Important!
# This import and setup will happen inside the process
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary
import CoolProp.CoolProp as CP
root = 'C:/Program Files (x86)/REFPROP' # Change this path as needed
RP = REFPROPFunctionLibrary(root)
RP.SETPATHdll(root)

def set_fluids(names):
    """ This happens inside the process that is forked, when it is initialized. IMPORTANTLY, IN SERIAL!! """
    RP.SETFLUIDSdll('*'.join(names))

def calc1(inputs):
    """
    Do the calculation for one mixture
    """
    T,p,z = inputs
    return RP.REFPROPdll('','TP','D',RP.MOLAR_BASE_SI,0,0,T,p,z).Output[0]

def calc_all(mapfcn):
    """
    Using the function passed in, evaluate all the inputs
    """
    inputs = []
    for i in range(10):
        T = 308.3084286
        p = 397780
        z = [0.23328,0.13008,0.05558,0.09246,0.01915,0.04628,0.02459,0.00474,0.00472,0.0046,0.0062,0.00426,0.00298,0.00614,0.00584,0.07216,0.00886,0.27808]
        inputs.append((T,p,z))
    return mapfcn(calc1, inputs) # calc1 is the function to be called, inputs the inputs

if __name__=='__main__':
    
    # Start up the timer
    tic = timeit.default_timer()

    # 1. Set up the map
    # Either comment out A or B, and if you use multiple cores, you may need to change Nprocesses

    names = [
    "Methane","Ethane","Ethylene","Propane","Propylene","Isobutane","Butane","trans-Butene",
    "Butene","Isobutene","Isopentane","Pentane","Pentene","Carbon dioxide","Oxygen","Nitrogen",
    "Carbon monoxide","Hydrogen"
    ]

    # A) Leave this section uncommented to use a serial evaluation
    # mapfcn = map; set_fluids(names)

    # B) Leave this section uncommented to carry out the calculations in parallel
    import multiprocessing
    Nprocesses = multiprocessing.cpu_count()-1
    p = multiprocessing.Pool(Nprocesses, initializer = set_fluids, initargs = (names,))
    mapfcn = p.map

    # Do the calculations
    print(calc_all(mapfcn))

    toc = timeit.default_timer()
    print('Took {0:g} seconds to carry out the evaluations w/ {1:d} processes'.format(toc-tic, Nprocesses))