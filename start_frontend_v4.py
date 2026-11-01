import subprocess
import os
import time

os.chdir(r'C:\AI-Office\claude-office\frontend')

# Try using the full path to next.js binary via npx with --package
proc = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'install', '--global', 'next@14.0.0'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

print("Installing next globally...")
time.sleep(3)

if proc.poll() is None or proc.returncode == 0:
    print("Next installed, now trying to start...")
    # Now try to start
    proc2 = subprocess.Popen([
        r'C:\Program Files\nodejs\npm.cmd', 'exec', '--', 'next', 'dev', '--turbo'
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    
    time.sleep(5)
    
    if proc2.poll() is None:
        print("✅ Frontend starting, PID:", proc2.pid)
        print("Access http://localhost:3000")
    else:
        print("❌ Process2 exited:", proc2.poll())
        stdout = proc2.stdout.read(500) if proc2.stdout else ''
        stderr = proc2.stderr.read(500) if proc2.stderr else ''
        print("stdout:", repr(stdout[:300]))
        print("stderr:", repr(stderr[:300]))
else:
    print("❌ Next install failed, code:", proc.returncode)
    stdout = proc.stdout.read(500) if proc.stdout else ''
    stderr = proc.stderr.read(500) if proc.stderr else ''
    print("stdout:", repr(stdout[:300]))
    print("stderr:", repr(stderr[:300]))