@echo off
for /f "skip=3 tokens=4" %%i in ('sc query apache2.4') do set "zt=%%i" &goto :next
:next
if /i "%zt%"=="RUNNING" (
	echo �Ѿ����ָ÷��������С�
	echo ׼���رո÷��񡣡���
	net stop "apache2.4"
	echo ֹͣapache2.4������ɣ���ȷ����û�д�������
) else (
	echo �÷������ڴ���ֹͣ״̬��
	echo ׼�������÷��񡣡���
	net start "apache2.4"
	echo ����apache2.4������ɣ���ȷ����û�д�������
)
pause>nul
