import os
import platform
import json
import requests

from voipms.base.exceptions import VoipException

class Client(object):
    def __init__(self, username=None, password=None):
        
        self.username = username or os.environ.get('VOIPMS_ACCOUNT_USER')
        self.password = password or os.environ.get('VOIPMS_API_TOKEN')
        self.api_base = "https://voip.ms/api/v1/rest.php"

        if not self.username or not self.password:
            raise VoipException("Credentials are required to create a Client")
        
        self.auth = (self.username, self.password)

        # Domains
        self._accounts = None
        self._call_detail_records = None
        self._dids = None
        self._general = None
        self._voicemail = None

    def request(self, method, auth=None, params={}):
        auth = auth or self.auth
        
        params["api_username"] = auth[0]
        params["api_password"] = auth[1]
        params["method"] = method
        params["content_type"] = "json"

        response = requests.get(self.api_base, params=params)
        data = json.loads(response.text)
        
        if data['status'] and data['status'] != 'success':
            err = data['status']
            raise VoipException("API Call failed with exception: {}".format(err))

        return data

    @property
    def accounts(self):
        if self._accounts is None:
            from voipms.api.accounts import Accounts
            self._accounts = Accounts(self)
        return self._accounts

    @property
    def call_detail_records(self):
        if self._call_detail_records is None:
            from voipms.api.call_detail_records import CallDetailRecords
            self._call_detail_records = CallDetailRecords(self)
        return self._call_detail_records

    @property
    def dids(self):
        if self._dids is None:
            from voipms.api.dids import DIDs
            self._dids = DIDs(self)
        return self._dids

    @property
    def general(self):
        if self._general is None:
            from voipms.api.general import General
            self._general = General(self)
        return self._general

    @property
    def voicemail(self):
        if self._voicemail is None:
            from voipms.api.voicemail import Voicemail
            self._voicemail = Voicemail(self)
        return self._voicemail

    @property
    def balance(self):
        return self.general.balance
    
    @property
    def ip(self):
        return self.general.ip

    @property
    def transaction_history(self):
        return self.general.transaction_history

    @property
    def countries(self):
        return self.general.countries

    @property
    def languages(self):
        return self.general.languages