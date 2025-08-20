import os
import shutil

source_folder = 'source'
destination_folder = 'destination'


for filename in os.listdir(source_folder):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):

        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
    
        shutil.move(src_path, dest_path)
        print(f"Moved: {filename}")
    else:
        print(f"Skipped (Not JPG): {filename}")