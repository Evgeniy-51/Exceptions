class RuntimeException(Exception):
    def __init__(self, msg=None):
        self.message = msg if msg else "Unknown error"

    def __str__(self):
        return self.message


class InvalidData(Exception):
    pass


class NotEnoughData(Exception):
    pass


class OverData(Exception):
    pass


class InvalidYear(Exception):
    pass


class InvalidPhoneNumber(Exception):
    pass


class ExistingEntry(Exception):
    pass
