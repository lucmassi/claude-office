@echo off
title Claude Office Frontend Server
cd C:\AI-Office\claude-office\frontend
echo.
echo Starting Claude Office Frontend Server...
echo.
echo Using Node.js from: C:\Program Files\nodejs
echo Using working directory: %CD%
echo.
rem Add Node.js to PATH for this session only
set PATH=C:\Program Files\nodejs;%PATH%
rem Also add npm global bin
set PATH=%APPDATA%\Roaming\npm;%PATH%
echo.
rem Display current PATH (first few paths)
echo PATH set with Node.js directory
rem Try to run the dev server
rem Using npm run dev with --turbo flag as specified in package.json
npm run dev --turbo
echo.
rem If we get here, the process ended
echo.
echo Frontend server process ended.
echo Check above for any errors.
pause