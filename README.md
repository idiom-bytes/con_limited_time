# Contracting - Limited Time
This is a simple contract that is only enabled between dt_start and dt_end

# Usage
Initialize the contract to be enabled for n_seconds

# Warning
For contracts to test against Datetime properly

environment = {'now': 
   contracting.stdlib.bridge.time.Datetime._from_datetime(
       datetime.datetime.now()
)}
