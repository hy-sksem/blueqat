from blueqat import Circuit
import numpy as np

def oracle_00(c):
    c.i[:]
    
def oracle_01(c):
    c.cx[0, 1]
    
def oracle_10(c):
    c.x[0]
    c.cx[0, 1]
    c.x[0]
    
def oracle_11(c):
    c.x[1]
    
def oracle(c):
    f = np.random.rand()
    if f < 0.25:
        oracle_00(c)
        return "f(0) = 0, f(1) = 0"
    elif f < 0.5:
        oracle_01(c)
        return "f(0) = 0, f(1) = 1"
    elif f < 0.75:
        oracle_10(c)
        return "f(0) = 1, f(1) = 0"
    else:
        oracle_11(c)
        return "f(0) = 1, f(1) = 1"

c = Circuit(2)
c.x[1].h[:]
oracle_str = oracle(c)
c.h[0].m[0]
res = c.run(shots = 128)
print(res)
print("Selected oracle:", oracle_str)