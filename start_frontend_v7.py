import subprocess
import time
import os

os.chdir(r'C:\AI-Office\claude-office\frontend')

print("=== Starting Frontend Setup ===")
print("Step 1: Uninstall any global next")
proc1 = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'uninstall', '--global', 'next'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
proc1.wait(timeout=30)
print("Uninstall return code:", proc1.returncode)

print("\nStep 2: Install next globally (v13 LTS)")
proc2 = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'install', '--global', 'next@13.5.6'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
proc2.wait(timeout=120)
stdout2 = proc2.stdout.read(1000) if proc2.stdout else ''
stderr2 = proc2.stderr.read(1000) if proc2.stderr else ''
print("Install return code:", proc2.returncode)
print("Install stdout:", stdout2[:300] if stdout2 else 'empty')
print("Install stderr:", stderr2[:300] if stderr2 else 'empty')

print("\nStep 3: Start frontend dev server")
proc3 = subprocess.Popen([
    r'C:\Program Files\nodejs\npm.cmd', 'run', 'dev', '--turbo'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

time.sleep(8)

if proc3.poll() is None:
    print("✅ Frontend process running, PID:", proc3.pid)
    import socket
    s = socket.socket()
    result = s.connect_ex(('localhost', 3000))
    print("Port 3000:", "OPEN" if result == 0 else "CLOSED")
    s.close()
else:
    print("❌ Process exited with code:", proc3.poll())
    try:
        stdout3 = proc3.stdout.read(2000).decode('utf-8', errors='replace')
        print("stdout:", stdout3[:500])
    except:
        print("Could not read stdout")
    try:
        stderr3 = proc3.stderr.read(2000).decode('utf-8', errors='replace')
        print("stderr:", stderr3[:500])
    except:
        print("Could not read stderr")

print("\n=== Done ===")