import os
from pathlib import Path 

SUBDIRECTORIES ={
	
	"DOCUMENTS":['.pdf', '.rtf','.txt', '.doc', '.docx'],
	"AUDIO":['.m4a','.m4b', '.mp3'],
	"VIDEOS":['.mov','.avi','.mp4'],
	"IMAGES":['.jpg','.jpeg','.png']
}

def pick_dir(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

def organizer_dir():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pick_dir(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() == False:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizer_dir()           