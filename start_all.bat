@echo off
title Claude Office - Inicialização Completa
echo.
echo ==========================================
echo  Iniciando Claude Office Visualizer...
echo ==========================================
echo.
rem Verificar se estamos no Codespaces ou local
hostname | find "codespace" >nul
if %errorlevel% equ 0 (
    echo Modo: GitHub Codespaces
    echo.
    echo Iniciando servidores no Codespaces...
    rem No Codespaces, usamos npm e python3
    call npm run dev --turbo &
    rem Esperar um pouco e iniciar backend
    timeout /t 3 >nul
    python3 -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 &
) else (
    echo Modo: Local (Windows)
    echo.
    echo Iniciando backend local...
    set PATH=C:\Program Files\nodejs;%PATH%
    npm run dev --turbo &
    timeout /t 3 >nul
    python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 &
)
echo.
echo Servidores iniciando em segundo plano...
echo.
echo Acesse:
echo - Backend API: http://localhost:8000
echo - Frontend: http://localhost:3000
echo.
echo Pressione qualquer tecla para continuar ou feche este terminal...
timeout /t 5 >nul
echo.
echo Servidores devem estar rodando em segundo plano.
echo Use os links acima para acessar.
pause