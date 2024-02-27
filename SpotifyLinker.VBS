Set WshShell = CreateObject("WScript.Shell" ) 
scriptDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WshShell.Run chr(34) & scriptDir & "\test.bat" & Chr(34), 0 
Set WshShell = Nothing 