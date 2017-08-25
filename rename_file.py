import string
import os

def rename_file():
    #1
    file_list = os.listdir('/Users/setholmstead/Downloads/prank')
    #print file_list
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir("/Users/setholmstead/Downloads/prank")
    #2
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_file()	
