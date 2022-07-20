from TablePrinter import create_table


class User:
    def __init__(self, info):
        self.id = int(info[0])
        self.first_name = info[1]
        self.last_name = info[2]
        self.address = info[3]
        self.phone_number = info[4]
        self.country = info[5]
        self.age = int(info[6])
        self.skills = info[7].split('-')
        self.title = True

    def to_list(self):
        result = [self.id, self.first_name, self.last_name, self.address, self.phone_number, self.country, self.age,
                  '-'.join(self.skills)]
        return result

    def __str__(self):
        return create_table([self], self.title)
