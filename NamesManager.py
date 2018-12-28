class NamesManager:
    def __init__(self, filename):
        self.filename = filename
        self.names = {}
        self.sum_names = {}

    def read_data(self):
        with open(self.filename) as f:
            is_first_line = True
            for line in f.readlines():
                if is_first_line:
                    first_line = line.strip().split(",")
                    is_first_line = False
                else:
                    name_line = line.strip().split(",")
                    name_frequency_by_year = {}
                    i = 2
                    for item in first_line[2:len(first_line)-1]:
                        name_frequency_by_year[item] = name_line[i]
                        i += 1
                    self.names[name_line[0]] = name_frequency_by_year
                    self.sum_names[name_line[0]] = name_line[-1]

    def most_favourite_name(self, year):
        max_frequency = 0
        result = []
        for name in self.names:
            value = int(self.names[name][year])
            if value > max_frequency:
                max_frequency = value
                result = []
                result.append(name)
            elif value == max_frequency:
                result.append(name)
        return result

    def most_favourite_name_historically(self):
        max_frequency = 0
        result = []
        for name in self.sum_names:
            value = int(self.sum_names[name])
            if value > max_frequency:
                max_frequency = value
                result = []
                result.append(name)
            elif value == max_frequency:
                result.append(name)
        print(max_frequency)
        return result

def uloha_4():
    names_manager = NamesManager("mena.csv")
    names_manager.read_data()
    print(names_manager.most_favourite_name("2014"))
    print(names_manager.most_favourite_name_historically())
