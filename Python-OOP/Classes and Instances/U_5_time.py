class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        if __name__ == '__main__':
            return self.hours, self.minutes, self.seconds

    def get_time(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def next_second(self):
        if self.seconds == self.max_seconds:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1

        if self.minutes == self.max_minutes + 1:
            self.minutes = 0
            self.hours += 1

        if self.hours == self.max_hours + 1:
            self.hours = 0

        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())



