import os

directory = 'J:/GitHub/redraw/dotshid'

for filename in os.listdir(directory):
    if filename.endswith('.shid'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'a') as file:
            file.write('><core_patch_comment><\n')