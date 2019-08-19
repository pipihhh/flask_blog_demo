class Response(object):
    def __init__(self):
        self.code = 200
        self.error = ""
        self.msg = ""

    @property
    def data(self):
        return self.__dict__
