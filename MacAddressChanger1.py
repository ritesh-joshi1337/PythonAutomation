import subprocess

print(subprocess.call('ifconfig'))

x=input('Enter the interface you want to change')
y=input('Enter the new preferred address:')
subprocess.call(['ifconfig '+x+ ' down'],Shell=True)
#here Shell=True will allow us to run terminal commands from this script

subprocess.call(['ifconfig '+x+ ' hw ether '+y],Shell=True)

subprocess.call(['ifconfig '+x+ ' up'])

