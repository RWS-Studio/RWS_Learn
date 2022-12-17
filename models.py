
class Grade:
    def __init__(self, value, value_max, subject, description, factor):
        self.value = value
        self.value_max = value_max
        self.subject = subject
        self.description = description
        self.factor = factor


class Subject:
    def __init__(self, name):
        self.name = name

