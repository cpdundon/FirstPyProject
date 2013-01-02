'''
Created on Dec 3, 2012

@author: cpdundon
'''
import numpy, MarketDataClasses

def vecsFromFile(fNm):
    f = MarketDataClasses.FileCls(fNm,True)
    np = numpy
    
    hdr = f.rLine()
    hdr = hdr[0:len(hdr)-1]
    tkrs = hdr.split(',')
    tkrs = tkrs[1:len(tkrs)]
    
    # Clip the \n off the end of the line
    # tkrs[len(tkrs)-1] = tkrs[len(tkrs)-1][0:len(tkrs[len(tkrs)-1])-1]
    sz = len(tkrs)
    
    ctr = 0
    rArr = []
    while True:
        ln = f.rLine()
        if ln == '':
            break
        ln = ln[0:len(ln)-1]
        ln = ln.split(',')
        ln = ln[1:sz+1]
        
        nLn = []
        for px in ln:
            nm = float(px)
            nLn.append(nm)
        
        if ctr == 0:
            stash = nLn
        elif ctr == 1:
            rArr = np.vstack((stash, nLn))
        else:
            rArr = np.vstack((rArr, nLn))
        ctr = ctr + 1
        
    return [tkrs, rArr.T]

def cCov(dta):
    np = numpy
    
    dtaStrm = dta[1]
    dtaTgs = dta[0]
    
    C = np.cov(dtaStrm)
    
    return [dtaTgs, C]
    
def cCorr(dta):
    np = numpy
        
    dtaStrm = dta[1]
    dtaTgs = dta[0]
    
    C = np.corrcoef(dtaStrm)
    
    return [dtaTgs, C]    

def cStats(dta):
    np = numpy
        
    dtaStrm = dta[1]
    dtaTgs = dta[0]
    
    sz = np.size(dtaStrm, 1)
    
    sm = dtaStrm.sum(1)
    av = sm / sz 
    sdv = dtaStrm.std(1)    
        
    return [dtaTgs, sm, av, sdv, dtaStrm.max(1), dtaStrm.min(1)]
