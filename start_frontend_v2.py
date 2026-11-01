import subprocess
import sys
import os
import time

os.chdir(r'C:\AI-Office\claude-office\frontend')

# Start the frontend process - detached so it stays alive
proc = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'run', 'dev'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

print("Frontend process started with PID:", proc.pid)
print("Waiting 5 seconds for server to initialize...")
time.sleep(5)

# Check if process is still alive
if proc.poll() is None:
    print("✅ Frontend process is running")
    print("Access http://localhost:3000 in your browser")
else:
    print("❌ Frontend process exited")
    stdout_data = proc.stdout.read(500) if proc.stdout else "No stdout"
    stderr_data = proc.stderr.read(500) if proc.stderr else "No stderr"
    print("stdout:", stdout_data)
    print("stderr:", stderr_data)