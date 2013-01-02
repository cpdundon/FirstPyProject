'''
Created on Nov 26, 2012

@author: cpdundon
'''
import GetPriceData

class BaseCls:
    '''
    container for basic information
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.px = []
        self.dt = []
        self.open = []
        self.close = []
        self.high = []
        self.low = []
        self.adjClose = []
        self.volume = []
        
class EquityCls(BaseCls):
    '''
    container for equity information
    '''

    def key(self):
        k = self.tkr + '|'
        k = k + self.dt.isoformat()
        return k
    
    def __init__(self):
        '''
        Constructor
        '''
        BaseCls.__init__(self)
        self.tkr = []
        
class DayPxs():
    '''
    container for one days px information
    '''
    
    def __init__(self, dt_):
        '''
        Constructor
        '''
        self.dt = dt_
        self.pxClstr = []

    def append(self, pxO):
        self.pxClstr.append(pxO)
    def remove(self, pxO):
        self.pxClstr.remove(pxO)
                
    def key(self):
        return self.dt
    
    def AdjClosePx(self, tkr_):
        r = False
        for o in self.pxClstr:
            if o.tkr == tkr_:
                r = o.adjClose     
                break
        return r 
    
class FileCls():
    '''
    container for equity information
    '''

    def key(self):
        return self.tkr
    
    def __init__(self, nm_, read):
        '''
        Constructor
        '''
        
        if read:
            sw = 'r'
        else:
            sw = 'wb'
        
        self.idx = 0
        self.nm = nm_
        self.fle = GetPriceData.rtnFile(self.nm, sw) 
              
    def rLine(self):
        self.idx = self.idx + 1
        r = self.fle.readline()
        return r
    
    def wLine(self,ln):
        self.idx = self.idx + 1
        self.fle.writelines(ln)
        return self.idx
    
    def __del__(self):
        self.fle.close()
    