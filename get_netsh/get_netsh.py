import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

profile_names = (re.findall("Tutti i profili utente    : (.*)\r", command_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}

        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode('unicode_escape')

        if re.search("Chiave di sicurezza           : Assente", profile_info):
            continue
        else:

            wifi_profile["ssid"] = name

            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode('unicode_escape')

            password = re.search("Contenuto chiave            : (.*)\r", profile_info_pass)

            if password == None:
                wifi_profile["password"] = None
            else:

                wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile) 


for x in range(len(wifi_list)):
    print(wifi_list[x])

with open("wifi_psw.txt", 'a') as f: 
    for value in wifi_list: 
        f.write(str(value) + "\n")
    f.write("\n\t\tScansione\n")