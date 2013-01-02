'''
Created on Nov 30, 2012

@author: cpdundon
'''
import unittest, MarketDataClasses, math
from datetime import date 

class Test(unittest.TestCase):


    def testName(self):
        pass

def writeRtns(inFNm, outFNm):
    m = MarketDataClasses
    inF = m.FileCls(inFNm, True)
    outF = m.FileCls(outFNm, False)
    
    info = inF.rLine()
    outF.wLine(info)
    
    tkrs = info.split(',')
    tkrs = tkrs[1:len(tkrs[1])]
    
    oldInfo_ = []
    dtOld = date.max
    while True:
        info = inF.rLine()
        
        if info == '':
            break
        
        info = info.split(',')
        dtS = info[0]
        dtS = dtS.split('-')
        
        dt = date(int(dtS[0]), int(dtS[1]), int(dtS[2]))
       
        days = float(dtOld.toordinal() - dt.toordinal())
        yr = days/365
        pDt = dtOld.isoformat()
        dtOld = dt
        
        idx = 0
        info_ = info[1:len(info)]
        for px in info_:
            p = float(px)
            info_[idx] = p 
            idx = idx + 1
            
        if len(oldInfo_) == 0:
            oldInfo_ = info_
            continue
            
        out = [pDt]
        l = len(info_)
        for idx in range(l):
            lnPx = math.log(oldInfo_[idx]/info_[idx])
            rtn = lnPx/yr
            out.append('%0.12f' % rtn)

        oldInfo_ = info_
        
        out = ','.join(out)
        out = out + '\n'    
        outF.wLine(out)
        
    inF.__del__()
    outF.__del__()
        
        
        
        
            
        