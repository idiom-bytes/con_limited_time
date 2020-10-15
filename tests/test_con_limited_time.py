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
        t = datetime.timedelta(seconds = 5)
        self.con_limited_time.set_timer(
            start=d + t,
            n_seconds=5
        )

        time.sleep(2)
        assert self.con_limited_time.can_trigger() == False

        time.sleep(4)
        assert self.con_limited_time.can_trigger() == True

        time.sleep(6)
        assert self.con_limited_time.can_trigger() == False