import os
import json

status_count={}
request_count=0

with open("json_logs/logs.json", "r") as file:
    logs = json.load(file)

for log in logs:
    status_code= log["status"]
    status_count[status_code] = status_count.get(status_code, 0) + 1
    request_count += 1

print(f"Total requests: {request_count}")
print(f"Total status codes: {status_count}")

status_code_list = list(map(int, status_count.keys()))
print(status_code_list)

ip_dict = {}

for log in logs:
    ip = log["ip"]
    ip_dict[ip] = ip_dict.get(ip, 0) + 1  # Count occurrences
sort_ips = sorted(list(ip_dict.keys()))
for ip in sort_ips:
    print(ip, ip_dict[ip])  
