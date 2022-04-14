import subprocess

data = subprocess.check_output("whoami", shell=True)
print(data)

for i in range(10):
  print(i)
