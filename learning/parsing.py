import os
import json

# Check if log_file directory and logs.txt exist
if os.path.exists("log_file") and os.path.isdir("log_file"):
    log_file_path = "log_file/logs.txt"
    
    if os.path.exists(log_file_path):  # Ensure logs.txt exists
        log_list=[]

        with open(log_file_path, "r") as file:
            for log in file:
                log = log.strip()  # Remove leading/trailing spaces and newlines
                
                try:
                    ip = log.split("-")[0].strip()
                    timestamp = log.split("[")[1].split("]")[0].strip()
                    request = log.split('"')[1].strip()
                    status = log.split('"')[2].split()[0].strip()
                    user_agent = log.split('"')[5].strip()

                    json_log = {
                        "ip": ip,
                        "timestamp": timestamp,
                        "request": request,
                        "status": status,
                        "user_agent": user_agent
                    }
                    log_list.append(json_log)
                except IndexError:
                    print(f"Skipping malformed log: {log}")

        # Ensure json_logs directory exists
        if not os.path.exists("json_logs"):
            os.mkdir("json_logs")
            print(f"Directory 'json_logs' created.")

        # Write JSON logs to file
        with open("json_logs/logs.json", "w") as file:
            json.dump(log_list, file, indent=4)  # Save entire list as JSON
            print("Logs saved in json_logs/logs.json")
    else:
        print("Error: logs.txt file not found.")
else:
    print("Error: log_file directory not found.")
