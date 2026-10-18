from SudoSpike import sudoDetect

from bad_ips import access_ip

from _404Thresh import Detect404

import os
File = "C:\\Users\\kingo\\Documents\\Vs_PythonCode\\Advance-scripting-project\\"

#write all findings in one file
def report_to_invest(Spike,alerts,error):
    Output_path = [os.path.join(File, f) for f in os.listdir(File) if f.startswith("Investigation_report")]
    with open(Output_path[0], "a") as L:
        L.writelines("Here are the auth.log that show the sudo spikes groups and their time\n")
        L.writelines("============================================================\n")
        for spikes in Spike:
            line = f"{spikes['count']} sudos from {spikes['start']} to {spikes['end']}\n"
            L.write(line)
            print(line)
        L.writelines("Here are the access.log results that show the Malicious ips\n")
        L.writelines("============================================================\n")
        for alert in alerts:
            L.writelines(alert + "\n")
            print(alerts)
        L.writelines("Here are the access.log results that show the the ips with more than 6 404 errors\n")
        L.writelines("============================================================\n")
        for errors in error:
            L.writelines(errors + "\n")
            print(error)

#call all functions with one click
def main():
    Spike = sudoDetect()
    alerts = access_ip()
    error = Detect404()
    report_to_invest(Spike,alerts,error)

main()