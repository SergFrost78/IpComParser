import datetime


class MyDatetime:
    def __init__(self):
        self.data = datetime.datetime.now()
        self.week_day = datetime.datetime.today().weekday()
        self.out()

    def current_date(self):
        date_now = self.data.date()
        date_now = str(date_now).split('-')[1:]
        date_now = date_now[1], date_now[0]
        date_now = ':'.join(date_now)
        return  date_now

    def current_time(self):
        time_now = self.data.time()
        time_now = str(time_now).split(':')[:2]
        time_now = ':'.join(time_now)
        return time_now

    def day_of_week(self):
        week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        return week[self.week_day]

    def out(self):
        weekday_date_time = [self.day_of_week(), self.current_date(), self.current_time()]
        return weekday_date_time
