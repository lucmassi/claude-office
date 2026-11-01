import subprocess
import sys
import os
import time
import socket

print("=" * 60)
print("Starting Claude Office Frontend Server (Python-based)")
print("=" * 60)

os.chdir(r'C:\AI-Office\claude-office\frontend')

# Setup environment - add Node.js paths
env = os.environ.copy()
env['PATH'] = r'C:\Program Files\nodejs' + ';' + env.get('PATH', '')
# Add npm global bin
npm_bin = r'%APPDATA%\Roaming\npm'
if npm_bin not in env['PATH']:
    env['PATH'] = npm_bin + ';' + env['PATH']

print("\nEnvironment PATH configured")
print("Using Node.js from:", r'C:\Program Files\nodejs')

# Try to start the development server
print("\nStarting: next dev --turbo")
print("Working directory:", os.getcwd())

proc = subprocess.Popen([
    sys.executable, '-c',
    '''
import subprocess, os, time, socket
os.chdir(r"''' + r'C:\AI-Office\claude-office\frontend' + '''" )
# Add paths
path_env = r'C:\\Program Files\\nodejs' + ';' + os.environ.get('PATH', '')
# Try running next dev
proc2 = subprocess.Popen([
    r'C:\\Program Files\\nodejs\\npm.cmd', 'run', 'dev', '--turbo'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000)  # CREATE_NEW_PROCESS_GROUP
time.sleep(8)
if proc2.poll() is None:
    print("FRONTEND_RUNNING")
else:
    print("FRONTEND_EXITED with code:", proc2.poll())
    stdout = proc2.stdout.read(500).decode('utf-8', errors='replace') if proc2.stdout else ''
    stderr = proc2.stderr.read(500).decode('utf-8', errors='replace') if proc2.stderr else ''
    print("stdout:", stdout[:300])
    print("stderr:", stderr[:300])
'''], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=0x08000000)

print("\nProcess started with PID:", proc.pid)

# Wait for initialization
time.sleep(8)

# Check if process is still alive
if proc.poll() is None:
    print("✅ Frontend process still running after 8 seconds, PID:", proc.pid)
    
    # Check if port 3000 is open
    try:
        s = socket.socket()
        result = s.connect_ex(('localhost', 3000))
        print("Port 3000:", "OPEN" if result == 0 else "CLOSED")
        s.close()
    except Exception as e:
        print("Socket error:", e)
else:
    print("❌ Process exited with code:", proc.poll())
    # Try to read output
    try:
        stdout_data = proc.stdout.read(3000).decode('utf-8', errors='replace') if proc.stdout else ''
        print("stdout (first 500 chars):", stdout_data[:500])
    except:
        print("Could not read stdout")
    try:
        stderr_data = proc.stderr.read(3000).decode('utf-8', errors='replace') if proc.stderr else ''
        print("stderr (first 500 chars):", stderr_data[:500])
    except:
        print("Could not read stderr")

print("\n" + "=" * 60)
print("Done - check if frontend is accessible at http://localhost:3000")
print("=" * 60)