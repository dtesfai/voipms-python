from voipms.api.voicemail.messages import Messages

class Voicemail():
    def __init__(self, base):
        self._messages = None
        self.base = base

    @property
    def messages(self):
        if self._messages is None:
            self._messages = Messages(self.base)
        return self._messages

    def create(self, params={}):
        self.method = "createVoicemail"
        return self.base.request(self.method, params=params)

    def delete(self, params={}):
        self.method = "delVoicemail"
        return self.base.request(self.method, params=params)

    def fetch(self, params={}):
        self.method = "getVoicemails"
        return self.base.request(self.method, params=params)

    def set(self, params={}):
        self.method = "setVoicemail"
        return self.base.request(self.method, params=params)