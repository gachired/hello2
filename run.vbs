Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & WshShell.ExpandEnvironmentStrings("%APPDATA%") & "\hello2-main\main.bat" & Chr(34), 0
Set WshShell = Nothing