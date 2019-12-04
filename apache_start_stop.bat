@echo off
for /f "skip=3 tokens=4" %%i in ('sc query apache2.4') do set "zt=%%i" &goto :next
:next
if /i "%zt%"=="RUNNING" (
	echo 已经发现该服务在运行。
	echo 准备关闭该服务。。。
	net stop "apache2.4"
	echo 停止apache2.4服务完成，请确认有没有错误发生。
) else (
	echo 该服务现在处于停止状态。
	echo 准备启动该服务。。。
	net start "apache2.4"
	echo 启动apache2.4服务完成，请确认有没有错误发生。
)
pause>nul
