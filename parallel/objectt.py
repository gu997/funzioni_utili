import CoolProp.CoolProp as CP

class Funz:  
    def __init__(self,mix):        
       self.mix = mix
       
    def imp(self,i):
       self.mix.update(CP.PT_INPUTS, i*10**5, 273.15)
       h=self.mix.hmass()
       return h
   
    
   
def f(i):
    print('b')
    return i