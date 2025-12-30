@echo off
set "log=C:\Temp\errorlog.txt"
set "output=C:\Temp\windows-lastboot-errors.txt"

PowerShell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$ErrorActionPreference='Stop'; ^
   try { ^
     $bt = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime; ^
     Get-WinEvent -LogName System | ^
     Where-Object { $_.TimeCreated -gt $bt -and $_.LevelDisplayName -eq 'Error' } | ^
     Select-Object TimeCreated, Id, ProviderName, Message | ^
     Out-File -Encoding UTF8 '%output%' ^
   } catch { $_ | Out-File -Encoding UTF8 '%log%' }"

echo Done. If error occurred, check: %log%
pause
