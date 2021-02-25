import numpy as np
def lyapunov(N,phi,QQ):
    return(np.matmul(np.linalg.inv(np.identity(N**2) - np.kron(phi,phi)), QQ.reshape(N**2,1)).reshape((N,N)))
