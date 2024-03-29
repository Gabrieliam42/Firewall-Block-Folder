Note: This Python script has been compiled as a executable file and works on Windows operating systems.


Therefore "Firewall Block Folder Win.exe" would perform the following actions:

1. In order to run this script you must copy the "Firewall Block Folder Win.exe" in the directory you want (the directory you want to block internet access to, via Firewall rules).

2. It starts in the current working directory, as the environment in which the script is running in (so the .exe file should be copied in the main directory you need to be Firewalled).

3. It verifies if it runs as administrator and if not, it will try to run it as the admin.

4. It identifies all the files in the current directory (including in all sub-folder levels).

5. It starts setting up rules for each of the binary files (.bin, .exe, .dll, .setup), while checking the entire directory structure.



Features:

Admin Privileges: The script checks if it has admin privileges and if not, it tries to grant itself administrator rights.

Directory Structure Preservation: The script maintains the directory structure and its sub-folders in the respective directory when processing Firewall rules for the specific file types, it doesn't modify any file, folder or subfolder.

Usage:

As a user you can copy "Firewall Block Folder Win.exe" in the directory you want, and run it from that location. A window will appear and it will show you each path and respective processed file.
The script will create Firewall rules for each of the binary files (.bin, .exe, .dll, .setup), that will block internet access to and from the redpective directory.

Please note that this script requires admin privileges to run. If it does not have admin privileges, it will try to grant required privileges to run, if they are declined by the system the script will exit.

This script is particularly useful when you want to test software, but you don't want it to send any data to it's servers.

Disclaimer: Please use this script responsibly. Always ensure you have a backup of important files and folders.
The author is not responsible for any loss of data. Use at your own consideration.
