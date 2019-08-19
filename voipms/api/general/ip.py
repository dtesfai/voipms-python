class IP():
    def __init__(self, base):
        self.method = "getIP"
        self.base = base
    
    def fetch(self, params={}):
        return self.base.request(self.method, params=params)