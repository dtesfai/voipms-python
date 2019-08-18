from voipms.api.accounts.balance import Balance

class Accounts():
  def __init__(self, base):
    self._balance = None
    self.base = base

  @property
  def balance(self):
    if self._balance is None:
      self._balance = Balance(self.base)
    return self._balance