# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


class ZiMuZuException(Exception):
    """Base exception for ZiMuZu"""

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return 'Exception Code: {code}, Message: {msg}'.format(
            code=self.code,
            msg=self.message,
        )


class InvalidParameterException(ZiMuZuException):
    """ZiMuZu exception class"""
    def __init__(self, code=1001, message='Invalid Parameter'):
        super(ZiMuZuException, self).__init__(code, message)


class ParameterCheckFailedException(ZiMuZuException):
    """ZiMuZu exception class"""
    def __init__(self, code=1002, message='Parameter Check Failed'):
        super(ZiMuZuException, self).__init__(code, message)


class AccessKeyErrorException(ZiMuZuException):
    """ZiMuZu exception class"""
    def __init__(self, code=1003, message='Access Key Error'):
        super(ZiMuZuException, self).__init__(code, message)


class InterfaceUnauthorizedException(ZiMuZuException):
    """ZiMuZu exception class"""
    def __init__(self, code=1004, message='Interface Unauthorized'):
        super(ZiMuZuException, self).__init__(code, message)


class ParameterCheckFailed2Exception(ZiMuZuException):
    """ZiMuZu exception class"""
    def __init__(self, code=1011, message='Parameter Check Failed 2'):
        super(ZiMuZuException, self).__init__(code, message)


class RequestTimeoutException(ZiMuZuException):
    """ZiMuZu exception class"""
    def __init__(self, code=1012, message='Request Timeout'):
        super(ZiMuZuException, self).__init__(code, message)


class NotLoginException(ZiMuZuException):
    """ZiMuZu exception class"""
    def __init__(self, code=1021, message='Not Login'):
        super(ZiMuZuException, self).__init__(code, message)
