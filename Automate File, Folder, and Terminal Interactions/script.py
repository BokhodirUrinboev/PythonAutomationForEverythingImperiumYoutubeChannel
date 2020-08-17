import subprocess

# subprocess.call('touch example.py', shell=True)
# output = subprocess.check_output('ls', shell=True)
# f = open('out.txt', 'w')
# line_split = output.split()
# for i in line_split:
#     f.writelines(str(i))
# f.close()

for i in range(0,5):
    subprocess.check_call(['python', 'example.py'])