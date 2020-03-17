from voipms.api.accounts.subaccount import Subaccount
from voipms.api.accounts.registration_status import RegistrationStatus


class Accounts():
    def __init__(self, base):
        self._subaccount = None
        self._registration_status = None

        self.base = base

    @property
    def subaccount(self):
        if self._subaccount is None:
            self._subaccount = Subaccount(self.base)
        return self._subaccount

    @property
    def registration_status(self):
        if self._registration_status is None:
            self._registration_status = RegistrationStatus(self.base)
        return self._registration_status
