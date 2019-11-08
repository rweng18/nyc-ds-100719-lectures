class Calculator:
    def __init__(self, data):
        self.data = sorted(data)
        self.__calc_stats()

    def add_data(self, data):
        # If data is list
        self.data.extend(data)
        self.__calc_stats()

    def remove_data(self, data):
        # If data is list
        if isinstance(data, list):
            for datum in data:
                self.data.remove(datum)

        else:
            self.data.remove(data)
        self.__calc_stats()

    def __calc_mean(self):
        return sum(self.data)/self.length

    def __calc_median(self):
        if self.length < 2:
            return self.data
        if self.length % 2:
            return self.data[self.length//2]

    def __calc_var(self):
        sum_squares = 0
        for x in self.data:
            sum_squares += (x - self.__calc_mean())**2
        return sum_squares/(self.length - 1)
    
    def __calc_stats(self):
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_var()
        self.stand_dev = self.__calc_var()**0.5