'''
Created on Nov 20, 2012

@author: cpdundon
'''

#import sys

import time, GenRtns, GetPriceData, bStats, bPlot
from datetime import date

def main():
    time.clock()
    
    m = GetPriceData
    mGen = GenRtns
    
    tkrs = ['cvx','ge','aapl']
    tkrs.sort()
    
    dt = date.today()
    o = dt.toordinal()
    
    ln = 365 * 40
    ordB = o - ln
    
    dtV = []
    for x in range(o, ordB, -1):
        d = date.fromordinal(x)
        dtV.append(d)
    
    intFNm = 'testOut'
    outFNm = 'testRtns'
    m.subSetPxs(intFNm, tkrs, dtV)
    mGen.writeRtns(intFNm, outFNm)
    
    dta = bStats.vecsFromFile(outFNm)
    
    bStats.cStats(dta)
    
    rtns = dta[1] # Srtip out tickers
    x = rtns[1] # cvx
    y = rtns[2] # ge

    print time.clock() 
    
    bPlot.xyScatter(x, y)
    
    bPlot.hist()
    
        
if __name__ == '__main__':
    main()
    
    