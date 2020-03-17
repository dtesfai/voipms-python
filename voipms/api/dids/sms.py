class SMS():
    def __init__(self, base):
        self.method = ""
        self.base = base

    def fetch(self, params={}):
        self.method = "getSMS"
        return self.base.request(self.method, params=params)

    def create(self, params={}):
        self.method = "sendSMS"
        return self.base.request(self.method, params=params)

    def set(self, params={}):
        self.method = "setSMS"
        return self.base.request(self.method, params={})
