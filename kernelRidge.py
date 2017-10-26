#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:30:43 2017

@author: fubao
"""

from sklearn.preprocessing import normalize

#implementation of kernel ridge regression from scratch
import numpy as np



def KRRS(trainData, testData, i, lambdaPara):     
    '''
    kernel ridge regression from scratch
    k(x1,x2) = (1+x1 * x2) ^i
    input :
        synthetic data
    '''

    trainX = trainData[0]
    trainY = trainData[1]
    
    testX = testData[0]
    testY = testData[1]
    
    #trainX -= .5
    #testX  -= .5
    #trainX = trainX.reshape(-1,1)
    #trainX = normalize(trainX, axis=0)
    #testX = normalize(testX.reshape(-1,1), axis=0)


    print ("trainX shape[0]: ", trainX, trainX.shape[0], trainY.shape)
    
    #get alpha below
    kArr = np.empty((trainX.shape[0], trainX.shape[0]), dtype=np.float)
    print ("kArr shape original: ", kArr.shape)

    #kArr = np.empty(1)
    for i in range(0, trainX.shape[0]):
        for j in range(0, trainX.shape[0]):
            xi = trainX[i]
            xj = trainX[j]
            kij = (1.0 + xi*xj) #np.dot(xi, xj))
            
            #print ("kij: ", kij)
            #kArr = np.vstack((kArr, np.array(kij)))
            #print ("trainX kij: ", kArr)
            np.append(kArr, kij)
            #print ("kij: ", kArr)
    print ("kArr shape: ", type(kArr), kArr.shape)
    #print ("kArr shape: ", kArr[0][0], kArr[2][0], kArr[199][199], type(kArr), kArr.shape)
    print ("kij: ", kArr)
    
    #get
    ridgeParas = lambdaPara*np.identity(trainX.shape[0], dtype=np.float)
    
    alpha = np.dot(np.linalg.inv(np.add(kArr, ridgeParas)), trainY)          #alpha for kernel ridge $\alpha = (\Phi(X)\phi^T(X)+\lambda I)^{-1}Y$ 
    print ("ridgeParas: ", ridgeParas,np.linalg.inv(np.add(kArr, ridgeParas)),  alpha, alpha.shape)
    
    
    for testInd in range(0, testX.shape[0]):
        
        xnew = testX[testInd]
        #for i in range(0, trainX.shape[0]):   # $y_{new} = \sum_{i}  \alpha_i \Phi(x_i) \Phi(x_{new}) 
        #innerVal = 
        ynew = np.sum([np.dot(alpha[i], (1 + np.dot(trainX[i], xnew))) for i in range(0, trainX.shape[0])])          #sum ??

        #alpha[i]
        #print ("xnew: ", xnew, ynew)
        
