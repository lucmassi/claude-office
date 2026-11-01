import subprocess
import os
import time

os.chdir(r'C:\AI-Office\claude-office\frontend')

# Try using npx next dev
proc = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'exec', '--', 'next', 'dev', '--turbo'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

print("Starting with npx next dev...")
time.sleep(5)

if proc.poll() is None:
    print("✅ Process still running, PID:", proc.pid)
    print("Access http://localhost:3000")
else:
    print("❌ Process exited with code:", proc.poll())
    stdout = proc.stdout.read(1000) if proc.stdout else ''
    stderr = proc.stderr.read(1000) if proc.stderr else ''
    print("stdout:", repr(stdout[:500]))
    print("stderr:", repr(stderr[:500]))