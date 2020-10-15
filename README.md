# Contracting - Limited Time
This is a simple contract that is only enabled between datetime dt_start and dt_end

# Usage
Initialize the contract:\n
- Pass in starting datetime dt_start down to the second\n
- Set the enabled window for 30 seconds\n
self.con_limited_time.set_limited_time_seconds(\n
   y=dt_start.year,\n
   m=dt_start.month,\n
   d=dt_start.day,\n
   H=dt_start.hour,\n
   M=dt_start.minute,\n
   S=dt_start.second,\n
   n_seconds=30n
)\n
\n
# Testing
- Test 15 seconds in con_limited.is_enabled() == True\n
- These "pythonic" imports are obnoxiously obnoxious\n
from datetime import datetime as dt\n
from datetime import timedelta as td\n
import contracting.stdlib.bridge.time.Datetime as lamden_dt\n
environment = {'now': lamden_dt._from_datetime(dt.now() + td(seconds=15))}\n
self.con_limited.is_enabled(environment=environment)\n
