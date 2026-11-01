import subprocess
import time
import os
import socket

os.chdir(r'C:\AI-Office\claude-office\frontend')

# Add global npm bin to PATH
global_bin = r'C:\Users\lucas\AppData\Roaming\npm'
if global_bin not in os.environ['PATH']:
    os.environ['PATH'] = global_bin + ';' + os.environ['PATH']
    print("Added", global_bin, "to PATH")

print("=== Starting Frontend Setup ===")
print("PATH now includes global bin:", global_bin in os.environ['PATH'])

print("\nStep 1: Verify next is accessible")
proc1 = subprocess.Popen([
    'next', '--version'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=os.environ)
stdout1 = proc1.stdout.read(200) if proc1.stdout else ''
stderr1 = proc1.stderr.read(200) if proc1.stderr else ''
print("next --version stdout:", stdout1.strip() if stdout1 else 'empty')
print("next --version stderr:", stderr1.strip()[:200] if stderr1 else 'empty')
proc1.wait()

print("\nStep 2: Start frontend dev server")
proc2 = subprocess.Popen([
    'next', 'dev', '--turbo'
], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, env=os.environ)

time.sleep(8)

if proc2.poll() is None:
    print("✅ Frontend process running, PID:", proc2.pid)
    s = socket.socket()
    result = s.connect_ex(('localhost', 3000))
    print("Port 3000:", "OPEN" if result == 0 else "CLOSED")
    s.close()
else:
    print("❌ Process exited with code:", proc2.poll())
    try:
        stdout2 = proc2.stdout.read(2000).decode('utf-8', errors='replace')
        print("stdout:", stdout2[:500])
    except:
        print("Could not read stdout")
    try:
        stderr2 = proc2.stderr.read(2000).decode('utf-8', errors='replace')
        print("stderr:", stderr2[:500])
    except:
        print("Could not read stderr")

print("\n=== Done ===")