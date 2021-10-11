"""
Oh Soldier Prettify my folder, 
Create a function which takes input a path, a .txt file, and a file format like jpg
you have to Capitalize first letter of all files present in the given path except folders 
and files names given in .txt file and rename all jpg files like in series from 1 to x
numbers of file present in the given path.
"""
import os

def soldier(path, txtfile, extension):
    a = os.path.exists(path)
    if a == True:
        with open(txtfile, "r") as f:
            ignore = f.readline() # For collecting ignore file name from file.
        ig = ignore.split("\n") # For splitting that ignore string from \n
        ignore1 = ig[0].split(",") # For splitting all file names by , and putting them in a list.
        file1 = os.listdir(path)
        for i in file1:
            if os.path.isdir(f"D:\Target folder\{i}") is True:
                file1.remove(i)
            else:
                pass
        jpg1 = []
        for i in file1:
            if i.endswith(extension):
                jpg1.append(i)
                file1.remove(i)
            else:
                pass
        print(file1)
        n = 1
        for i in jpg1:
            os.rename(i, f"{n}.{extension}")
            n += 1
        # for i in file1:
        #     os.rename(i, str(i.capitalize()))
            
        
    else:
        print("Your given path is invalid!! please enter a valid path..")

soldier("D:\Target folder", "list.txt", "jpg")
