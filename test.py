import os

home_directory = os.getcwd()
print(home_directory)
os.system("whoami")

def calc(num1, num2):
  return num1 + num2

print(calc(1, 5))
