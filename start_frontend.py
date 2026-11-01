import subprocess
import sys
import os

os.chdir(r'C:\AI-Office\claude-office\frontend')

proc = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'run', 'dev'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("Frontend process started with PID:", proc.pid)
print("Access the app at http://localhost:3000")
print("Press Ctrl+C to stop")

# Wait for the process
try:
    stdout, stderr = proc.communicate()
    print("stdout:", stdout[:500] if stdout else "empty")
    print("stderr:", stderr[:500] if stderr else "except")
except KeyboardInterrupt:
    print("Stopping frontend...")
    proc.terminate()
    proc.wait()