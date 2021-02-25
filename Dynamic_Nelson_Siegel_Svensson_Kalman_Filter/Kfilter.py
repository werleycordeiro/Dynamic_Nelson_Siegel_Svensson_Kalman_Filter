import numpy as np
def Kfilter(logLik,N,T,Y,Z,a_t,P_t,HH,a_tt,P_tt,v2,v1,phi,mu,QQ,frct,ahead,Yf,lik):
    for t in range(0,T):
        v = Y.iloc[t,:] - Z.dot(a_t[t,:])
        try:
            L = Z.dot(P_t[:,:,t]).dot(Z.T) + HH
            L = np.linalg.cholesky(L)
        except:
            L = 1e100
        if isinstance(L, np.ndarray):
            u = np.linalg.inv(L).dot(np.identity(L.shape[0]))
            Xinv = np.linalg.inv(L.T).dot(u)
            K = P_t[:,:,t].dot(Z.T).dot(Xinv)
            logLik = logLik - 0.5 * (np.log(np.linalg.det(L)*np.linalg.det(L)) + v.T.dot(Xinv).dot(v))
            a_tt[t,:] = a_t[t,:] + K.dot(v)
            P_tt[:,:,t] = P_t[:,:,t] - K.dot(Z).dot(P_t[:,:,t])
            v1[t,:] = Z.dot(a_tt[t,:])
            v2[t,:] = Y.iloc[t,:] - v1[t,:]
            a_t[t + 1,:] = phi.dot(a_tt[t,:]) + (np.identity(N) - phi).dot(mu)
            P_t[:,:,t + 1] = phi.dot(P_tt[:,:,t]).dot(phi.T) + QQ
        else:
            logLik = logLik + 0
    if frct:
        if t>((T-1)-1): # 347 > 346
            for m in range(0,ahead):
                Yf[m,:] = Z.dot(a_t[t + m,:])
                a_tt[t + m,:] = a_t[t + m, ]
                P_tt[:,:,t + m] = P_t[:,:,t + m]
                a_t[t + m + 1,:] = phi.dot(a_tt[t + m,:]) + (np.identity(N) - phi).dot(mu)
                P_t[:,:,t + m + 1] = phi.dot(P_tt[:,:,t + m]).dot(phi.T) + QQ
    if lik:
        return(-logLik)
    else:
        return(a_tt,a_t,P_tt,P_t,v2,v1,Yf)
