import os
import sys
import subprocess
import ctypes
from subprocess import DEVNULL

def check_admin():
    """ Check if the user has administrative privileges """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False

def add_rule(rule_name, file_path):
    """ Add rule to Windows Firewall """
    subprocess.run(
        f"netsh advfirewall firewall add rule name=\"{rule_name}\" dir=in action=block enable=yes program=\"{file_path}\"",
        shell=True,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    print(f"Rule {rule_name} for {file_path} added")

def main():
    if sys.platform != 'win32':
        print("This script only runs on Windows")
        sys.exit(1)
        
    if not check_admin():
        # Re-run the script with admin privileges
        subprocess.run(['runas', '/user:Administrator', sys.executable, __file__])
        sys.exit(0)

    my_dir = os.getcwd()
    rule_name = "*Blocked"
    for path, sub_dirs, files in os.walk(my_dir):
        for file in files:
            if file.endswith(".exe") or file.endswith(".dll") or file.endswith(".bin") or file.endswith(".setup"):
                file_path = os.path.join(path, file)
                add_rule(rule_name, file_path)

if __name__ == '__main__':
    main()

def add_rule(rule_name, file_path):
    """ Add rule to Windows Firewall """
    subprocess.run(
        f"netsh advfirewall firewall add rule name=\"{rule_name}\" dir=out action=block enable=yes program=\"{file_path}\"",
        shell=True,
        stdout=DEVNULL,
        stderr=DEVNULL
    )
    print(f"Rule {rule_name} for {file_path} added")

def main():
    if sys.platform != 'win32':
        print("This script only runs on Windows")
        sys.exit(1)
        
    if not check_admin():
        # Re-run the script with admin privileges
        subprocess.run(['runas', '/user:Administrator', sys.executable, __file__])
        sys.exit(0)

    my_dir = os.getcwd()
    rule_name = "*Blocked"
    for path, sub_dirs, files in os.walk(my_dir):
        for file in files:
            if file.endswith(".exe") or file.endswith(".dll") or file.endswith(".bin") or file.endswith(".setup"):
                file_path = os.path.join(path, file)
                add_rule(rule_name, file_path)

if __name__ == '__main__':
    main()
