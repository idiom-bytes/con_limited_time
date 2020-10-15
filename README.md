# Contracting - Limited Time
This is a simple contract that is only enabled between datetime dt_start and dt_end

# Usage
Initialize the contract: 
- Pass in starting datetime dt_start down to the second
- Set the enabled window for 30 seconds
self.con_limited_time.set_limited_time_seconds(
   y=dt_start.year,
   m=dt_start.month,
   d=dt_start.day,
   H=dt_start.hour,
   M=dt_start.minute,
   S=dt_start.second,
   n_seconds=30
)

# Testing
- Test 15 seconds in con_limited.is_enabled() == True
- These "pythonic" imports are obnoxiously obnoxious
from datetime import datetime as dt
from datetime import timedelta as td
import contracting.stdlib.bridge.time.Datetime as lamden_dt
environment = {'now': lamden_dt._from_datetime(dt.now() + td(seconds=15))}
self.con_limited.is_enabled(environment=environment)
