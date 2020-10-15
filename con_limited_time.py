dt_start = Variable()
dt_end = Variable()

@construct
def seed():
    dt_start.set(0)
    dt_end.set(0)

@export
def set_timer(start:str, n_seconds:int):
    d = datetime.Datetime(year=2020, month=10, day=10)
    t = datetime.Timedelta(seconds=n_seconds)

    dt_start.set(d)
    dt_end.set(d + t)

@export
def can_trigger():
    return now > dt_start.get() and now < dt_end.get()