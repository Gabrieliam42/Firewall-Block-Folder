# Script Developer: Gabriel Mihai Sandu
# GitHub Profile: https://github.com/Gabrieliam42

import os
import ctypes
import sys

def check_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if check_admin():
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".exe",".dll",".bin",".setup")):
                filepath = os.path.join(root, file)
                os.system(f'NETSH advfirewall firewall delete rule name="*Allowed" dir=in program="{filepath}"')
                os.system(f'NETSH advfirewall firewall delete rule name="*Allowed" dir=out program="{filepath}"')
                os.system(f'NETSH advfirewall firewall delete rule name="*Blocked" dir=in program="{filepath}"')
                os.system(f'NETSH advfirewall firewall delete rule name="*Blocked" dir=out program="{filepath}"')
                os.system(f'NETSH advfirewall firewall add rule name="*Allowed" dir=in program="{filepath}" action="allow" enable="yes"')
                os.system(f'NETSH advfirewall firewall add rule name="*Allowed" dir=out program="{filepath}" action="allow" enable="yes"')
else:
    # Run the script again with admin privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
