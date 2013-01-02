'''
Created on Dec 10, 2012

@author: cpdundon
'''
import unittest
import matplotlib.pyplot as plt
import numpy as np

class Test(unittest.TestCase):


    def testName(self):
        pass

def xyScatter(x, y):
    scat = plt.subplot(111)
    scat.scatter(x, y)
    scat.set_aspect(1.)
    plt.draw()
    plt.show()
def hist():
    ''' What if IQ was lognormal - it probably is not but what if... '''
    
    # mu, sigma = 100.0, 15.0
    # x = mu + sigma * np.random.randn(10000000)
    
    # mu = np.log(0.0**2/np.sqrt(0.0**2+15.0**2))
    # v = np.log(1.0+15.0**2/100.0**2)
    m = -0.25
    s = 0.225
    scale = 105
    
    x_ = np.arange(0.01, 6., 0.01)
    y_ = pdf(x_, m, s)
    x = x_ * scale
    y = y_ / scale
    plt.plot(x, y) 
    
    
    meanCalc = np.sum(0.01*y_*x)
    print 'PDF Mean: ' + str(meanCalc)
    
    x = scale * np.random.lognormal(m, s, 100000)
    # the histogram of the data
    n, bins, patches = plt.hist(x, bins=100, normed=1, facecolor='g', alpha=0.75)  
    
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([0, 200, 0, 0.05])
    plt.grid(True)
    plt.show()

def mu():
    c = np.log(33.0/7.0)
    b = np.log(165)
    a = np.log(50)
    
    mu = (a - b - np.sqrt(a**2 - 2*a*b + b**2 - (c - 1)*(c*a**2 - b**2))) / (c - 1)
          
    return mu
 
def sig(mu):
    a = np.log(100)
     
    s = np.sqrt(2*(a - mu))
    
    return s 
       
def pdf(x, mu, sig):
    
    a = 1 / (x*np.sqrt(2*np.pi*sig**2))
    r = a*np.exp(-1*(np.log(x) - mu)**2/(2*sig**2))
    
    return r 

    
    
if __name__ == "__main__":
    #imporst sys;sys.argv = ['', 'Test.testName']
    unittest.main()