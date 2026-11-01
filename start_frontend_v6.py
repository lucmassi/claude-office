import subprocess
import time
import os

os.chdir(r'C:\AI-Office\claude-office\frontend')

print("Step 1: Installing next globally...")
proc1 = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'install', '--global', 'next@14.0.0'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

stdout1 = proc1.stdout.read(1000) if proc1.stdout else ''
stderr1 = proc1.stderr.read(1000) if proc1.stderr else ''
print("Install output:", stdout1[:300] if stdout1 else 'empty')
print("Install error:", stderr1[:300] if stderr1 else 'empty')
print("Install return code:", proc1.returncode)

time.sleep(3)

if proc1.returncode == 0:
    print("\nStep 2: Starting frontend dev server...")
    proc2 = subprocess.Popen([
        r'C:\Program Files\nodejs\npm.cmd', 'run', 'dev', '--turbo'
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    
    time.sleep(5)
    
    if proc2.poll() is None:
        print("✅ Frontend process running, PID:", proc2.pid)
        # Check port
        import socket
        s = socket.socket()
        result = s.connect_ex(('localhost', 3000))
        print("Port 3000:", "OPEN" if result == 0 else "CLOSED")
        s.close()
    else:
        print("❌ Process2 exited with code:", proc2.poll())
        try:
            stdout2 = proc2.stdout.read(1000).decode('utf-8', errors='replace')
            print("stdout:", stdout2[:300])
        except:
            print("Could read stdout")
        try:
            stderr2 = proc2.stderr.read(1000).decode('utf-8', errors='replace')
            print("stderr:", stderr2[:300])
        except:
            print("Could read stderr")
else:
    print("\n❌ Step 1 failed, cannot proceed with Step 2")