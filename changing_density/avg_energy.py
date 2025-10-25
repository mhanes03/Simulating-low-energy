import numpy as np 

volt = change_this

P = and_this

Z,N,meanX,sigmaX,meanY,sigmaY,emitX,emitY,emitTrans,betaX,betaY,betaTrans,alphaX,alphaY,alphaTrans,meanP= np.loadtxt('profile.txt', unpack=True)

E = (meanP[-1]**2)/(2*105.66)

print(E, volt, P)