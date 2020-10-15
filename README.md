# Contracting - Limited Time
This is a simple contract that is only enabled between datetime dt_start and dt_end

# Usage
Initialize the contract:<br/>
- Pass in starting datetime dt_start down to the second<br/>
- Set the enabled window for 30 seconds<br/>
<t>self.con_limited_time.set_limited_time_seconds(<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y=dt_start.year,<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;m=dt_start.month,<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d=dt_start.day,<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H=dt_start.hour,<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M=dt_start.minute,<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;S=dt_start.second,<br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n_seconds=30<br/>
<t>)<br/>
<br/>

# Testing<br/>
- Test 15 seconds in con_limited.is_enabled() == True<br/>
- These "pythonic" imports are obnoxiously obnoxious<br/><br/>
from datetime import datetime as dt<br/>
from datetime import timedelta as td<br/>
import contracting.stdlib.bridge.time.Datetime as lamden_dt<br/><br/>
environment = {'now': lamden_dt._from_datetime(dt.now() + td(seconds=15))}<br/>
self.con_limited.is_enabled(environment=environment)<br/>
