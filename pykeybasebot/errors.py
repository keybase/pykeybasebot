class Error(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class RevisionError(Error):
    pass


class DeleteNonExistentError(Error):
    pass
