class Subaccount():
    def __init__(self, base):
        self.method = ""
        self.base = base

    def create(self, params={}):
        self.method = "createSubAccount"
        return self.base.request(self.method, params=params)

    def delete(self, params={}):
        self.method = "delSubAccount"
        return self.base.request(self.method, params=params)

    def fetch(self, params={}):
        self.method = "getSubAccounts"
        return self.base.request(self.method, params=params)

    def set(self, params={}):
        self.method = "setSubAccount"
        return self.base.request(self.method, params=params)
