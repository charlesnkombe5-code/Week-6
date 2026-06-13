
"""
11. Defensive Config Inspector

Scenario: A configuration parsing script traverses nested environmental properties. Missing keys must resolve smoothly without killing the runner.
Requirements:
Parse a valid, multi-layered JSON string representing environment variables that looks like this: {"database": {"connection": {"port": 5432}}}.
Write defensive checking logic to look for a nested path that does not exist: database -> replica -> timeout.
If any key chain breaks along the path, explicitly assign the target configuration variable to None. Do not use a raw try/except block; use structural containment validation tools (in).
Acceptance Criteria:
Attempting to read the missing path must print: Timeout setting: None.
The script must not throw a KeyError.
"""


import json 

json_string = '{"database": {"connection": {"port": 5432 }}}'

configuration = json.loads(json_string)
timeout = None

if 'database' in configuration:
    if 'replica' in  configuration["database"]:  
        if 'timeout' in configuration["database"] ["replica"]:
            timeout=configuration["database"]["replica"] ["timeout"]
    print("Timeout settings:", timeout) 
    
