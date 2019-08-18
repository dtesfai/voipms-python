from __future__ import absolute_import, division, print_function

import sys

class VoipException(Exception):
    pass

class VoipRestException(VoipException):
    def __init__(self, status, message=""):
        self.msg = message
        self.status = status

    def __str__(self):
        return self.msg or "<empty message>"