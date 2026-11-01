@echo off
title Inicializando Git Repository
cd C:\AI-Office
echo.
echo Inicializando repositório Git...
git init
if %errorlevel% neq 0 (
    echo ERRO: Não foi possível inicializar o git
    pause
    exit /b 1
)
echo.
git add .
if %errorlevel% neq 0 (
    echo ERRO: Não foi possível adicionar arquivos
    pause
    exit /b 1
)
echo.
git commit -m "Claude Office Visualizer - Setup Inicial"
if %errorlevel% neq 0 (
    echo ERRO: Não foi possível fazer commit
    pause
    exit /b 1
)
echo.
echo Repositório local configurado com sucesso!
echo.
echo Arquivos commitados:
git log --oneline -1
pause