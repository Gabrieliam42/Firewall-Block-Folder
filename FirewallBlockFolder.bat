@echo off
color 09
setlocal EnableDelayedExpansion

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (

    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"
:: End BatchGotAdmin
@setlocal enableextensions
@cd /d "%~dp0"
set location=%cd%

FOR /r %%G in ("*.exe","*.dll","*.bin","*.setup","*.scr","*.tmp","*.ms","*.mse","*.msc","*.mcr","*.mzp") Do (@echo %%G
NETSH advfirewall firewall add rule name="*Blocked" dir=in program="%%G" action="block" enable="yes")
FOR /r %%G in ("*.exe","*.dll","*.bin","*.setup","*.scr","*.tmp","*.ms","*.mse","*.msc","*.mcr","*.mzp") Do (@echo %%G
NETSH advfirewall firewall add rule name="*Blocked" dir=out program="%%G" action="block" enable="yes")
ren "FirewallBlockFolder.bat" "___FIREWALLED___"
