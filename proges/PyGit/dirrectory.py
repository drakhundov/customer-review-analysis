import os
import path


def sub_folders(folder):
    return [os.path.join(folder, subfolder) for subfolder in os.listdir(folder)]


def remove(folder):
    if os.path.exists(folder) and os.path.isdir(folder):
        for location in os.listdir(folder):
            try:
                location = os.path.join(folder, location)
                os.chmod(location, 438)
                
                if os.path.isfile(location): path.remove(location)
                elif os.path.isdir(location): remove(location)
            
            except: continue

        try:
            os.chmod(folder, 438)
            os.removedirs(folder)

        except: pass