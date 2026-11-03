@echo off
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%~f0'; $c=[IO.File]::ReadAllText($p); if($c -notmatch '\r\n'){ $c = $c -replace '(?<!\r)\n', [char]13+[char]10; [IO.File]::WriteAllText($p, $c); Write-Host '【自动修复】检测到 LF 换行，已自动转为 CRLF。请重新双击运行！' -ForegroundColor Green; Pause; exit 1 }"
if %errorlevel%==1 exit /b 1

chcp 65001 >nul

if defined GIT_ASKPASS_MARKER (
    py "%~dp0close.py" --askpass "%~1"
    exit /b %ERRORLEVEL%
)
py "%~dp0close.py" %*

exit /b %ERRORLEVEL%