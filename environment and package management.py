"""
10. Fault-Tolerant Metrics Parser

Scenario: A background health-check daemon receives stringified configuration packets over UDP. Broken packets must not crash the monitoring system.
Requirements:
Take an intentional, broken JSON string input (e.g., missing a closing brace: {"status": "healthy", "uptime": 3600).
Attempt to deserialize the string using the built-in json module inside a defensive exception structure.
Catch the parsing exception, print a recovery warning message, and fallback to assign a hardcoded local dictionary: {"status": "unknown", "uptime": 0}.
Acceptance Criteria:
The script must finish execution with an exit code of 0.
The final state of your metrics variable must hold the fallback dictionary value.
"""

import json
from json.decoder import JSONDecodeError
broken_json= '{"status" : "healthy", "uptime": 3600'

try:
    metrics = json.loads(broken_json)

except JSONDecodeError:
    print("warning: invalid Json detected.using fallback values.")
    metrics = {"status": "unkown", "uptime": 0 }
    print ("metrics:r" , metrics)




