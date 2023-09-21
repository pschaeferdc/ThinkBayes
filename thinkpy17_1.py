class Time(object):
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

t1 = Time()
t1.hour = 11
t1.minute = 59
t1.second = 30

t1.print_time()
print(t1.time_to_int())