def format_time(total_minutes):
    # 570 -> '09:30'
    return f'{total_minutes // 60:02d}:{total_minutes % 60:02d}'


class Activity:
    def __init__(self, day, month, year, hours, minutes, duration, description):
        self.day = day
        self.month = month
        self.year = year
        self.hours = hours
        self.minutes = minutes
        self.duration = duration          # in minutes
        self.description = description

    # ---------- getters and setters ----------
    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day

    def set_month(self, month):
        self.month = month

    def get_month(self):
        return self.month

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_hours(self, hours):
        self.hours = hours

    def get_hours(self):
        return self.hours

    def set_minutes(self, minutes):
        self.minutes = minutes

    def get_minutes(self):
        return self.minutes

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    # ---------- helpers ----------
    def get_start(self):
        # start time as minutes since midnight
        return self.hours * 60 + self.minutes

    def get_end(self):
        # end time as minutes since midnight
        return self.get_start() + self.duration

    def get_date(self):
        return f'{self.day:02d}/{self.month:02d}/{self.year}'

    # ---------- required functions ----------
    def __str__(self):
        return ('Date: ' + self.get_date() +
                '\nTime: ' + format_time(self.get_start()) + ' - ' + format_time(self.get_end()) +
                '\nDuration: ' + str(self.duration) + ' minutes' +
                '\nDescription: ' + self.description)

    def get_activity(self):
        # one-line version for tables
        return (f'{self.get_date():<12}'
                f'{format_time(self.get_start()):<8}'
                f'{format_time(self.get_end()):<8}'
                f'{self.duration:>8}   '
                f'{self.description}')

    def get_overlap(self, other):
        # 0 if no overlap, otherwise the overlapping time in minutes
        if (self.day, self.month, self.year) != (other.day, other.month, other.year):
            return 0
        start = max(self.get_start(), other.get_start())
        end = min(self.get_end(), other.get_end())
        if end > start:
            return end - start
        return 0
