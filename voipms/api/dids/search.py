class Search():
    def __init__(self, base):
        self.method = ""
        self.base = base
    
    def canada(self, params={}):
        self.method = "searchDIDsCAN"
        return self.base.request(self.method, params=params)

    def usa(self, params={}):
        self.method = "searchDIDsUSA"
        return self.base.request(self.method, params=params)