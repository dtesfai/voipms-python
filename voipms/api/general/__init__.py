from voipms.api.general.balance import Balance
from voipms.api.general.ip import IP

class General():
    def __init__(self, base):
        self._balance = None
        self._ip = None

        self.base = base

    @property
    def balance(self):
        if self._balance is None:
            self._balance = Balance(self.base)
        return self._balance

    @property
    def ip(self):
        if self._ip is None:
            self._ip = IP(self.base)
        return self._ip