'''
Created on Nov 27, 2012

@author: cpdundon
'''
import unittest, MarketDataClasses
from datetime import date 

class Test(unittest.TestCase):

    def testName(self):
        pass


def importPxs(tkrs):
    mdc = MarketDataClasses
    
#     tkrs = ['cvx','ge','aapl']
    files = []
    
    for tkr in tkrs:        
        files.append(mdc.FileCls(tkr))
    
    pxDays = []
    for f in files:  
        while True:
            r = loadPxs(f.fle, f.tkr)
            if r[0] == -1: 
                break
            
            pX = r[1]
            
            pxCl = findPxCl(pX.dt, pxDays)
            pxCl.append(pX)
    
    for f in files:
        f.fle.close()
        del f

    return pxDays 

def getPx(dt_, fIn_):
    while True:
        r = fIn_.rLine()
        
        if r == '':
            return [date.min, -1]
        
        ln = r.split(',')
        
        dt = ln[0].split('-')
        
        l = len(dt)
        
        if not l == 3:
            continue
        
        dt = date(int(dt[0]), int(dt[1]), int(dt[2]))
        
        if dt <= dt_:
            break
    
    px = float(ln[6].replace('\n', ''))
    
    return [dt, px] 
        
def subSetPxs(oFNm, tkrs, dtV):
    '''This routine takes incomplete data lines out of the set and saves it out
    to a file - oFNm.  It is a pain in but butt to scrub the data but that is how 
    I have chosen to address missing data here. - Chris Dundon'''
    mdc = MarketDataClasses

    fList = []
    b = []
    
    outF = mdc.FileCls(oFNm, False)
    for tkr in tkrs:        
        inF = mdc.FileCls(tkr, True)
        fList.append(inF)   
        b.append([date.max, -1])
    
    ot = 'Date,' + ','.join(tkrs) + '\n'
    outF.wLine(ot)
    
    for _dt in dtV:
        
        ot = str(_dt.year) + '-' + str(_dt.month) + '-' + str(_dt.day)
        
        eof = True
        pxCt = 0
        idx = 0
        for tkr in tkrs:
            if b[idx][0] > _dt:
                bT = getPx(_dt, fList[idx])
                b[idx] = bT
                
            eof = eof * (b[idx][0] == date.min)    
            
            if b[idx][0] == _dt:
                ot = ot + ',' + '%0.2f' % b[idx][1]
                pxCt = pxCt + 1 
            else:
                ot = ot + ','

            idx = idx + 1
        
        if (eof == 1):
            break
        
        ot = ot + '\n'
        
        if pxCt == len(tkrs):
            outF.wLine(ot)    
        
    outF.fle.close
    for f in fList:
        f.fle.close()
    
    
    
    
def rtnFile(nm, oTyp):
    nm = '../textFiles/' + nm + '.csv'
    
    f = open(nm, oTyp)
    return f 

def loadPxs(f, tkr):
    b = 1
    p = MarketDataClasses.EquityCls()

    ln = f.readline()
    
    if ln == '':
        return [-1, p]
    
    v = ln.split(',')
    
    if v[0] == 'Date':
        ln = f.readline()
        v = ln.split(',')
    
    dt = v[0].split('/')
    p.dt = date(int(dt[2]), int(dt[0]), int(dt[1]))
    p.tkr = tkr
    p.adjClose = float(v[6].replace('\n', ''))
    
    return [b,p]     

def findPxCl(dt, clList):
    r = []
    if len(clList) == 0:
        r = MarketDataClasses.DayPxs(dt)
        clList.append(r)
        return r
    
    ctr = 0
    for e in clList:
        if e.dt == dt:
            r = e
            return r
            
        elif dt > e.dt:
            r = MarketDataClasses.DayPxs(dt)
            clList.insert(ctr, r)
            return r 
        
        ctr = ctr + 1
            
    if e.dt > dt:
        r = MarketDataClasses.DayPxs(dt)
        clList.append(r)    
    
    return r


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()