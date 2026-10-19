import os
from dotenv import load_dotenv


load_dotenv()
File = os.getenv("FILE_PATH")




#get bad ips
def access_ip():
    Bad_ip = []
    Mal_ip = []

    ioc_path = [os.path.join(File, f) for f in os.listdir(File) if f.startswith("ioc")]
    with open(ioc_path[0],"r") as f:
        for line in f:
            line = line.strip()
            Mal_ip.append(line)
    
    
    alerts=[]
    path = [os.path.join(File, f) for f in os.listdir(File) if f.startswith("access")]
    with open(path[0],"r") as T:
        Bad_ip = T.readlines()
        for line in Bad_ip:
            parts = line.split()
            if parts:
                ip = parts[0]         
                if ip in Mal_ip:
                    alerts.append(f"Malicious IP found: --> {line.strip()}")
    return alerts


        



