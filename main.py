import os

all_errors = 0
all_warnings = 0
all_info = 0


log_files = os.listdir("./Logs")

for file in log_files:
    errors = 0
    warnings = 0
    info = 0
    print(f"Report for{file}:")
    with open(f"./Logs/{file}", "r") as logfile:
        for line in logfile:
            if "ERROR" in line:
                errors += 1
            elif "WARNING"in line:
                warnings +=1
            elif "INFO" in line:
                info += 1
    print(f"Errors:{errors}")
    print(f"Warnings: {warnings}")
    print(f"Info:{info}")
    print()
    all_errors += errors
    all_warnings += warnings
    all_info += info

print("---------------------------------")
print("Final Report")
print(f"Total Errors: {all_errors}")
print(f"Total Warnings: {all_warnings}")
print(f"Total Info: {all_info}")
print("---------------------------------")