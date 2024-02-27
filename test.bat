ECHO OFF

goto loop

PAUSE

:loop
tasklist /fi "ImageName eq Spotify.exe" /fo csv 2>NUL | find /I "Spotify.exe">NUL
if "%ERRORLEVEL%"=="1" (goto check) else (goto startBat)

:check
tasklist /fi "ImageName eq SpotifyLinker.exe" /fo csv 2>NUL | find /I "SpotifyLinker.exe">NUL
if "%ERRORLEVEL%"=="0" taskkill /f /im "SpotifyLinker.exe"
goto loop

:startBat
tasklist /fi "ImageName eq SpotifyLinker.exe" /fo csv 2>NUL | find /I "SpotifyLinker.exe">NUL
if "%ERRORLEVEL%"=="1" (START "" "%~dp0\SpotifyLinker.exe")
goto loop