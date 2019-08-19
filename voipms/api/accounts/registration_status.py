class RegistrationStatus():
    def __init__(self, base):
        self.method = "getRegistrationStatus"
        self.base = base
    
    def fetch(self, params={}):
        return self.base.request(self.method, params=params)