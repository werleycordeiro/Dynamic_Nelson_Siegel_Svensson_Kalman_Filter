# Author: Werley Cordeiro
# werleycordeiro@gmail.com
import numpy as np
import pandas as pd
from .factor_loadings import factor_loadings
from .Kfilter import Kfilter
from .lyapunov import lyapunov
def kalman(param,Y,lik,frct,ahead,mty,model):
    T = Y.shape[0]
    W = Y.shape[1];
    if model == 'NS':
        N = 3;
        j = 1;
    else:
        N = 4;
        j = 2;
    Z = factor_loadings(param = param, mty = mty, model = model)
    H = np.diag(param[j:(W + j)])
    HH = H.dot(H)
    phi = param[(W + j):(W + j + N * N)].reshape(N,N)
    mu = param[(W + j + N * N):(W + j + N * N + N)] 
    Q = np.identity(N)
    tmp = param[(W + j + N * N + N):param.shape[0]]
    Q[0,:] = tmp[0:N] # first row
    Q[(N-1),(N-1):] = tmp[tmp.shape[0]-1] # last row
    if model =='NS':
        Q[1,(N-2):] = tmp[(N):(N+2)] # second row 'NS'	
    else:
        Q[1,(N-3):] = tmp[(N):(N+3)] # second row 'S'
        Q[2,(N-2):] = tmp[(N+3):(N+5)] # third row 'S'
    QQ = Q.dot(Q.T)
    v1 = np.zeros((T,W))
    v2 = np.zeros((T,W))
    if frct:
        Yf = np.zeros(((ahead),W))
        a_tt = np.zeros(((T + ahead - 1),N))
        a_t = np.zeros(((T + ahead),N))
        P_tt = np.zeros((N,N,(T + ahead - 1)))
        P_t = np.zeros((N,N,(T + ahead)))
    else:
        Yf = 'NA'
        a_tt = np.zeros((T,N))
        a_t = np.zeros(((T + 1),N))
        P_tt = np.zeros((N,N,T))
        P_t = np.zeros((N,N,(T + 1)))
    a_t[0,:] = mu
    P_t[:,:,0] = lyapunov(N = N, phi = phi,QQ = QQ)
    logLik = - 0.5 * T * W * np.log(2 * np.pi)
    return(Kfilter(logLik = logLik, N = N, T = T, Y = Y, Z = Z, a_t = a_t, P_t = P_t, HH = HH, a_tt = a_tt, P_tt = P_tt, v2 = v2, v1 = v1, phi = phi, mu = mu, QQ = QQ, frct = frct, ahead = ahead, Yf = Yf, lik = lik))
