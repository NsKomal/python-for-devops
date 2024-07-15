import os 
def files_in_folder(path):
    try:
        files = os.listdir(path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
 

def main ():   
    folders = input("pls entrt the folders: ").split()
    print(folders)

    for folder in folders : 
        print ("=========" + folder + "===========")
        files, errormsg  = files_in_folder(folder)
        if errormsg == None:
            for file in files : 
                print (file)
        else :
            print (folder + " : " + errormsg )
if __name__ == "__main__":
    main()