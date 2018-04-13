import os
def rename_files():
    #1 get file names from a folder
    file_list = os.listdir("/Users/yuxiaoguo/Google Drive/Udacity nonodegree/stage3/prank")
    #print (file_list)
    saved_path = os.getcwd()
    #print saved_path
    os.chdir("/Users/yuxiaoguo/Google Drive/Udacity nonodegree/stage3/prank")
    #2 for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate (None,"0123456789"))
        
rename_files()
