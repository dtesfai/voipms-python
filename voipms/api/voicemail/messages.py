class Messages():
    def __init__(self, base):
        self.method = ""
        self.base = base
    
    def fetch(self, params={}):
        self.method = "getVoicemailMessages"
        return self.base.request(self.method, params=params)

    def delete(self, params={}):
        self.method = "delMessages"
        return self.base.request(self.method, params=params)