
class DateTimeCheck:

    def format_hours_12(self, hours):
        print(type(hours))
        import datetime

        if hours == 0:
            return datetime.time(0).strftime("%I:%M %p")
        elif len(str(hours)) < 3:
            minutes = hours
            return datetime.time(0, minutes).strftime("%I:%M %p")
        else:
            hour = int(str(hours)[:-2])
            minutes = int(str(hours)[-2:])
            return datetime.time(hour, minutes).strftime("%I:%M %p")