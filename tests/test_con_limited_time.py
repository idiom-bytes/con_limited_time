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
        now = dt.now()

        # Limited Time Contract will START in now + 5 seconds
        # Limited Time Contract will END in now + 35 seconds
        wait_to_start = datetime.timedelta(seconds=5)
        dt_start = now + wait_to_start
        self.con_limited_time.set_limited_time_seconds(
            y=dt_start.year,
            m=dt_start.month,
            d=dt_start.day,
            H=dt_start.hour,
            M=dt_start.minute,
            S=dt_start.second,
            n_seconds=30
        )

        # Limited Time Contract should be DISABLED @ now + 4 seconds
        # t_forward = datetime.timedelta(seconds=4)
        # environment = {'now': now + t_forward}
        # has_started = self.con_limited_time.has_started(environment=environment)
        # has_ended = self.con_limited_time.has_ended(environment=environment)
        # is_enabled = self.con_limited_time.is_enabled(environment=environment)
        # assert has_started == False
        # assert has_ended == False
        # assert is_enabled == False

        # Limited Time Contract should be ENABLED @ now + 6 seconds
        # TODO - Adjusted t_forward to be @ start + 15 seconds
        con_start = self.con_limited_time.dt_start.get()
        t_forward = datetime.timedelta(seconds=15)
        test_time = now + t_forward
        con_end = self.con_limited_time.dt_end.get()
        environment = {'now': test_time}
        has_started = self.con_limited_time.has_started(environment=environment)
        has_ended = self.con_limited_time.has_ended(environment=environment)
        is_enabled = self.con_limited_time.is_enabled(environment=environment)
        assert has_started == True
        assert has_ended == False
        assert is_enabled == True

        # Limited Time Contract should be ENABLED @ now + 34 seconds
        t_forward = datetime.timedelta(seconds=34)
        environment = {'now': now + t_forward}
        has_started = self.con_limited_time.has_started(environment=environment)
        has_ended = self.con_limited_time.has_ended(environment=environment)
        is_enabled = self.con_limited_time.is_enabled(environment=environment)
        assert has_started == True
        assert has_ended == False
        assert is_enabled == True

        # Limited Time Contract should be DISABLED @ now + 36 seconds
        t_forward = datetime.timedelta(seconds=36)
        environment = {'now': now + t_forward}
        has_started = self.con_limited_time.has_started(environment=environment)
        has_ended = self.con_limited_time.has_ended(environment=environment)
        is_enabled = self.con_limited_time.is_enabled(environment=environment)
        assert has_started == True
        assert has_ended == True
        assert is_enabled == False