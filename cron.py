import requests

requests.post("http://127.0.0.1:5000/updateLogs")
print(requests.get("http://127.0.0.1:5000/getEntries?from=all"))