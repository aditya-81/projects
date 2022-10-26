
from pathlib import Path
from PIL import Image
directory = 'images'
files = Path(directory).glob('*')
for file in files:
    with Image.open(file) as name:
        print(file)
        name.rotate(90).resize((128,128)).save(f"/opt/icons/{file}.jpeg")


from PIL import Image
from glob import glob
import os

# Note: put this script in images folder
# Iterate through each file in the folder
for file in glob('ic_*'):
    image = Image.open(file).convert('RGB')
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0] # get filename without extension
    image.rotate(270).resize((128,128)).save('/opt/icons/{}.jpeg'.format(filename))

print('OK')