# importing required modules
from zipfile import ZipFile
import os
import sys

zip_name = "text.zip"

this_file = file_name =  os.path.basename(sys.argv[0])
print(this_file)
  
def get_all_file_paths(directory):
  
    # initializing empty file paths list
    files_in_directory = []
  
    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            if filename == zip_name or filename == this_file:
                continue
            filepath = os.path.join(root, filename)
            print(filepath)
            files_in_directory.append(filepath)
  
    # returning all file paths
    return files_in_directory        
  
def main():
    # path to folder which needs to be zipped
    directory = './.'
  
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
  
    # writing files to a zipfile
#    with ZipFile(file,'w') as zip:
#        # writing each file one by one
#        for file in file_paths:
#            zip.write(file)
  
    print('All files zipped successfully!')        
  
  
if __name__ == "__main__":
    main()
