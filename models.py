from urllib.request import urlopen


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
        self.last_version_url = urlopen("https://rws-studio.github.io/api/rws_learn/last_version.txt")

    def show_update_available(self, update_number):
        # include static/js/msg/update_available.js in the html
        pass

    def get_if_new_version(self):
        with open("database/actual_version.txt", "r") as file:
            actual = file.read()
        last = self.last_version_url.read()  # response -> b'0.1-beta\n' / <class 'bytes'>
        last = str(last).split("'")[1].split("\\n")[0]  # convert last in str, split ' , split \\n the 1 item of this
                                                        # list and take the first item of this rest
        print(actual)
        print(last)
        if actual != last:
            self.show_update_available(last)
            print("update available")
        else:
            print("Software up-to-date")

