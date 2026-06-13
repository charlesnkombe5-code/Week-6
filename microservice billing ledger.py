"""
8. Microservice Billing Ledger

Scenario: Compute infrastructure utilization costs over a billing cycle. Raw numbers must be rounded deterministically to establish price thresholds.
Requirements:
Given an instance runtime of 523450 seconds at a performance tier cost of $0.0000153 per second.
Use functions from the math module to find the absolute maximum ceiling price (rounded up to the nearest whole integer) and the absolute minimum floor price (rounded down to the nearest whole integer).
Format the actual raw cost calculation using a string format specifier showing exactly 4 decimal places.
Acceptance Criteria:
The terminal output must display three items: the precise formatted raw cost string, the mathematical ceiling integer, and the mathematical floor integer.
"""


import math
run_time = 523450
tier_cost=0.0000153

raw_cost= run_time*tier_cost

ceiling_price= math.ceil(raw_cost)
absolute_minimum= math.floor(raw_cost)



print (f"Raw Cost: ${raw_cost:.4f}")
print(f"ceiling_price: ${raw_cost:.4f}")
print(tier_cost)





 