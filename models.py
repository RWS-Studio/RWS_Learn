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
    def __init__(self):
        """
        for more information about number of the version, https://semver.org/
        """
        self.last_version_url = urlopen("https://rws-studio.github.io/api/rws_learn/last_version.txt")

    def get_if_new_version(self):
        with open("database/actual_version.txt", "r") as file:
            actual = file.read()
        last = self.last_version_url.read()  # response -> b'0.1-beta\n' / <class 'bytes'>
        last = str(last).split("'")[1].split("\\n")[0]  # convert last in str, split ' , split \\n the 1 item of this
                                                        # list and take the first item of this rest
        if actual != last:
            return True
        else:
            return False

