class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def set_time(self, hour, minute, second):
        if hour <= Time.max_hours and minute <= Time.max_minutes and second <= Time.max_seconds:
            self.hours = hour
            self.minutes = minute
            self.seconds = second

    def get_time(self):
        if self.hours < 10:
            hh = "0" + str(self.hours)

        else:
            hh = self.hours
        if self.minutes < 10:
            mm = "0" + str(self.minutes)

        else:
            mm = self.minutes

        if self.seconds < 10:
            ss = "0" + str(self.seconds)

        else:
            ss = self.seconds
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        if self.seconds == 59:
            if self.minutes == 59:
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1

                self.minutes = 0
            else:
                self.minutes += 1

            self.seconds = 0

        else:
            self.seconds += 1

        return self.get_time()

time = Time(10, 59, 59)

print(time.next_second())