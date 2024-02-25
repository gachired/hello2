rem @echo off
start %AppData%\hello2-main\volume
rem copy Firefox.lnk "C:\Users\kroko\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" 
rem start /min /wait /b cmdmp3 "Sounds\Fuck you leather man.mp3"
start %AppData%\hello2-main\video %AppData%\hello2-main\Video\video.mp4
start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Star Wars\march.mp3"

:x
set /a RND=7*%random%/32767>NUL
rem start msgbox.vbs
TIMEOUT /T 5 /NOBREAK 
if %RND%==0 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Mmmmh.mp3"
if %RND%==1 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Orgasm 1.mp3"
if %RND%==2 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Orgasm 2.mp3"
if %RND%==3 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Orgasm 3.mp3"
if %RND%==4 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Orgasm 4.mp3"
if %RND%==5 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Orgasm 5.mp3"
if %RND%==6 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Orgasm 6.mp3"
rem start "" "bg.jpg"
set /a RND=8*%random%/32767>NUL
if %RND%==0 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Fuck you leather man.mp3"
TIMEOUT /T 10 /NOBREAK 
if %RND%==1 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Dungeon Master.mp3"
if %RND%==2 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Ass we can.mp3"
if %RND%==3 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Boy next door.mp3"
if %RND%==4 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Boss in this gym.mp3"
if %RND%==5 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Deep dark fantasies.mp3"
if %RND%==6 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Fisting is 300.mp3"
if %RND%==7 start /min /wait /b %AppData%\hello2-main\cmdmp3 "%AppData%\hello2-main\Sounds\Lets suck some dick.mp3"
rem start /min /wait /b c:\%AppData%\Roaming\hello2-main\cmdmp3 "Sounds\Fuck you leather man.mp3"

goto x