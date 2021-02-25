import numpy as np
def factor_loadings(param,mty,model):
    lam = np.exp(param[0])
    A = lam * mty
    c1 = np.ones(mty.shape[0])
    c2 = (1 - np.exp(- A)) / (A)
    c3 = c2 - np.exp(- A)
    if model == 'S':
        l2 = np.exp(param[1])
        A2 = l2 * mty
        c4 = ((1 - np.exp(- A2)) / (A2)) - np.exp(- A2)
        lambmat = np.vstack((c1,c2,c3,c4)).T
    else:
        lambmat = np.vstack((c1,c2,c3)).T
    return(lambmat)
