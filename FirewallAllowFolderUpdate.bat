echo off
color 09
@setlocal enableextensions
@cd /d "%~dp0"
set location=%cd%
del "___ALLOWED___"
del "___ALLOWED_LAN___"
del "___FIREWALLED___"
del "___UNFIREWALLED___"
FOR /r %%G in ("*.exe","*.dll","*.bin","*.setup","*.scr","*.tmp") Do (@echo %%G
NETSH advfirewall firewall delete rule name="*Allowed" dir=in program="%%G")
FOR /r %%G in ("*.exe","*.dll","*.bin","*.setup","*.scr","*.tmp") Do (@echo %%G
NETSH advfirewall firewall delete rule name="*Allowed" dir=out program="%%G")
timeout /t 2
FOR /r %%G in ("*.exe","*.dll","*.bin","*.setup","*.scr","*.tmp") Do (@echo %%G
NETSH advfirewall firewall add rule name="*Allowed" dir=in program="%%G" action="allow" enable="yes")
FOR /r %%G in ("*.exe","*.dll","*.bin","*.setup","*.scr","*.tmp") Do (@echo %%G
NETSH advfirewall firewall add rule name="*Allowed" dir=out program="%%G" action="allow" enable="yes")
ren "FirewallAllowFolderUpdate.bat" "___ALLOWED___"