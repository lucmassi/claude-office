import subprocess
import sys
import os
import time
import io

os.chdir(r'C:\AI-Office\claude-office\frontend')

# Redirect stdout/stderr to binary to avoid encoding issues
proc = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'run', 'dev', '--turbo'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

print("Frontend process started with PID:", proc.pid)
print("Waiting 8 seconds...")

# Wait and check
try:
    time.sleep(8)
    if proc.poll() is None:
        print("✅ Process still running after 8 seconds")
        # Try to check port
        import socket
        s = socket.socket()
        result = s.connect_ex(('localhost', 3000))
        print("Port 3000:", "OPEN" if result == 0 else "CLOSED")
        s.close()
    else:
        print("❌ Process exited with code:", proc.poll())
        # Read output
        try:
            stdout = proc.stdout.read(2000).decode('utf-8', errors='replace')
            print("stdout:", stdout[:500])
        except:
            print("Could not read stdout")
        try:
            stderr = proc.stderr.read(2000).decode('utf-8', errors='replace')
            print("stderr:", stderr[:500])
        except:
            print("Could not read stderr")
except KeyboardInterrupt:
    print("Interrupted, terminating process...")
    proc.terminate()
    proc.wait()