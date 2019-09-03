from voipms.api.dids.search import Search
from voipms.api.dids.sms import SMS

class DIDs():
    def __init__(self, base):
        self._search = None
        self._sms = None

        self.base = base

    @property
    def search(self):
        if self._search is None:
            self._search = Search(self.base)
        return self._search

    @property
    def sms(self):
        if self._sms is None:
            self._sms = SMS(self.base)
        return self._sms

    def cancel(self, params={}):
        self.method = "cancelDID"
        return self.base.request(self.method, params=params)

    def order(self, params={}):
        self.method = "orderDID"
        return self.base.request(self.method, params=params)

    def fetch(self, params={}):
        self.method = "getDIDsInfo"
        return self.base.request(self.method, params=params)