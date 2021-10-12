"""
Oh Soldier Prettify my folder, 
Create a function which takes input a path, a .txt file, and a file format like jpg
you have to Capitalize first letter of all files present in the given path except folders 
and files names given in .txt file and rename all jpg files like in series from 1 to x
numbers of file present in the given path.
"""
import os
import time
def soldier(path, txtfile, extension):
    a = os.path.exists(path)
    if a == True:
        print("Please wait.. Soldier has been sent to prettify your folder..")
        time.sleep(.5)
        with open(txtfile, "r") as f:
            ignore = f.readline() # For collecting ignore file name from file.
        ig = ignore.split("\n") # For splitting that ignore string from \n
        ignore1 = ig[0].split(",") # For splitting all file names by , and putting them in a list.
        file1 = os.listdir(path)
        for i in file1: # For removing folders from our list1
            if os.path.isdir(f"D:\Target folder\{i}") is True:
                file1.remove(i)
            else:
                pass
        jpg1 = []
        for i in file1: # For removing jpg files from our list1 and adding them into jpg list.
            if i.endswith(extension):
                jpg1.append(i)
                file1.remove(i)
            else:
                pass
        print("Checking for ignored files ...")
        for i in ignore1: # For removing ignored files from our main list1.
            for k in file1:
                if i == k:
                    file1.remove(k)
        os.chdir(path)
        n = 1
        print(f"Renaming your given extension files...")
        for i in jpg1: # Renaming given extension in natural numbers.
            os.rename(i, f"{n}.{extension}")
            n += 1
        print("Capitalizing names...")
        for i in file1: # For capitalizing other file names.
            os.rename(i, str(i.capitalize()))
        
        print("Task completed...")

    else:
        print("Your given path is invalid!! please enter a valid path..")

soldier("D:\Target folder", "list.txt", "jpg")
