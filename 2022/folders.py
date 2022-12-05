import os

root_path = '/home/lucas/advent-of-code/2022/'
folders = []

for c in range(1, 32):
    folders.append(f'Day-{c}')

for folder in folders:
    os.makedirs(os.path.join(root_path,folder))
    os.system(f'touch /home/lucas/advent-of-code/2022/{folder}/program.py')
