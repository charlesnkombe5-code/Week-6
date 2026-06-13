
"""
9. Disaster Recovery Volume Splitter

Scenario: A large backup data stream must be broken down into symmetrical storage slices. The input requires robust mathematical handling to avoid runtime mathematical failures.
Requirements:
Prompt the user for a total archive size (in GB) and the number of target cloud storage volumes.
Use math.ceil to calculate the backup slice allocation per volume.
Wrap the execution logic within a try...except block to capture errors stemming from alphabetic input types or division by zero.
Acceptance Criteria:
Entering 0 volumes must print an error message indicating invalid division, instead of crashing.
Entering 100 GB and 3 volumes must output a volume chunk calculation size of 34 GB.
"""



import math

try:
    archive_size=float(input("Enter the total archive size in GB: "))
    cloud_storage=int(input("Enter the number of target cloud storage volumes: "))


    small_size= math.ceil (archive_size/cloud_storage )

    print("Each cloud_storage volume should store")
    print(small_size, "GB")


except ZeroDivisionError:
    print("Error:  number of volumes cannot be zero")


except ValueError:
    print("Error: please enter numeric values only") 



