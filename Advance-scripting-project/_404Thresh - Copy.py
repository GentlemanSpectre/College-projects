import os
import re
from collections import Counter

File = "C:\\Users\\kingo\\Documents\\Vs_PythonCode\\Advance-scripting-project\\"
def Detect404():

    ip_404_count = Counter()
    ip_list = []
    error = []
    auth_path = [os.path.join(File, f) for f in os.listdir(File) if f.startswith("access")]
    with open(auth_path[0],"r") as Q:
        for line in Q:
            if re.search(r"\b404\b", line):
                ipMatch = re.search(r"(\d{1,3}\.){3}\d{1,3}", line)
                if ipMatch:
                    ip = ipMatch.group()
                    ip_404_count[ip] += 1

    for ip, count in ip_404_count.items():
        if count >= 6:
            error.append(f" {ip} had {count} 404 errors")
    return error


