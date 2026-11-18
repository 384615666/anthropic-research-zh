@echo off
chcp 65001 >nul
rem ============================================================
rem  Anthropic 论文阅读 — 局域网服务 启动器 (Windows)
rem  双击本文件即可启动；也可在命令行传入端口: start.bat 9000
rem ============================================================
setlocal

rem 1) 优先使用本机 WorkBuddy 自带 Python(无需额外安装)
set "PY=%USERPROFILE%\.workbuddy\binaries\python\versions\3.13.12\python.exe"
if exist "%PY%" goto run

rem 2) 退回系统 Python 启动器 / 直接 python
where py >nul 2>nul && set "PY=py" && goto run
where python >nul 2>nul && set "PY=python" && goto run

echo [错误] 未找到 Python。请安装 Python 3.7+(勾选 "Add to PATH") 后重试。
pause
exit /b 1

:run
"%PY%" "%~dp0serve.py" %*
endlocal
