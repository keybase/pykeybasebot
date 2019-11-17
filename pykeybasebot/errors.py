"""
pykeybasebot.errors
===================

Set of custom exceptions

"""
from typing import Union


class Error(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class RevisionError(Error):
    CODE = 2760


class DeleteNonExistentError(Error):
    CODE = 2762


def disambiguate_error(e: Exception) -> Union[Exception, Error]:
    """
        Try to convert Exception presumably from kbsubmit()
        (from CLI response json) into our custom Error types.
    """
    if e.args[0]["code"] == RevisionError.CODE:
        return RevisionError(e.args[0]["message"])
    elif e.args[0]["code"] == DeleteNonExistentError.CODE:
        return DeleteNonExistentError(e.args[0]["message"])
    else:
        # return original exception
        return e
