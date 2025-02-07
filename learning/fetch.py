import os
import requests

# URL to download the file
url ="https://raw.githubusercontent.com/elastic/examples/refs/heads/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
response = requests.get(url)

directory = "log_file"

if os.path.exists(directory) and os.path.isdir(directory):
    file_path = os.path.join(directory, "logs.txt") # Ensure it's a directory
    with open(file_path, "w") as file:
        file.write(response.text)  # Save response inside a file
    print("Response saved in log_file/log.txt")
else:
    os.mkdir(directory)
    print(f"Directory '{directory}' created.")
