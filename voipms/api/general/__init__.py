from voipms.api.general.balance import Balance
from voipms.api.general.ip import IP
from voipms.api.general.transaction_history import TransactionHistory
from voipms.api.general.countries import Countries
from voipms.api.general.languages import Languages

class General():
    def __init__(self, base):
        self._balance = None
        self._ip = None
        self._transaction_history = None
        self._countries = None
        self._languages = None

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

    @property
    def transaction_history(self):
        if self._transaction_history is None:
            self._transaction_history = TransactionHistory(self.base)
        return self._transaction_history

    @property
    def countries(self):
        if self._countries is None:
            self._countries = Countries(self.base)
        return self._countries

    @property
    def languages(self):
        if self._languages is None:
            self._languages = Languages(self.base)
        return self._languages