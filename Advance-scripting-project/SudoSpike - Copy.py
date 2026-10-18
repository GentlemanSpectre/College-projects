import os
import re

File = "C:\\Users\\kingo\\Documents\\Vs_PythonCode\\Advance-scripting-project\\"
#to do
#use regex to detect sudo 
#use counter to count ammount of sudo
#secondary counter that counts sudos in a row
#print secondary counter to list and track time(first and last of them in a row)

def sudoDetect():
    streak = 0
    Spike = []
    auth_path = [os.path.join(File, f) for f in os.listdir(File) if f.startswith("auth")]
    with open(auth_path[0],"r") as Y:
        for line in Y:
            Time = re.search(r"\b\d{2}:\d{2}:\d{2}\b", line)
            Match_Line = re.search(r"\bsudo\b", line)
            if Time:
                current_time = Time.group() # needed otherwise return is <re.Match object; span=(7, 15), match='11:20:07'> to <re.Match object; span=(7, 15), match='11:43:44'>
            
            if Match_Line:
                if streak == 0:
                    start_time = current_time
                streak += 1
                last_time = current_time

            else:
                if streak > 0:
                    Spike.append({
                        "count": streak,
                        "start": start_time,
                        "end": last_time
                    })
                    streak = 0
                    start_time = None
                    last_time = None

    
    return Spike

    

