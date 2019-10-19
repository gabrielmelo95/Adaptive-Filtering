#adptive library version 0.1
#developed by Gabriel de Benevides, UFPE, 2019

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import csv, sqlite3
from scipy import signal

#Class with some adaptive algorithms - LMS, NLMS, RLS
class AdaptLIB():
    def filterlms(self, x, d, u, N):
        x = np.append(np.zeros(N),x)
        self.w = np.zeros(N+1)
        self.wf = np.zeros((N+1,len(x)-N))
        self.y = np.zeros_like(x)
        self.e = np.zeros_like(x)
        for i in range(len(x) - N):
            self.xn = np.flipud(x[i:i+N+1])
            self.y[i] = np.dot(self.w, self.xn)
            self.e[i] = d[i] - self.y[i]
            self.w = self.w+2*u*self.e[i]*self.xn
            self.wf[:,i] = self.w

                
