dt_start = Variable()
dt_end = Variable()

@construct
def seed():
    dt_start.set(0)
    dt_end.set(0)

@export
def set_limited_time_seconds(y:int, m:int, d:int, H:int, M:int, S:int, n_seconds:int):
    d = datetime.datetime(
        year=y,
        month=m,
        day=d,
        hour=H,
        minute=M,
        second=S,
    )

    t = datetime.timedelta(seconds=n_seconds)

    dt_start.set(d)
    dt_end.set(d + t)

@export
def can_trigger():
    return now > dt_start.get() and now < dt_end.get()