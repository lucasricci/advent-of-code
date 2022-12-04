import os

root_path = 'E:\\FOSS-Projects\\advent-of-code\\2022\\'
folders = []

for c in range(1, 32):
    folders.append(f'Day-{c}')

for folder in folders:
    os.mkdir(os.path.join(root_path,folder))
