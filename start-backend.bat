@echo off
cd /d "%~dp0backend"
echo 正在執行資料庫遷移...
python manage.py makemigrations
python manage.py migrate
echo.
echo 啟動 Django 開發伺服器...
python manage.py runserver
pause
