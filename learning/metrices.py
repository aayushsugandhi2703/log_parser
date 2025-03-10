import os
import json
from prettytable import PrettyTable

# Dictionary to count occurrences of each HTTP status code
status_count = {}
# Counter for total number of requests
request_count = 0

# Load JSON logs from the file
with open("json_logs/logs.json", "r") as file:
    logs = json.load(file)

# Process each log entry
for log in logs:
    status_code = log["status"]
    # Increment the count for the status code
    status_count[status_code] = status_count.get(status_code, 0) + 1
    # Increment total request count
    request_count += 1

# Print total request count and status code distribution
print(f"Total requests: {request_count}")
print(f"Total status codes: {status_count}")

# Convert status codes to a list of integers
status_code_list = list(map(int, status_count.keys()))
print("List of status codes:", status_code_list)

# Dictionary to count occurrences of each IP address
ip_dict = {}

# Process each log entry to count IP occurrences
for log in logs:
    ip = log["ip"]
    ip_dict[ip] = ip_dict.get(ip, 0) + 1  # Count occurrences

# Sort IP addresses in ascending order and by request
sorted_ips_assending = sorted(ip_dict.keys())

sorted_ips_request =sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
# Print each sorted IP along with its occurrence count
for ip in sorted_ips_assending:
    print(ip, ip_dict[ip])

for count in sorted_ips_request:
    print(count)

# sorting hte ip on hte basis of status code frequency
status_code_dict = {}
for log in logs:
    ip =log["ip"]
    status_code = log["status"]
    if ip not in status_code_dict:
        status_code_dict[ip] = {}
    status_code_dict[ip][status_code] = status_code_dict[ip].get(status_code, 0) + 1

sorted_status_code_dict = {ip: status_code_dict[ip] for ip in sorted(status_code_dict.keys())}

# Save sorted logs to a file
with open("sorted_logs.json", "w") as file:
    json.dump(sorted_status_code_dict, file, indent=4)

# Print the sorted logs
for ip, status_count in sorted_status_code_dict.items():
    print(ip, status_count)

t = PrettyTable(["IP Address", "Frequency", "Status Code", "Count"])

# Iterate over sorted IPs and retrieve status codes
for ip in sorted_ips_assending:
    for status, count in status_code_dict[ip].items(): 
        t.add_row([ip, ip_dict[ip], status, count])
# Print the table
print(t)