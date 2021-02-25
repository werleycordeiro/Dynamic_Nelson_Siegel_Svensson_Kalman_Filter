=====================================
Dynamic-Nelson-Siegel-Svensson Models
=====================================


.. image:: https://img.shields.io/pypi/v/Dynamic_Nelson_Siegel_Svensson_Kalman_Filter.svg
        :target: https://pypi.python.org/pypi/Dynamic_Nelson_Siegel_Svensson_Kalman_Filter


This package implements the Dynamic Nelson-Siegel-Svensson models with Kalman filter in Python.

* Free software: MIT license
* Python 3.7 or later supported


Features
--------

* Python implementation of the Dynamic Nelson-Siegel curve (three factors) with Kalman filter
* Python implementation of the Dynamic Nelson-Siegel-Svensson curve (four factors) with Kalman filter
* Forecasting the yield curve is available
* Log-likelihood is available to use optimize.minimize

Fitting the Dynamic-Nelson-Siegel
---------------------------------

To fitting the yield curve, we must set (param,Y,lik,frct,ahead,mty,model)

param: initial parameters vector of Dynamic-Nelson-Siegel models obtained by OLS in the two-step approach = 

([

The log of lambdas,

the square root of sample covariance diagonal matrix of VAR(1) residuals (H),

the VAR(1) matrix (phi),

the betas averages (mu), and

the cholesky deconposition of the VAR(1) estimated innovations covariance matrix (Q)

]);

Y: pandas data frame;

lik: log-likelihood;

frct: forecasts;

ahead: months (years) ahead forecasts;

mty: maturities in months (years);

model: 'NS' for the Dynamic Nelson-Siegel model  or 'S' for the Dynamic Nelson-Siegel-Svensson model;

.. code-block:: python

        from Dynamic_Nelson_Siegel_Svensson_Kalman_Filter import kalman
        import numpy as np
        import pandas as pd
        
        url = 'https://www.dropbox.com/s/inpnlugzkddp42q/bonds.csv?dl=1' # US Yield Curve 1972 - 2000
        df = pd.read_csv(url,sep=';',index_col=0)

        frct = False
        ahead = 0
        lik = True
        mty =  np.array([3,6,9,12,15,18,21,24,30,36,48,60,72,84,96,108,120]) # maturities in months
        model = 'NS'

        param = np.array([-2.798522, # log of 0.0609
        0.14170940,0.07289485,0.11492339,0.11120008,0.09055795,0.07672075,0.07222108,0.07076431,0.07012891,0.07267366,0.10624206,0.09029621,0.10374527,0.09801215,0.09122014,0.11794190,0.13354418, # H
        0.99010443,0.02496842,-0.002294319, # phi
        -0.02812401,0.94256154, 0.028699387, # phi
        0.05178493,0.01247332, 0.788078795, # phi
        8.345444,-1.572442,0.2029919,  # mu
        0.3408764,-0.07882772,-0.21351036, # Q
        0.62661018,-0.00425989, # Q
        1.08802059]) # Q

        kalman(param = param,Y = df, lik = lik, frct = frct, ahead = ahead, mty = mty, model = model)

which gives the following output

.. code-block:: python

        -2281.5860793152


Forecasting the Dynamic-Nelson-Siegel 
-------------------------------------

Kalman function also provides forecasts. We set 12 months ahead, and we define param, Y, mty, and model as above. 

.. code-block:: console

        frst = True
        lik = False
        ahead = 12

        kalman(param = param,Y = df, lik = lik, frct = frct, ahead = ahead, mty = mty, model = model)

which returns (a_tt,a_t,P_tt,P_t,v2,v1,Yf)

a_tt: the a posteriori state estimate,

a_t: the a priori state estimate,

P_tt: the a posteriori estimate covariance matrix,

P_t: the a posteriori estimate covariance matrix,

v2: filtered yields,

v1: filtered erros, and

Yf: forecasts.
        
Fitting and Forecasting the Dynamic-Nelson-Siegel-Svensson
----------------------------------------------------------

We can replicate the steps above but using the following initial parameters.

.. code-block:: console

        model = 'S'

        param = np.array([-2.798522,-3.55908713, # lambdas
        0.14170940,0.07289485,0.11492339,0.11120008,0.09055795,0.07672075,0.07222108,0.07076431,0.07012891,0.07267366,0.10624206,0.09029621,0.10374527,0.09801215,0.09122014,0.11794190,0.13354418, # H
        0.99010443,0.02496842,-0.002294319,0.0000, # phi
        -0.02812401,0.94256154, 0.028699387,0.000, # phi
        0.05178493,0.01247332, 0.788078795,0.0000, # phi
        0.00000000,0.00000000,0.0000000000,0.6000, # phi
        8.345444,-1.572442,0.2029919,2.96696726, # mu 
        0.3408764,-0.07882772,-0.21351036,0.1, # Q
        0.62661018,-0.00425989,0.2, # Q
        1.08802059,0.3, # Q
        0.4]) # Q

optimize.minimize 
------------------

.. code-block:: console

        from scipy import optimize

        optimize.minimize(fun = kalman, x0 = param, args = (df,lik,frct,ahead,mty,model),method = 'L-BFGS-B', bounds = None,options={'disp':True})

which gives the following output for the Dynamic-Nelson-Siegel model

.. code-block:: console

        ...
        CONVERGENCE: REL_REDUCTION_OF_F_<=_FACTR*EPSMCH
        fun: -3184.551029683603
        ...
        success: True
        x: array([-2.55419095,  0.2682528 ,  0.07550792,  0.09029396,  0.10450556,
        0.09915572,  0.08648558,  0.07862346,  0.07209206,  0.07267585,
        0.07909973,  0.10295337,  0.09260472,  0.10041753,  0.1117615 ,
        0.10696698,  0.15069579,  0.17277911,  0.99437232,  0.02861622,
       -0.02214779, -0.02886483,  0.93904762,  0.03963317,  0.02540488,
        0.02288304,  0.84151308,  7.99042415, -1.46634099, -0.43379175,
        0.30276472, -0.02340832,  0.0488872 ,  0.61858155,  0.01026079,
        0.89411573])

Credits
-------

Main developer is Werley Cordeiro_.

.. _Cordeiro: https://werleycordeiro.github.io/
