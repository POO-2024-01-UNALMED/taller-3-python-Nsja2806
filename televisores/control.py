class Control:
    def __init__(self, tv=None):
        self._tv=tv
    
    def enlazar(self, tv):
        self._tv=tv
        tv.setControl(self)
    
    def turnOn(self):
        if self._tv:
            self.tv.turnOn()

    def turnOff(self):
        if self._tv:
            self.tv.turnOff()
    
    def canalUp(self):
        if self._tv:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv:
            self._tv.canalDown()        
    
    def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()        
    
    def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()
    
    def setCanal(self, canal):
        if self._tv:
            self._tv.setCanal(canal)
    
    def setVolumen(self,volumen):
        if self._tv and self._tv.getEstado():
            self._tv.setVolumen(volumen)
    
    def setTV (self, televisor):
        self._tv=televisor
    
    def getTV(self):
        return self._tv