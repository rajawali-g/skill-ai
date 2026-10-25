@echo off
echo Pushing Antigravity skills backup to https://github.com/rajawali-g/skill-ai...
git push -u origin main --tags
if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo   Backup and Release v1.0.0 successfully pushed!
    echo ========================================================
) else (
    echo.
    echo [ERROR] Pastikan repository 'skill-ai' sudah dibuat di:
    echo https://github.com/new (nama repo: skill-ai)
)
pause
