import imageio
import os 
from pathlib import Path
MYPATH = Path().absolute()

def convertor(inputpath, targetFormat = '.gif'):
    outputpath = os.path.splitext(inputpath)[0] + targetFormat
    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputpath, fps = fps)
    for img in reader:
        writer.append_data(img)
    writer.close()

FileName = '\\1.mp4'
convertor(str(MYPATH)+FileName,'.gif')    