import time
import datetime
from datetime import datetime as dt

from unittest import TestCase
from contracting.client import ContractingClient

class ConLimitedTimeSpecs(TestCase):
    # before each test, setup the conditions
    def setUp(self):
        self.client = ContractingClient()
        self.client.flush()

        with open('../con_limited_time.py') as f:
            code = f.read()
            self.client.submit(code, name='con_limited_time')

        self.con_limited_time = self.client.get_contract('con_limited_time')

    def test_1_limited_time(self):
        d = dt.now()
        t = datetime.timedelta(seconds=5)

        dt_start = d+t
        self.con_limited_time.set_limited_time_seconds(
            y=dt_start.year,
            m=dt_start.month,
            d=dt_start.day,
            H=dt_start.hour,
            M=dt_start.minute,
            S=dt_start.second,
            n_seconds=30
        )

        # time.sleep(2)
        # can_trigger = self.con_limited_time.can_trigger()
        # assert can_trigger == False

        time.sleep(10)
        con_start = self.con_limited_time.dt_start.get()
        dt_now = dt.now()
        has_started = dt_now > con_start

        con_end = self.con_limited_time.dt_end.get()
        has_ended = dt_now < con_end

        # can_trigger() == dt_now > con_start and dt_now < con_end
        can_trigger = self.con_limited_time.can_trigger()
        assert can_trigger == True

        time.sleep(6)
        can_trigger = self.con_limited_time.can_trigger()
        assert can_trigger == False