import subprocess
try:
    subprocess.Popen(r"Windows\pythonUE.exe")
    subprocess.Popen(r"dist\server\server.exe")
except:
    print('File not found')