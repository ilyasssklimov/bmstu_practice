# TODO: сделать классы ошибок


class MyError(Exception):
    def __init__(self, text):
        self.txt = text

