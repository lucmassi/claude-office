import subprocess
import time
import os
import socket

os.chdir(r'C:\AI-Office\claude-office\frontend')

print("=== Starting Frontend with npx ===")

print("\nStep 1: Try npx next dev --turbo")
proc = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'exec', '--', 'next', 'dev', '--turbo'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

try:
    time.sleep(5)
    if proc.poll() is None:
        print("✅ Process still running, PID:", proc.pid)
        s = socket.socket()
        result = s.connect_ex(('localhost', 3000))
        print("Port 3000:", "OPEN" if result == 0 else "CLOSED")
        s.close()
    else:
        print("❌ Process exited with code:", proc.poll())
        stdout = proc.stdout.read(2000).decode('utf-8', errors='replace') if proc.stdout else ''
        stderr = proc.stderr.read(2000).decode('utf-8', errors='replace') if proc.stderr else ''
        print("stdout:", stdout[:500])
        print("stderr:", stderr[:500])
except subprocess.TimeoutExpired:
    proc.terminate()
    print("⏰ Timeout, process likely stuck")