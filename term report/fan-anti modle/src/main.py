import numpy as np

class Simulator(object):
    def __init__(self):
        self.alpha :float = 0.0
        self.beta :float = 0.0
    
    def R(self,f,b):
        np.tanh(
            self.alpha * f
            + self
            .beta * (1-np.pow(f,))
        )

def run():
    return 0

if __name__ == "__main__":
    run()