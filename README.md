# Contracting - Limited Time
This is a simple contract that is only enabled between datetime dt_start and dt_end

# Usage
Initialize the contract:<br/>
- Pass in starting datetime dt_start down to the second<br/>
- Set the enabled window for 30 seconds<br/>
self.con_limited_time.set_limited_time_seconds(<br/>
   y=dt_start.year,<br/>
   m=dt_start.month,<br/>
   d=dt_start.day,<br/>
   H=dt_start.hour,<br/>
   M=dt_start.minute,<br/>
   S=dt_start.second,<br/>
   n_seconds=30<br/>
)<br/>
<br/>

# Testing<br/>
- Test 15 seconds in con_limited.is_enabled() == True<br/>
- These "pythonic" imports are obnoxiously obnoxious<br/>
from datetime import datetime as dt<br/>
from datetime import timedelta as td<br/>
import contracting.stdlib.bridge.time.Datetime as lamden_dt<br/>
environment = {'now': lamden_dt._from_datetime(dt.now() + td(seconds=15))}<br/>
self.con_limited.is_enabled(environment=environment)<br/>
