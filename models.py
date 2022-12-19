
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


class SoftwareVersion:
    def __init__(self, number):
        """
        for more information about number, https://semver.org/
        :param number:
        """
        self.number = number

    def show_update_available(self, update_number):
        # include static/js/msg/update_available.js in the html
        pass

    def get_if_new_version(self):
        with open("database/actual_version.txt", "r") as file:
            actual = file.read()
        with open("https://rws-studio.github.io/rws_learn/last_version.txt", "r") as file:
            last = file.read()
        if not actual == last:
            self.show_update_available(last)
