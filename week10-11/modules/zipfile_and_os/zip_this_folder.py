#Author Lauri Putkonen
#Choose 3 different modules and explain 2 functions (purpose and code) from
#each module:

#ZipFile - module
# You can pack files easily
# With this script you can pack current folder
# which is handy if you want send multiple files somewhere

# I use .write() method in this code
# You can use read(), extract(), extractall() functions
# and multiple others with ZipFile
# ZipFile works quite much same as normal files, you need open it with specific mode

# OS -module
# You can use operating system dependent functionalies
# Example in this code i get path for current file name so i don't pack it too
# With os.path methods
# I tried os.getcwd() to get current working directory to pack folder
#But it packed all sub folders aswell so i decided use just "./"
# I haven't try code on windows so not sure if it works there

# Part of this code is copied from geeksforgeeks.org

from zipfile import ZipFile
import os
import sys

zip_file = "folder.zip"

this_file = file_name =  os.path.basename(sys.argv[0])
  
def get_all_file_paths(directory):
  
    files_in_directory = []

        # Add file paths to array
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Ignore script and zip file
            if filename == zip_file or filename == this_file: 
                continue
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            print(filepath)
            files_in_directory.append(filepath)
  
    # returning all file paths
    return files_in_directory        
  
def main():

    directory = './' # Folder to zip 
  
    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)
  
    with ZipFile(zip_file,'w') as zip:
        for file in file_paths:
            zip.write(file)
  
    print('Files zipped!')        
  
  
if __name__ == "__main__":
    main()
