from voipms.api.call_detail_records.billing import Billing
from voipms.api.call_detail_records.records import Records
from voipms.api.call_detail_records.rates import Rates
from voipms.api.call_detail_records.termination_rates import TerminationRates


class CallDetailRecords():
    def __init__(self, base):
        self.base = base
        self._billing = None
        self._records = None
        self._rates = None
        self._termination_rates = None

    @property
    def billing(self):
        if self._billing is None:
            self._billing = Billing(self.base)
        return self._billing

    @property
    def records(self):
        if self._records is None:
            self._records = Records(self.base)
        return self._records

    @property
    def rates(self):
        if self._rates is None:
            self._rates = Rates(self.base)
        return self._rates

    @property
    def termination_rates(self):
        if self._termination_rates is None:
            self._termination_rates = TerminationRates(self.base)
        return self._termination_rates
