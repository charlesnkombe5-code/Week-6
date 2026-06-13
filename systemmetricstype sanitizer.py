"""
13. System Metrics Type Sanitizer

Scenario: A data ingestion pipeline processes raw values from unreliable nodes. The metric array contains mixed garbage types that must be cleaned inline.
Requirements:
Initialize a static data collection array containing: [82, "91", None, 45, "Error", 73.5].
Iterate through the array to calculate the total sum and mathematical average.
Use a try...except handling mechanism combined with explicit type filtering to skip strings that cannot be parsed, numbers that are missing, or None values.
Acceptance Criteria:
The loop must run completely without breaking.
The script must output the calculated average using only the clean valid numeric entries (82, 91, 45, 73.5).
"""


metrics = [82, "91", None, 45,"Error", 73.5]
total = 0
count = 0

for value in metrics :
    try: 
        if value is None:
            continue
        numbers = float(value)
        total +=numbers
        count=+1

    except ValueError:
        continue
    average = total / count
    print ("Total: ", total) 
    print("Average: ", average)   
